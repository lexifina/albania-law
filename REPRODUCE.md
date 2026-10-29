# How this repository was made (Albania)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Qendra e Botimeve Zyrtare (qbz.gov.al): amending laws (.docx), act records and Fletorja Zyrtare issues | <https://qbz.gov.al/api/v1> | 2026-10-29 | Official texts of the Republic of Albania; legal acts and their official collections are not subject to copyright (ligji nr. 35/2016, neni 12, pika 1, shkronja “b”). |
| Qendra e Botimeve Zyrtare: consolidated Constitution (today's edition, PDF) | <https://qbz.gov.al/pdf/eb9d762f48d82dc4834e4905b5516edc13690d6fea092b27e36f48a1fa59db8c.pdf> | 2026-10-29 | As above. |
| Internet Archive: QBZ consolidated editions 2008, 2012, 2015, 2016 | <https://web.archive.org/> | 2026-10-29 | Internet Archive terms of use; texts as above. |
| Internet Archive: Kuvendi i Shqipërisë, "Kushtetuta e RSH.pdf" (the 1998 text) | <https://web.archive.org/web/20060525195849id_/http://parlamenti.albaniaonline.net:80/menu/foto/Kushtetuta%20e%20RSH.pdf> | 2026-10-29 | Internet Archive terms of use; official text of the Assembly. |
| Qendra e Botimeve Zyrtare (qbz.gov.al): Tatimi mbi të ardhurat as published and its consolidated versions | <https://qbz.gov.al/api/v1/acts/25881/versions> | 2026-10-29 | Official texts of the Republic of Albania; legal acts and their official collections are not subject to copyright (ligji nr. 35/2016, neni 12, pika 1, shkronja “b”). |
| Qendra e Botimeve Zyrtare (qbz.gov.al): Parandalimi i pastrimit të parave as published and its consolidated versions | <https://qbz.gov.al/api/v1/acts/33728/versions> | 2026-10-29 | Official texts of the Republic of Albania; legal acts and their official collections are not subject to copyright (ligji nr. 35/2016, neni 12, pika 1, shkronja “b”). |
| Qendra e Botimeve Zyrtare (qbz.gov.al): Shtetësia as published and its consolidated versions | <https://qbz.gov.al/api/v1/acts/22155/versions> | 2026-10-29 | Official texts of the Republic of Albania; legal acts and their official collections are not subject to copyright (ligji nr. 35/2016, neni 12, pika 1, shkronja “b”). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `kushtetuta` | Kushtetuta e Republikës së Shqipërisë | 8 | 1998-11-28 to 2022-03-24 |
| `tatimi-mbi-te-ardhurat` | Për tatimin mbi të ardhurat | 7 | 2023-05-17 to 2026-01-30 |
| `pastrimi-i-parave` | Për parandalimin e pastrimit të parave dhe financimit të terrorizmit | 8 | 2008-09-10 to 2026-05-02 |
| `shtetesia` | Për shtetësinë | 3 | 2020-10-14 to 2026-06-20 |

The build made 27 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 22 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `e-ardhme`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 26 laws in the record.
- 52 tags.

## Dates

Each commit is dated at noon (Europe/Tirane) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Kushtetuta, neni 84 pika 3: "Ligji hyn në fuqi me kalimin e jo më pak se 15 ditëve nga botimi i tij në Fletoren Zyrtare." A law's own clause sets its day; most say "15 ditë pas botimit". https://qbz.gov.al/pdf/eb9d762f48d82dc4834e4905b5516edc13690d6fea092b27e36f48a1fa59db8c.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `c82446a2c46ca5909b8092cb3acf2630bdf70b776e692b329e7918f4d973dd0a` (936875 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

26 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 27 history commits and 52 tags (history tip `815bb221a18f23cb4ce8e58ebcec67c81e29330f`).

## Decisions made by hand

- The act archive of qbz.gov.al starts in 2000 and has no dated versions of the Constitution, so its history is rebuilt by replaying the seven amending laws on the 1998 text.
- The 1998 text is the Assembly's own copy ("Kushtetuta e RSH.pdf", made from Word on 8 January 2006, linked from parlament.al), read from an Internet Archive capture of 25 May 2006. It predates the first amendment (law 9675 of 13 January 2007), so it is the text as enacted. The Fletorja Zyrtare 1998 nr. 28 itself is not online.
- Each law's instructions are applied to the text before it by Lexifina's code (whole articles replaced, added or repealed; paragraphs, letters and phrases replaced or deleted). No instruction was applied by hand.
- The words of each version come from the official QBZ consolidated edition of that state where one exists (2008, 2012, 2015, 2016 and today), and from the replay otherwise. A provision that no later law changes reads as in today's edition throughout, so editorial differences between copies (capitals, spacing, word-division hyphens) never show as changes.
- Every provision the replay touches is compared with the QBZ edition of its state; differences that remain after ignoring whitespace and word-division hyphens are listed below.
- In-force dates: art. 84(3) of the Constitution sets the default (a law takes effect no sooner than 15 days after publication in the Fletorja Zyrtare). Each amending law states its own: 9675/2007 and 137/2015 "hyn në fuqi menjëherë" (dated here to the day of publication), the other five "15 ditë pas botimit" (publication day + 15). Publication days are the Fletorja Zyrtare issue dates given by qbz.gov.al, each checked against the date printed on the first page of that issue's PDF.
- The Constitution itself took effect on promulgation by the President (art. 183), by decree nr. 2260 of 28 November 1998, after the referendum of 22 November 1998.
- Enactment dates are read from each law's own text ("Miratuar në datën ..." or its heading); the qbz.gov.al act record is a day early for 88/2012 and 16/2022.
- Repealed provisions are removed: QBZ prints them only as a heading and a note ("(Shfuqizuar me ligjin ...)"). Part Twelve (the Central Election Commission, arts. 153-154) was repealed whole by law 9904/2008.
- The publisher's amendment notes are kept out of the text and used only to check the credits.
- Replay vs edition: ligji-76-2016: neni-125: ““dh”” → ““dh”.”
- Replay vs edition: ligji-76-2016: neni-131: “kushtetutshmerinë” → “kushtetutshmërinë”
- Replay vs edition: ligji-76-2016: neni-136: “mbaj-tur” → “mbajtur”; ““dh”” → ““dh”.”
- Credit check: every credited provision is named in QBZ's note for that law, and every note matches a credited change.
- Law text: ligji-76-2016: "Pas nenit 179/a shtohet neni 179/b me këtë përmbajtje:" — there is no article 179/a; neni-179-b was placed after neni-179-01
- Law text: ligji-16-2022: replaces “është 5 vjet nga data e fillimit të funksionimit të tyre” in neni-179-b point 8, but the text reads “është 5 vjet nga data e fillimit të funksionimit tyre”; that phrase was replaced.
- Law text (76/2016): A stray closing quote ends the quoted text early before “2. Për ndryshimin e praktikës gjyqësore,…”; that paragraph was kept in the quoted provision.
- Editorial differences between the Assembly's 1998 copy and the QBZ words used for the same provisions while unamended: 15 provisions differ in their words (listed here), 7 more only in spacing or line breaks: neni-001: “republikë” → “Republikë” | neni-002: “drejtpërsëdrejti.” → “drejtpërsë-drejti.”; “kombëtarë,” → “kombëtare,” | neni-010: “ndërsjelltë” → “ndërsjellë” | neni-024: “eshtë” → “është” | neni-028: “c,” → ““c”,” | neni-034: “per” → “për” | neni-058: “përdorim” → “përdorim,” | neni-083: “dh.” → ““dh”.” | neni-108: “me” → “më” | neni-112: “buxheti” → “Buxheti”; “shtetit.” → “Shtetit.” | neni-157: “shtetit” → “Shtetit” | neni-166: “forcat” → “Forcat”; “armatosura,” → “Armatosura,” | neni-169: “ministrit” → “Ministrit” | neni-173: “forcave” → “Forcave”; “armatosura” → “Armatosura” | neni-179: “”Për” → ““Për”
- Tatimi mbi të ardhurat: in force on 2023-05-17: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare dhe i shtrin efektet nga data 1 janar 2024, me përjashtim të shkronjës “ç” të pikës 1 të nenit 69, që i fillon efektet me hyrjen në fuqi të këtij ligji, dhe pikës 2 të nenit 69, që i fillon efektet nga data 1 qershor 2023", published 2023-05-02.
- Tatimi mbi të ardhurat: Akti normativ nr. 2/2023 (Fletorja Zyrtare nr. 92/2023, 2023-06-23) takes effect on 2023-06-07: normative act: "hyn në fuqi menjëherë", in force on the day it was adopted (Kushtetuta, neni 101). QBZ dates its consolidated version 1 2023-06-07.
- Tatimi mbi të ardhurat: Akti normativ nr. 7/2023 (Fletorja Zyrtare nr. 182/2023, 2023-12-16) takes effect on 2023-12-14: normative act: "hyn në fuqi menjëherë", in force on the day it was adopted (Kushtetuta, neni 101). QBZ dates its consolidated version 2 2023-12-14.
- Tatimi mbi të ardhurat: Vendimi i Gjykatës Kushtetuese nr. 52/2024 (Fletorja Zyrtare nr. 136/2024, 2024-08-05) takes effect on 2024-08-05: Constitutional Court decision: in force on publication in the Fletorja Zyrtare (Kushtetuta, neni 132). QBZ dates its consolidated version 3 2024-06-27.
- Tatimi mbi të ardhurat: Akti normativ nr. 4/2024 (Fletorja Zyrtare nr. 201/2024, 2024-11-27) takes effect on 2024-11-27: normative act: "hyn në fuqi menjëherë", in force on the day it was adopted (Kushtetuta, neni 101). QBZ dates its consolidated version 4 2024-11-27.
- Tatimi mbi të ardhurat: Ligji nr. 9/2025 (Fletorja Zyrtare nr. 40/2025, 2025-02-26) takes effect on 2025-03-13: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 5 2025-01-30.
- Tatimi mbi të ardhurat: Ligji nr. 81/2025 (Fletorja Zyrtare nr. 11/2026, 2026-01-15) takes effect on 2026-01-30: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 6 2025-12-11.
- Ligji 29/2023: neni 72 puts the law in force 15 days after publication and gives it effect from 1 January 2024 (parts of neni 69 earlier, and, after akti normativ nr. 7/2023, nenet 22, 23 and 24 pika 1 from 1 January 2025). The history dates the words by entry into force; the later dates of effect are in the text of neni 72 itself.
- Ligji 29/2023: the normative acts (akte normative) took effect when adopted and, under Kushtetuta neni 101, lapse unless the Assembly approves them within 45 days; QBZ links no other act as changing this law, and its consolidated versions keep their words, so no lapse is recorded.
- Ligji 29/2023: QBZ notes the first five changes; the changes of ligji 81/2025 to nenet 4, 13, 15 and 16 have no note but follow its article 1 ("Kudo në përmbajtje të ligjit fjalët “mjete virtuale” zëvendësohen me fjalën “kripto-aset”"), and Shtojca nr. 1 is the annex it adds; the inflected forms ("kripto-aseteve") are QBZ’s.
- Ligji 29/2023: vendimi i Gjykatës Kushtetuese nr. 52/2024 struck the second and third sentences of neni 69 pika 1 shkronja "dh"; QBZ’s version 3 removes exactly those words, published in the Fletorja Zyrtare on 2024-08-05.
- Parandalimi i pastrimit të parave: in force on 2008-09-10: its clause "hyn në fuqi 3 muaj pas botimit në Fletoren Zyrtare", published 2008-06-10.
- Parandalimi i pastrimit të parave: Ligji nr. 10391/2011 (Fletorja Zyrtare nr. 31/2011, 2011-03-31) takes effect on 2011-04-15: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 1 2011-03-03.
- Parandalimi i pastrimit të parave: Ligji nr. 66/2012 (Fletorja Zyrtare nr. 80/2012, 2012-07-13) takes effect on 2012-07-28: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 2 2012-06-07.
- Parandalimi i pastrimit të parave: Ligji nr. 44/2017 (Fletorja Zyrtare nr. 85/2017, 2017-04-21) takes effect on 2017-05-06: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 3 2017-04-06.
- Parandalimi i pastrimit të parave: Ligji nr. 33/2019 (Fletorja Zyrtare nr. 99/2019, 2019-07-10) takes effect on 2019-07-25: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 4 2019-06-16.
- Parandalimi i pastrimit të parave: Ligji nr. 120/2021 (Fletorja Zyrtare nr. 197/2021, 2021-12-21) takes effect on 2022-01-05: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 5 2021-12-01.
- Parandalimi i pastrimit të parave: Ligji nr. 62/2023 (Fletorja Zyrtare nr. 116/2023, 2023-08-03) takes effect on 2023-08-18: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 6 2023-07-20.
- Parandalimi i pastrimit të parave: Ligji nr. 37/2026 (Fletorja Zyrtare nr. 80/2026, 2026-04-17) takes effect on 2026-05-02: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 7 2026-04-09.
- Shtetësia: in force on 2020-10-14: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare", published 2020-09-29.
- Shtetësia: Ligji nr. 77/2024 (Fletorja Zyrtare nr. 95/2024, 2024-06-06) takes effect on 2024-06-21: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 1 2024-05-02.
- Shtetësia: QBZ’s consolidated version 1 changes Neni 24, which neither a note nor Ligji nr. 77/2024 names; the change is recorded as unexplained, from the publisher.
- Shtetësia: Ligji nr. 49/2026 (Fletorja Zyrtare nr. 116/2026, 2026-06-05) takes effect on 2026-06-20: its clause "hyn në fuqi 15 ditë pas botimit në Fletoren Zyrtare". QBZ dates its consolidated version 2 2026-05-08.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text: every word comes from the official files.
