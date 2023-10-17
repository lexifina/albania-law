# Shtojca
STANDARDET SHTETËRORE
PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI
- TEMA: “ZONAT EKOLOGJIKE”
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1. Qëllimi
2.2. Si lexohet dokumenti
2.3. Detyrimet ligjore
2.4. Fusha e veprimit
3. TEMA
3.1. ZONAT EKOLOGJIKE
3.1.1. Parathënie
3.1.2. Terma dhe përkufizime
3.1.3. Skemat e aplikimit dhe diagrami UML për temën “Zonat ekologjike”
3.1.4. Katalogu i tipologjive
3.1.4.1. Zonat ekologjike
3.1.4.2. Vlerat e klasifikimit të bimësisë natyrore
3.1.4.3. Vlerat e klasifikimit të Direktivës së Kornizës së Strategjisë Detare
3.1.4.4. Vlerat e klasifikimit të shtresëzimit mjedisor
3.1.4.5. Vlerat e klasifikimit të zonave
3.1.4.6. Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
3.1.4.7. Vlerat e nivelit të klasifikimit të zonës
3.1.4.8. Vlerat e skemës së klasifikimit të zonës
3.1.4.9. Vlerat e klasifikimit të zonave ekologjike të Direktivës së Kornizës së Ujit
3.2. Metadata
3.3. Kodi EPSG për KRGJSH-në
3.4. Cilësia e të dhënave
3.4.1. Përputhja logjike - Përputhja konceptuale (Logical consistency - Conceptual cosistency)
3.4.2. Përputhja logjike - Përputhja me domeinin (Logical consistency - Domain consistency)
4. ANEKSE
4.1. Aneksi A - Katalogu i tipologjisë
4.2. ANEKSI B - Kodlistat
4.2.1. Skema e aplikimit për temën “Zonat ekologjike”
4.2.1.1. Vlerat e klasifikimit të bimësisë natyrore
4.2.1.2. Vlerat e klasifikimit të Direktivës për Kornizën e Strategjisë Detare
4.2.1.3. Vlerat e klasifikimit të shtresëzimit mjedisor
4.2.1.4. Vlerat e klasifikimit të zonave
4.2.1.5. Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
4.2.1.6. Vlerat e nivelit të klasifikimit të zonës
4.2.1.7. Vlerat e skemës së klasifikimit të zonës
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG), në bashkëpunim me Agjencinë Kombëtare të Zonave të Mbrojtura (AKZM), e cila është autoritet publik përgjegjëse, për temën “Zonat ekologjike”.
Data e publikimit të versionit nr. 1 është Qershor 2020. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2020_ ZE_v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit
Standard - Lloji i dokumentit
NSDI - Qëllimi i dokumentit
2020 - Viti i krijimit
ZE - Tema për të cilën është krijuar standardi “Zonat ekologjike”, i referohet temës “Bio-geographical Regions” së direktivës INSPIRE
v.1 - Numri i versionit të standardit
2. HYRJE
2.1. Qëllimi
Ky dokument përcakton specifikimet teknike, për të dhënat gjeohapësinore të temës “Zonat ekologjike”, temë e cila është përcaktuar në nenin 11, pika 2/v, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI-së në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse, për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë midis tyre.
2.2. Si lexohet dokumenti.
2.2.1. Struktura e dokumentit
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve - Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje - Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema - Në këtë pjesë jepen specifikimet teknike për temën “Zonat ekologjike”.
4. Anekse - Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 4 pjesë kryesore:
3.1. Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës dhe si është e ndarë kjo temë.
3.2. Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3. Sistemi Koordinativ Referencë - Këtu përcaktohet sistemi koordinativ referencë (KRGJSH).
3.4. Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2. DIAGRAMET UML DHE KATALOGU I TIPOLOGJIve
Diagramit UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe të marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në Katalogun i Tipologjive (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i Tipologjive. Për përdoruesit e aplikacioneve, Katalogu i Tipologjive mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në Katalogun e Tipologjive.
Tabelat nr. 1, 2, me anë të shembujve, shpjegojnë mënyrën e organizimit të informacionit, në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit, në tabelën e kodlistës.
Tabela 1
EMRI - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi për tipologjinë
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
«FeatureType» - një element që mund të jetë real, në terren, apo një dukuri abstrakte.
«DataType» - një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër
«Enumeration» “codeList» - listë e parapërgatitur vlerash, ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
«Union» - një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet, të cilat bien brenda shtrirjes gjeohapësinore të dy grupeve të të dhënave hyrëse.
«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden të shqipëruara si “Të dhënat e importuara”
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë, poligon.
Abstrakt - kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
Shumëllojshmëria
Lloji dhe numri i vlerave që mund të marrë atributi:
0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë
1..* - mund të marrë minimumi 1 vlerë ose shumë vlera
0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme.
1 - duhet të marrë detyrimisht 1 vlerë
I detyrueshëm
Po - nëse atributi është i detyrueshëm të plotësohet
Jo - nëse atributi nuk është i detyrueshëm të plotësohet
Rol-shoqërime
Në tabelën e lidhjeve “Rol-shoqërime” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi i elementeve
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh.: PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh.: Ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh.: Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
2.2.3. Karakteristikat <<voidable>> dhe shumëllojshmëria
Stereotipi <<voidable>> përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat, e përcaktuara për objektet gjeohapësinore, duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera “void”. Një vlerë “void” nënkupton që nuk ekziston një vlerë përkatëse, në grupet e të dhënave gjeohapësinore, që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës “void” duhet të paraqitet kurdo që të jetë e mundur, duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
- E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni të caktuar, nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E papopulluar”
- Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë, por është konfidenciale.
-- Përshkrimi --
Shembull. Të dhënat personale të popullsisë, të cilat ekzistojnë, por që nuk mund të shfaqen, pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi <<voidable>> nuk jep asnjë informacion nëse ekziston një karakteristikë në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh., nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh., nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria përkatëse do të jetë 1..*.
2.2.4. MBULIMET - COVERAGES
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe, ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh. vendndodhja e sensorëve), kurbat përcaktuese (p.sh. izolinjat), rrjetet (p.sh. ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit INSPIRE, funksionet e mbulimit janë përcaktuar si veti të llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është realizim i një prej llojeve të specifikuara në SSH EN ISO 19123-1 dhe SH EN ISO - 3.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh., SSH EN ISO 19136-1 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik, për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptual të Përgjithshëm “Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 2, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi, një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje mbulimi (ose një nëntip i tyre) në skemat e aplikimit në INSPIRE.
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5. NUMëRTIMEt dhe kodlistat (Enumeration and code list)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistën, “vlera të tjera” përcaktohet lloji i përmbajtjes së kodlistës, e përcaktuar specifikisht, si më poshtë:
- “jo”’ përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
- “të kufizuara” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave;
- “të hapura” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave;
- “po” përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë, apo të modifikojnë, vlerat ekzistuese, të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo”, pra të specifikuara në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6. Paraqitja e DIMENSIONIT kohor
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
- Shënim i rëndësishëm
Disa terma në Katalogun e Tipologjive, si p.sh.: FeatureType, DataType, Void, Coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike, sipas termave të direktivës INSPIRE.
2.3. Detyrimet ligjore
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është institucioni përgjegjës për krijimin e standardeve, për secilën nga temat e përcaktuara në nenin 11, të këtij ligji, në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (sikurse është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM nr. 1077, datë 23.12.2015).
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë, të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4. Fusha e veprimit
Të gjitha autoritetet publike, kompanitë private apo individë që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruara t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2: Proceset e ciklit jetësor
“Planifikimi” është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
“Vlerësimi” është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
“Procesimi (përpunimi)” është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
“Shpërndarja” është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
“Zbulimi” është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
“Analiza” është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
“Përditësimi” është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
“Arkivimi” është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen, duke u bazuar në standarde kombëtare dhe në legjislacionin në fuqi të vendit ku implementohet standardi. Rezultat i këtij procesi janë të dhënat që bëhen të pa aksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen, për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
“Shkatërrimi” është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde kombëtare ose në legjislacione në fuqi.
3. TEMA
3.1. ZONAT EKOLOGJIKE
3.1.1. Parathënie
Tema “Zonat ekologjike” përmban zona të cilat kanë kushte ekologjike relativisht homogjene, me karakteristika të përbashkëta mjedisore dhe ekologjike. Këto zona përcaktohen në bazë të një sërë faktorësh të ndërlidhur, siç janë gjeologjia, toka, klima, gjeomorfologjia dhe vegjetacioni.
Modeli i të dhënave të temës “Zonat ekologjike” siguron një përfaqësim të përbashkët panevropian të këtyre zonave. Objekti gjeohapësinor i “Zonave ekologjike” është objekti kryesor gjeohapësinor i skemës së aplikimit për përfaqësimin e rajoneve ose të zonave me kushte ekologjike relativisht homogjene dhe me karakteristika të përbashkëta. Ky objekt gjeohapësinor do të lejojë përshkrimin e duhur të klasifikimit të zonave ekologjike për çdo veçori që përfaqëson. Skema e aplikimit mbështet klasifikimin e zonave ekologjike sipas përcaktimit të Direktivës Evropiane të Habitateve, por, gjithashtu, plotëson kërkesat e ngritura nga specifikimet teknike të standardit me temë “Zonat ekologjike”.
Tema “Zonat ekologjike” ka një ndërvarësi me disa nga temat e tjera, si:
- Zonat e mbrojtura;
- Habitatet;
- Shpërndarja e specieve.
Duke qenë se “Zonat ekologjike” bazohen në klasifikimin e bërë nga dokumenti udhëzues i Direktivës së Habitateve, këto zona janë baza e një sërë seminaresh, të cilat vlerësojnë rrjetin Natura 2000, e cila përdoret për raportim çdo 6 vjet mbi “statusin e ruajtjes” të llojeve të habitateve dhe të specieve të mbrojtura nga direktiva (shiko figurën 3).
Figura 3: Harta në të majtë tregon shpërndarjen e një lloj habitati në Francë me ngjyrë të koduar nga zona ekologjike ku ai ndodhet, harta në të djathtë tregon “statusin e ruajtjes” së të njëjtit habitat sipas zonës ekologjike
Të gjitha zonat ekologjike të Evropës përcaktohen në specifikimin e të dhënave të Direktivës së Habitateve, e cila ofron një listë të këtyre zonave. Kjo direktivë përmban 9 rajone, që përfshijnë 27 shtete anëtare të BE-së. Këto rajone janë përshtatur në mënyrë të tillë për t’i bërë ato më të lehta për t’u përdorur në mënyrë administrative dhe formojnë njësi ekologjikisht koherente me kushte të ngjashme mjedisore, të cilat mund të dallohen, duke bërë krahasimin e hartës me klasifikimet e tjera mjedisore të Evropës. Këto rajone ekologjike të detajuara mund të përfshijnë, gjithashtu, nënkategori lokale të zonave ekologjike të përshkruara në Direktivën e Habitateve.
Figura 4: Harta e rajoneve biogjeografike, panevropiane
Duhet të theksohet se ndërsa këto specifikime të dhënash përqendrohen në dimensionin evropian, të njëjtat koncepte dhe udhëzime janë po aq të vlefshme për zonat ekologjike në nivelin e shtetit anëtar. Shtetet anëtare janë në gjendje të ngarkojnë kodlista për zonat ekologjike përmes një regjistri kodlistash. Për më tepër, këto specifikime të dhënash nuk nënkuptojnë që zonat ekologjike evropiane janë një zëvendësim i zonave më të detajuara ekologjike që shtetet anëtare mund të kenë.
3.1.2. Terma dhe përkufizime
- Neni 17 - neni 17 i Direktivës së Habitateve kërkon që çdo 6 vjet Shtetet Anëtare të përgatisin raporte që t’i dërgohen Komisionit Evropian për zbatimin e Direktivës. Neni 11 i Direktivës së Habitateve kërkon që Shtetet Anëtare të monitorojnë habitatet dhe speciet e listuara tek anekset dhe neni 17 kërkon që një raport t’i dërgohet Komisionit Evropian çdo 6 vjet, sipas një formati të dakorduar. Raporti përfshin vlerësime mbi statusin e ruajtjes së llojeve të habitatit dhe llojeve të interesit të komunitetit në nivelin biogjeografik.
- Zonat ekologjike - zona të cilat kanë kushte ekologjike relativisht homogjene me karakteristika të përbashkëta mjedisore dhe ekologjike.
- Shtresëzimi mjedisor - është krijuar për të prodhuar një shtresëzim statistikor të mjedisit evropian, i përshtatshëm për marrjen e mostrave të rastësishme të shtresëzuara të burimeve ekologjike. Në këto shtresa gjenden rajone të gjera ekologjike të përdorura në Direktivën e Habitateve.
- Rajonet detare - janë të përcaktuara në legjislacionin ndërkombëtar, të unionit, kombëtar ose nënkombëtar, me qëllim të vlerësimit, menaxhimit dhe rregullimit.
Shënim. Rajonet detare përdoren në kontekstin e Natura 2000 vetëm për arsye praktike-teknike, ato nuk kanë asnjë status juridik në krahasim me rajonet tokësore ose zonat ekologjike të Direktivës së Habitateve.
- Natura 2000 - është një rrjet i gjerë i zonave të mbrojtjes së natyrës në Bashkimin Evropian, i themeluar në bazë të Direktivës së Habitateve të vitit 1992. Qëllimi i rrjetit është të sigurojë mbijetesën afatgjatë të specieve dhe habitateve më me vlerë dhe më të kërcënuara të Evropës. Ai përbëhet nga zonat speciale të konservimit, të përcaktuara nga shtetet anëtare në bazë të Direktivës së Habitateve, dhe, gjithashtu, përfshin zonat e veçanta të mbrojtjes të përcaktuara nën Direktivën e Zogjve të vitit 1979. Themelimi i këtij rrjeti të zonave të mbrojtura, gjithashtu, përmbush një detyrim të komunitetit sipas Konventës për Diversitetin Biologjik.
- Bimësia natyrore - harta e Bimësisë Natyrore të Evropës është përpiluar dhe prodhuar nga një ekip ndërkombëtar i gjeobotanistëve. Është botuar për herë të parë më 1979-n, më pas me një version të dytë u botua më 1987-n nga Këshilli i Evropës.
3.1.3. Skemat e aplikimit dhe DIAGRAMI UML për temën “Zonat ekologjike”
Skema e aplikimit e temës “Zonat ekologjike” paraqet një përfaqësim të përbashkët panevropian të zonave ekologjike dhe llojeve të tjera të shtresëzimeve mjedisore dhe rajoneve ekologjike. Tipologjia (feature-i) ZonatEkologjike është objekti gjeohapësinor kryesor i kësaj skeme aplikimi për përfaqësimin e rajoneve ose të zonave me kushte ekologjike relativisht homogjene me karakteristika të përbashkëta. Ky lloj objekti gjeohapësinor do të ofrojë një përshkrim të duhur të klasifikimit ekologjik që është përdorur për të identifikuar dhe klasifikuar zonat ekologjike për çdo veçori që përfaqëson. Në këtë aspekt duhet të theksohet se skema e aplikimit jo vetëm që mbështet klasifikimin e zonave ekologjike, siç përcaktohet nga Direktiva Evropiane e Habitateve, por, gjithashtu, plotëson kërkesat e ngritura nga specifikimet teknike të standardit me temë “Zonat ekologjike”.
Në këtë skemë aplikimi përfshihen katër skema të dallueshme të klasifikimit evropian, megjithatë përmes mekanizmit të kodlistave modeli mund të zgjerohet për të përcaktuar dhe për të përfshirë klasifikime të tjera. Struktura që përmban kjo skemë aplikimi është e thjeshtë, në mënyrë që të realizohet një harmonizim maksimal i të dhënave, si dhe për objektet gjeohapësinore që përfshijnë informacione gjeometrike.
Figura 5: Diagrami UML: Përmbajtja e skemës së aplikimit për temën “Zonat ekologjike”
Në figurën e mësipërme paraqitet përmbledhja e paketës ZonatEkologjike, ky objekt gjeohapësinor i referohet paketës bazë LlojiBazë të modelit konceptual të përgjithshëm.
Skema e plotë e aplikimit për temën “Zonat ekologjike” është treguar në figurën 6 dhe përshkruhet me detaje, si më poshtë.
Figura 6: Diagrami UML: Përmbajtja e skemës së aplikimit për temën “Zonat ekologjike”
ZonatEkologjike është i vetmi objekt gjeohapësinor i përfshirë në skemën e aplikimit dhe përfaqëson çdo lloj zone ekologjike. Meqenëse tipologjia (Fetaure Type) ZonatEkologjike mund të përbëhen nga poligone ose poligone shumëpjesësh, përfaqësimi i tyre gjeometrik shprehet me llojin, sipërfaqe e shumëfishtë. Zonat ekologjike përshkruhen nga një klasifikim ekologjik. Sistemi i klasifikimit specifikohet nga tre atribute: informacioni mbi skemën e klasifikimit dhe vlera e klasifikimit që është e zbatueshme për rastin ku sigurohen dy atribute të detyrueshme përkatësisht të quajtura SkemaEKlasifikimitRajonal dhe KlasifikimiRajonal. Vlerat për këto atribute mund të zgjidhen nga një kodlistë. Atributi i tretë NiveliKlasifikimitRajonal, i cili është jo i detyrueshëm (Voidable) është përcaktuar për të dokumentuar nivelin e sistemit të klasifikimit. Vlerat e mundshme për këtë nivel janë: ndërkombëtar, kombëtar, rajonal ose lokal. Shumë sisteme të ndryshme klasifikimi ekzistojnë në nivele të ndryshme; skema aktuale e aplikimit përfshin vetëm informacione mbi skemën e klasifikimit dhe vlerat përkatëse të 4 sistemeve evropiane të klasifikimit, por skema mund të zgjatet për të përfshirë sisteme të tjera të klasifikimit përmes mekanizmit të kodlistave.
- Natura 2000 dhe Zonat ekologjike
Natura 2000 dhe Zonat ekologjike, siç përshkruhen përkatësisht te Direktiva e Habitateve dhe Konventa e Bernës janë njësi raportuese që mbështesin procesin e ruajtjes së natyrës, dhe më konkretisht ruajtjen e specieve dhe llojeve të habitatit, në kushte të ngjashme natyrore në një grup vendesh, pavarësisht kufijve politikë dhe administrativë. Këto zona ekologjike janë tokësore për të krijuar një njësi të ngjashme që mund të përdoret për vlerësimin e 5 rajoneve detare shtesë, bazuar në konventat detare evropiane. Për dallim të zonave ekologjike tokësore, këto rajone detare nuk kanë një bazë ligjore. Do të ketë vetëm një grup të dhënash koresponduese për rajonet Natura 2000 dhe Emerald, të cilat do të sigurohen nga Agjencia Evropiane e Mjedisit.
- Shtresëzimi mjedisor në Evropë.
Zonat Mjedisore të Evropës rrjedhin nga “Shtresëzimi mjedisor” i Evropës. Shtresëzimi bazohet në të dhënat e klimës, të dhënat mbi ndikimin e oqeanit dhe pozicionin gjeografik.
- Bimësia natyrore e Evropës
Kodet për bimësinë natyrore në Evropë rrjedhin nga harta e “Vegjetacionit natyror” të Evropës.
- Rajonet e direktivës në kuadër të Strategjisë Detare
Kodet për rajonet e direktivës së “Strategjisë detare” rrjedhin nga vetë kjo direktivë.
Figura 7: Diagrami për Zonat ekologjike: Kodlista: VleratEKlasifikimitTëDirektivësTëKornizësSëStrategjisëDetare
Figura 8: Diagrami për Zonat ekologjike: Kodlistat
Figura 9: Diagrami për zonat ekologjike
Figura 10: Struktura e diagramit për zonat ekologjike
3.1.4. Katalogu i tipologjive
3.1.4.1. Zonat ekologjike
-- Emri --
Zonat ekologjike
-- Përkufizimi --
Zona të cilat kanë kushte ekologjike relativisht homogjene me karakteristika të përbashkëta mjedisore dhe ekologjike.
-- Përshkrimi --
Shembull. Evropa është e ndarë në njëmbëdhjetë zona tokësore ekologjike të gjera dhe pesë zona ekologjike detare.
Shënim. Rajonet detare përdoren në kontekstin e Natura 2000 vetëm për arsye praktike dhe teknike, ato nuk kanë asnjë status juridik në kontrast me zonat ekologjike “tokësore”.
-- Tipi i elementit --
FeatureType
ATRIBUTET
InspireId : Identifikues
Shumëllojshmëria: [0..1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikimi i objektit të jashtëm gjeohapësinor.
-- Përshkrimi --
Një identifikues i jashtëm është një objekt identifikues unik i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikimet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një objekt gjeohapësinor, jo një identifikues i fenomenit në realitet.
[ I detyrueshëm: PO]
Gjeometria : MultiSurface
Shumëllojshmëria: [1]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria që përcakton zonën ekologjike.
[ I detyrueshëm: PO]
KlasifikimiIZonës : VleratEKlasifikimitTëZonave
Shumëllojshmëria: [1]
-- Emri --
Klasifikimi i zonës
-- Përkufizimi --
Kodi i klasifikimit të zonës, sipas një skeme klasifikimi.
[ I detyrueshëm: PO]
SkemaEKlasifikimitTëZonës : VleratESkemësSëKlasifikimitTëZonës
Shumëllojshmëria: [1]
-- Emri --
Skema e klasifikimit të zonës
-- Përkufizimi --
Skema e klasifikimit që përdoret për klasifikimin e rajoneve.
[ I detyrueshëm: PO]
NiveliIKlasifikimitTëZonës : VleratENivelitTëKlasifikimitTëZonës
Shumëllojshmëria: [1]
-- Emri --
Niveli i klasifikimit të zonës
-- Përkufizimi --
Niveli i klasifikimit të klasës së rajonit.
[ I detyrueshëm: PO]
FillimiICiklitJetësor : Datë-Orë
Shumëllojshmëria: [1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data dhe ora në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[ I detyrueshëm: PO]
PërfundimiICiklitJetësor : Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i ciklit jetësor
-- Përkufizimi --
Data dhe ora në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq nga grupi i të dhënave gjeohapësinore.
[ I detyrueshëm:PO]
3.1.4.2. Vlerat e klasifikimit të bimësisë natyrore
-- Emri --
Vlerat e klasifikimit të bimësisë natyrore
-- Përkufizimi --
Kodet për klasifikimin e bimësisë natyrore.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneruar nga «codeList» VleratEKlasifikimitTëBimësisëNatyrore tek «codeList» VleratEKlasifikimitTëZonave
ATRIBUTET
TundratArktikeDheBimësiaAlpine
-- Emri --
Tundrat arktike dhe bimësia alpine.
-- Përkufizimi --
Tundrat arktike dhe bimësia alpine.
ShkurreTëVoglaNëAtlantikë
-- Emri --
Shkurre të vogla në Atlantikë
-- Përkufizimi --
Shkurret të vogla në Atlantikë.
BimësiaBregdetareDheBimësiaHalofitikeNëBrendësi
-- Emri --
Bimësia bregdetare dhe bimësia halofitike në brendësi
-- Përkufizimi --
Bimësia bregdetare dhe bimësia halofitike në brendësi
Shkretëtirë
-- Emri --
Shkretëtirë
-- Përkufizimi --
Shkretëtirë.
VegjetacioniIGrykëderdhjeveTëLumenjveDheTreguesveTëUjëraveTëËmbëlDheTokaveMeLagështi
-- Emri --
Vegjetacioni i grykëderdhjeve të lumenjve dhe treguesve të ujërave të ëmbla dhe tokave me lagështi
-- Përkufizimi --
Bimësia e fushave me lagështi.
HapësiraPyjoreLivadheStepaAlternuarMeGjetheTëGjeraDheKullotaTëThataDukeAlternuarMeShkurreXerofitik
-- Emri --
Stepat pyjore dhe kullotat e thata që alternohen me shkurre
-- Përkufizimi --
Stepat pyjore (stepat e livadhit që alternohen me pyje gjethe gjera) dhe kullota të thata që alternohen me shkurre xerofitike.
PyjeGjetheGjeraTëPërzieraMeHigro-Termofile
-- Emri --
Pyje gjethe gjera të përziera me higro-termofile
-- Përkufizimi --
Pyje gjethe gjera të përziera me higro-termofile.
ShkurreDhePyjeSklerofileMesdhetare
-- Emri --
Shkurre dhe pyje sklerofile mesdhetare
-- Përkufizimi --
Shkurre dhe pyje sklerofile mesdhetare.
MesofiteDheHigromezofiteTëPërzieraMePyjeHalorGjetheGjera
-- Emri --
Mesofite dhe higromesofite të përziera me pyje halor gjethe gjera
-- Përkufizimi --
Mesofite dhe higrofite të përziera me pyje halor gjethe gjera.
PyjeMeGjetheHaloreMezofiteDheGjetheGjeraTëPërziera
-- Emri --
Pyje të përziera me gjethe halore mezofite dhe gjethe gjera
-- Përkufizimi --
Pyje të përziera me gjethe halore mezofite dhe gjethe gjera.
Moçal
-- Emri --
Moçal
-- Përkufizimi --
Moçal.
VegjetacioniIXeherorëve
-- Emri --
Vegjetacioni i xeherorëve
-- Përkufizimi --
Vegjetacioni i xeherorëve.
ShkretëtiratPolareDheVegjetacioniNivalionalIMaleveTëLarta
-- Emri --
Shkretëtirat polare dhe vegjetacioni aluvional i maleve të larta
-- Përkufizimi --
Shkretëtirat polare dhe vegjetacioni aluvional i maleve të larta.
BimësiaEKallamishteveTëLartaKënetatEGjelbërtaDheBimësiaUjore
-- Emri --
Bimësia e kallamishteve të larta, kënetave të gjelbra dhe bimësia ujore
-- Përkufizimi --
Bimësia e kallamishteve të larta, kënetave të gjelbra dhe bimësia ujore.
Stepat
-- Emri --
Stepat
-- Përkufizimi --
Stepat.
BimëPyjoreSubarktikeBorealeDheNemoraleMontaneSiDheBimësiSubalpineDheMesdhetare.
-- Emri --
Bimë pyjore subarktike boreale dhe nemorale montane, si dhe bimësi subalpine dhe mesdhetare
-- Përkufizimi --
Bimë pyjore subarktike, boreale dhe nemorale-montane, si dhe bimësi subalpine dhe mesdhetare.
PyjetMoçalisteDheKënetore
-- Emri --
Pyjet moçalore dhe kënetore
-- Përkufizimi --
Pyjet moçalore dhe kënetore.
PyjeGjetheGjerëTëPërzierMeTermofile
-- Emri --
Pyje gjethe gjerë të përzier me termofile
-- Përkufizimi --
Pyje gjethe gjerë të përzier me termofile.
PyjeHaloreXerofitikePyjeTëDendurDheShkurre
-- Emri --
Pyje halore xerofitike, pyje të dendur dhe shkurre
-- Përkufizimi --
Pyje halore xerofitike, pyje të dendur dhe shkurre.
3.1.4.3. Vlerat e klasifikimit të Direktivës së Kornizës së Strategjisë Detare
-- Emri --
Vlerat e klasifikimit të Direktivës së Kornizës së Strategjisë Detare.
-- Përkufizimi --
Kodet për klasifikimin e Direktivës së Kornizës së Strategjisë Detare.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneruar nga «codeList» VleratEKlasifikimitTëDirektivaveTëKornizësSëStrategjisëDetare tek «codeList» VleratEKlasifikimitTëZonave
ATRIBUTET
DetiBaltik
-- Emri --
Deti Baltik
-- Përkufizimi --
E gjithë shtrirja e ujërave detare të mbuluara nga sovraniteti ose juridiksioni i Estonisë, Finlandës, Letonisë, Lituanisë dhe Polonisë dhe pjesë të ujërave të Danimarkës, Gjermanisë dhe Suedisë që ndodhen në lindje të Kattegat.
OqeaniAtlantikVeriLindor
-- Emri --
Oqeani Atlantik Veri-Lindor
-- Përkufizimi --
Ujërat detare të mbuluara nga sovraniteti ose juridiksioni i shteteve anëtare. Ai përfshin nënrenditjet e Detit të Madh të Veriut, duke përfshirë Kattegat dhe Kanalin Anglez, detin Kelt, gjirin Biskai, brigjet Iberiane dhe ujërat përreth Azorës, Maderia dhe ishujt Kanarie.
DetiMesdhe
-- Emri --
Deti Mesdhe
-- Përkufizimi --
Ujërat detare të mbuluara nga sovraniteti ose juridiksioni i shteteve anëtare. Ai përfshin nënrenditjet e Detit Mesdhe Perëndimor, detin Jon, Adriatik, Detin Mesdhe Qendror dhe detin Egje-Levantik.
DetiIZi
-- Emri --
Deti i Zi
-- Përkufizimi --
E gjithë shtrirja e ujërave detare që mbulohet nga sovraniteti ose juridiksioni i Bullgarisë dhe Rumanisë.
DetiIVeriut
-- Emri --
Deti i Veriut
-- Përkufizimi --
Një nënrajon i oqeanit Atlantik Veri-Lindor, i përbërë nga ujërat e zonës më të madhe të Detit të Veriut, përfshirë Kattegat dhe kanalin Anglez.
DetetKelte
-- Emri --
Detet Kelte
-- Përkufizimi --
Një nënrajon i Oqeanit Atlantik Veri-Lindor, i përbërë nga ujërat e deteve Kelte, që mbulojnë detet irlandeze, detin Kelt, ujërat e perëndimit të Irlandës dhe Mbretërisë së Bashkuar.
GjiriiBiskajësDheBregdetiIberian
-- Emri --
Gjiri i Biskajës dhe Bregdeti Iberian
-- Përkufizimi --
Një nënrajon i Oqeanit Atlantik Veri-Lindor, i përbërë nga ujërat e gjirit të Biskajës dhe jashtë bregdetit (Atlantik) iberian.
Makronezia
-- Emri --
Makronezia
-- Përkufizimi --
Një nënrajoni i oqeanit Atlantik Veri-Lindor, i përbërë nga ujërat që rrethojnë Azoret, Madeirat dhe ishujt Kanarie.
DetiMesdhetarPerëndimor
-- Emri --
Deti i Mesdheut Perëndimor
-- Përkufizimi --
Një nënrajon i Detit Mesdhe që mbulon ujërat e Mesdheut Perëndimor.
DetiAdriatik
-- Emri --
Deti Adriatik
-- Përkufizimi --
Një nënrajon i Detit Mesdhe që mbulon ujërat e detit Adriatik.
DetiJonDheDetiMesdhetarQendror
-- Emri --
Deti Jon dhe Deti i Mesdheut Qendror
-- Përkufizimi --
Një nënrajon i Detit Mesdhe që mbulon detin Jon dhe Detin e Mesdheut Qendror.
DetetLevantineDheEgje
-- Emri --
Detet Levantine dhe Egje
-- Përkufizimi --
Një nënrajon i Detit Mesdhe që përbëhet nga detet Egje dhe Levantine.
3.1.4.4. Vlerat e klasifikimit të shtresëzimit mjedisor
-- Emri --
Vlerat e klasifikimit të shtresëzimit mjedisor
-- Përkufizimi --
Kodet për shtresëzimin klimatik të mjedisit në Evropë.
-- Përshkrimi --
Bazuar në variablat mjedisorë (klima, gjeomorfologjia), duke përdorur një analizë të komponentëve kryesorë dhe rutinën e grupimit ISO-DATA. Shtresëzimi mjedisor i Evropës (EnS) përbëhet nga 84 shtresa, të cilat janë grumbulluar në 13 zona mjedisi me rezolucion hapësinor prej 1 km².
Shënim. Ky shtresëzim është sipas Metzger et al. 2005.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneruar nga «codeList» VleratEKlasifikimitTëShtresëzimitMjedisor tek «codeList» VleratEKlasifikimitTëZonave
ATRIBUTET
AlpetNëVeri
-- Emri --
Alpet në Veri
-- Përkufizimi --
Malet e Skandinavisë Perëndimore së bashku me fushat bregdetare.
-- Përshkrimi --
Zona është shumë e larmishme jo vetëm nga luginat e thella në formë U-je, por edhe me një vijë bregdetare të theksuar. Pjesa më e madhe e sipërfaqes së tokës është e mbuluar nga depozitat akullnajore të llojeve të ndryshme. Klima në perëndim është oqeanike, për shkak të ndikimit të rrjedhës së Gulf Stream, dhe bëhet progresive kontinentale më në lindje. Regjimi i temperaturës dhe kufizimet e terrenit kufizojnë bujqësinë moderne në kufirin bregdetar, por kullotat e gjera janë, gjithashtu, të pranishme, megjithëse shpesh në rënie. Mbulesa e tokës mbizotërohet nga tundra arktike në veri, kullotat arktike-alpine dhe nga malet e larta dhe të gjera. Rënia e kullotjes po çon në kolonizim të përhapur nga pyjet, duke shtuar pyjet halore ekzistuese të bredhave dhe pishave.
AlpetNëJug
-- Emri --
Alpet në jug
-- Përkufizimi --
Malet e larta, të mesme dhe të ulëta të Evropës Qendrore
-- Përshkrimi --
Kryesisht i përkasin brezit kryesor orogjenik alpin. Luginat të ngrira dhe të thella me formë U-je, paraqesin majat, të cilat janë mjaft të larta në Alpe, por edhe vende të tjera të cilat mund të jenë të mbuluara me dëbore. Prandaj, prodhimet janë të kufizuara në këto lugina, por ka dhe kullota pjellore. Shpatet e maleve janë të mbuluara nga pyje halore të bredhit dhe larshit, si dhe lloje të ndryshme të pyjeve gjetherënëse. Zonat në përgjithësi përdoren për pylltari dhe kryesisht janë të mbrojtura. Mbi niveli e pemëve ka kullota që mund të shfrytëzohen gjerësisht.
Shembull: Karpatet, Pirenejt, alpet, malet Tatra.
Anatolian
-- Emri --
Anadollian
-- Përkufizimi --
Zona mjedisore që përfshijnë rajonet e mëposhtme: 1. Anadolli Perëndimor (Turqi); 2. Anadolli Qendror (Turqi).
AtlantikuQendror
-- Emri --
Atlantiku Qendror
-- Përkufizimi --
Jug dhe jug-perëndimi i ishujve britanikë, Franca Veriore dhe Vendet e Ulëta.
-- Përshkrimi --
Toka përbëhet kryesisht nga terrene me ultësira, nivele sipas gjeologjisë, por, gjithashtu, ka reliev malor në perëndim dhe në jug. Klima zakonisht është shumë oqeanike në perëndim, me dimër të freskët dhe verë të butë dhe të lagësht, e cila bëhet më kontinentale në lindje. Bujqësia mbizotëron në pjesën më të madhe të zonës, por ka edhe kullota pjellore në perëndim. Pyjet janë prezent, kryesisht me pisha.
AtlantikuVerior
-- Emri --
Atlantiku Verior
-- Përkufizimi --
Ultësirat dhe malet e ulëta në Britaninë Qendrore dhe Veriore, Irlandën Veriore dhe bregdetin Perëndimor të Norvegjisë, si dhe fushat bregdetare. Ultësirat e Danimarkës dhe Gjermania Veriperëndimore i përkasin kësaj zone.
-- Përshkrimi --
Ekziston një kontrast midis peizazheve të dendura të veriut dhe perëndimit të zonave dhe tipareve të depozitimit. Klima është shumë oqeanike në perëndim me dimër tipik të butë të lagësht dhe verë të freskët, e cila bëhet më kontinentale në lindje. Si rezultat, në shtresat jugore mbizotërojnë tokat e punueshme ndërsa në veri ka lloje të ndryshme të barërave që shërbejnë si ushqim për delet. Shtresat e mëparshme, gjithashtu, kanë shumë sipërfaqe toke urbane. Në ultësirat britanike ka plantacione të gjera bredhash, por ndryshe mbulesa pyjore është kryesisht gjetherënëse.
ZonaVeriore
-- Emri --
Zona veriore
-- Përkufizimi --
Shpatet lindore të maleve skandinave, si dhe fushat dhe ultësirat mbizotëruese të Baltikut Verior dhe Lindor.
-- Përshkrimi --
Zona ka qenë e ngrirë, gjë që rezultoi në depozitimin e shumë tipareve të mbetjeve, siç janë morenë dhe eskers (është një kreshtë e gjatë dredha-dredha e rërës dhe zhavorrit të shtresuar). Klima është kontinentale dhe temperatura kufizon prodhimin e bujqësisë, por në veri janë të pranishme kullotat pjellore. Në këtë zonë mbizotërojnë pyjet halore të bredhave dhe të pishave, shpesh të përziera me thupër dhe plepi i egër. Ka shumë ligatina dhe liqene veçanërisht në Finlandë.
Kontinentale
-- Emri --
Kontinentale
-- Përkufizimi --
Rrafshnaltat dhe ultësirat e Evropës Qendrore, Lindore dhe ato të Ballkanit, si dhe disa kodra të ulëta në kufirin e ALS-së.
-- Përshkrimi --
Klima kontinentale ka karakteristika si një mesatare vjetore të temperaturave dhe reshje të përqendruara në muajt e verës, karakteri kontinental është më i theksuar në lindje sesa në perëndimin. Pyjet janë të shtrira në toka të cekëta dhe të varfra, të mbjella me ah, bredh dhe pishë, si dhe shumica e zonave menaxhohen për prodhimin e drurit. Zonat kryesore urbane janë të pranishme në të gjithë zonën, e cila, gjithashtu, ka rrjet të gjerë lumor.
Luzitanian
-- Emri --
Luzitane
-- Përkufizimi --
Pjesa bregdetare dhe kodrat e ulëta në perëndim dhe jug-perëndim të Francës, si dhe Spanjës Veriore dhe Portugalisë.
-- Përshkrimi --
Klima është e ngrohtë dhe e lagësht, me reshje të përqendruara në muajt e dimrit. Sezonet e gjata të rritjes së prodhimit dhe disponueshmëria e lartë e ujit do të thotë që kullotat e përhapura pjellore mund të korren disa herë në vit. Prodhimi është me rëndësi në tokat pjellore, vreshtat janë, gjithashtu, të rëndësishme në të gjithë zonën.
MaletMesdhetare
-- Emri --
Malet Mesdhetare
-- Përkufizimi --
Malet e larta dhe të mesme në Mesdheun Verior.
-- Përshkrimi --
Rreth kufijve të vargjeve kryesore malore si Pirenejtë dhe Alpet përfshihen malet me lartësi të ulët dhe të mesme në Mesdheun Verior përreth kufijve të vargjeve kryesore. Klima është mesdhetare, me verë të ngrohtë dhe reshje të përqendruara në muajt e dimrit. Tokat e varfra dhe terreni i vështirë kufizojnë prodhimin e të mbjellave në pjesën më të madhe të zonës, por vreshtat janë ende të rëndësishme në vend. Livadhet e gjera janë të përhapura dhe përdoren për kullotjen e bagëtive dhe deleve, por në përgjithësi këto janë në rënie.
MesdheuVerior
-- Emri --
Mesdheu Verior
-- Përkufizimi --
Ultësira e Mesdheut Verior dhe Qendror, por edhe kodra dhe male të ulëta më tej në jug.
-- Përshkrimi --
Topografia është e shumëllojshme dhe përfshin fushat bregdetare, pllajën me male të izoluara, ultësira dhe lugina malore. Klima është mesdhetare, me verë të ngrohtë dhe të thatë dhe me reshje të përqendruara në muajt e dimrit. Prodhimi i të korrave kufizohet nga prania e ujit, ujitja e përhershme është e rëndësishme në vend për të rritur produktivitetin. Vreshtat dhe ullinjtë kanë shumë rëndësi në të gjithë zonën, pemishtet, gjithashtu, si dhe tokat për përdorimin bujqësor, megjithëse përdorimi i këtyre të fundit është në rënie.
MesdheuJugor
-- Emri --
Mesdheu Jugor
-- Përkufizimi --
Rrafshnalta dhe malet në Mesdheun Jugor dhe disa ultësira në Spanjën Veriore dhe deltën e Rhone në Francë.
-- Përshkrimi --
Topografia është e shumëllojshme dhe përfshin fushat bregdetare, pllaja me male të izoluara, ultësira dhe lugina malore. Klima është mesdhetare, me verë të nxehtë dhe të thatë dhe me reshje maksimale në dimër. Prodhimi i të korrave kufizohet nga disponueshmëria e ujit dhe ujitja e përhershme është e rëndësishme në vend për të rritur produktivitetin. Vreshtat dhe ullishtat janë një mbulesë e rëndësishme tokësore në të gjithë zonën. “Dehesas” dhe “Montados” janë, gjithashtu, të rëndësishëm, veçanërisht në Spanjë dhe në Portugali. Mbulesa pyjore është e kufizuar, për shkak të shfrytëzimit të gjatë dhe kjo vërehet te vija bregdetare që është shumë e urbanizuar.
Nemoral
-- Emri --
Nemoral
-- Përkufizimi --
Ultësirat dhe fushat e Baltikut Jugor dhe Lindor shtrihen në perëndim të brigjeve të Detit të Veriut.
-- Përshkrimi --
Klima është kontinentale dhe e ftohtë, por e përshtatshme për prodhimin e bimëve në tokat pjellore, megjithëse braktisja po ndodh në rajonet margjinale. Toka është e mbuluar kryesisht nga pyje halore, pishë dhe bredh shpesh e përzier me thupër dhe aspen, të përdorura nga industria pyjore. Bogs janë këneta të mëdha të pranishme në të gjithë zonën, por veçanërisht në lindje.
Panonian
-- Emri --
Panonian
-- Përkufizimi --
Rrafshnalta, luginat dhe skajet malore në pellgun e mesëm dhe të poshtëm të Danubit, si dhe ultësirat e Detit të Zi.
-- Përshkrimi --
Klima e ngrohtë kontinentale ka një karakter stepik dhe përqendrimi i reshjeve në fillim të verës. Pjesa më e madhe e tokës është relativisht e sheshtë, por ka disa kodra të ulëta dhe ndryshime në gjeologji duke shkaktuar ndryshime rajonale. Bujqësia aktive mbizotëron në të gjithë zonën dhe shndërrohet nga kullotat origjinale të stepave, të cilat tani mbeten vetëm në arna të vogla. Mbulesa pyjore, megjithëse është e rëndësishme në nivel lokal, është e kufizuar në masë. Ka disa liqene të mëdhenj dhe sisteme të mëdha lumenjsh.
3.1.4.5. Vlerat e klasifikimit të zonave
-- Emri --
Vlerat e klasifikimit të zonave
-- Përkufizimi --
Kodet që përcaktojnë zonat e ndryshme ekologjike.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneruar nga «codeList» VleratEKlasifikimitTëShtresëzimitMjedisor tek «codeList» VleratEKlasifikimitTëZonave
Gjeneruar nga «codeList» VleratEKlasifikimitTëDirektivaveTëKornizësSëStrategjisëDetare tek «codeList» VleratEKlasifikimitTëZonave
Gjeneruar nga «codeList» VleratEKlasifikimitTëBimësisëNatyrore tek «codeList» VleratEKlasifikimitTëZonave
Gjeneruar nga «codeList» VleratEKlasifikimitTëZonaveEkologjikeEmeraldDheNatura2000 tek «codeList» VleratEKlasifikimitTëZonave
3.1.4.6. Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
-- Emri --
Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
-- Përkufizimi --
Kodet për klasifikimin e zonave ekologjike.
-- Përshkrimi --
http://www.eea.europa.eu/data-and-maps/data/biogeographical-regions-europe/codelist-for-bio-geographical-regions
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneruar nga «codeList» VleratEKlasifikimitTëZonaveEkologjikeEmeraldDheNatura2000 tek «codeList» VleratEKlasifikimitTëZonave
ATRIBUTET
Alpin
-- Emri --
Alpin
-- Përkufizimi --
Zonat ekologjike alpine përbëhen nga disa zinxhirë malorë të rëndësishëm. Rajoni përfshin Alpet që shtrihen mbi Francë, Itali, Gjermani, Austri, Slloveni dhe vendet jo të BE-së të Zvicrës dhe Monakos, pjesët më të larta të Apenineve që zbresin kurrizin e Italisë, Pirenej në kufirin midis Spanjës dhe Francës. Skandat që shtrihen në Suedi, Finlandë, Norvegji dhe Karpatet që shtrihen përtej kufijve të BE-së të Sllovakisë, Polonisë, Rumanisë dhe Ukrainës. Jashtë BE-së, rajoni përfshin gjithashtu Kaukazin dhe Uralet.
Atlantik
-- Emri --
Atlantik
-- Përkufizimi --
Rajoni i Atlantikut shtrihet nga ishujt Faroes dhe Norvegjia Jugperëndimore poshtë në brigjet veriore të Spanjës dhe Portugalisë, duke përfshirë të gjithë Mbretërinë e Bashkuar, Irlandën dhe Holandën dhe pjesë të Gjermanisë, Danimarkës, Belgjikës, Francës, Spanjës dhe Portugalisë.
Boreal
-- Emri --
Boreal
-- Përkufizimi --
Përmban pjesë të territorit të Finlandës, Suedisë dhe territorin e Estonisë, Letonisë dhe Lituanisë. Rajoni Boreal në Evropë është pjesë e një zone të madhe të mbizotëruar nga pyjet halore, e cila rrethon Hemisferën Veriore në Evropë, Azi dhe Amerikën e Veriut.
Kontinental
-- Emri --
Kontinental
-- Përkufizimi --
Rajoni kontinental mbulon mbi çerekun e Bashkimit Evropian dhe shtrihet në një brez të gjerë nga perëndimi në lindje, duke filluar me Francën Qendrore dhe duke vazhduar në skajin lindor të Polonisë. Jashtë BE-së ajo shtrihet në malet Urale, në kufi me Azinë. Në jug, rajoni është pothuajse i ndarë në dy nga vargmalet e larta malore të zonës Alpine dhe fushat stepë të rajonit Panonian. Përfshihen, gjithashtu, pjesë të vijave bregdetare të Adriatikut dhe Baltikut. Gjithsej 13 shtete të BE-së kanë shtrirjen në të gjithë ose në një pjesë të territorit të tyre në rajonin kontinental.
Makronezian
-- Emri --
Makronezian
-- Përkufizimi --
Zonat ekologjike makroneziane përbëhen nga ishuj vullkanikë në Oqeanin Atlantik dhe përfshijnë arkipelagët e Azoreve, Madeira dhe ishujt Kanarie.
Mesdhetar
-- Emri --
Mesdhetar
-- Përkufizimi --
Pellgu i Mesdheut shtrihet 800 km në lindje-perëndim nga maja e Portugalisë deri në brigjet e Libanit dhe 1,000 km në veri-jug nga Italia në Marok dhe Libi. Brenda Bashkimit Evropian, rajoni i Mesdheut përfshin shtatë shtete anëtare ose pjesërisht (Francë, Portugali, Itali, Spanjë) plotësisht (Greqi, Maltë, Qipro), si dhe vendin tonë.
Arktik
-- Emri --
Arktik
-- Përkufizimi --
Zonat ekologjike të Arktikut siç përcaktohet nga Komisioni Evropian dhe Këshilli i Evropës për vlerësimin dhe raportimin për ruajtjen e natyrës, përfshin Islandën, Norvegjinë Veriore, gadishullin Kola të Veriut, Federatën Ruse në veri-perëndim dhe ishujt më tej në veri, të tilla si “Svalbard”, tokat e “Franc Josef” dhe “Novaja Zemla”.
Panonian
-- Emri --
Panonian
-- Përkufizimi --
Rajoni Panonian është i mbizotëruar nga një pellg i madh aluvial i sheshtë i cili përshkruhet nga veriu në jug nga dy lumenj të mëdhenj Danubi dhe Tisza. Dikur një det i lashtë në brendësi të pellgut është mbyllur pothuajse plotësisht nga të gjitha anët nga kodra dhe male të ulëta. Në veri dhe lindje shtrihen Karpatet, në perëndim Alpet dhe në jug Dinaritet. E gjithë Hungaria përfshihet në Rajonin Panonian ashtu si edhe zonat periferike të Sllovakisë, Republikës Çeke dhe Rumanisë brenda BE-së, dhe jashtë BE-së Serbia dhe Ukraina.
Stepik
-- Emri --
Stepik
-- Përkufizimi --
Brenda BE-së, rajoni Stepik gjendet vetëm në një shtet anëtar, Rumania. Përtej BE-së, ajo zhvillohet në një brez të gjerë të bimësisë që shtrihet mbi Moldavinë e Jugut, Ukrainën, Rusinë dhe Kazakistanin Perëndimor. Ajo vazhdon gjatë gjithë rrugës për në Azi, në ultësirat e maleve Altai në kufijtë e Mongolisë.
Deti Zi
-- Emri --
Deti Zi
-- Përkufizimi --
Rajoni i Detit të Zi shkon në drejtim të antiklavës përreth Detit të Zi nga Rumanisë dhe Bullgarisë, përmes Turqisë Veriore dhe Gjeorgjisë. Brenda Bashkimit Evropian, rajoni nuk është më shumë se një rrip bregdetar i hollë rreth 20-60 km i gjerë që shkon pothuajse në të gjithë gjatësinë e Rumanisë dhe Bullgarisë.
Anadollit
-- Emri --
Anadollit
-- Përkufizimi --
Rajoni korrespondon me pjesën e brendshme në lindje të gadishullit Anadoll, duke mos pasur asnjë kontakt me Detin e Zi apo Mesdheun. Rajoni shtrihet mbi tri zona të ndryshme gjeografike: Rrafshnalta Qendrore Anadolliane, vargmalet Lindore të Anadollit dhe Mesopotamia Veriore.
UjratPërgjatëAtlantikut
-- Emri --
Ujërat përgjatë Atlantikut
-- Përkufizimi --
E gjithë shtrirja e ujërave detare të mbuluara nga sovraniteti ose juridiksioni i Irlandës, Mbretërisë së Bashkuar, i Belgjikës, pjesëve të ujërave të Danimarkës, Gjermanisë, Suedisë, Portugalisë dhe Spanjës (duke përjashtuar ujërat përreth zonave ekologjike makroneziane: që janë ujërat që rrethojnë Azoret, Maderia (PT) dhe Ishujt Kanarie (ES).
Deti Baltik
-- Emri --
Deti Baltik
-- Përkufizimi --
E gjithë shtrirja e ujërave detare të mbuluara nga sovraniteti ose juridiksioni i Estonisë, Finlandës, Letonisë, Lituanisë dhe Polonisë është pjesë e ujërave të Danimarkës, Gjermanisë dhe Suedisë që ndodhet në lindje të Kategatit.
Hapësira DetareEDetitTëZi
-- Emri --
Hapësira detare e Detit të Zi
-- Përkufizimi --
E gjithë shtrirja e ujërave detare të mbuluara nga sovraniteti ose juridiksioni i Bullgarisë dhe Rumanisë.
BreziDetarMakronezian
-- Emri --
Brezi detar makronezian
-- Përkufizimi --
Ujërat që rrethojnë zonat ekologjike të Makronezisë: janë ujërat që rrethojnë Azoret, Madeira (PT) dhe ishujt Kanarie (ES).
BreziDetarIMesdheut
-- Emri --
Brezi detar i Mesdheut
-- Përkufizimi --
E gjithë shtrirja e ujërave detare të mbuluara nga sovraniteti ose juridiksioni i shteteve anëtare, ndërsa një pjesë e ujërave të Francës dhe Spanjës ndodhen brenda njësisë gjeografike që është Deti Mesdhe.
3.1.4.7. Vlerat e nivelit të klasifikimit të zonës
-- Emri --
Vlerat e nivelit të klasifikimit të zonës
-- Përkufizimi --
Kodet që përcaktojnë nivelin e klasifikimit të klasës së rajonit.
-- Tipi i elementit --
Kodlistë
ATRIBUTET
Ndërkombëtar
-- Emri --
Ndërkombëtar
-- Përkufizimi --
Ky është një klasifikim rajoni në nivel ndërkombëtar.
Kombëtar
-- Emri --
Kombëtar
-- Përkufizimi --
Ky është një klasifikim rajoni në nivel kombëtar.
Rajonal
-- Emri --
Rajonal
-- Përkufizimi --
Ky është një klasifikim zone në nivel rajonal.
Lokal
-- Emri --
Lokal
-- Përkufizimi --
Ky është një klasifikim zone në nivel lokal.
3.1.4.8. Vlerat e skemës së klasifikimit të zonës
-- Emri --
Vlerat e skemës së klasifikimit të zonës
-- Përkufizimi --
Kodet që përcaktojnë zonat ekologjike.
-- Tipi i elementit --
Kodlistë
ATRIBUTET
Natura2000DheZonatEkologjikeEmerald
-- Emri --
Natura 2000 dhe zonat ekologjike Emerald.
-- Përkufizimi --
Një grup kodlistash që do të përdoren për të përcaktuar zonat ekologjike të rrjetit Emerald të përcaktuara te Natura 2000.
Shtresëzimi i mjedisit
-- Emri --
Shtresëzimi i mjedisit
-- Përkufizimi --
Një grup i kodlistave që do të përdoren për të përcaktuar shtresëzimin e mjedisit.
Bimësi natyrore
-- Emri --
Bimësi natyrore
-- Përkufizimi --
Një grup kodlistash që do të përdoren për të përcaktuar bimësinë natyrore.
DirektivaEStrukturësSëStrategjisëDetare
-- Emri --
Direktiva e Strukturës së Strategjisë Detare
-- Përkufizimi --
Një grup kodesh që do të përdoren për klasifikimin e strategjisë detare dhe klasifikimit të rajonit.
3.1.4.9. Vlerat e klasifikimit të zonave ekologjike të Direktivës së Kornizës së Ujit
-- Emri --
Vlerat e klasifikimit të zonave ekologjike të Direktivës së Kornizës së Ujit.
-- Përkufizimi --
Zonat ekologjike për lumenjtë dhe për liqenet, siç janë renditur në shtojcën XI, harta A, e Direktivës së Punës së Kornizës së Ujit (2000/60/EC). Përkufizimet e dhëna në këtë pjesë të katalogut të karakteristikave u referohen vetëm zonave ekologjike të përshkruara në Direktivën e Punës së Kornizës së Ujit.
ATRIBUTET
Alpe
-- Emri --
Alpet
-- Përkufizimi --
Alpet janë zona ekologjike.
RajoniIberik-Makronezian
-- Emri --
Rajoni Iberik-Makronezian
-- Përkufizimi--
Rajoni Iberik-Makronezian është zonë ekologjike.
Pirenejtë
-- Emri --
Pirenejtë
-- Përkufizimi --
Malet Pirenej janë zonë ekologjike.
ItaliaKorsikaMalta
-- Emri --
Italia, Korsika dhe Malta
-- Përkufizimi --
Italia, Korsika dhe Malta janë zona ekologjike.
DinaritetEBallkanitPerëndimor
-- Emri --
Dinaritet e Ballkanit Perëndimor
-- Përkufizimi --
Dinaritet e Ballkanit Perëndimor janë zonë ekologjike.
BallkaniPerëndimorHelenik
-- Emri --
Ballkani Perëndimor Helenik
-- Përkufizmi --
Ballkani Perëndimor Helenik është zonë ekologjike.
BallkanLindor
-- Emri --
Ballkan Lindor
-- Përkufizimi --
Ballkani Lindor është zonë ekologjike.
MalësitëPerëndimore
-- Emri --
Malësitë Perëndimore
-- Përkufizimi --
Malësitë Perëndimore është zonë ekologjike.
MalësitëQendrore
-- Emri --
Malësitë Qendrore
-- Përkufizimi --
Malësitë Qendrore është zonë ekologjike.
Karpatet
-- Emri --
Karpatet
-- Përkufizimi --
Karpatet janë zonë ekologjike.
UltësiraHungareze
-- Emri --
Ultësira Hungareze
-- Përkufizimi --
Ultësira Hungareze është zonë ekologjike.
ProvincaPontiac
-- Emri --
Provinca Pontiac
-- Përkufizimi --
Provinca Pontiac është zonë ekologjike.
RrafshnaltaPerëndimore
-- Emri --
Rrafshnalta Perëndimore
-- Përkufizimi --
Rrafshnalta Perëndimore është zonë ekologjike.
RrafshnaltaQendrore
-- Emri --
Rrafshnalta Qendrore
-- Përkufiyimi --
Rrafshnalta Qendrore është zonë ekologjike.
KrahinaBaltike
-- Emri --
Krahina Baltike
-- Përkufizimi --
Krahina Baltike është zonë ekologjike.
RrafshnaltaLindore
-- Emri --
Rrafshnalta Lindore
-- Përkufizimi --
Rrafshnalta Lindore është zonë ekologjike.
IrlandaDheIrlandaEVeriut
-- Emri --
Irlanda dhe Irlanda e Veriut
-- Përkufizimi --
Irlanda dhe Irlanda e Veriut janë zona ekologjike.
BritaniaEMadhe
-- Emri --
Britania e Madhe
-- Përkufizimi --
Britania e Madhe është zonë ekologjike.
Islanda
-- Emri --
Islanda
-- Përkufizimi --
Islanda është zonë ekologjike.
Borealis
-- Emri --
Borealis
-- Përkufizimi --
Ngarkimet Borealis janë zonë ekologjike.
Tundra
-- Emri --
Tundra
-- Përkufizimi --
Tundra është zonë ekologjike.
MburojaSkandinave
-- Emri --
Mburoja Skandinave
-- Përkufizimi --
Mburoja Skandinave është zonë ekologjike.
Tajga
-- Emri --
Tajga
-- Përkufizimi --
Tajga është zonë ekologjike.
Kaukaz
-- Emri --
Kaukazi
-- Përkufizimi --
Kaukazi është zonë ekologjike.
UltësiraKaspiane
-- Emri --
Ultësira Kaspiane
-- Përkufizimi --
Ultësira Kaspiane është zonë ekologjike
3.2. Metadata
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3. Kodi EPSG për KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në sistemin referues gjeodezik zyrtar, Korniza Referuese Gjeodezike Shqiptare (KRGJSH), miratuar me vendimin e Këshillit të Ministrave nr. 669, datë 7.8.2013, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë”, i ndryshuar me vendimin nr. 322, datë 27.4.2016 dhe me vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është: EPSG - 6870.
3.4. Cilësia e të dhënave
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve si dhe cilësinë e matjes së të dhënave, që duhen përdorur, për të vlerësuar dhe dokumentuar cilësinë për grupet e të dhënave gjeohapësinore të temës “Zonat ekologjike”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- Vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku pronat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit.
- Vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore.
- Për të specifikuar kërkesat ose rekomandimet, në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore që lidhen me temën “Zonat ekologjike”.
Tabela e mëposhtme paraqet të gjitha elementet dhe nënelementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, datasetit ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën “Sfera e vlerësimit”.
Masat që do të përdoren për secilin nga nënelementet e listuara të cilësisë së të dhënave janë përcaktuar në nënseksionet e mëposhtme.
Tabela - Elementet e cilësisë së të dhënave të përdorura në temën “Zonat ekologjike”
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
3.6.1
Përputhja
logjike
Përputhja konceptuale
Zbatimi i rregullave në skemën konceptuale
Grup të dhënash; llojet e objektit gjeohapësinor; objekti gjeohapësinor
3.6.2
Përputhja
logjike
Përputhja
në domein
Zbatimi i vlerave në vlerat e domeinit
Grup të dhënash; llojet e objektit gjeohapësinor; objekti gjeohapësinor
3.4.1. Përputhja logjike - Përputhja konceptuale (Logical consistency - Conceptual cosistency)
Rekomandim
Për testet në përputhjen konceptuale është e rekomanduar të përdoret Përputhja ligjore - Përputhja konceptuale e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me rregullat e skemës konceptuale, sikurse është specifikuar në tabelën e mëposhtme:
Emri
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja logjike
Cilësia e të dhënave të nënelementeve
Përputhja konceptuale
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i të gjitha elementeve në grupin e të dhënave që nuk janë në përputhje me rregullat e skemës konceptuale.
Përshkrimi
Nëse skema konceptuale përshkruan shprehimisht ose në mënyrë absolute rregullat, këto rregulla duhet të ndiqen. Shkeljet ndaj rregullave të tilla mund të jenë, për shembull, vendosja e pavlefshme e karakteristikave brenda një tolerance të definuar, dyfishimin e karakteristikave dhe mbivendosja e pavlefshme e karakteristikave.
Fusha e vlerësimit
Objektet gjeohapësinore dhe llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencë
SSH EN ISO 19157-1 Informacioni Gjeografik - Cilësia e të dhënave
Shembulli
-
Masa identifikuese
10
3.4.2. Përputhja logjike - Përputhja me Domeinin (Logical consistency - Domain consistency)
Rekomandim
Për testet në përputhje me domeinin, është e rekomanduar të përdoret Përputhja logjike - Përputhja në domein e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me vlerën e domeinit sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i artikujve që nuk janë në përputhje me vlertat e domeinit të tyre
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja logjike
Cilësia e të dhënave të nënelementeve
Përputhje me domeinin
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i të gjitha elementeve në grupin e të dhënave që nuk janë në përputhje vlerat e domeinit të tyre
Përshkrimi
-
Fusha e vlerësimit
Objektet gjeohapësinore dhe llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
4. ANEKSE
4.1. Aneksi A - Katalogu i tipologjisë
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
Zonat ekologjike
3.1.4.1.
Bio-GeographicalRegion
ZonatEkologjike
ZonatEkologjike
FeatureType
3.1.4.2.
NaturalVegetationClassificationValue
VleratEKlasifikimitTëBimësisëNatyrore
ZonatEkologjike
CodeList
3.1.4.3.
MarineStrategyFrameworkDirectiveClassificationValue
VleratEKlasifikimitTëDirektivaveTëKornizësSëStrategjisëDetare
ZonatEkologjike
CodeList
3.1.4.4.
EnvironmentalStratificationClassificationValue
VleratEKlasifikimitTëShtresëzimitMjedisor
ZonatEkologjike
CodeList
3.1.4.5.
RegionClassificationValue
VleratEKlasifikimitTëZonave
ZonatEkologjike
CodeList
3.1.4.6.
Natura2000AndEmeraldBio-GeographicalRegionClassificationValue
VleratEKlasifikimitTëZonaveEkologjikeEmeraldDheNatura2000
ZonatEkologjike
CodeList
3.1.4.7.
RegionClassificationLevelValue
VleratENivelitTëKlasifikimitTëZonës
ZonatEkologjike
CodeList
3.1.4.8.
RegionClassificationSchemeValue
VleratESkemësSëKlasifikimitTëZonës
ZonatEkologjike
CodeList
3.1.4.9.
WaterFrameworkDirectiveEcoregionsClassificationValue
VleratEKlasifikimitTëZonaveEkologjikeTëDirektivësSëKornizësSëUjit
ZonatEkologjike
CodeList
4.2. ANEKSI B - Kodlistat
4.2.1 Skema e aplikimit për temën “Zonat ekologjike”
KODLISTAT
VleratEKlasifikimitTëBimësisëNatyrore
VleratEKlasifikimitTëDirektivësPërKornizënEStrategjisëDetare
VleratEKlasifikimitTëShtresëzimitMjedisor
VleratEKlasifikimitTëZonave
VleratEKlasifikimitTëZonaveEkologjikeEmeraldDheNatura2000
VleratENivelitTëKlasifikimitTëZonës
VleratESkemësSëKlasifikimitTëZonës
4.2.1.1. Vlerat e klasifikimit të bimësisë natyrore
-- Emri --
Vlerat e klasifikimit të bimësisë natyrore
-- Përkufizimi --
Kodet për klasifikimin e bimësisë natyrore.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/naturalVegetation
-- Vlerat -
Vlerat e kësaj kodliste përcaktohen në:
Hartën e bimësisë natyrore të Evropës: shkalla 1:2,500,000, pjesa 2: Legjenda, Bundesamt für Naturschutz (Agjencia Federale Gjermane për ruajtjen e natyrës), Bon, 2000.
4.2.1.2. Vlerat e klasifikimit të Direktivës për Kornizën e Strategjisë Detare
-- Emri --
Vlerat e klasifikimit të Direktivës për Kornizën e Strategjisë Detare
-- Përkufizimi --
Kodet për klasifikimin e Direktivës për Kornizën e Strategjisë Detare.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/marineStrategyFrameëorkDirective
-- Vlerat -
Vlerat e kësaj kodliste përcaktohen në: Klasifikimi i llojeve të habitatit sipas tabelës 1 të shtojcës III, të Direktivës 2008/56/EC.
4.2.1.3. Vlerat e klasifikimit të Shtresëzimit mjedisor
-- Emri --
Vlerat e klasifikimit të shtresëzimit mjedisor
-- Përkufizimi --
Kodet për shtresëzimin klimatik të mjedisit në Evropë.
-- Përshkrimi --
Bazuar në variablat mjedisorë (klima, gjeomorfologjia, oqeani dhe nortifikimi) përdoret një analizë e komponentëve kryesorë të grupimit ISODATA. Shtresëzimi mjedisor i Evropës përbëhet nga 84 shtresa, të cilat janë grumbulluar në 13 zona mjedisore me rezolucion hapësinor prej 1 km².
Shënim. Ky shtresëzim është sipas Metzger et al. 2005.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/environmentalStratification
-- Vlerat -
Vlerat e kësaj kodliste përcaktohen në:
Përshkrime të zonave mjedisore evropiane dhe shtresave, Wageningen, 2012.
http://content.alterra.wur.nl/Webdocs/PDFFiles/Alterrarapporten/AlterraRapport2281.pdf
4.2.1.4. Vlerat e klasifikimit të zonave
-- Emri --
Vlerat e klasifikimit të zonave
-- Përkufizimi --
Kodet që përcaktojnë rajone të ndryshme të zonave ekologjike.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/RegionClassificationValue
4.2.1.5. Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
-- Emri --
Vlerat e klasifikimit të zonave ekologjike Emerald dhe Natura 2000
-- Përkufizimi --
Kodet për klasifikimin e zonave ekologjike.
-- Përshkrimi --
http://www.eea.europa.eu/data-and-maps/data/biogeographical-regions-europe/codelistfor-bio-geographical-regions
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/Natura2000AndEmeraldBiogeographicalRegionClassificationValue
-- Vlerat -
Vlerat e kësaj kodliste përcaktohen në:
Kodet për klasifikimin e zonave ekologjike, siç përcaktohet në kodlistën për zonat ekologjike, Evropë 2011, të botuara në faqen e internetit të Agjencisë Evropiane të Mjedisit.
4.2.1.6. Vlerat e nivelit të klasifikimit të zonës
-- Emri --
Vlerat e nivelit të klasifikimit të zonave
-- Përkufizimi --
Kodet që përcaktojnë nivelin e klasifikimit të klasës së zonave.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/RegionClassificationLevelValue
-- Vlerat -
Vlerat e lejuara për këto kodlista përmbajnë vetëm vlerat e specifikuara në tabelën më poshtë.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëri prej tyre mund të përdoret.
KODLISTË
-- Emri -
Ndërkombëtar
-- Përkufizimi -
Ky është një klasifikim rajoni në nivel ndërkombëtar.
-- Emri -
Lokal
-- Përkufizimi --
Ky është një klasifikim i zonave në nivel lokal.
-- Emri --
Kombëtar
-- Përkufizimi -
Ky është një klasifikim i zonave në nivel kombëtar.
-- Emri --
Rajonal
-- Përkufizimi -
Ky është një klasifikim rajoni në nivel rajonal.
4.2.1.7. Vlerat e skemës së klasifikimit të zonës
-- Emri --
Vlerat e skemës të klasifikimit të zonës
-- Përkufizimi --
Kodet që përcaktojnë rajone të ndryshme për zonat ekologjike.
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/RegionClassificationSchemeValue
-- Vlerat -
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëri prej tyre mund të përdoret.
KODLISTË
-- Emri -
Shtresëzimi mjedisor
-- Përkufizimi -
Një grup kodlistash që do të përdoren për të përcaktuar shtresëzimin e mjedisit.
-- Përshkrimi -
Shiko Metzger tek al. 2005
-- Emri -
Natura 2000 dhe zona ekologjike Emerald
-- Përkufizimi --
Një grup kodlistash që do të përdoren për të përcaktuar rrjetin Natura 2000 dhe Zona Ekologjike Emerald.
-- Përshkrimi -
Shiko Direktivën e Habitateve (1992)
-- Emri --
Bimësi natyrore
-- Përkufizimi -
Një grup kodlistash që do të përdoren për të përcaktuar bimësinë natyrore.
-- Përshkrimi -
Shiko Bohn et al. (2000)
-- Emri --
Direktiva e Kornizës së Strategjisë Detare
-- Përkufizimi -
Një grup kodesh që do të përdoren për klasifikimin e strategjisë detare për klasifikimin e rajonit.
-- Përshkrimi -
Shiko Direktivën e Kornizës së Strategjisë Detare (2008)
