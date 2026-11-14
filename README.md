# Shqipëria: historia e së drejtës në git

**Shqip** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/sq/effort-dark.svg">
<img alt="Legjislacioni i Shqipërisë në këtë repozitor: çfarë përmban, ndryshimet sipas vitit të hyrjes në fuqi, plotësia ndaj burimeve zyrtare dhe saktësia e asaj që përmban" src="data/sq/effort-light.svg" width="880">
</picture>

E drejta e Shqipërisë si histori git: një skedar për çdo dispozitë, një commit për çdo version në ditën kur hyri në fuqi, dhe akti që bëri çdo ndryshim si autor i commit-it. `git blame` tregon aktin pas çdo paragrafi; `git log` liston çdo ndryshim të një neni; zgjedhja e një date jep tekstin në fuqi atë ditë.

Pjesë e [lexifina/global-law](https://github.com/lexifina/global-law), një histori e vetme git për të drejtën e çdo vendi: ky është legjislacioni kombëtar i Shqipërisë, të cilin global-law e lexon te `albania/national/acts/`.

**Çfarë përmban tani:** Kushtetutën dhe 17.819 akte nga regjistrat e Qendrës së Botimeve Zyrtare (QBZ, botuesi zyrtar): 2.188 ligje, 10.918 vendime të Këshillit të Ministrave, 1.504 udhëzime dhe 3.147 urdhra të ministrave dhe të organeve të tjera, 54 akte normative dhe 8 dekrete të Presidentit, me 22.682 versione (2.724 nga këto akte janë shfuqizuar që atëherë); si dhe 393 vendime të 20 këshillave bashkiakë. [`registry/ACTS.md`](registry/ACTS.md) liston çdo akt, sipas llojit, me statusin e tij; [`data/pending.json`](data/pending.json) liston ligjet e botuara, por ende jo në fuqi.

Çdo akt ndodhet në `<lloji>/<viti>/<numri>/` (`ligj/1995/7961/` është Kodi i Punës, ligji nr. 7961/1995; Kushtetuta është `kushtetuta/1998/`); udhëzimet dhe urdhrat shtojnë ditën e miratimit (`udhezim/2024/1212-1090/`), ndërsa vendimet e këshillave janë në `local/<bashkia>/<viti>/<numri>/`. `registry/data/paths.json` lidh id-në e çdo akti me dosjen e tij. Deri më 4 nëntor 2026 dosjet e akteve të para kishin emra të tjerë (`kushtetuta/`, `ligji-8569-2000/`); `git log --follow`, `git blame` dhe `tools/on.py` shkojnë prapa përmes riemërtimit.

Teksti është në shqip, ashtu siç e boton QBZ. Përkthimi në anglisht nuk është pjesë e këtij repozitori.

## Pyetjet si komanda git

| Pyetja | Komanda |
| --- | --- |
| Çdo ndryshim i nenit 64 të Kushtetutës | `git log -p --word-diff --follow -- kushtetuta/1998/neni-064.md` |
| Cili akt shkroi çdo rresht të nenit 64? | `git blame kushtetuta/1998/neni-064.md` |
| Çdo version i Kushtetutës, me ditën kur hyri në fuqi secili | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- kushtetuta` |
| Neni 64 siç ishte në fuqi më 1 janar 2008 | `python tools/on.py 2008-01-01 kushtetuta/1998 neni-064` |

**Jashtë git-it** këto të dhëna i ofrojmë edhe publikisht dhe falas:

- **[Pyetni Claude për të drejtën e Shqipërisë](https://global-law.lexifina.com/v1/try_claude?country=albania)**: hap Claude me pyetjen e parë gati.
- **[Pyetni ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=albania)**: e njëjta pyetje në ChatGPT.
- **[Thirrni API-në në shfletues](https://global-law.lexifina.com/v1/search_law?query=pushimet+vjetore&jurisdictions=albania)**: kërkim në legjislacionin e Shqipërisë për „pushimet vjetore“, përgjigje në JSON. Dokumentimi është [këtu](https://lexifina.com/api/global-law).

Të dy asistentët i lexojnë të dhënat përmes konektorit falas Global law (MCP, `https://global-law.lexifina.com/mcp`); herën e parë biseda jep lidhjen që e shton. Pyetni në shqip ose në anglisht.

**Vinieni në punë vetë, lehtë.** Mjaftojnë git dhe Python, dhe mjetet punojnë në kompjuterin tuaj:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add albania/national/acts
python3 tools/law.py show 2026-01-01 albania/national/acts/kushtetuta/1998/neni-064.md
```

I hapur në Claude Code, Cursor, VS Code ose Codex, kloni nis edhe një server MCP lokal me të njëjtat mjete ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Datat

Çdo commit datohet në mesditë, sipas orës Europe/Tirane, në ditën kur versioni hyri në fuqi, dhe këtë ditë e mban në trailer-in e tij `In-force:` (ditët e miratimit dhe të botimit janë në `Enacted:` dhe `Published:`):

- për një akt siç është botuar, dita që jep dispozita e tij, e numëruar nga dita kur u botua numri i Fletores Zyrtare ku doli: „hyn në fuqi pas botimit“ ose „menjëherë“ është ajo ditë, „15 ditë pas botimit“ pesëmbëdhjetë ditë më vonë, dhe një ditë e emërtuar është ajo ditë;
- për çdo tekst të konsoliduar të mëvonshëm, dita kur hyri në fuqi akti që e ndryshoi (akti normativ në ditën e miratimit, Kushtetuta neni 101; vendimi i Gjykatës Kushtetuese në ditën e botimit, neni 132), jo data që i jep QBZ versionit;
- për një shfuqizim, një version i fundit bosh në ditën kur hyri në fuqi akti shfuqizues;
- për një vendim këshilli, dita që përmend dispozita e tij, përndryshe dita më e vonë që lejon ligji (shpallet brenda 10 ditëve nga miratimi dhe hyn në fuqi 10 ditë më vonë: Ligji 8652/2000 neni 33(6)).

Çdo version i atribuohet aktit që e bëri, ashtu siç e emërton QBZ (`Ligji nr. 115/2020`), me një adresë që nuk mund të ekzistojë (`…@qbz.gov.al.invalid`); versioni i parë i një akti i atribuohet vetë aktit. Një ndryshim që nuk e shpjegojnë as shënimet e QBZ-së, as teksti i aktit ndryshues, i atribuohet `Qendra e Botimeve Zyrtare` (755 commit-e).

## Sa i përditësuar është

- [data/freshness.json](data/freshness.json): kur u kontrollua për herë të fundit çdo akt me QBZ-në (regjistri i tij, lidhjet me aktet ndryshuese dhe shfuqizuese, versionet e konsoliduara); kontrolli bëhet brenda 7 ditëve për Kushtetutën, ligjet, vendimet e Këshillit të Ministrave, aktet normative dhe dekretet, brenda 30 ditëve për udhëzimet, urdhrat dhe vendimet e këshillave. `python tools/freshness.py <act>` e lexon.
- [data/status.json](data/status.json): nëse përditësimet janë në punë dhe kur është përgjigjur QBZ për herë të fundit.

## Si kontrollohet

- Çdo version është teksti i vetë QBZ-së, siç është botuar ose siç e ka konsoliduar QBZ. Një akt botohet vetëm kur teksti, datat dhe struktura e tij lexohen qartë dhe çdo ndryshim që QBZ lidh me të ka një version; përndryshe mbahet mënjanë.
- Para se të dërgohet (push) çdo paketë, `tools/check_repo.py` lexon nga git çdo version në ditën kur hyri në fuqi dhe një ditë më parë dhe e krahason me korpusin; nuk duhet të ketë asnjë commit bashkimi (merge), asnjë commit të datuar prapa ose në të ardhmen, dhe trailer-at e çdo commit-i duhet të lexohen pa gabim.
- Historia e Kushtetutës është rizbatimi i shtatë ligjeve të saj ndryshuese mbi tekstin e vitit 1998, i krahasuar dispozitë për dispozitë me botimet e konsoliduara të QBZ-së të viteve 2008, 2012, 2015, 2016 dhe me atë të sotëm; çdo dallim është renditur në `REPRODUCE.md`.

## Çfarë nuk tregon

- **Aktet e mbajtura mënjanë.** 3.935 akte (2.720 akte kombëtare dhe 1.215 vendime këshillash), teksti, datat ose versionet e të cilave ende nuk mund të lexohen me siguri, ose që përmendin persona privatë, nuk janë këtu; [data/held.json](data/held.json) liston secilin me arsyen dhe faqen zyrtare.
- **Ndryshimet që QBZ nuk i konsolidon.** 507 akte që ndryshohen nga akte të mëvonshme, por pa tekst të konsoliduar nga QBZ, janë teksti i tyre siç është botuar, të etiketuara `amended, not consolidated`; `registry/data/acts.json` përmend aktet ndryshuese.
- **Gjendjet e mëparshme të gjashtë kodeve të miratuara para vitit 2000** (Civil, i Procedurës Civile, i Punës, Penal, i Procedurës Penale, Rrugor). Secili ka një version, botimin aktual të konsoliduar të QBZ-së: kodet siç u miratuan nuk janë të disponueshme në internet nga burime zyrtare.
- **Shumicën e këshillave.** 41 nga 61 këshillat bashkiakë nuk kanë ende asnjë vendim këtu ([data/local-coverage.json](data/local-coverage.json) tregon pse), dhe ndryshimet e mëvonshme të një vendimi këshilli nuk ndiqen.
- **Praktikën gjyqësore, projektligjet dhe projektaktet.** Vendimet e Gjykatës Kushtetuese shfaqen vetëm si akti pas një ndryshimi në një ligj.

## Burimet

| Burimi | Lloji | Versionet e mëparshme | Shënime |
| --- | --- | --- | --- |
| [Qendra e Botimeve Zyrtare](https://qbz.gov.al) (QBZ), API e hapur | Botuesi zyrtar: Fletorja Zyrtare, aktet, tekstet e konsoliduara | po, versionet e konsoliduara që mban për një akt | Regjistrat nga viti 2000: teksti siç është botuar, çdo tekst i konsoliduar dhe akti që e ndryshoi |
| QBZ, „Kodet e RSH-së“ | Botimet zyrtare të konsoliduara të kodeve | botimi aktual | Gjashtë kodet e miratuara para vitit 2000 |
| Botimet e Kushtetutës nga QBZ (2008, 2012, 2015, 2016), përmes [Internet Archive](https://web.archive.org/) | Botime zyrtare të konsoliduara | një për çdo gjendje | Formulimet e mëparshme të Kushtetutës |
| Kuvendi i Shqipërisë, „Kushtetuta e RSH.pdf“ (2006), përmes Internet Archive | Kopja e Kuvendit e tekstit të vitit 1998 | nuk zbatohet | Kushtetuta siç u miratua |
| Faqet zyrtare të 61 këshillave bashkiakë | Vendimet e këshillave | siç janë botuar | Ligji 139/2015 (neni 15(2), 18(3)) kërkon që çdo këshill t'i botojë aktet e veta; nuk ka regjistër shtetëror |

## Licenca

Shih [`LICENSE`](LICENSE). Tekstet janë tekste zyrtare të Republikës së Shqipërisë; ligji shqiptar për të drejtën e autorit (ligji nr. 35/2016, neni 12, pika 1, shkronja „b“) përjashton aktet ligjore dhe përmbledhjet e tyre zyrtare nga e drejta e autorit. Renditja, mesazhet e commit-eve, tabelat dhe mjetet e Lexifina-s janë CC0 1.0.

Asnjë model i inteligjencës artificiale nuk ka shkruar, përkthyer ose korrigjuar tekst ligjor; skriptet i ka shkruar një model i inteligjencës artificiale, dhe asnjë model nuk ekzekutohet kur ndërtohet historia (shih `REPRODUCE.md` dhe `registry/REPRODUCE.md`).

Ky është përkthim i versionit në anglisht ([README.en.md](README.en.md)); nëse ndryshojnë, vlen versioni në anglisht.

## Më shumë

Nga repozitori [lexifina/global-law](https://github.com/lexifina/global-law) (në anglisht):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): të gjitha funksionet dhe çfarë duhet të mbështesë çdo korpus (`git blame`, `law.py`, mjetet MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): pyetje dhe përgjigje · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): si të propozoni ndryshime · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): serveri MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): si është ndërtuar · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): sa i përditësuar është çdo korpus · [Monitorimi](https://github.com/lexifina/global-law/tree/main/monitoring): nëse përditësimet funksionojnë · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): si ndiqet çdo burim zyrtar për ndryshime
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): sa të shpejta janë mjetet, të matura
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): grafikë dhe lidhje në të drejtën e gjithë botës
- [Dobësitë](https://github.com/lexifina/global-law/tree/main/vulnerabilities): gabime në akte ashtu siç janë botuar
