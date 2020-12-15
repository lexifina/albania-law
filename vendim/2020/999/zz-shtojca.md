# Shtojca
STANDARDET SHTETËRORE
PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI - TEMA: NJËSITË STATISTIKORE”
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Njësitë statistikore
3.1.1 Parathënie
3.1.2 Skema e aplikimit dhe diagrami UML për temën “Njësitë statistikore”
3.1.2.1 Njësitë statistikore - Formati bazë
3.1.2.2 Njësitë statistikore - Formati rrjet
3.1.2.3 Njësitë statistikore - Formati vektor
3.1.3 Katalogu i tipologjisë
3.1.3.1 Njësitë statistikore
3.1.3.2 Rrjeti statistikor
3.1.3.3 Njësitë statistikore vektor
3.1.3.4 Evolucion
3.1.3.5 Elementet statistikore të rrjetit
3.1.3.6 Gjeometria e njësisë statistikore vektor
3.1.3.7 Gjeometria përshkruese
3.1.3.8 Mozaiku statistikor
3.1.3.9 Njësitë statistikore poligon/sipërfaqe
3.1.3.10 Pozicioni i rrjetit
3.1.3.11 Rezolucioni i rrjetit statistikor
3.1.3.12 Vlerat e llojeve të gjeometrisë
3.1.3.13 Vlerat e llojit të evolucionit
3.2 Metadata
3.3 Kodi EPSG për KRGJSH-në
3.4 Cilësia e të dhënave
3.4.1 Kompletimi - Autorizimi (Completness - Commission)
3.4.2 Kompletimi - Përjashtimi (Completness - Ommission)
3.4.3 Përputhja logjike - Përputhja topologjike (Logical consistency - Topological consistency)
3.4.4 Saktësia pozicionale - Saktësia absolute ose e jashtme (Positional accuaracy - Absolute or extrenal accuaracy)
3.4.5 Saktësia tematike - Korrektësia e klasifikimit (Thematic accuaracy - Classification correctenss)
3.4.6 Cilësia e kohës - Vlefshmëria e kohës (Temporal quality - Temporal validity)
4. ANEKSE
4.1. Aneksi A - Katalogu i tipologjisë
4.2. Aneksi B - Kodlistat
4.2.1 Skema e aplikimit të temës “Njësitë statistikore’’
4.2.2 Vlerat e llojeve të evolucionit
4.2.3 Vlerat e llojeve të gjeometrisë
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standarde të specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG) në bashkëpunim me Institutin e Statistikave (INSTAT), i cili është autoriteti publik përgjegjës për temën “Njësitë statistikore”.
Data e publikimit të versionit nr. 1 është tetor 2018. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2018_ NJS_v.1, ku:
ASIG - autoriteti përgjegjës për krijimin e standardit;
Standard - lloji i dokumentit;
NSDI - qëllimi i dokumentit;
2018 - viti i krijimit;
NJS - tema për të cilën është krijuar standardi “Njësitë statistikore”, e cila i referohet temës “Statistical Units” në Direktivën INSPIRE;
v.1 - Numri i versionit të standardit.
2. HYRJE
2.1 Qëllimi
Ky dokument përcakton specifikimet teknike, të harmonizuara konform direktivës INSPIRE, për të dhënat gjeohapësinore të temës “Njësitë statistikore”, temë e cila është përcaktuar në nenin 11, pika 2/k, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI-së në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse për mbledhjen përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë mes tyre.
2.2 Si lexohet dokumenti
2.2.1 Struktura e dokumentit
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve - Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje - Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema - Në këtë pjesë jepen specifikimet teknike për temën “Njësitë statistikore”.
4. Anekse - Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
Përmbajtja e kapitullit të 3-të është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës si dhe se si është e ndarë kjo temë.
3.2 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3 Sistemi Koordinativ Referencë - Këtu përcaktohet Sistemi Koordinativ Referencë (KRGJSH).
3.4 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në “Katalogun i tipologjive” (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave, duke u fokusuar te katalogu i tipologjive. Për përdoruesit e aplikacioneve, katalogu i tipologjive, mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të shembujve, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit në tabelën e kodlistës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi sipas direktivës INSPIRE për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
“feature Type” - një element që mund të jetë real, në terren, apo një dukuri abstrakte;
“data Type” - një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër;
“enumeration” “kodlistë” - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa “codeList” nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”;
“union” - një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet që bien brenda shtrirjes gjeohapësinore të të dyja grupeve të të dhënave hyrëse;
“Imported” - të dhëna të specifikuara në tema të tjera të DIREKTIVËS INSPIRE. Në dokument gjenden “Të dhënat e importuara”.
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë, poligon.
Abstrakt - kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
Shumëllojshmëria
Lloji dhe numri i vlerave që mund të marrë atributi:
0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë;
1..* - mund të marrë minimumi 1 vlerë ose shumë vlera;
0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme;
1 - duhet të marrë detyrimisht 1 vlerë.
I detyrueshëm
Po - nëse atributi është i detyrueshëm të plotësohet;
Jo - nëse atributi nuk është i detyrueshëm të plotësohet.
Rolshoqërimi
Në tabelën e lidhjeve “Rolshoqërimet” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve.
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh.: PO].
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh.: Ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh.: Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve.
2.2.3 Karakteristikat e “voidable” dhe shumëllojshmëria
Stereotipi “voidable” përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore, që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera “void”. Një vlerë “void” nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore, që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës “void” duhet të paraqitet kurdo që të jetë e mundur, duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrimi --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni të caktuar, nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “e panjohur”.
E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “e pa populluar”.
Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull: Të dhënat personale të popullsisë, të cilat ekzistojnë por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi “voidable” nuk jep asnjë informacion nëse ekziston një karakteristikë në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh., nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh., nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit Coverages përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe/ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh., vendndodhja e sensorëve), kurbat përcaktuese (p.sh., izolinjat), rrjetet (p.sh., ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit të Inspire, funksionet e mbulimit janë përcaktuar si vetitë e llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është një realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh., ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptues të Përgjithshëm.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
Rrjeti i Mbulimit i Korrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
Rrjeti i Mbulimit Referencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje të mbulimit (ose një nëntip i tyre) në skemat e aplikimit në Inspire.
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 Numërtimet dhe kodlistat (Enumeration and Kodliste)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, “vlera të tjera” përcaktojnë llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht si më poshtë:
“jo” përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
“të kufizuara” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave;
“të hapura” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave;
“po” përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo”, pra të specifikuara në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 Paraqitja e dimensionit kohor
Skemat e aplikimit përdorin atributin “Fillimi i Ciklit Jetësor” dhe “Përfundimi i Ciklit Jetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “Fillimi i Ciklit Jetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “Përfundimi i Ciklit Jetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “Përfundimi i Ciklit Jetësor” nuk shkaktojnë ndryshime në atributin “Fillimi i Ciklit Jetësor”.
Shënim i rëndësishëm
Disa terma në Katalogun e tipologjive, si p.sh., Feature Type, Data Type, Void, Coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të direktivës Inspire.
2.3 Detyrimet ligjore
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet evropiane (direktiva Inspire).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën Inspire, si dhe nga praktikat më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - Në këtë fushë, direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM nr. 1077, datë 23.12.2015).
- Specifikimi i të dhënave - Standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. Inspire ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 Fusha e veprimit
Të gjithë autoritetet publike, kompanitë private apo individët që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva Inspire ka proceset dhe ciklin jetësor si më poshtë:
Figura 2: Proceset e ciklit jetësor
“Planifikimi” është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
“Vlerësimi” është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
“Procesimi (përpunimi)” është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
“Shpërndarja” është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, institucionet ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
“Zbulimi” është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
“Analiza” është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
“Përditësimi” është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
“Arkivimi” është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen, arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
“Shkatërrimi” është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 Njësitë statistikore
3.1.1 Parathënie
Njësitë statistikore janë përcaktuar si “njësi për shpërndarjen ose përdorimin e informacionit statistikor”.
Një Njësi Statistikore (NS) është një tipar gjeohapësinor (poligon, vijë, pikë ose rrjet qelizash), që mund të përdoret për të bashkëngjitur informacionin statistikor. Informacioni statistikor mund të përkufizohet si “çdo përfaqësim numerik i një fenomeni”, si për shembull, popullsia (referenca është për popullsinë njerëzore). Ky informacion, duhet të japë informacionin për një popullsi të caktuar dhe jo të kufizohet në popullatën njerëzore.
Informacioni statistikor nuk konsiderohet si pjesë e njësisë statistikore. Është një informacion johapësinor tematik, harmonizimi i të cilit është jashtë qëllimit të këtij dokumenti. Për këtë informacion i referohemi specifikimit të temës “Demografia/Shpërndarja e Popullsisë”. Ky dokument përqendrohet vetëm në përfaqësimin e tipologjive gjeohapësinore që përdoren për të bashkëngjitur çdo lloj informacioni statistikor.
Të gjitha tipologjitë e temave të Inspire mund të shihen si njësi statistikore. Për shembull, të dhënat e trafikut rrugor mund të lidhen me tipologjinë Lidhje Rrugore e temës “Rrjetet e Transportit”. Të dhënat e popullsisë mund të lidhen me tipologjinë e ndërtesave të temës “Ndërtesat”.
Tema “Njësitë statistikore” trajton njësitë që nuk janë adresuar nga tema të tjera dhe që zakonisht përdoren vetëm për shpërndarjen e të dhënave statistikore.
Ky dokument paraqet specifikimet e të dhënave për njësitë statistikore, duke u mbështetur në parimet e mëposhtme:
- Ndarja ndërmjet të dhënave statistikore dhe njësive statistikore
Të dhënat statistikore përkufizohen si “çdo përfaqësim numerik i një fenomeni”. Një njësi statistikore jep informacion për vendndodhjen e të dhënave statistikore. Informacioni statistikor nuk cilësohet si pjesë e njësisë statistikore. Ky dokument trajton vetëm specifikimet e të dhënave për njësitë statistikore (ndërsa specifikimi i të dhënave statistikore është jashtë qëllimit). Parimi është të sigurohet një paraqitje e qëndrueshme dhe e identifikueshme e njësive statistikore (të dhënat statistikore u referohen këtyre objekteve nëpërmjet identifikuesit të tyre). Në këtë dokument janë dhënë disa rekomandime për mënyrën e paraqitjes së identifikuesit të qëndrueshëm të njësisë statistikore dhe si të përdoren këto identifikues për të bashkëngjitur informacionin statistikor mbi to. Kjo është veçanërisht e rëndësishme nëse përgjegjësia për gjeometrinë dhe të dhënat statistikore ndahet midis institucioneve të ndryshme, p.sh., agjencitë e hartave dhe zyrat statistikore.
Lidhja e të dhënave statistikore me objektin gjeohapësinor nuk është vetëm lidhja e një objekti të një baze të dhënash me një tjetër, por objektivi është përmirësimi i ndërveprimit midis statistikave dhe sistemit të informacionit gjeografik (GIS). Rekomandimet e këtij dokumenti synojnë përmirësimin e integrimit të analizave gjeohapësinore dhe statistikore.
- Përgjithësim
Modeli i të dhënave nuk ka për qëllim të harmonizojë të gjithë njësitë statistikore ekzistuese si për shembull: zonat e censusit, zonat e menaxhimit, njësitë mjedisore etj. Ky dokument ka për qëllim të ofrojë një model abstrakt të njësive statistikore. Këtu janë nxjerrë karakteristikat e përbashkëta dhe që përfaqësohen në një model të përgjithshëm të të dhënave.
- Njësitë statistikore si gjeometri vektoriale dhe qelizat e rrjetit
Njësitë statistikore zakonisht përfaqësohen si:
Gjeometri vektoriale (pikat, vijat, sipërfaqet), kryesisht sipërfaqet. Njësitë statistikore, kryesisht sipërfaqet përbëjnë një mozaik (një mozaik është një bashkim i sipërfaqeve që mbulojnë një pjesë të hapësirës gjeografike pa mbivendosje dhe pa boshllëqe).
Qelizat e rrjetit
Ky dokument ofron rekomandime për përfaqësimin e llojeve të mësipërme të njësive statistikore.
- Marrëdhëniet hierarkike ndërmjet njësive statistikore
Disa njësi statistikore janë organizuar në një strukturë hierarkike: disa njësi statistikore formojnë njësi të tjera të një niveli më të lartë. Për këtë arsye janë paraqitur rekomandime për të përfaqësuar struktura të tilla.
- Përfaqësim në shkallë të gjerë
Njësitë statistikore kanë disa përfaqësime në shkallë të ndryshme. Për shpërndarjen e të dhënave statistikore në shkallë evropiane, kërkohen përfaqësime të thjeshta të njësive statistikore. Për të përmbushur këtë kërkesë, ky dokument përcakton se si mund të specifikohen përfaqësime të ndryshme të njësive statistikore.
- Evoluimi i njësive statistikore
Ekzistojnë kërkesa specifike në lidhje me evoluimin e njësive statistikore në kohë. Disa njësi mund të ndryshohen, fshihen, krijohen, bashkohen ose ndahen. Shumë raste të përdorimit të njësive statistikore kanë të bëjnë me evoluimin e të dhënave statistikore në kohë dhe hapësirë. Ky dokument specifikon se si mund të përfaqësohen faza të ndryshme dhe ecuria e njësive statistikore.
Disa nga karakteristikat e rëndësishme të njësive statistikore janë:
- Ato mund të kenë një strukturë hierarkike (p.sh., NUTS1, NUTS2 dhe NUTS3).
- Shtrirja e tyre gjeohapësinore mund të shkojë nga niveli më i ulët administrativ (më i vogël se- bashkitë/komunitetet) deri në nivel kombëtar vendi.
- Shtrirja e tyre kohore ndryshon sipas vendit. Ata mund të ndryshojnë në kohë, gjë që e bën të vështirë krahasimin në kohë.
- Në shumë raste ato rrjedhin nga njësitë administrative, por burime të tjera janë, gjithashtu, të mundshme.
Njësitë statistikore ekzistuese
NUTS - Nomenklatura e Njësive Territoriale për Statistika
Që prej shumë vitesh statistikat rajonale evropiane janë mbledhur, përpunuar dhe shpërndarë në bazë të një klasifikimi të përbashkët rajonal, të quajtur Nomenklatura e Njësive Territoriale për Statistikat (NUTS). Në krye të hierarkisë qëndrojnë shtetet anëtare të Bashkimit Evropian dhe nën nivelet NUTS 1 deri 3. Në përgjithësi, një ose dy nivele NUTS përputhen me njësitë administrative kombëtare ekzistuese të vendeve të ndryshme. Për këtë arsye, njësitë NUTS janë një lloj i rëndësishëm i njësive statistikore. Për këtë sistem klasifikimi janë përcaktuar rregulla të qarta në kuadrin ligjor (Rregullorja (KE) nr. 1059/2003).
LAU Njësitë Administrative Lokale dhe Urban Audit (qytete me dendësi të lartë)
Klasifikimi i NUTS-ve shërben si një sistem i harmonizuar për aplikime në nivel evropian dhe rajonal, ndërkohë që nuk përjashton ekzistencën e nënndarjeve dhe klasifikimeve të tjera. Në një nivel më të detajuar, ekzistojnë bashkitë e përdorura në kontekstin evropian. Këto quhen Njësitë Administrative Lokale (LAU) të përdorura në legjislacionin evropian. Shembuj të tjerë të njësive statistikore janë zona urbane të përdorura në projektin e qyteteve me dendësi të lartë (Urban Audit), organizuar nga Eurostat. As Njësitë Administrative Lokale (LAU) dhe as Urban Audit (UA) nuk janë subjekt i NUTS apo i ndonjë rregulloreje tjetër evropiane.
- Njësi statistikore lokale të tjera
Brenda shumicës së bashkive ekzistojnë dhe nënndarje të tjera territoriale, që përdoren për administrimin bashkiak, vrojtimet statistikore (p.sh. zonat e Censusit etj.) dhe qëllime të tjera specifike tematike dhe për të cilat jepen të dhënat statistikore. Të gjitha këto njësi nuk janë të harmonizuara në Evropë dhe nuk janë përshtatur në nivel evropian.
- Njësi statistikore specifike sektoriale
Njësitë statistikore përdoren gjithashtu për qëllime specifike sektoriale (si për shembull rajonet e sigurisë civile, zonat e jurisprudencës ose rajonet turistike). Njësi të tilla statistikore sektoriale konsiderohen jashtë qëllimit, pasi harmonizimi i të gjitha këtyre njësive statistikore specifike në nivel evropian mund të jetë një përpjekje që nuk ia vlen. Meqë modeli i të dhënave është i përgjithshëm, është e mundur që të përdoret edhe për qëllime specifike sektoriale, por nuk ka asnjë detyrim për të siguruar njësi të tilla statistikore sipas këtij specifikimi të të dhënave.
- Rrjeti
Ndarja e njësive statistikore bazohet në ndarjet administrative ose tematike, por gjithashtu përdoren edhe ndarjet territoriale abstrakte, të cilat shërbejnë si referencë gjeohapësinore për statistikat dhe quhen rrjete. Rrjetet janë kuadrate me madhësi të ndryshme të orientuara në sistemin koordinativ KRGJSH, të pavarur nga kufijtë administrativë ose tematikë.
- Përdorimet e njësive statistikore
Njësitë statistikore janë të nevojshme në kuadër të qeverisjes vendore, qeverisjes qendrore, vendbanimeve, zhvillimit urban dhe rajonal, planifikimit shëndetësor dhe arsimor, planifikimit të regjistrimit në shkolla, vlerësimit të rreziqeve etj. Ato janë me rëndësi të madhe për analiza të integruara për zona dhe rajone. Gjithashtu, janë të nevojshme si karakteristika gjeografike edhe në vlerësimet mjedisore dhe sociale. Njësitë statistikore mund të përdoren si bazë gjeografike për hulumtime në pothuajse çdo fenomen.
Njësitë statistikore mund të përdoren për mbledhjen e të dhënave, si dhe për agregimin ose paraqitjen e të dhënave (në shkallë të ndryshme, për qëllime të ndryshme, për shembull: në nivele të ndryshme statistikore NUTS). Në mënyrë të ngjashme si njësitë administrative, njësitë statistikore mund të përdoren për të gjeoreferuar të dhënat nga fusha të ndryshme statistikore, si demografia dhe statistikat sociale, ekonomia, mjedisi dhe burimet natyrore. Njësitë statistikore përdoren, gjithashtu, për analizën e riskut (p.sh., rreziku i përmbytjes), kryesisht në lidhje me shpërndarjen e popullsisë.
- Lidhja me temat e tjera
Grupet e të dhënave të adresuara në këtë temë mund të mbulohen, gjithashtu, dhe në tema të tjera të INSPIRE ose si gjeometri/objekte të mbivendosura, ose si një gjeometri e nevojshme për prezantime tematike. Njësitë statistikore mund të përdoren si bazë për bashkimin, grumbullimin dhe paraqitjen e hartave për pothuajse çdo temë ose çështje të sektorit. Tema “Njësitë statistikore” ka lidhje me temat “Kufijtë e njësive administrative”, “Demografia”, “Zonat me përdorim të kufizuar”, “Sistemet e rrjeteve gjeografike” dhe “Shëndeti i njerëzve dhe siguria e tij”.
Skema e aplikimit dhe diagrami UML për temën “Njësitë statistikore”
Një njësi statistikore është shprehur si një njësi e përdorur për shpërndarjen ose mbështetjen e përdorimit të informacionit statistikor. Sipas këtij përkufizimi, të gjitha objektet gjeohapësinore të temave të gjeoinformacionit mund të konsiderohen si njësi statistikore. Kjo skemë aplikimi ofron objekte që nuk janë mbuluar nga tema të tjera dhe që përdoren zakonisht për referencën gjeohapësinore të të dhënave statistikore.
Karakteristikat kryesore të modelit të të dhënave të njësisë statistikore nga Inspire janë si më poshtë:
Të përgjithshme
Modeli i të dhënave nuk ka për qëllim të harmonizojë të gjitha njësitë statistikore specifike ekzistuese, si zonat e Censusit, zonat e menaxhimit, njësitë raportuese mjedisore etj. Filozofia është të sigurojë një model abstrakt të njësive statistikore që më tej mund të specializohen për njësi të veçanta statistikore (nëse nevojiten). Kjo ka të bëjë me legjislacionin specifik të temave për të përshkruar nevojat e specializimit të këtij modeli.
Rrjeti, gjeometria dhe mozaiku
Njësitë statistikore mund të përfaqësohen si rrjet qelizash dhe gjeometri vektoriale (pikë, linjë (vijë) dhe poligon). Një numër i konsiderueshëm i njësive statistikore ekzistuese janë njësitë statistikore poligone (sipërfaqe), që formojnë një mozaik. Për aplikimet panevropiane, përshkruhet një rrjet i rekomanduar panevropian.
Përfaqësim në shkallë të gjerë
Njësitë statistikore vektor mund të përfaqësohen nga gjeometri të ndryshme në shkallë të ndryshme.
Struktura hierarkike
Strukturat hierarkike të njësive statistikore mund të përfaqësohen në disa nivele. Lëvizja ndërmjet njësive statistikore të niveleve të njëpasnjëshme është e mundur.
Dimensioni kohor
Evoluimi në kohë i njësive statistikore vektoriale mund të përfaqësohet. Është e mundur gjithashtu të gjurmojmë se si këto njësi kanë ndryshuar në kohë. Evoluimi i njësive statistikore nënkupton dhe mundëson krijimin, fshirjen, modifikimin, bashkimin dhe ndarjen e tyre. Këto ndryshime mund të përfaqësohen në mënyrë të qartë. Kjo përshkruhet më tej në pjesën e përfaqësimit të dimensionit kohor.
Përmbledhja e UML-së
Skema e aplikimit mbi njësitë statistikore përbëhet nga paketa të ndryshme:
Baza: Paketa bazë.
Rrjet: Klasat për të përfaqësuar rrjetet statistikore.
Vektor: Klasat për të përfaqësuar njësitë statistikore që kanë gjeometri vektoriale (pikë, vijë, poligon/sipërfaqe).
Këto paketa importojnë paketat e mëposhtme:
Paketa e tipave bazë e përcaktuar në modelin konceptual.
Gjeometria: Standardi ISO për të përfaqësuar gjeometritë (SSH EN ISO 19107:2005).
Këto paketa përshkruhen në seksionet e mëposhtme.
Njësitë statistikore - Formati bazë
Kjo paketë përmban klasifikimin abstrakt të kategorisë së Njësive Statistikore (shih figurën 3). Një njësi statistikore përcaktohet si një element gjeohapësinor i përdorur për shpërndarjen ose përdorimin e informacionit statistikor.
Figura 3: Diagrami e klasifikimit të paketës UML bazë
Njësitë statistikore mund të karakterizohen nga disa të dhëna statistikore. Modeli i të dhënave ofron dy specializime të klasës së Njësi Statistikore: Rrjeti i qelizave, të përshkruara në paketën Rrjeti dhe Njësitë Statistikore Vektoriale, të përshkruara në paketën Vektor.
3.1.2.2 Njësitë statistikore - Formati rrjet
Kjo paketë (shih figurën 4) përmban klasa për të përfaqësuar rrjetet statistikore (klasa Rrjetet Statistikore) të përbërë nga rrjeti i qelizave (klasa Qeliza e Rrjetit Statistikor).
Figura 4: Diagrami UML e paketës së Rrjetit
Një rrjet statistikor identifikohet nga një identifikues Inspire dhe karakterizohet nga një sistem referues koordinativ (përfaqësuar nga kodi i tij EPSG). Ajo karakterizohet, gjithashtu, nga një rezolucion, i cili mund të jetë një gjatësi, (nëse sistemi i referimit të koordinatave është i projektuar) ose një kënd (nëse sistemi i referimit të koordinatave nuk është i projektuar).
Një kërkesë e rëndësishme, e rrjeteve statistikore është formimi i tyre nga qeliza me sipërfaqe të barabartë, prandaj rrjetet e bazuara në sistemet koordinative referencë, të paprojektuar duhet të përdoren vetëm në hapësira të vogla për të cilat qelizat mbajnë përmasa të krahasueshme.
Përveç kësaj, nëse kërkohet një sistem referimi i rrjetit, rrjeti mund të karakterizohet nga një pikë origjine. Pika e origjinës është pika e poshtme në të majtë të rrjetit. Akset janë paralele me aksin e sistemit referues koordinativ, të orientuar nga e majta në të djathtë dhe nga poshtë - lartë. Dyshja (gjerësi, lartësi) përcakton madhësinë e rrjetit.
Një rrjet statistikor përbëhet nga qeliza të rrjetit statistikor. Qelizat statistikore të rrjetit karakterizohen nga atributet e mëposhtme:
Kodi i qelizës: Ky kod vepron si një identifikues. Rregullat e ndërtimit të tij janë përshkruar më poshtë.
Pozicioni gjeografik: Ky pozicion është pozicioni i qelizës në këndin e poshtëm majtas brenda sistemit koordinativ referues të rrjetit. Pika referuese e një qelize të rrjetit duhet të jetë këndi i poshtëm majtas i rrjetit të qelizës.
Pozicioni i rrjetit: Pozicioni i rrjetit përcaktohet nga tipi i të dhënave Pozicioni i Rrjetit. Është pozicioni i qelizës në sistemin e referimit të rrjetit.
Gjeometria: Kjo gjeometri është një poligon katror, që përfaqëson qelizën e rrjetit.
Ekziston një tepricë informacioni mes atributeve. Natyrisht, të gjitha këto pjesë të ndryshme të informacionit duhet të jenë të qëndrueshme dhe të paktën një nga Kodet e Atributeve, Pozicioni Gjeografik, dhe Pozicioni i Rrjetit.
Përfitimi i përdorimit të këtij kodi qëndron në faktin se ai mundëson rindërtimin e qelizës së rrjetit lehtësisht prej tij. Përfshirja e kodit EPSG brenda kodit mundëson përzierjen e qelizave me CRS të ndryshme në një grup të dhënash.
Për një qelizë të rrjetit, kodi i vlerave të atributeve, Pozicioni Gjeografik, Pozicioni i Rrjetit dhe Gjeometria, duhet të jenë në përputhje së bashku dhe gjithashtu me atributet e rrjetit.
Rrjetet hierarkike
Rrjetet me rezolucione të shumëfishta përfaqësohen nga një strukturë hierarkike përmes dy lidhjeve. Çdo Rrjet Statistikor mund të shoqërohet me një rrjet tjetër statistikor me rezolucion më të lartë ose më të ulët përmes lidhjes së marrëdhënieve hierarkike. Qelizë e Rrjetit Statistikor që i përket një Rrjeti Statistikor të caktuar, është e përbërë nga qeliza mbivendosëse të rrjetit me rezolucion më të ulët të tij dhe krijon qelizën që mbivendoset në rezolucionin më të lartë të rrjetit. Qelizat e rrjetit statistikor të ulët apo të lartë janë lidhur përmes përbërjes hierarkike.
Në raste të ndryshme, kur kërkohet, rrjetet sipas rezolucioneve të ndryshme përfaqësohen nëpërmjet përbërjes hierarkike dhe shoqërimeve të marrëdhënieve hierarkike.
Shembull 1: Në rastet kur një qelizë e një rrjeti të një niveli më të lartë hierarkik, është e lidhur me katër qeliza të një rrjeti të nivelit më të ulët, kjo është një strukturë pemë të dhënash (shih figura 5).
Figura 5: Shembull i rrjetit hierarkik: Një strukturë quad tree
Shembull 2: Figura 6 paraqet një shembull të një rrjeti me shumë rezolucione (nivele hierarkike). Qelizat më të mëdha (rezolucion prej 1 km) janë agregimet e qelizave më të vogla e 4 * 4 (rezolucion 250 m).
Figura 6: Shembull i rrjetit me shumë rezolucione
Një model i përgjithshëm i mbulimit të rrjetit bazuar në SSH EN ISO 19123:2007 është specifikuar në modelin konceptual të përgjithshëm. Ky model nuk është i përshtatshëm për rrjetet statistikore, sepse krahasuar me rrjetet e tjera, rrjetet statistikore nuk përdoren si mbulime në këtë kohë. Qelizat e rrjetit përdoren nga profesionistët, si karakteristika normale për referencën gjeohapësinore. Për më tepër, modeli konceptual i përgjithshëm i rrjetit është shumëdimensional, ndërsa rrjetet statistikore janë vetëm rrjete të thjeshtë dydimensionale. Megjithatë, nëse ekziston nevoja për të përfaqësuar rrjetet statistikore si mbulime, rekomandohet të përdoret modeli konceptual i përgjithshëm për Mbulimi i Rrjetit të Korrigjuar. Për të përfaqësuar mbulimet e rrjeteve statistikore, duhet të përdoret modeli konceptual i përgjithshëm për Mbulimin e Rrjetit të Korrigjuar.
Rrjeti Panevropian
Për aplikimet panevropiane, janë të nevojshëm të specifikohen disa rrjete të përbashkëta evropiane. Rrjetet statistikore të rekomanduara ndjekin sa më shumë të jetë e mundur rekomandimet e specifikimeve të INSPIRE për sistemet e rrjetit gjeografik.
3.1.2.3 Njësitë statistikore - Formati vektor
Kjo paketë lejon përfaqësimin e njësive statistikore të pikës, linjës ose poligonit (shih figurën 7). Këto njësi statistikore vektoriale karakterizohen nga një Inspire Id, të paktën një gjeometri, kodi i shtetit, disa emra të mundshëm gjeografik dhe kanë atribute të përkohshme.
Figura 7 - Diagrami UML për paketën vektor
Një njësi statistikore vektoriale mund të ketë disa gjeometri të specifikuara dhe me shoqërime gjeometrike. Këto gjeometri përfaqësohen nga tipi i të dhënave Gjeometria e Njësisë Statistikore Vektor. Një gjeometri e njësisë statistikore vektoriale karakterizohet nga:
- Nga vetë gjeometria vektoriale (atribut i gjeometrisë). Ky tip atributi është Objekt, siç përshkruhet në SSH EN ISO 19107:2005. Ky standard përdoret gjerësisht në GIS për të përfaqësuar gjeometritë pikë, linjë, sipërfaqe, të plotë etj.
- Një gjeometri (atributi Gjeometria Përshkruese). Gjeometria përshkruese ka një lloj atributi, me vlera midis kodeve Lloji i Gjeometrisë. Fushat me shkallë më të detajuara dhe më pak të detajuara duhet të sigurohen vetëm për përshkrimin e gjeometrisë përshkruese me një lloj Gjeometrie të përgjithësuar (shih figurën 8).
Figura 8: Disa gjeometri të përgjithshme të njësive statistikore të zonës
Kur është e mundur, mund të publikohen disa përfaqësime gjeometrike të njësive statistikore vektoriale.
Janë shtuar kufizimet e mëposhtme:
Çdo njësi statistikore vektoriale nuk mund të ketë më shumë se një gjeometri me një lloj gjeometrie referencë.
Gjeometria përshkruese me llojin e Gjeometrisë së Përgjithshme duhet të jenë shembuj të klasës së Gjeometrisë Përshkruese së Përgjithshme.
Njësitë statistikore vektoriale me një shembull të gjeometrisë së referencës së Multisipërfaqe duhet të jenë raste të klasifikimit të Njësisë Statistikore të Zonës të specializuar.
Për secilën njësi statistikore vektoriale, duhet të përcaktohet saktësisht një gjeometri referencë. Kjo gjeometri referencë është gjeometria “zyrtare” e njësisë statistikore.
Nuk ka asnjë detyrim për të publikuar gjeometrinë referencë: Një ofrues i të dhënave mund të publikojë vetëm një version të përgjithësuar. Në këtë rast, burimi i gjeometrisë duhet të përcaktohet në metadatë (si element i linjës).
Njësitë statistikore të llojit poligon (sipërfaqe) zakonisht organizohen në një strukturë hierarkike (shih figurën 9). Këto njësi statistikore përbëhen nga njësitë statistikore të tjera të po të njëjtit lloj, poligon. Një strukturë e tillë përfaqësohet përmes marrëdhënies hierarkike: një njësi statistikore e një zone të caktuar mund të lidhet me njësitë më të ulëta përbërëse, si dhe me njësitë më të larta që ajo formon.
Figura 9: Hierarkia e njësive statistikore të llojit poligon
Atëherë kur është e mundur, marrëdhëniet ndërmjet njësive statistikore duhet të jepen.
Shënim 1. Një njësi statistikore poligon mund të formojë disa njësi të ndryshme të një niveli më të lartë. siç tregohet në figurën 10: Marrëdhënia kardinale në këtë rast është 0 .. *.
Figura 10: Çdo njësi statistikore mund të formojë disa njësi statistikore të një niveli më të lartë
Shënim 2. Nuk ka asnjë detyrim për të dhënë një gjeometri për njësitë statistikore të niveleve të mësipërme: Një njësi statistikore mund të paraqitet si një përbërje e njësive të tjera statistikore të një niveli më të ulët dhe nuk ka ndonjë detyrim që të sigurohet një gjeometri për këtë njësi të agreguar. Sigurisht, në rast se jepet një gjeometri, kjo gjeometri duhet të jetë një agregim i njësive më të ulëta.
Në shumë grupe të dhënash të njësive statistikore, njësitë statistikore mbulojnë hapësirën gjeografike dhe përbëjnë një mozaik. Lidhje të tilla që formojnë mozaikë përfaqësohen nga rastet e klasës Mozaiku Statistikor. Një mozaik statistikor nuk është një njësi statistikore, por një mbledhje e njësive statistikore me kufizime topologjike (nuk lejohet mbivendosja apo boshllëqet ndërmjet njësive statistikore që formojnë një mozaik statistikor).
Mozaikët statistikorë mund të organizohen në një hierarki, siç tregohet në figurën 11. Lidhja e marrëdhënieve hierarkike lejon lidhjen e mozaikëve të sipërm dhe të poshtëm statistikorë. Marrëdhëniet hierarkike midis mozaikëve statistikorë dhe njësitë e tyre statistikore përbërëse duhet të jenë të qëndrueshme.
Për njësitë statistikore poligon që formojnë një mozaik, duhet të sigurohet një objekt i qartë që përfaqëson këtë mozaik. Mund të jepen marrëdhëniet ekzistuese hierarkike mes këtyre mozaikëve.
Njësitë statistikore poligon shpesh janë ndërtuar nga njësitë administrative. Për të nxjerrë nga një njësi e dhënë statistikore njësinë administrative nga e cila është ndërtuar, ekziston një lidhje drejt klasës së njësisë administrative.
Figura 11: Lidhja ndërmjet njësive statistikore poligon dhe njësive administrative prej të cilave ajo është ndërtuar
Atributet Fillimi i Ciklit Jetësor dhe Përfundimi i Ciklit Jetësor i klasës së Njësisë Statistikore Vektoriale dhe lidhja e prejardhjes së klasës së Njësive Statistikore të Zonave përdoren për të përfaqësuar përkohshmërinë e Njësisë Statistikore Vektoriale. Këto komponentë përshkruhen më tej në seksionin mbi përfaqësimin e dimensionit kohor.
Menaxhimi i identifikuesit
Njësitë statistikore vektoriale, mozaikët statistikorë dhe rrjetet statistikore janë të identifikueshëm nga një identifikues Inspire. Përveç kësaj, qelizat statistikore të rrjetit identifikohen nga një kod dhe njësitë statistikore vektoriale mund të identifikohen me identifikuesit tematikë alternativë.
Përfaqësimi i kohës
Të dhënat statistikore dhe njësitë statistikore ndryshojnë me kalimin e kohës. Ndryshimi i të dhënave statistikore është jashtë qëllimit të këtij dokumenti. Të dhënat statistikore të bashkangjitura në një njësi statistikore duhet të kenë përfaqësimin e tyre kohor, duke përdorur, për shembull, një periudhë kohore që përfaqëson periudhën në të cilën këto të dhëna janë konsideruar reale. Kështu që, vetëm ndryshimet e njësisë statistikore janë marrë në konsideratë në këtë dokument.
Qelizat statistikore të rrjetit dhe rrjetet statistikore nuk ndryshojnë me kalimin e kohës (kjo është një nga përparësitë e përdorimit të tyre). Asnjë përfaqësim kohor nuk kërkohet për to.
Për njësitë statistikore vektoriale, një metodë tradicionale për të paraqitur ndryshimet është që të pranojë një model “të çastit”. Ndryshimet nuk menaxhohen në nivelin e objektit, por në nivelin e të dhënave. Këtu propozohet që evolucioni të përfaqësohet në mënyrë të qartë në nivel objekti. Më poshtë janë paraqitur evolucionet e ndryshme:
- krijimi (shiko fig. 12a);
- fshirje/zhdukje (shiko fig. 12b);
- ndryshimi (shiko fig. 12c) (këtu merren në konsideratë si ndryshimet gjeometrike ashtu edhe ato të atributeve).
Këto ndryshime përfaqësohen përmes atributeve Periudha e Vlefshmërisë, Fillimi i Ciklit Jetësor dhe Përfundimi i Ciklit Jetësor.
Krijimi, ndryshimet dhe fshirja/zhdukja duhet të përfaqësohen, duke përdorur atributet Periudha e Vlefshmërisë, Fillimi i Ciklit Jetësor dhe Përfundimi i Ciklit Jetësor.
Figura 12. Rastet tipike të ndryshimeve të njësive statistikore
Për njësitë statistikore poligon, mund të paraqiten dy zhvillime shtesë:
- agregimi (bashkimi) (shih figurën 12d.), kur disa njësi statistikore bashkohen për të formuar një njësi tjetër;
- ndarja (shih figurën 12e.), kur një njësi statistikore ndahet në një pjesë ose disa të tilla.
Objektet e agreguara dhe të ndara janë të lidhura përmes marrëdhënies origjinë.
Prejardhja e njësive statistikore të agreguara dhe të ndara duhet të përfaqësohet duke përdorur një lidhje me origjinën, me rolet e pasardhësve dhe paraardhësve.
Përfaqësimi i evolucioneve
Elementet e mëparshme mundësojnë përfaqësimin e versioneve të ndryshme të njësive statistikore vektoriale në kohë të ndryshme. Një klasë shtesë, e quajtur Evolucion (shih figurën 13), gjithashtu është e dhënë për të paraqitur në mënyrë të qartë evolucionet që çojnë nga një version në një tjetër.
Figura 13: Evolucioni
Një njësi statistikore vektoriale është e lidhur me objektet e zhvillimit të saj. Format e evolucionit të një njësie statistikore vektoriale përfaqësojnë rrjedhën e ngjarjeve që kanë ndodhur gjatë ciklit të tij jetësor. Një evolucion karakterizohet nga një datë, një vlerë e tipit, midis kodlistave Llojet e Evolucionit dhe dy atributeve në zonën dhe variacionet e popullsisë gjatë evolucionit. Së fundi, një evolucion çon drejt versioneve të ndryshme që ka, fillestare dhe përfundimtare (përmes lidhjeve Versioni Fillestar i Njësive dhe Versioni Përfundimtar i Njësive). Sigurisht, këto role kanë kufizimet e mëposhtme në varësi të llojit të evolucionit:
- një zhvillim i tipit krijim nuk duhet të ketë ndonjë version fillestar të njësisë, por vetëm një final;
- një zhvillim i tipit ndryshim duhet të ketë një version të njësisë fillestare dhe një përfundimtare.
- një zhvillim i tipit fshirje duhet të ketë një version fillestar të njësisë dhe nuk ka një version përfundimtar.
- një zhvillim i tipit agregim duhet të ketë të paktën dy versione të njësisë fillestare (njësitë që duhet të agregohen) dhe një të vetme finale (agregimi që rezulton).
- një zhvillim i tipit ndarje duhet të ketë një version të vetëm të njësisë përfundimtare (njësia për t’u ndarë) dhe të paktën dy të fundit (njësitë që rezultojnë nga ndarja).
Për shkak se objekti i evolucionit paraqet informacion të tepërt tashmë të përfaqësuar në mënyrë absolute nga versionet e ndryshme të objekteve, ekziston një nevojë për kontrollin e qëndrueshmërisë së këtyre objekteve.
Përfaqësimet e evolucionit duhet të jenë në përputhje me versionet e objekteve në fjalë.
Shembull: Nëse një shembull ndryshimi përfaqëson një fshirje objekti në një kohë të dhënë, versioni i fundit i objektit duhet të ketë vlerën e tij të atributit të Periudhës së Vlefshmërisë.fund vendosur në këtë kohë.
3.1.3 Katalogu i tipologjisë
Njësitë statistikore
-- Emri -
Njësitë statistikore
-- Përkufizimi --
Njësi për shpërndarjen ose përdorimin e informacionit statistikor.
-- Përshkrimi --
Burimi: [Direktiva INSPIRE: 2007].
Shembull: Qelizat e rrjetit, pikë, vijë/linjë, poligon.
Shënim. Elementet gjeohapësinorë të çdo skeme aplikimi nga Inspire mund të konsiderohen si një njësi statistikore, sepse të gjitha mund të përdoren si referencë gjeohapësinore. Kjo klasë ofrohet për të paraqitur karakteristikat që përdoren vetëm për të shpërndarë informacion statistikor dhe që nuk janë të përfshira në një skemë tjetër aplikimi të Inspire.
-- Tipi i elementit --
Feature Type
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga “featureType” NjësiëtStatistikoreVektor te “featureType” NjësitëStatistikore
Gjeneralizuar nga “featureType” ElementetStatistikoreTëRrjetit te “featureType” NjësitëStatistikore
LIDHJE
Lidhje (drejtimi: Burimi-> Objektivi)
-- Përkufizimi --
Njësia statistikore bazë, në të cilën referohen statistikat e Shëndetit Mjedisor.
Burimi: (Class) TëDhënatStatistikorePërShendetin“featureType”
Objektivi: “version” NjësiAgregimi (Class) NjësitëStatistikore “featureType”
Shumëllojshmëria: [1]
-- Përkufizimi --
Njësia statistikore bazë, në të cilën referohen statistikat e Shëndetit Mjedisor.
Lidhje (drejtimi: Burimi -> Objektivi) “Versioni”
Burimi:(Class) Dimensionet “dataType”
Objektivi: Hapësirë (Class) NjësitëStatistikore “featureType”
Shumëllojshmëria: [1]
-- Emri --
Gjeohapësinor
-- Përkufizimi --
Dimensioni gjeohapësinor i vlerës statistikore.
3.1.3.2 Rrjeti statistikor
-- Emri --
Rrjeti statistikor
-- Përkufizimi --
Një rrjet i përbërë nga qeliza statistikore.
-- Përshkrimi --
Një rrjet i tillë lidhet me një rrjet më të lartë, që ka një rezolucion më të madh dhe një rrjet më të ulët që ka një rezolucion më të vogël. Disa rrjete statistikore janë organizuar në një hierarki të rrjeteve me rezolucione të ndryshme. Qelizat që përbëjnë dy rrjete të lidhura duhet të plotësojnë disa kufizime topologjike: çdo element i rrjetit të lartë duhet të jetë bashkimi i elementeve të rrjetit më të ulët.
-- Tipi i elementit --
Feature Type
LIDHJE STRUKTURORE TË BRENDSHME
Agreguar nga “feature Type” ElementetStatistikoreTëRrjetit te “feature Type” RrjetiStatistikor
ATRIBUTET
InspireId: Identifikues
Shumëllojshmëria: [1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i objektit të jashtëm është një identifikues unik i objektit i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikimet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
KodiEPSG: Integer
Shumëllojshmëria: [0..1]
-- Emri --
EPSGCode
-- Përkufizimi --
Kodi EPSG për të identifikuar sistemin koordinativ referencë të rrjetit.
-- Përshkrimi --
Ky informacion është i rëndësishëm vetëm nëse të gjitha qelizat e rrjetit kanë të njëjtin CRS.
[I detyrueshëm: PO]
Rezolucion: RezolucioniIRrjetitStatistikor
Shumëllojshmëria: [0..1]
-- Emri --
Resolution
-- Përkufizimi --
Rezolucioni i rrjetit.
-- Përshkrimi --
Ky informacion është i rëndësishëm vetëm nëse të gjitha qelizat e rrjetit kanë të njëjtin rezolucion.
[I detyrueshëm: PO]
Origjina: PozicioniDirekt
Shumëllojshmëria: [0..1]
-- Emri --
Origjina
-- Përkufizimi --
Pozicioni i pikës së origjinës së rrjetit në sistemin koordinativ referencë të specifikuar (nëse është përcaktuar).
-- Përshkrimi --
Pika e origjinës është pika e ulët në të majtë të rrjetit.
[I detyrueshëm: PO]
Gjerësia: Integer
Shumëllojshmëria: [0..1]
-- Emri --
Gjerësia
-- Përkufizim--
Gjerësia e rrjetit, në numrin e qelizës (nëse përcaktohet).
[I detyrueshëm: PO]
Lartësia: Integer
Shumëllojshmëria: [0..1]
-- Emri --
Lartësia
-- Përkufizimi --
Lartësia e rrjetit, në numrin e qelizës (nëse përcaktohet).
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtimi: Dydrejtimësh) Relacioni hierarkik
-- Përkufizimi --
Lidhja hierarkike midis rrjeteve statistikore.
Burimi: “voidable” poshtë (Class) RrjetiStatistikor “featureType”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rrjeti statistikor më i ulët.
Objektivi: “voidable” lart (Class) RrjetiStatistikor “featureType”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rrjeti statistikor më i lartë.
Lidhje (Drejtimi: Dydrejtimësh) Relacioni hierarkik
-- Përkufizimi --
Lidhja hierarkike midis rrjeteve statistikore.
Burimi: “voidable” poshtë (Class) RrjetiStatistikor “featureType”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rrjeti statistikor më i ulët.
Objektivi: “voidable” lart (Class) RrjetiStatistikor “featureType”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rrjeti statistikor më i lartë.
3.1.3.3 Njësitë statistikore vektor
--Emri-
Njësitë statistikore vektor
-- Përkufizimi --
Njësia statistikore e përfaqësuar si një gjeometri vektoriale (pikë, vijë/linjë ose poligon/sipërfaqe).
-- Tipi i elementit --
Feature Type
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga “feature Type” NjësitëStatistikoreVektor te “feature Type” NjësitëStatistikore
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga “feature Type” ZonatENjësiveStatistikore te “feature Type” NjësitëStatistikoreVektor
ATRIBUTET
Emërtimi Gjeografik: Emërtimet Gjeografike
Shumëllojshmëria:[0..*]
--Emri-- Emërtimi gjeografik
--Përkufizimi-- Emërtimet gjeografike të mundshme për objektin.
[ I detyrueshëm: PO]
Fillimi i Ciklit Jetësor: Datë-Orë
Shumëllojshmëria: [1]
--Emri-- Fillimi i ciklit jetësor
--Përkufizimi-- Data dhe koha në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
Identifikuesi Tematik: Identifikuesi Tematik
Shumëllojshmëria: [0..*]
--Emri-- Identifikuesi tematik
-- Përkufizimi -
Identifikues unik i objektit përshkrues që zbatohet në objektet gjeohapësinore në një temë informacioni të përcaktuar.
-- Përshkrimi --
Disa njësive statistikore mund t’u caktohen identifikues të shumëfishtë.
Shembull: Kodet e NUTS janë identifikues tematikë.
[I detyrueshëm:PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
--Emri-- Inspire Id
-- Përkufizimi --
Identifikuesi i jashtëm i objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i jashtëm është një identifikues unik i objektit i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
Përfundimi i Ciklit Jetësor: Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i Ciklit Jetësor
-- Përkufizimi -
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: JO]
Periudha e Vlefshmërisë: Periudhë
Shumëllojshmëria:[0..1]
--Emri-- Periudha e vlefshmërisë
-- Përkufizimi --
Periudha kur supozohet që njësia statistikore të përdoret ose jo.
[I detyrueshëm: PO]
Periudha Referuese: Periudhë
Shumëllojshmëria:[1]
--Emri-- Periudha e referencës
-- Përkufizimi --
Periudha kur të dhënat duhet të japin një pamje të ndarjes territoriale në njësi statistikore.
[I detyrueshëm: PO]
Vendi: Kodi i Shtetit
Shumëllojshmëria:[ 1]
-- Emri --
Vendi/Shteti
-- Përkufizimi--
Kodi i vendit të cilit i përket objekti.
[I detyrueshëm: PO]
LIDHJE
Lidhje (drejtimi: Burimi -> Objektivi)
Burimi:(Class) NjësitëStatistikoreVektor “featureType”
Objektivi: Gjeometria (Class) GjeometriaENjësisëStatistikoreVektor “dataType”
Shumëllojshmëria: [1..*]
-- Emri --
Gjeometria
-- Përkufizimi --
Përfaqësitë gjeometrike të njësisë statistikore vektoriale.
Lidhje (drejtimi: Burimi -> Objektivi) “version”
Burimi: (Class) Evolucion “voidable”
Objektivi: “voidable” Versioni i Njësisë Fillestare (Class) Njësitë Statistikore Vektor “feature Type”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha versionet e njësisë fillestare të prekura nga evolucioni.
Lidhje (drejtimi: Dydrejtime)
-- Përkufizimi --
Shoqërimet ndërmjet një njësie strukturore bazë dhe gjithë ndryshimet që ndodhin në të.
Burimi: “voidable” Evolucionet (Class) Evolucion “voidable”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha ndryshimet që ka hasur njësia statistikore.
Objektivi: “voidable” Njësitë (Class) Njësitë Statistikore Vektor “featureType”
Shumëllojshmëria: [1..*]
-- Përkufizimi --
Të gjitha njësitë e prekura nga evolucioni.
Lidhje (drejtimi: Burimi -> Objektivi) “version”
Burimi: (Class) Evolucion “voidable”
Objektivi: “voidable” Versioni i Njësisë Përfundimtare (Class) Njësitë Statistikore Vektor “featureType”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha versionet e njësisë përfundimtare të prekura nga evolucioni.
3.1.3.4 Evolucion
-- Emri --
Evolucion
-- Përkufizimi --
Përfaqësimi i evolucionit të njësisë statistikore vektoriale.
-- Tipi i elementit --
Feature Type
ATRIBUTET
Data: Datë-Orë
Shumëllojshmëria: [1]
--Emri-- Data
-- Përkufizimi --
Data kur ndodh ndryshimi.
[I detyrueshëm: PO]
Lloji i Evolucionit: VleratELlojittëEvolucionit
Shumëllojshmëria: [1]
--Emri-- Lloji i evolucionit
--Përkufizimi-- Lloji i evolucionit.
[I detyrueshëm: PO]
Variacioni i Popullsisë: Integer
Shumëllojshmëria: [1]
--Emri-- Ndryshimi i popullsisë
-- Përkufizimi --
Ndryshimet e popullsisë gjatë evolucionit. Ky atribut duhet të jetë i populluar vetëm nëse lloji është “ndryshim”.
[I detyrueshëm: PO]
Variacioni i Zonës: Zona
Shumëllojshmëria: [1]
--Emri-- Variacioni i zonës
-- Përkufizimi --
Variacioni i zonës gjatë evolucionit. Ky atribut duhet të jetë i populluar vetëm nëse lloji është “ndryshim”.
[I detyrueshëm: PO]
LIDHJE
Lidhje (drejtimi: Burimi-> Objektivi) “version”
Burimi:(Class) Evolucion “voidable”
Objektivi: “voidable” Versionet e Njësisë Fillestare (Class) Njësitë Statistikore Vektor “feature Type”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha versionet e njësisë fillestare të prekura nga evolucioni.
Lidhje (drejtimi: Dy drejtime)
-- Përkufizimi --
Shoqërimet ndërmjet një njësie strukturore bazë dhe gjitha ndryshimet që ndodhin në të.
Burimi: “voidable” Evolucionet (Class) Evolucion “voidable”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha ndryshimet që ka hasur njësia statistikore.
Objektivi: “voidable” Njësitë (Class) Njësitë Statistikore Vektor “feature Type”
Shumëllojshmëria: [1..*]
--Përkufizimi --
Të gjitha njësitë e prekura (që ndikohen) nga evolucioni.
Lidhje (drejtimi: Burimi-> Objektivi) “version”
Burimi:(Class) Evolucion “voidable”
Objektivi: “voidable” Verisoni i Njësisë Përfundimtare (Class) Njësitë Statistikore Vektor “feature Type”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Të gjitha versionet e njësisë përfundimtare të prekura nga evolucioni.
3.1.3.5 Elementet statistikorë të rrjetit
-- Emri --
Elementet statistikorë të rrjetit
-- Përkufizimi --
Njësia për shpërndarjen ose përdorimin e informacionit statistikor që përfaqësohet si një element i rrjetit.
-- Përshkrimi --
Një element statistikor i rrjetit është i lidhur me:
- elementet e rrjetit unik statistikor të nivelit të tij të lartë (nëse ka) të mbuluara;
- elementet e rrjetit statistikor të nivelit të ulët (nëse ka) të mbuluara.
Shembull: Në një strukturë katror, disa elemente janë të lidhura me katër elemente në të cilat ato dekompozohen.
-- Tipi i elementit --
Feature Type
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga “feature Type” Elementet Statistikore të Rrjetit te “feature Type” Njësitë Statistikore
Agreguar nga “feature Type” Elementet Statistikore të Rrjetit te “feature Type” Rrjeti Statistikor
Agreguar nga “feature Type” Elementet Statistikore të Rrjetit te “feature Type” Elementet Statistikore të Rrjetit
-- Përkufizimi --
Përbërja hierarkike midis qelizave të rrjetit statistikor.
LIDHJE STRUKTURORE TË BRENDSHME
Agreguar nga “feature Type” Elementet Statistikore të Rrjetit tek “feature Type” Elementet Statistikore të Rrjetit
-- Përkufizimi --
Përbërja hierarkike midis qelizave të rrjetit statistikor.
ATRIBUTET
Kodi: Tekst
Shumëllojshmëria: [1]
-- Emri --
Kodi
-- Përkufizimi --
Një kod qelizash
-- Përshkrimi --
Ky kod përbëhet nga:
1. Një pjesë e sistemit referencë të koordinatave, e përfaqësuar nga fjala CRS, e ndjekur nga kodi EPSG.
2. Rezolucioni në pozicionin e qelizës:
- Nëse parashikohet sistemi i referimit të koordinatave, fjala RES pasuar nga zgjidhja e rrjetit në metra dhe shkronja M. Pastaj, shkronja N e ndjekur nga vlera veriore në metra dhe shkronja E e ndjekur nga vlera e lindjes në metra.
- Nëse sistemi i referencës së koordinatave nuk është i projektuar, fjala RES pasohet nga zgjidhja e rrjetit në shkallë-minutë-sekondë, e ndjekur nga fjala DMS. Pastaj fjala LON e ndjekur nga vlera e gjatësisë në minutën e shkallës së dytë dhe fjala LAT e ndjekur nga vlera e gjerësisë në minutën e shkallës së dytë.
Për të dyja rastet, pozicioni i dhënë është pozicioni i qosheve të qelizës së poshtme në të majtë.
Shënim. Ky kod vepron si një identifikues.
[I detyrueshëm: PO]
Pozicioni Gjeografik: Pozicioni direkt
Shumëllojshmëria: [1]
-- Emri --
Pozicioni gjeografik
-- Përkufizimi --
Elementet e rrjetit qëndrojnë në pozitën gjeografike të këndit të majtë.
[I detyrueshëm: PO]
Pozicioni i Rrjetit: Pozicioni i rrjetit
Shumëllojshmëria: [0..1]
-- Emri --
Pozicioni i rrjetit
-- Përkufizimi --
Pozicionimi i qelizave të rrjetit brenda rrjetit bazuar në koordinatat e rrjetit.
[I detyrueshëm: PO]
Gjeometria: Poligon
Shumëllojshmëria: [ ]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria e qelizave të rrjetit.
[I detyrueshëm: PO]
3.1.3.6 Gjeometria e njësisë statistikore vektor
--Emri-- Gjeometria e njësisë statistikore vektor
-- Përkufizimi --
Një përfaqësim gjeometrik për njësitë statistikore vektoriale.
-- Përshkrimi --
Njësitë statistikore vektor mund të kenë disa përfaqësime në varësi të kontekstit për të cilin ato përdoren. Këshillohet që të prodhohet të paktën një gjeometri referimi.
Shembulli 1: Një njësi statistikore vektoriale mund të përfaqësohet si nga një gjeometri poligon ashtu edhe nga një gjeometri pikë. Një pikë e tillë mund të jetë qendra e gravitetit ose një vendndodhje etike ose shenjë.
Shembulli 2: Për hartëzimin, kërkohet paraqitje e përgjithshme e njësive statistikore vektoriale. Këto gjeometri varen nga shkalla e vizualizimit.
-- Tipi i elementit --
Data Type
ATRIBUTET
Gjeometria: GM_Objekt
Shumëllojshmëria: [1]
--Emri-- Gjeometria
-- Përkufizimi --
Gjeometria
[I detyrueshëm: PO]
GjeometriaPërshkruese: GjeometriaPërshkruese
Shumëllojshmëria: [1]
--Emri-- Gjeometria përshkruese
-- Përkufizimi --
Përshkrimi i gjeometrisë së njësisë statistikore.
[I detyrueshëm: PO]
LIDHJE
Lidhje (drejtimi: Burimi -> Objektivi)
Burimi: (Class) Njësitë Statistikore Vektor “feature Type”
Objektivi: Gjeometria (Class) Gjeometria e Njësisë Statistikore Vektor “data Type”
Shumëllojshmëria: [1..*]
-- Emri --
Gjeometria
-- Përkufizimi --
Përfaqësitë gjeometrike të njësisë statistikore vektoriale.
3.1.3.7 Gjeometria përshkruese
-- Emri --
Gjeometria përshkruese
-- Përkufizimi --
Gjeometria përshkruese e njësisë statistikore vektoriale.
-- Tipi i elementit --
Data Type
ATRIBUTET
Llojet e Gjeometrisë: Vlerat e llojeve të gjeometrisë
Shumëllojshmëria: [1]
--Emri-- Llojet e gjeometrisë
--Përkufizimi --
Llojet e gjeometrisë.
[I detyrueshëm: PO]
Shkalla më e Detajuar: Integer
Shumëllojshmëria: [0..1]
-- Emri --
Shkalla më e detajuar
-- Përkufizimi --
Shkalla më e detajuar për të cilën, gjeometria e përgjithësuar supozohet të jetë e përshtatshme (e shprehur si inversi i shkallës treguese).
[I detyrueshëm: PO]
Shkalla më e vogël: Integer
Shumëllojshmëria: [0..1]
-- Emri --
Shkalla më e vogël
-- Përkufizimi --
Shkalla më e vogël e detajuar për të cilën, gjeometria e përgjithësuar supozohet të jetë e përshtatshme (e shprehur si inversi i shkallës treguese).
[ I detyrueshëm:PO]
3.1.3.8 Mozaiku statistikor
--Emri-
Mozaiku statistikor
-- Përkufizimi --
Një mozaik i përbërë nga njësitë statistikore të një zone.
--Përshkrimi-
Shembull: Mbulimi i rajoneve NUTS
-- Tipi i elementit --
Feature Type
LIDHJE STRUKTURORE TË BRENDSHME
Agreguar nga “feature Type” ZonatENjësive Statistikore te “feature Type” MozaikuStatistikor
-- Përkufizimi--
Përbërja ndërmjet një mozaiku statistikor dhe njësive të saj statistikore të zonës së kompozimit.
ATRIBUTET
InspireId: Identifikues
Shumëllojshmëria: [1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikuesi i jashtëm i objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i jashtëm është një identifikues unik i objektit i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
LIDHJE
Lidhje (drejtimi: Dy drejtime) Lidhje hierarkike
-- Përkufizimi --
Lidhja hierarkike midis mozaikimit statistikor.
Burimi: “voidable” Rënia (Class) Mozaiku Statistikor “feature Type”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rënia e menjëhershme e mozaikimit statistikor.
Objektivi: “voidable” ngritja (Class) Mozaiku Statistikor “feature Type”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Ngritja e menjëhershme e mozaikimit statistikor.
Lidhje (drejtimi: Dy drejtime) Lidhje hierarkike
-- Përkufizimi --
Lidhja hierarkike midis mozaikimit statistikor.
Burimi: “voidable” Rënia (Class) Mozaiku Statistikor “featureType”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Rënia e menjëhershme e mozaikimit statistikor.
Objektivi: “voidable” ngritja (Class) Mozaiku Statistikor “feature Type”
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Ngritja e menjëhershme e mozaikimit statistikor.
3.1.3.9 Njësitë statistikore poligon/sipërfaqe
-- Emri --
Njësitë statistikore poligon/sipërfaqe
-- Përkufizimi --
Njësitë statistikore vektor me një gjeometri referencë sipërfaqësore.
-- Përshkrimi --
Objekti i tillë mund të përbëhet nga njësia statistikore e zonës tjetër.
Shembull: Sipërfaqja e një vendit, një njësi administrative, një rajon NUTS.
-- Tipi i elementit -
Feature Type
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga “feature Type” Zonat e Njësive Statistikore te “feature Type” Njësitë Statistikore Vektor
Agreguar nga “feature Type” Zonat e Njësive Statistikore te “feature Type” Mozaiku Statistikor
-- Përkufizimi --
Përbërja ndërmjet një mozaiku statistikor dhe njësive të saj statistikore që e kanë kompozuar.
Agreguar nga “feature Type” Zonat e Njësive Statistikore te “feature Type” Zonat e Njësive Statistikore
-- Përkufizimi --
Përbërja hierarkike midis njësive statistikore.
LIDHJE STRUKTURORE TË BRENDSHME
Agreguar nga “feature Type” Zonat e Njësive Statistikore te “feature Type” Zona e Njësive Statistikore
-- Përkufizimi --
Përbërja hierarkike midis njësive statistikore.
ATRIBUTET
Vlerat e Sipërfaqes: Sipërfaqe
Shumëllojshmëria: [1]
--Emri-- Vlerat e sipërfaqes
-- Përkufizimi --
Zona e gjeometrisë referencë.
[I detyrueshëm: PO]
Vlerat e Sipërfaqes Tokësore: Sipërfaqe
Shumëllojshmëria: [1]
--Emri-- Vlerat e sipërfaqes tokësore
-- Përkufizimi --
Pjesa e sipërfaqes mbi ujë.
[I detyrueshëm: PO]
Vlerat e Sipërfaqes së Jetueshme: Sipërfaqe
Shumëllojshmëria: [1]
-- Emri --
Vlerat e sipërfaqes së jetueshme
-- Përkufizimi --
Sipërfaqja e pjesës së jetueshme.
[I detyrueshëm: PO]
LIDHJE
Lidhje (drejtimi: Dy drejtime) Informacion i Ciklit Jetësor Prejardhje
-- Përkufizimi --
Lidhja e prejardhjes midis njësive të agreguara dhe të ndara.
Burimi: voidable Pasardhësit (Class) Zonat e Njësive Statistikore featureType
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Pasardhësit e njësisë statistikore poligon.
Objektivi: voidable Paraardhësit (Class) Zonat e Njësive Statistikore featureType
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Paraardhësit e njësisë statistikore poligon.
Lidhje (drejtimi: Burimi -> Objektivi)
Burimi: (Class) Zonat e Njësive Statistikore “featureType”
Obektivi: “voidable” Njësitë Adminsitrative (Class) Njësitë Administrative “featureType”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Njësitë administrative të përdorura për të formuar njësinë statistikore poligon.
Lidhje (drejtimi: Dy drejtime) Informacion i Ciklit Jetësor Prejardhja
-- Përkufizimi --
Lidhja e prejardhjes midis njësive të agreguara dhe të ndara.
Burimi: “voidable” Pasardhësit (Class) Zonat e Njësive Statistikore “feature Type”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Pasardhësit e njësisë statistikore poligon.
Objektivi: “voidable” Paraardhësit (Class) Zonat eNjësive Statistikore “feature Type”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Paraardhësit e njësisë statistikore poligon.
3.1.3.10 Pozicioni i rrjetit
-- Emri --
Pozicioni i rrjetit
-- Përkufizimi --
Një pozicion i qelizave të rrjetit brenda një rrjeti.
-- Tipi i elementit --
Data Type
ATRIBUTET
x: Integer
Shumëllojshmëria: [1]
-- Emri --
Vlerat e aksit x
-- Përkufizimi --
Pozicioni i qelizës në boshtin horizontal, duke filluar nga ana e majtë, në të djathtë, nga 0 deri në gjerësinë e rrjetit -1.
[I detyrueshëm: PO]
y: Integer
Shumëllojshmëria: [1]
-- Emri--
Vlerat e aksit y
-- Përkufizimi --
Pozicioni i qelizës në boshtin vertikal, duke filluar nga poshtë-lart, nga 0 deri në lartësinë e rrjetës -1.
[I detyrueshëm: PO]
3.1.3.11 Rezolucioni i rrjetit statistikor
-- Emri --
Statistical grid resolution
-- Përkufizimi --
Vlera e rezolucionit të njësisë statistikore.
-- Përshkrimi --
Rezolucioni mund të jetë një distancë ose një kënd.
-- Tipi i elementit --
Union
ATRIBUTET
Rezolucioni i Gjatësisë: Gjatësi
Shumëllojshmëria: [1]
-- Emri --
Rezolucioni i gjatësisë
-- Përkufizimi --
Një rezolucion në gjatësi.
[I detyrueshëm: PO]
Rezolucioni i Këndit: Kënd
Shumëllojshmëria: [1]
-- Emri --
Rezolucioni i këndit
-- Përkufizimi-
Një rezolucion këndi.
[I detyrueshëm: PO]
3.1.3.12 Vlerat e llojeve të gjeometrisë
-- Emri --
Vlerat e llojeve të gjeometrisë
-- Përkufizimi--
Vlerat e kodit për llojet e gjeometrisë.
-- Tipi i elementit -
Kodlistë
3.1.3.13 Vlerat e llojit të evolucionit
--Emri-- Vlerat e llojit të evolucionit
-- Përkufizimi -
Vlerat e kodit për llojet e evolucionit.
-- Tipi i elementit -
Kodlistë
3.2 Metadata
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3 Kodi EPSG për KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare, sipas vendimit nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si metadatë” ndryshuar me vendimet e Këshillit të Ministrave nr. 322, datë 27.4.2016 dhe nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është: EPSG - 6870.
3.4 Cilësia e të dhënave
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur për të vlerësuar dhe dokumentuar cilësinë e tyre për grupet e të dhënave që lidhen me temën “Njësitë statistikore”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku pronat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit;
- vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore;
- për të specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore që lidhen me temën “Njësitë statistikore”.
Tabela e mëposhtme, paraqet të gjitha elementet dhe nën elementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, dataset-it ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën e “Sfera e Vlerësimit”.
Masat që do të përdoren për secilën nga nën elementet e listuara të cilësisë së të dhënave janë përcaktuar në nën seksionet e mëposhtme.
Tabela - Elementet e cilësisë së të dhënave të përdorura në temën “Njësitë statistikore” të të dhënave gjeohapësinore
Pjesa
Elementi i cilësisë së të dhënave
Nën elementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
7.1.1
Kompletimi
Komision
Të dhëna të tepërta të pranishme në grupin e të dhënave, siç përshkruhet nga fushëveprimi.
Grupet e të dhënave
7.1.2
Kompletimi
Përjashtimi
Të dhënat që mungojnë nga grupi i të dhënave, siç përshkruhet nga fushëveprimi.
Grupet e të dhënave
7.1.3
Përputhja logjike
Përputhja topologjike
Korrektësia e topologjisë së koduar në mënyrë të qartë, karakteristikat e grupeve të të dhënave, siç përshkruhet nga fushëveprimi.
Grupet e të dhënave
7.1.4
Saktësia pozicionale
Saktësia absolute ose e jashtme.
Aftësia e vlerave të koordinatës së raportuar, për vlerat e pranuara si ose të qenët të vërteta.
Grupet e të dhënave
7.1.5
Saktësia tematike
Korrektësia e klasifikimit
Karakteristikat e krahasimit të klasave të caktuara ose atributet e tyre në një univers ligjërimi.
Grupet e të dhënave
7.1.6
Cilësia e kohës
Vlefshmëria e dimensionit kohor
Vlefshmëria e të dhënave të përcaktuara nga fushëveprimi në lidhje me kohën.
Grupet e të dhënave
3.4.1 Kompletimi - Autorizimi (Completness - Commission)
Rekomandim
Autorizimi duhet të vlerësohet dhe dokumentohet, duke përdorur normën e artikujve të tepërt, siç specifikohet në tabelat e mëposhtme.
Emri
Norma e artikujve të tepërt
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletimi
Cilësia e të dhënave të nënelementeve
Autorizimi
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numri i artikujve të tepërt në grupin e të dhënave, në lidhje me numrin e artikujve që duhet të ishin të pranishëm
Përshkrimi
-
Fusha e vlerësimit
Grupi i të dhënave
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
E vërtetë, përqindje, përpjesëtim (shembull: 0,0189; 98,11%; 11:582)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
-
Shembulli
-
Masa identifikuese
3 (ISO 19138)
3.4.2 Kompletimi - Përjashtimi (Completness - Ommission)
Rekomandim
Përjashtimi duhet të vlerësohet dhe dokumentohet, duke përdorur normën e artikujve që mungojnë siç specifikohet në tabelat e mëposhtme.
Emri
Norma e artikujve që mungojnë
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletimi
Cilësia e të dhënave të nënelementeve
Përjashtimi
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numri i artikujve që mungojnë në grupin e të dhënave, në lidhje me numrin e artikujve që duhet të ishin të pranishëm
Përshkrimi
-
Fusha e vlerësimit
Grupi i të dhënave
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
E vërtetë, përqindje, përpjesëtim (shembull: 0,0189; 98,11%; 11:582)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
-
Shembulli
-
Masa identifikuese
7 (ISO 19138)
3.4.3 Përputhja logjike - Përputhja topologjike (Logical consistency - Topological consistency)
Rekomandim
Përputhja topologjike duhet të vlerësohet dhe dokumentohet, duke përdorur thyerje të përcaktuar në tabelën e mëposhtme:
Emri
Thyerjet
Emri alternativ
Thyerje
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja topologjike
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizim
Një thyerje është një zonë e padëshiruar, që e hasim kur sipërfaqet kufitare nuk janë digjitalizuar siç duhet. Kufijtë e këtyre sipërfaqeve mund të jenë të paqëndrueshëm ose të kenë mbivendosje me sasi të vogla që shkakton një gabim topologjik.
Përshkrimi
Kjo cilësi të dhënash ka 2 parametra:
- madhësia maksimale e thyerjeve;
- koeficienti i trashësisë.
Koeficienti i trashësisë do të jetë një numër real midis 0 dhe 1. Ky koeficient përcaktohet nga formula e mëposhtme:
T është përcaktuar si: T= 4π sipërfaqe/perimetër2
T vlerat janë brenda [0,1]. 1 korrespondojnë me një rreth dhe 0 me një vijë/linjë segment.
Koeficienti i trashësisë është i pavarur nga madhësia e sipërfaqes dhe sa më afër vlerës 0, aq më e hollë duhet të jetë sipërfaqja e zgjedhur e pllakës. Zona maksimale përcakton kufirin e sipërm të një pjese. Kjo është për të parandaluar sipërfaqet me perimetrin sinus dhe zonat e mëdha nga të qenët të gabuar si thyerje.
Fusha e vlerësimit
Grupi i të dhënave
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
Instituti i Kërkimeve të Sistemeve Mjedisore, Inc. (ESRI) GIS Data ReViewer 4.2 Udhëzuesi i përdoruesit
Shembulli
Zgjedhja:
Largimin e vijës/linjës së vetme;
Largimin e vijës/linjës së dyfishtë:
parametri maksimal i zonës pengon portretizimin e saktë të vijës/linjës së dyfishtë nga të qenit i shënjuar si një gabim.
Zgjedhja:
Rërë;
Thyerje;
Largimin e vijës/linjës së dyfishtë:
thyerja është më pak se parametri maksimal dhe është shënuar për vlerësimin e gabimit të mundshëm.
Masa identifikuese
25
3.4.4 Saktësia pozicionale - Saktësia absolute ose e jashtme (Positional accuaracy - Absolute or extrenal accuaracy)
Rekomandim
Saktësia absolute ose e jashtme duhet të vlerësohet dhe dokumentohet duke përdorur saktësinë pozicionale, siç specifikohet në tabelën e mëposhtme:
Emri
Saktësia pozicionale
Emri alternativ
-
Cilësia e të dhënave të elementeve
Saktësia pozicionale
Cilësia e të dhënave të nënelementeve
Saktësi absolute ose e jashtme
Cilësia e të dhënave të matjeve themelore
Nuk aplikohet
Përkufizim
Vlera mesatare e pasigurive pozicionale për një grup pozicionesh, ku pasiguritë pozicionale përcaktohen si distanca ndërmjet një pozicioni të matur dhe atij që konsiderohet si pozicioni i vërtetë.
Fusha e vlerësimit
Grupi i të dhënave
Fusha e raportimit
Grupi i të dhënave
Përshkrimi
Gabimi Mesatar Kuadratik (GMK = RMSE në anglisht) është rrënja katrore e mesatares së ndryshimeve në katror ndërmjet vlerave të koordinatave të një grupi të dhënash të matura dhe vlerave të koordinatave nga një burim i pavarur i saktësisë më të lartë për pikat identike. GMK dallon dy raste:
Rasti 1 - Kur llogariten gabimet e mundshme vi
: :
Ku:
vi - gabimi i mundshëm që llogaritet si diferencë e vlerës përfaqësuese me vlerën e matur.
- vlera përfaqësuese që merret si vlera mesatare e vlerave të matura xi
n - numri i matjeve
Saktësia pozicionale e përcaktuar nga të dhënat e kontrolluara:
- Saktësia horizontale
ku:
janë koordinat horizontale e pikave të kontrolluara në grupin e të dhënave;
- janë koordinatat e pikave të kontrolluara nga burime të pa varuara të një saktësie më të lartë;
- është numri i pikave të testuara;
- është numri përkatës i pikës.
Gabimi horizontal i pikës përcaktohet nga:
Nëse nga llogaritjet kemi ,
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale dhe të pavarura në secilin komponent (x, z) një koeficient (faktor) 2.4477 përdoret për të llogaritur saktësinë horizontale me nivel besimi 95% (Greenwalt and Schultz 1968). Kur zbatohen kushtet e mësipërme,, vlera e saktësisë horizontale referuar NSSDA duhet të llogaritet nga formula:
Saktësia vertikale
ku:
janë koordinata vertikale e pikave të kontrolluara në grupin e të dhënave;
- janë koordinata vertikale e pikave të kontrolluara nga burime të pavaruara të një saktësie më të lartë;
- është numri i pikave të testuara;
- është numri përkatës i pikës.
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale, një koeficient (faktor) 1.9600 përdoret për të llogaritur saktësinë vertikale me nivel besimi 95% (Greenwalt and Schultz 1968). Nga kjo, saktësia vertikale, e raportuar sipas NSSDA duhet të llogaritet nga formula:
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Matjet
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
-
Shembulli
-
Masa identifikuese
28
3.4.5 Saktësia tematike - Korrektësia e klasifikimit (Thematic accuaracy - Classification correctenss)
Rekomandim
Korrektësia e klasifikimit duhet të vlerësohet dhe të dokumentohet, duke përdorur saktësinë tematike, siç specifikohet në tabelën e mëposhtme:
Emri
Saktësia tematike
Emri alternativ
-
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Korrektësia e klasifikimit
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numri i karakteristikave të klasifikuara gabimisht, në lidhje me numrin e karakteristikave që supozohet të jenë të pranishme
Përshkrimi
-
Fusha e raportimit
Grupi i të dhënave
Fusha e vlerësimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
E vërtetë, përqindje, përpjesëtim
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
-
Shembulli
-
Masa identifikuese
61
3.4.6 Cilësia e kohës - Vlefshmëria e kohës (Temporal quality - Temporal validity)
Rekomandim
Vlefshmëria e kohës duhet të vlerësohet dhe të dokumentohet, duke përdorur saktësinë e kohës, siç specifikohet në tabelën e mëposhtme:
Emri
Saktësia e Kohës
Emri alternativ
-
Cilësia e të dhënave të elementeve
Saktësia e kohës
Cilësia e të dhënave të nënelementeve
Vlefshmëria e kohës
Cilësia e të dhënave të matjeve themelore
Treguesi i korrektësisë
Përkufizimi
Tregon nëse një artikull është në përputhje me domenin e vlerës së tij
Përshkrimi
-
Fusha e raportimit
Grupi i të dhënave
Fusha e vlerësimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Bolean (True tregon se një artikull është në përputhje me domeinin e vlerës së tij)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
-
Shembulli
-
Masa identifikuese
15
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
NJËSITË STATISTIKORE
3.1.4.1
Statistical Unit
Njësitë Statistikore
Njësitë Statistikore
Feature Type
3.1.4.2
Statistical Grid
Rrjeti Statistikor
Njësitë Statistikore
Feature Type
3.1.4.3
Vector Statistical Unit
Njësitë Statistikore Vektor
Njësitë Statistikore
Feature Type
3.1.4.4
Evolution
Evolucioni
Njësitë Statistikore
Voidable
3.1.4.5
Statistical Grid Cell
Elementet Statistikor të Rrjetit
Njësitë Statistikore
Feature Type
3.1.4.6
Vector Statistical Unit Geometry
Gjeometria e Njësisë Statistikore Vektor
Njësitë Statistikore
Data Type
3.1.4.7
Geometry Descriptor
Gjeometria Përshkruese
Njësitë Statistikore
Data Type
3.1.4.8
Statistical Tesselation
Mozaiku Statistikor
Njësitë Statistikore
Feature Type
3.1.4.9
Area Statistical Unit
Njësitë Statistikore Poligon /Sipërfaqe
Njësitë Statistikore
Feature Type
3.1.4.10
Grid Position
Pozicioni i Rrjetit
Njësitë Statistikore
Data Type
3.1.4.11
Statistical Grid Resolution
Rezolucioni i Rrjetit Statistikor
Njësitë Statistikore
Union
3.1.4.12
Geometry Type Value
Vlerat e Llojeve të Gjeometrisë
Njësitë Statistikore
Kodelistë
3.1.4.13
Evolution Type Value
Vlerat e Llojit të Evolucionit
Njësitë Statistikore
Kodelistë
4.2 Aneksi B - Kodlistat
4.2.1 Skema e aplikimit të temës “Njësitë statistikore’’
Kodlistat
Vlerat e Llojeve të Evolucionit
Vlerat e Llojeve të Gjeometrisë
4.2.2 Vlerat e llojeve të evolucionit
Emri: Vlerat e llojeve të evolucionit
Përkufizimi: Vlerat e kodeve për llojet e evolucionit
Vlerat shtesë: Çfarëdo
Identifikimi: http://inspire.ec.europa.eu/codelist/EvolutionTypeValue
Vlerat: Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, kontrolloni nëse njëri prej tyre mund të përdoret.
Kodlistë
-- Emri --
Krijimi
-- Përkufizimi --
Vlera e kodit për krijim.
-- Emri --
Ndryshim
-- Përkufizimi --
Vlera e kodit për ndryshim.
-- Emri --
Fshirja
-- Përkufizimi --
Vlera e kodit për fshirje.
-- Emri --
Agregim/bashkim
-- Përkufizimi --
Vlera e kodit për grumbullim.
-- Emri --
Ndarja
-- Përkufizimi --
Vlera e kodit për ndarje.
4.2.3 Vlerat e llojeve të gjeometrisë
Emri: Vlerat e llojeve të gjeometrisë
Përkufizimi: Vlerat e kodeve për llojet e gjeometrisë
Shtrirja: E hapur
Identifikimi: http://inspire.ec.europa.eu/codelist/GeometryTypeValue
Vlerat: Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë dhe vlerat shtesë në çdo nivel të përcaktuar nga ofruesit e të dhënave.
Kodlistë
-- Emri --
Gjeometria referencë kod
-- Përkufizimi --
Gjeometria e përshkruar është gjeometria e referencës.
-- Emri --
Etiketimi i pikave
-- Përkufizimi --
Gjeometria e përshkruar është një gjeometri pikë për etiketimin.
-- Përshkrimi --
Natyrisht, gjeometritë që kanë këtë lloj duhet të jenë pika.
-- Emri --
Qendra e gravitetit
-- Përkufizimi --
Gjeometria e përshkruar është një gjeometri pikë e vendosur në qendër të graviteti të njësisë.
-- Emri --
Gjeometria e përgjithshme
-- Përkufizimi --
Një gjeometri e përgjithshme e njësisë statistikore.
-- Përshkrimi--
Gjeometritë që kanë një kod të tillë duhet të kenë një përshkrues për gjeometrinë e përgjithësuar.
-- Emri --
Të tjera
-- Përkufizimi --
Tipi tjetër i llojit të gjeometrisë.
