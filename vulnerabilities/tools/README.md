# Tools

The scripts behind this Albania-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/albania-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only albania-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `config.json` sit three folders up, next to
the copy of global-law (`gl/vulnerabilities/scripts/`).

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds Albania's history rows, and runs the detectors that apply to Albania |
| `add_root.py` | Builds Albania's history rows from this repository's own commits (global-law's published list did not include Albania), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses up to 40 empty periods for global-law's review of that category (here all 16) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Albanian and English, light and dark |
| `config.json` | The repository, the Albanian category names and chart labels, and the folders that are not law (`caselaw/`, `data/`, `registry/`, `tools/` and the root documentation) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(caselaw|data|registry|tools)/'`.

Three changes were needed for this repository:

- `add_root.py` counts the `Kind` values `decree` (changes made by decisions, instructions, orders, decrees and normative acts), `as-enacted` (an act's text as published) and `court` (a Constitutional Court decision that changes a law) as changes to the law, as it already counted `law`. `publisher` (the 755 changes QBZ consolidated without naming the act that made them) and `caselaw` keep their own kind, so the history detectors leave them out.
- `run.sh` takes `LE_WORKERS` and `LE_GREP_THREADS` from the environment when they are set; with six processes the text scan ran out of memory on a shared machine, so this run used `LE_WORKERS=2 LE_GREP_THREADS=2 bash run.sh 2`. The output does not depend on the number of processes.
- `build_vulns.py` links a retroactive-date flag to the act's commit for the day flagged, not to the act's newest commit (for Law No. 62/2020 that was the commit in which it repealed other laws).
