# Albania: law history in git

The law of Albania as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `al/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `kushtetuta/` | Kushtetuta e Republikës së Shqipërisë (ligji nr. 8417, datë 21.10.1998) | 8 | From its entry into force on 28 November 1998, through all seven amending laws (2007, 2008, 2012, 2015, 2016, 2020, 2022), to today |

The per-act `README.md` in the folder lists every provision, how often it changed and when. The text in force today is, provision for provision, the official consolidated edition published by Qendra e Botimeve Zyrtare (QBZ).

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 64 say on 1 January 2008? | `python tools/ne_fuqi_me.py 2008-01-01 kushtetuta 64` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2008-01-01T23:59:59Z" main -- kushtetuta/neni-064.md):kushtetuta/neni-064.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2008-01-01T23:59:59Z" main -- kushtetuta/neni-064.md; git show "$($r):kushtetuta/neni-064.md"` |
| Which law wrote each paragraph of art. 131? | `git blame kushtetuta/neni-131.md` |
| Every change to art. 64, word by word | `git log -p --word-diff kushtetuta/neni-064.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/ligji-76-2016` (tags `law/<key>` mark each law's commit) |
| The whole Constitution on a date | `python tools/ne_fuqi_me.py 2010-01-01 kushtetuta` |

File names: `neni-064.md` is art. 64, `neni-006-01.md` art. 6/1, `neni-147-c-ced.md` art. 147/ç, `neni-147-e-uml.md` art. 147/ë; `aneks-neni-a.md` is art. A of the Annex (2016); `pjesa-03-kreu-01.md` holds the heading of Part Three, Chapter I; `kalimtare-ligji-9675.md` holds the transitional provisions of law 9675/2007 that QBZ prints after art. 183.

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Tirane, on the day the change took effect**. Enactment and publication dates are trailers (`Enacted:`, `Published:`), and the in-force day is in `In-force:`, which the tools read.
- **Default rule.** Constitution art. 84(3): "Ligji hyn në fuqi me kalimin e jo më pak se 15 ditëve nga botimi i tij në Fletoren Zyrtare" (a law takes effect no sooner than 15 days after its publication in the Fletorja Zyrtare). Each amending law sets its own day: 9675/2007 and 137/2015 "hyn në fuqi menjëherë" (dated to the day the Fletorja Zyrtare published it), and the other five "15 ditë pas botimit" (publication day + 15).
- **The Constitution itself** was adopted by the Assembly on 21 October 1998, approved by referendum on 22 November 1998 and promulgated by presidential decree nr. 2260 on 28 November 1998; by its art. 183 it took effect on promulgation. Its first commit is dated 1998-11-28.
- Publication days are the Fletorja Zyrtare issue dates in qbz.gov.al's records, each checked against the date printed on that issue's first page. Enactment dates are read from each law's own text: qbz.gov.al's act record is a day early for 88/2012 and 16/2022.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How the history was rebuilt

QBZ's online archive starts in 2000 and keeps no dated versions of the Constitution, so the history is rebuilt:

1. **The 1998 text** is the Assembly's own copy ("Kushtetuta e RSH.pdf", made from Word on 8 January 2006 and linked from the Assembly's website), read from an Internet Archive capture of 25 May 2006. That is before the first amendment (13 January 2007), so it is the text as enacted.
2. **Each amending law** is read from its official .docx on qbz.gov.al and its instructions are applied in turn by `tools/parse.py`: whole articles replaced, added or repealed; paragraphs, letters and phrases replaced, added or deleted; Part Twelve repealed. No instruction is applied by hand.
3. **The words of each version** come from QBZ's official consolidated edition of that state wherever one exists: the editions of 2008, 2012, 2015 and 2016 (Internet Archive copies of qbz.gov.al) and today's edition. A provision that no later law changes reads as in today's edition throughout. The replay supplies the words only where no edition of that state survives (the 1998 wording of provisions later amended, and the states after 9675/2007 and 115/2020).

## How it is checked

- **Replay against the official editions.** Each law, replayed on the text before it, is compared provision by provision with QBZ's edition of the state after it. All 82 provision changes the seven laws make (73 distinct provisions) match once whitespace and word-division hyphens are set aside, except three small typographic points in the 2016 law's own text (a final period lost where two closing quotes meet in arts. 125 and 136, and "kushtetutshmerinë" for "kushtetutshmërinë" in art. 131). Every difference is listed in `REPRODUCE.md`.
- **Today's text is the official text.** The last version equals QBZ's consolidated edition of today, provision for provision.
- **Credits against QBZ's notes.** Every provision credited to a law is named in QBZ's own note for that law in today's edition ("Ndryshuar me ligjin nr. 9904, datë 21.4.2008"), and every such note matches a credited change.
- Every version of the act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Health checks: no merge commits, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`ligji-76-2016@qbz.gov.al.invalid`), so `git blame` and `git log --author` name laws. The committer is always Lexifina. The first commit is credited to ligji nr. 8417 (the Constitution as enacted). Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a law changed.

## What it does not show

- **The Fletorja Zyrtare of 1998** (nr. 28/1998) is not online; the 1998 text is the Assembly's copy. It differs from QBZ's wording of the same, never-amended provisions only in typography (capitals such as "Forcat e Armatosura", a few accents, quotes and commas, in 15 provisions, listed in `REPRODUCE.md`; 7 more differ only in spacing). Those provisions read as QBZ prints them today, so such differences never appear as changes.
- **Editorial changes between QBZ editions** (spacing, capitals, corrected accents) are not shown as changes, for the same reason.
- **Rulings of the Constitutional Court** do not change the text of the Constitution and are not in the record.
- **Other acts.** Only the Constitution so far. The Civil Code (1994) and the Penal Code (1995) predate QBZ's online archive, and no official machine-readable copy of their original texts has been found yet.

## How it is built

`tools/fetch.py` downloads every source once through curl (cached by the sha256 of the URL; archive.org through the shared rate-limited client), `tools/parse.py` with `tools/qbzpdf.py` turns the cache into `corpus.json`, and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Qendra e Botimeve Zyrtare](https://qbz.gov.al) (QBZ), open JSON API `qbz.gov.al/api/v1` | Official publisher (gazette, acts, consolidated editions) | no dated versions; acts from 2000 | the amending laws are separate acts | per act and per gazette issue | Used: the .docx of each amending law, the gazette issue dates, and today's consolidated Constitution (free PDF with a text layer) |
| QBZ editions of the Constitution 2008, 2012, 2015, 2016, via the [Internet Archive](https://web.archive.org/) | Official consolidated editions | one per state | yes, a note per article | n/a | Used as the words of each state and to check the replay |
| Kuvendi i Shqipërisë, "Kushtetuta e RSH.pdf" (2006), via the Internet Archive | The Assembly's copy of the 1998 text | n/a | n/a | n/a | Used for the text as enacted |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of the Republic of Albania, published by Qendra e Botimeve Zyrtare and by the Assembly of Albania. Albania's copyright law (ligji nr. 35/2016, neni 12, pika 1, shkronja "b") excludes legal acts and their official collections from copyright. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## Shqip

Historia e së drejtës shqiptare në git: një skedar për çdo dispozitë dhe një commit për çdo ligj, me datën e hyrjes së tij në fuqi dhe me ligjin që bëri ndryshimin si autor (`git blame` tregon ligjin e çdo paragrafi). Përmban Kushtetutën e Republikës së Shqipërisë që nga hyrja në fuqi më 28 nëntor 1998, me të shtatë ligjet që e kanë ndryshuar (nr. 9675/2007, 9904/2008, 88/2012, 137/2015, 76/2016, 115/2020 dhe 16/2022), deri sot.

- Teksti në fuqi në një datë: `python tools/ne_fuqi_me.py 2008-01-01 kushtetuta 64`
- Datat: neni 84, pika 3, i Kushtetutës (ligji hyn në fuqi jo më pak se 15 ditë pas botimit në Fletoren Zyrtare); çdo ligj ndryshues e cakton vetë ditën ("menjëherë" ose "15 ditë pas botimit").
- Si u rindërtua: teksti i vitit 1998 është kopja e Kuvendit (PDF, 2006, nga Internet Archive); çdo ligj ndryshues zbatohet me radhë mbi tekstin e mëparshëm, dhe fjalët e çdo versioni merren nga botimi zyrtar i konsoliduar i QBZ-së për atë gjendje (2008, 2012, 2015, 2016 dhe sot) kudo që ekziston. Teksti i fundit është, dispozitë për dispozitë, botimi zyrtar i sotëm i QBZ-së.
- Burimi: Qendra e Botimeve Zyrtare (qbz.gov.al) dhe Kuvendi i Shqipërisë. Asnjë model i inteligjencës artificiale nuk ka shkruar tekst ligjor.
