# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI
TEMA: “INFRASTRUKTURA PËR MONITORIMIN E MJEDISIT”
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Infrastruktura për monitorimin e mjedisit
3.1.1 Parathënie
3.1.2 Skemat e aplikimit dhe diagrami UML për temën Infrastruktura për monitorimin e mjedisit
3.1.3 Katalogu i tipologjive
3.1.3.1 Aktiviteti i monitorimit të mjedisit
3.1.3.2 Hierarkia
3.1.3.3 Lidhjet me domein
3.1.3.. Kapaciteti i monitorimit
3.1.3.5 Objekti i monitorimit
3.1.3.6 Periudha e aktivitetit operacional
3.1.3.7 Programi i monitorimit të mjedisit
3.1.3.8 Rrjeti i monitorimit të mjedisit
3.1.3.9 Raportimi në aktin ligjor
3.1.3.10 Infrastruktura për monitorimin e mjedisit
3.1.3.11 Rrjeti i infrastrukturës
3.1.3.12 Tipologjia e monitorimit
3.1.3.13 Vlerat e elementeve të monitorimit
3.1.3.14 Vlerat e qëllimit të grumbullimit
3.1.3.15 Vlerat e llojit të procesit
3.1.3.16 Vlerat e rezultatit në burim
3.1.3.17 Vlerat e natyrës së rezultatit
3.1.3.18 Vlerat e specializuara të llojit të infrastrukturës për monitorimin e mjedisit
3.1.3.19 Vlerat e matjes së regjimit
3.2 Metadata
3.3 Kodi EPSG për KRGJSH-në
3.4 Cilësia e të dhënave
3.4.1 Përputhja ligjore - Përputhja konceptuale (Logical consistency - Conceptual consistency)
3.4.2 Përputhja ligjore - Përputhja me domeinin (Logical consistency - Domain consistency)
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjive
4.2 ANEKSI C - Kodlistat
4.2.1. Skema e aplikimit për temën Infrastruktura për monitorimin e mjedisit
4.2.1.1 Vlerat e matjes së regjimit
4.2.1.2 Vlerat e elementit të monitorimit
4.2.1.3 Vlerat e llojit të procesit
4.2.1.4 Vlerat e rezultatit në burim
4.2.1.5 Vlerat e natyrës së rezultatit
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG), në bashkëpunim me Agjencinë Kombëtare të Mjedisit (AKM), e cila është autoritet publik përgjegjës, për temën Infrastruktura për monitorimin e mjedisit.
Data e publikimit të versionit nr. 1 është 20 dhjetor 2019. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2019_ IMM_v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit
Standard - Lloji i dokumentit
NSDI - Qëllimi i dokumentit
2019 - Viti i krijimit
IMM - Tema për të cilën është krijuar standardi: Infrastruktura për monitorimin e mjedisit, e cila i referohet temës “Environmental Facilities” të direktivës INSPIRE
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 Qëllimi
Ky dokument përcakton specifikimet teknike, për të dhënat gjeohapësinore të temës; Infrastruktura për monitorimin e mjedisit, temë e cila është përcaktuar në nenin 11, pika 2/o, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse, për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmëri midis tyre.
2.2 Si lexohet dokumenti
2.2.1 Struktura e dokumentit
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve - Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje - Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema - Në këtë pjesë jepen specifikimet teknike për temën Infrastruktura për monitorimin e mjedisit.
4. Anekse - Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës, si dhe detajohen: Diagramet UML dhe katalogu i tipologjive.
3.2 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3 Sistemi Koordinativ Referencë - Këtu përcaktohet sistemi koordinativ referencë (KRGJSH)
3.4 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJIve
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në “Katalogun e tipologjive” (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave, duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive, mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në Katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të shembujve, shpjegojnë mënyrën e organizimit të informacionit, në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit, në tabelën e kodlistave.
Tabela 1
EMRI - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
«FeatureType», një element që mund të jetë real, në terren, apo një dukuri abstrakte
«DataType», një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër.
«Enumeration» “codeList”, listë e parapërgatitur vlerash, ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara, si “Numërtimet dhe kodlistat”.
«Union», një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet, të cilat bien brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse.
«Imported», të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden të shqipëruara, si “Të dhënat e importuara”.
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë, poligon.
“Abstrakt”, kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
Shumëllojshmëria
Lloji dhe numri i vlerave që mund të marrë atributi:
0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë;
1..* - mund të marrë minimumi 1 vlerë ose shumë vlera;
0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme;
1 - duhet të marrë detyrimisht 1 vlerë.
I detyrueshëm
Po - nëse atributi është i detyrueshëm të plotësohet.
Jo - nëse atributi nuk është i detyrueshëm të plotësohet.
Rol shoqërimi
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
Përkufizimi i elementeve
Vlera e dytë (etj.) e listës së gatshme, p.sh.: Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve
2.2.3 Karakteristikat <<voidable>> dhe shumëllojshmëria
Stereotipi <<voidable>> përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në realitet. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat, e përcaktuara për objektet gjeohapësinore, duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera “void”. Një vlerë “void” nënkupton që nuk ekziston një vlerë përkatëse, në grupet e të dhënave gjeohapësinore, që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës “void” duhet të paraqitet kurdo që të jetë e mundur, duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
- E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrimi --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni të caktuar, nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E papopulluar”
- Konfidenciale (Withheld).
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull. Të dhënat personale të popullsisë, të cilat ekzistojnë, por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi <<voidable>> nuk jep asnjë informacion nëse ekziston një karakteristikë në realitet. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në realitet, vlera minimale do të përcaktohet si 0. P.sh., nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në realitet, vlera minimale do të përcaktohet si 1. P.sh., nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe/ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh., vendndodhja e sensorëve), kurbat përcaktuese (p.sh., izolinjat), rrjetet (p.sh., ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si veti të llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është realizim i një prej llojeve të specifikuara në SSH EN ISO 19123.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh., ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik, për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptual të Përgjithshëm “Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi, një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje mbulimi (ose një nëntip i tyre) në skemat e aplikimit në INSPIRE.
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 NUMëRTIMEt dhe kodlistat (Enumeration and code list)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistën, “vlera të tjera” përcaktohet lloji i përmbajtjes së kodlistës, e përcaktuar specifikisht, si më poshtë:
- “jo” përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
- “të kufizuara” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave;
- “të hapura” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave.
- “po” përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese, të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo”, pra të specifikuara në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 Paraqitja e DIMENSIONIT kohor
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në realitet.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
- Shënim i rëndësishëm
Disa terma në Katalogun e tipologjive, si p.sh. FeatureType, DataType, Void, Coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike, sipas termave të direktivës INSPIRE.
2.3 Detyrimet ligjore
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, ASIG është institucioni përgjegjës për krijimin e standardeve, për secilën nga temat e përcaktuara në nenin 11, të këtij ligji, në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (sikurse është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM nr. 1077, datë 23.12.2015).
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 Fusha e veprimit
Të gjitha autoritetet publike, kompanitë private apo individë që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2: Proceset e ciklit jetësor
Planifikimi - Është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
Vlerësimi - Është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
Procesimi (Përpunimi) - Është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
Shpërndarja - Është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
Zbulimi - Është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
Analiza - Është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
Përditësimi - Është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
Arkivimi - Është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen, arkivohen, duke u bazuar në standarde kombëtare dhe në legjislacionin në fuqi të vendit ku implementohet standardi. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen, për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
Shkatërrimi - Është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde kombëtare ose legjislacionin në fuqi.
3. TEMA
3.1 Infrastruktura për monitorimin e mjedisit
3.1.1 Parathënie
Tema Infrastruktura për monitorimin e mjedisit përfshin vendndodhjen, funksionimin, vëzhgimin dhe matjet e shkarkimeve në stacionin e monitorimit, si dhe gjendjen e parametrave mjedisorë dhe të ekosistemeve (biodiversiteti, kushtet ekologjike të bimësisë etj.), realizuar nga, apo në emër të autoriteteve publike.
Kjo temë përfshin dy aspekte kryesore, që janë: stacionet e monitorimit të mjedisit, si objekte gjeohapësinore, si dhe të dhënat e marra përmes vëzhgimeve dhe matjeve të kryera në këto objekte.
Tema Infrastruktura për monitorimin e mjedisit është ndërvepruese në fushat tematike mjedisore, kështu që modeli i përgjithshëm lejon lirinë për të sjellë nevoja specifike dhe tematike, duke mbajtur një strukturë të përbashkët të të dhënave.
Nënfusha tematike mjedisore e përcaktuar nga tema e të dhënave gjeohapësinore Infrastruktura për monitorimin e mjedisit është ndërlidhëse, për çdo zonë tematike që merret me mjedisin, dhe se qëllimet mund të arrihen nga sondazhet dhe marrjet e mostrave me metoda të ndryshme, deri nga satelitët. Fokusi është në objektet e monitorimit mjedisor, si dhe në elementet lidhëse midis temave të tjera të të dhënave gjeohapësinore, si vëzhgimet dhe matjet në aspektet specifike të mjedisit (p.sh. cilësia e ajrit, kushtet atmosferike, cilësia e ujit etj.).
Specifikimi i të dhënave në këtë temë përpiqet të adresojë dy dimensione. Nga njëra anë, objektet e monitorimit mjedisor janë të lidhura me informacionin që përshkruan grupin e stacioneve të monitorimit për nënfushën e caktuar. Nga ana tjetër, objektet e monitorimit mjedisor lidhen me vëzhgimet dhe matjet e kryera. Kjo pjesë e specifikimit të të dhënave do të mbulohet duke përdorur në standard vëzhgime dhe matje të përshtatura për një strukturë të përbashkët të përdorur në specifikimin e të dhënave INSPIRE, në të gjitha fushat tematike.
Specifikimi i të dhënave krijon mundësinë për të zbatuar modelin konceptual, sipas nevojave funksionale të shteteve. Mënyra të ndryshme të lidhjes së objekteve të monitorimit mjedisor, që shprehen sipas niveleve hierarkike, marrëdhëniet gjenealogjike në ndonjë lidhje tematike, të cilat japin mundësinë për të ofruar informacione në nivelin e duhur të detajeve/grumbullimit dhe një organizim të mirë për nevojat tematike. Dokumentimi i legjislacionit në të gjitha nivelet, nga ai lokal në atë evropian apo global, është një informacion thelbësor për monitorimin e aktiviteteve. Lidhjet nga objektet e monitorimit mjedisor me raportimin mjedisor janë të përfshira në modelin konceptual të temës Infrastruktura për monitorimin e mjedisit.
Modeli konceptual i të dhënave, në këtë version të specifikimit të të dhënave, është zhvilluar përmes disa hapave drejt një qasjeje të përgjithshme, por të shkallëzueshme. Modeli i ofruar është një kornizë e përbashkët brenda së cilës duhet të përshkruhet tema Infrastruktura për monitorimin e mjedisit, në një mënyrë të përbashkët në zonat e territoreve, ndërsa harmonizimi për aspektet e hollësishme mbetet me aspektet e fushës.
Synimi i përgjithshëm për specifikimin e të dhënave për temën Infrastruktura për monitorimin e mjedisit është të ofrojë një model të përgjithshëm i cili mund të përdoret në fusha të ndryshme dhe ofrimi i lirisë së nevojshme për fushat tematike, për të sjellë nevoja specifike, duke mbajtur një strukturë të përbashkët. Pra, specifikimi i të dhënave siguron një strukturë të përbashkët por jo një harmonizim tematik në të gjitha fushat.
Struktura mund të duket komplekse, por mundëson që komunitetet të specifikojnë lehtësirat e monitorimit mjedisor me vëzhgime dhe matje të lidhura me nivelin e duhur të detajeve që është e rëndësishme për shkëmbimin e të dhënave. Ky dokument specifik përpiqet të ruajë ekuilibrin midis të qenët (i përshtatshëm dhe i zotërueshëm) dhe jo të qenët abstrakt dhe i lexueshëm nga ekspertët. Infrastruktura për monitorimin e mjedisit përcakton gjuhën e vetme, e cila duhet të përdoret për fushat ndërlidhëse dhe kjo ofron një mundësi për të hyrë në informacione me këndvështrim ndërdisiplinor.
Specifikimi i të dhënave të temës Infrastruktura për monitorimin e mjedisit
Përshkrimi i Infrastrukturës për monitorimin e mjedisit është një element themelor për të lidhur vëzhgimet dhe matjet me një veçori gjeohapësinore. Objektet e monitorimit mund të grupohen në rrjetet e monitorimit, pasi një numër objektesh u përkasin programeve monitoruese me perspektivë afatgjatë (kryesisht të nxitura nga legjislacioni) ose mund të përfshihen në aktivitete specifike monitorimi.
Legjislacioni është një element themelor për krijimin e lehtësirave për monitorimin e mjedisit i cili siguron informacion të rëndësishëm për autoritetet publike që merren me mjedisin. Meqë vëzhgimet dhe matjet janë të lidhura me strukturën e monitorimit mjedisor, kontribuojnë në çdo lloj raportimi (të detyrueshëm apo vullnetar), kjo lidhje përfshihet në specifikimin e të dhënave për të krijuar një marrëdhënie midis objekteve të monitorimit mjedisor dhe raporteve që duhen dorëzuar ose dhënë. Kjo ka për qëllim të mbështesë opsionalisht raportimin elektronik në të ardhmen.
Specifikimet e të dhënave mbulojnë të gjitha llojet e monitorimit mjedisor, duke përdorur stacione fikse, pajisje lëvizëse ose sensorë të largët, të cilët mund të zbatohen për nevojat tematike të fushave të ndryshme.
Të drejtat e aksesit dhe mbrojtja e të dhënave në pikat e nivelit të vëzhgimit të stacionit është një aspekt mjaft i rëndësishëm për monitorimin specifik, si mbrojtja e natyrës dhe monitorimi i biodiversitetit. Publikimi i stacionit të objektit të monitorimit mund të ndryshojë pikën e vëzhguar dhe për këtë arsye e kryen vetë monitorimin.
Aspektet që lidhen me nivelin e përshtatshëm të detajeve dhe shkëmbimin e të dhënave të informacionit janë pjesë e organizimit të Infrastrukturës për monitorimin e mjedisit. Aspektet e tjera që lidhen me të drejtat e aksesit dhe mbrojtjen e të dhënave janë jashtë mjeteve mbrojtëse.
Nuk mbulohen nga specifikimet e të dhënave të temës Infrastruktura për monitorimin e mjedisit:
- Kuptimi i strukturës specifike dhe përshtatja e elementeve të tyre.
- Udhëzues për nivelin e duhur të detajeve, pasi ky është specifik i fushës së studimit.
- Shembuj që mbulojnë fushat tematike, të adresuara nga temat e tjera të INSPIRE, si ekspertizë domeini nuk është në dispozicion të infrastrukturës për monitorimin e mjedisit.
- Menaxhimi i saktë i të drejtave të aksesit dhe mbrojtja e të dhënave nuk është objekt i këtij specifikimi të dhënash.
3.1.2 Skemat e aplikimit dhe DIAGRAME UML për temën Infrastruktura për monitorimin e mjedisit
Skema e aplikimit të temës Infrastruktura për monitorimin e mjedisit përfshin dy aspekte, që janë: përshkrimi i një objekti, si dhe monitorimi dhe lidhja për vëzhgime dhe matje. Skema ndjek një trajtë të përgjithshme, e cila duhet t’u mundësojë komuniteteve tematike të përdorin këtë strukturë në fushat përkatëse. Specifikimet dhe përkufizimet ofrojnë fleksibilitet të mjaftueshëm për fushat tematike për të sjellë të dhënat e tyre. Për të mos krijuar një bashkësi tematike, elementet e zakonshme janë të përcaktuar në specifikimin e të dhënave, janë mbajtur në minimum dhe janë zvogëluar në elemente të cilat shihen si thelbësore për të hyrë në objektet e monitorimit mjedisor, në një mënyrë të përbashkët dhe për të mbajtur një emërues të përbashkët nëpër domeine. Kërkesat tematike të domeineve janë shumë të ndryshme dhe harmonizimi nëpër tema është kompleks. Dimensioni i harmonizimit specifik të temës/domeinit nuk është nënvlerësuar dhe mbetet me përparësi të lartë, në lidhje me shkëmbimin e të dhënave të rëndësishme, por nuk mund të mbulohet nga skema e aplikimit të temës Infrastruktura për monitorimin e mjedisit. Kjo do të përfshijë përdorimin e domeinit të kodeve dhe kërkesave të përbashkëta për të ofruar informacione për objektet e monitorimit mjedisor. Nga ky këndvështrim, specifikimi i të dhënave të temës Infrastruktura për monitorimin e mjedisit duhet të mbulojë kërkesat nga fusha specifike e domeinit, por, gjithashtu, të sigurojë një mundësi për zhvillimet e ardhshme.
Tema Infrastruktura për monitorimin e mjedisit përfshin aspektin e përshkrimit të shërbimit të monitorimit mjedisor. Linku për vrojtimin dhe matjet përfshihet në modelin e ofruar, por duke u adresuar nga një udhëzim që përfshin referenca të sakta.
Skema e aplikimit të temës Infrastruktura për monitorimin e mjedisit përmban 4 lloje objektesh gjeohapësinore:
- Programi i monitorimit të mjedisit;
- Aktiviteti i monitorimit të mjedisit;
- Rrjeti i monitorimit të mjedisit;
- Infrastruktura për monitorimin e mjedisit;
Infrastruktura për monitorimin e mjedisit është lloji qendror i objektit gjeohapësinor për të dyja aspektet e temës. Përshkrimi përqendrohet në shpjegimin e llojeve të objekteve gjeohapësinore, siç u përmendën më sipër, për të shpjeguar marrëdhëniet e tyre, si dhe për lidhjen me vrojtimet dhe matjet. Për arsye modelimi, dy kategoritë abstrakte janë futur në grupin e atributeve, të përbashkëta të ndara, midis llojeve të objekteve gjeohapësinore.
Ideja e përgjithshme e modelit të dhënë është që secili domein mund të vendosë bazuar në kërkesat specifike, se cili nivel i detajeve është më i përshtatshëm. Modeli nuk nënkupton një nivel të detyrueshëm të detajeve, por jep mundësinë për ta kryer aty ku është më e përshtatshme.
Figura 3: Ndërlidhja e diagrameve me skemën e aplikimit të temës “Infrastruktura për monitorimin e mjedisit”
Figura 4: Diagrami UML: Përshkrimi i skemës së aplikimit të temës “Infrastruktura për monitorimin e mjedisit”
Infrastruktura për monitorimin e mjedisit
Ekzistenca gjeohapësinore e temës Infrastruktura për monitorimin e mjedisit është rezultat i informacionit të modeluar në këtë temë, por edhe në dy kategori abstrakte të përmendura më lart. Përshkrimi i infrastrukturës për monitorimin e mjedisit ndan elementet me llojet e tjera të objektit gjeohapësinor të këtij modeli dhe këto atribute janë modeluar në kategori abstrakte, si të gjitha llojet e tjera të objekteve gjeohapësinore. Infrastruktura për monitorimin e mjedisit ka një atribut gjeometrik si pikë përfaqësuese për të lehtësuar nevojën për të pasur një paraqitje të pikës në kontekstin tematik. Një strukturë e monitorimit të mjedisit mund të jetë fikse, e lëvizshme ose e bashkëngjitur me një tjetër. Meqenëse infrastruktura për monitorimin mjedisor mund të përshkruhet në nivele të ndryshme detajesh, modeli ofron një lidhje hierarkike. Kjo pasqyron faktin se një stacion mund të ketë pjesë të ndryshme ose një platformë në të cilën mund të jenë një numër sensorësh ose pajisjesh matëse, duke u modeluar si një lidhje atributesh “hierarkike”.
Figura 5: Skema e aplikimit të hierarkisë së temës “Infrastruktura për monitorimin e mjedisit”
Për rastet kur infrastruktura e monitorimit të mjedisit është duke përfunduar funksionimin e saj dhe mbivendoset nga një tjetër, modeli i lidhjes gjenealogjike është modeluar. Kjo lidhje reflekton që infrastruktura për monitorimin e mjedisit zëvendësohet nga një tjetër. Arsyeja kryesore për ta integruar këtë në modelin tonë është të sigurojmë një mekanizëm i cili siguron që vëzhgimet në lidhje me mjedisin mund të interpretohen si seri dhe vazhdimësi nga një këndvështrim tematik.
Figura 6: Skema e aplikimit të lidhjes gjenealogjike brenda një hierarkie të temës “Infrastruktura për monitorimin e mjedisit”
Lidhja tematike është modeluar për të pasqyruar çështjen që në grupe të ndryshme tematike është e nevojshme të kryhen lidhje midis infrastrukturës për monitorimin e mjedisit, për të krijuar një lidhje të pavarur nga lidhjet hierarkike ose gjenealogjike. Për shembull, kur një strukturë për monitorimin e sasisë së ujit ka të bëjë me një stacion monitorimi në rrjedhën e sipërme, të cilësisë së ujit. Lidhja e modeluar ofron një mundësi për bashkësitë tematike, që lidhin infrastrukturën për monitorimin e mjedisit, në përputhje me nevojat e tyre specifike të brendshme.
Përpunimi i avancuar i grumbullimit të automatizuar, duke filluar nga niveli më i lartë i detajeve dhe i kufizimeve, se si të zhvillohet grumbullimi, i cili është në përgjegjësinë e plotë të ekspertëve tematikë dhe, për këtë arsye, nuk mund të jetë pjesë e modelit të temës Infrastruktura për monitorimin e mjedisit, i cili duhet të qëndrojë në aspekt të përgjithshëm.
Figura 7: Diagrami UML i nxjerrë nga skema e aplikimit të temës “Infrastruktura për monitorimin e mjedisit”
Rrjeti i monitorimit të mjedisit:
RrjetiIMonitorimitTëMjedisit është një lloj objekti gjeohapësinor në modelin përkatës, me një numër në infrastrukturën e monitorimit mjedisor. Është e mundur të sigurohen informacione për nivelin e grumbulluar të një rrjeti të monitorimit mjedisor, duke përfshirë mundësinë për të pasur kaskada të rrjeteve dhe nënrrjeteve. Një strukturë e infrastrukturës së monitorimit mjedisor mund t’u përkasë rrjeteve të ndryshme të monitorimit, p.sh., duke qenë pjesë e një rrjeti rajonal dhe kombëtar.
Figura 8: Diagrami UML i nxjerrë nga skema e aplikimit “Rrjetet e monitorimit të mjedisit”
Programi i monitorimit të mjedisit
Programi i monitorimit të mjedisit është një përshkrim i rëndësishëm për politikën që përcakton objektivin për grumbullimin e vrojtimeve/vendosjen e infrastrukturës për monitorimin e mjedisit në këtë fushë. Programi i monitorimit të mjedisit ka një perspektivë afatgjatë për të paktën disa vjet. Program i monitorimit të mjedisit mbulon një zonë interesi (p.sh., një rajon) dhe bazohet në legjislacionin mjedisor. Përshkrimi i këtij lloji të objektit gjeohapësinor ofron një pasqyrë të qartë dhe mund të përdoret për vlerësimin e politikave.
Informacioni i lidhur me programin e monitorimit të mjedisit është i rëndësishëm edhe nëse lokacioni i objekteve është i fshehur. Ai siguron një pikë hyrjeje të përgjithshme për informacionin e monitorimit të mjedisit me një pamje të përgjithshme ku mund të zbatohet nga domeine të kryqëzuara. Niveli i detajeve të vëna në dispozicion është në domeinin tematik, por jo i shkaktuar nga skema e aplikacionit. Klasa ObjektiIMonitorimit modelon të gjitha elementet e përbashkëta midis Infrastrukturës për monitorimin e mjedisit, Rrjetit të monitorimit të mjedisit dhe Programit të monitorimit të mjedisit. Këto atribute ofrojnë një emërues të përbashkët midis llojeve thelbësore të objekteve gjeohapësinore dhe lejojnë një grupim ose qasje duke përdorur të njëjtat atribute.
Figura 9: Diagrami UML i nxjerrë nga skema e aplikimit “Programi i monitorimit të mjedisit”
Aktiviteti i monitorimit të mjedisit:
Skema e aplikimit të Aktiviteti i monitorimit të mjedisit shpreh nevojën për të përshkruar fushat e monitorimit mjedisor që kryhen me pajisje specifike për një periudhë të caktuar kohore.
Shembull mund të jetë një lundrim kërkimor i një anijeje me pajisje monitorimi në oqean ose fluturime nga një aeroplan që ka sensorë të ndryshëm për vëzhgimet në ajër. Këta shembuj tregojnë rëndësinë e lartë për objektet e lëvizshme të monitorimit të mjedisit, në lidhje me një perspektivë afatgjatë të programeve të monitorimit mjedisor. Aktiviteti i monitorimit të mjedisit modelohet si një lidhje ndërmjet Infrastrukturës për monitorimin e mjedisit dhe Rrjetit për monitorimin e mjedisit për një kohë specifike, në Programin e monitorimit të mjedisit, duke përdorur kategorinë abstrakte të TipologjiaEMonitorimit si elementi i tyre i përbashkët.
Figura 10: Diagrami UML i nxjerrë nga skema e aplikimit “Aktiviteti i monitorimit të mjedisit”
Një pjesë thelbësore e temës Infrastruktura për monitorimin e mjedisit lidhet me vrojtimet dhe matjet e marra në një strukturë të shërbimit mjedisor. Lidhja me kategorinë Vrojtimi pasqyron lidhje të drejtpërdrejtë, e cila është e mundur nga çdo infrastrukturë për monitorimin e mjedisit ose rrjet i monitorimit të mjedisit. Kategoria KapacitetiIMonitorimit është modeluar për të treguar nevojën që një regjim matjeje të përshkruhet pa siguruar vetë vlerën e vëzhguar ose të matur. Kategoria përmban atribute për të përshkruar kohën operacionale për një regjim matjeje, një vlerë të llojit të procesit për të bërë dallimin midis Procesit dhe Sensorit si tregues i asaj që pritet të ketë lidhje me procesin, VleraENatyrësSëRezultatit, të cilat janë të dhëna parësore, të dhëna të përpunuara ose që vijnë nga modele të ngjashme dhe në rast se është në dispozicion informacioni që regjimi i matjes është krijuar për të shërbyer në mënyrë specifike nga një raportim detyruar.
Së bashku me lidhjen Vrojtimi kategoria KapacitetiIMonitorimit krijon një lidhje të qëndrueshme nga tema Infrastruktura për monitorimin e mjedisit për vëzhgimet dhe matjet. Përputhjet duhet të sigurohen midis lidhjeve nga kategoritë e KapacitetiIMonitorimit dhe Vrojtimit. Pra, nëse një vrojtim është i lidhur me një infrastrukturë për monitorimin e mjedisit, edhe ky objekt duhet të ketë një përshkrim të aftësisë monitoruese. KapacitetiIMonitorimit duhet t’i referohet Fenomenit dhe Procesit identik si Vrojtimi. Domeini duhet të jetë identik ose në disa raste, domeini i vrojtimit është një tipologji e domeinit të KapacitetiIMonitorimit.
Figura 11: Diagrami UML i nxjerrë nga skema e aplikimit “Kapaciteti i monitorimit dhe vëzhgimi”
Këtu paraqiten ato pjesë të adresuara të skemës së aplikimit të temë Infrastruktura për monitorimin e mjedisit, që kanë të bëjnë me vrojtimet dhe matjet e kryera te shërbimi.
Roli i Vrojtimit duhet të zbatohet, si më poshtë:
- të mos përdoret asnjë vlerë nëse nuk ka vrojtim në stacion (d.m.th. ai nuk është akoma funksional).
- përdorimi “të pavlefshme” dhe “jo populluar” nëse ka vëzhgime, por shërbimi i monitorimit/ofruesi i të dhënave të rrjetit nuk ka qasje në to.
- përdorimi “fshehur” nëse ka vrojtime, por këto nuk janë në dispozicion në përputhje me këtë specifikim.
Referencat e monitorimit të mjedisit:
Figura 12: Skema e aplikimit “Referencat e monitorimit të mjedisit”
Kodlistat dhe numërtimet për temën “Infrastruktura për monitorimin e mjedisit”
Figura 13: Kodlistat
3.1.3 Katalogu i tipologjive
3.1.3.1 Aktiviteti i monitorimit të mjedisit
-- Emri --
Aktiviteti i monitorimit të mjedisit
-- Përkufizim --
Grupi specifik i TipologjiaEMonitorimit, i përdorur për një domein të caktuar, në një kornizë kohore koherente, për një zonë ose destinacion. Zakonisht informacionet e mbledhura trajtohen si një e dhënë kohore në një program monitorimi afatgjatë. Është një realizim konkret i caktuar në PrograminEMonitorimitTëMjedisit.
-- Përshkrim --
Për shembull, një anije mund të pajiset me një koleksion të InfrastrukturësPërMonitoriminEMjedisit për një fushë të dhënë (AktivitetiIMonitorimitTëMjedisit), që përmbush kërkesën për PrograminEMonitorimitTëMjedisit. Pas një periudhe të caktuar, kjo anije mund të jetë e pajisur me një grup tjetër për InfrastrukturënEMonitorimitTëMjedisit për një fushë që përmbush kërkesat e ProgramitTëMonitorimitTëMjedisit.
-- Tipi i elementit --
FeatureType
ATRIBUTET
BurimetOnline: URL
Shumëllojshmëria: [0..*]
-- Emri --
Burimet online
-- Përkufizimi --
Lidhja me dokumentet e jashtëm që ofron informacione të mëtejshme mbi AktivitetiIMonitorimitTëMjedisit.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
-- Emri --
InspireId
-- Përkufizimi --
Identifikuesi i objektit të jashtëm.
[I detyrueshëm: PO]
PeriudhaEMonitorimit: Objekt
Shumëllojshmëria: [1]
-- Emri --
Periudha e monitorimit
-- Përkufizimi --
Jetëgjatësia e AktivitetiIMonitorimitTëMjedisit.
[I detyrueshëm: PO]
KornizaKufizuese: Kufiri
Shumëllojshmëria: [0..1]
-- Emri --
Korniza kufizuese
-- Përkufizimi --
Korniza kufizuese në të cilën zhvillohet AktivitetiIMonitorimitTëMjedisit
-- Përshkrimi --
Shembull. Nëse një anije kërkimore ka disa aktivitete monitorimi (AktivitetiIMonitorimitTëMjedisit ) është e rëndësishme të dimë për secilën nga anijet se kur do dalë në det (AktivitetiIMonitorimitTëMjedisit).
[I detyrueshëm: PO]
KushtetEAktivitetit: Tekst
Shumëllojshmëria: [1]
-- Emri --
Kushtet e aktivitetit
-- Përkufizimi --
Përshkrimi i AktivitetiIMonitorimitTëMjedisit.
[I detyrueshëm: PO]
PalëtPërgjegjëse: Palët përgjegjëse
Shumëllojshmëria: [1]
-- Emri --
Palët përgjegjëse
-- Përkufizimi --
Palët përgjegjëse për AktivitetiIMonitorimitTëMjedisit.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Dy-Drejtime)
Burimi: Publike “voidable” shkakton (Class) AktivitetiIMonitorimitTëMjedisit “featureType”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
AktivitetiIMonitorimitTëMjedisit shkaktuar nga ProgramiIMonitorimitTëMjedisit
Objektivi: Publike «voidable» VendosurPër (Class) ProgramiIMonitorimitTëMjedisit “featureType”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
ProgramiIMonitorimitTëMjedisit për të cilën AktivitetiIMonitorimitTëMjedisit është vendosur.
Lidhja (Drejtimi: Dy-Drejtime)
Burimi: Publike “voidable» përdorime (Class) TipologjiaEMonitorimit “featureType”
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Struktura specifike e TipologjiaEMonitorimit e përfshirë në një AktivitetiIMonitorimitTëMjedisit.
Target: Publike «voidable» IPërfshirë (Class) AktivitetiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
AktivitetiIMonitorimitTëMjedisit në të cilën është përfshirë TipologjiaEMonitorimit.
3.1.3.2. Hierarkia
-- Emri --
Hierarkia
-- Përkufizim --
Lidhja hierarkike midis ObjektiIMonitorimit.
-- Tipi i elementit --
DataType (AssociationClass)
ATRIBUTET
PeriudhaELidhjes: Objekt
Shumëllojshmëria: [1]
-- Emri --
Periudha e lidhjes
-- Përkufizimi --
Periudha kohore e lidhjes hierarkike.
[I detyrueshëm: PO]
3.1.3.3. Lidhjet me domein
-- Emri --
Lidhjet me domein
-- Përkufizimi --
Lidhjet e përshtatshme të InfrastrukturaPërMonitoriminEMjedisit, e cila nuk është hierarkike ose e lidhur nga pikëpamja gjenealogjike.
-- Tipi i elementit --
DataType (AssociationClass)
ATRIBUTET
Komente: CharacterString
Shumëllojshmëria: [1]
-- Emri --
Komente
-- Përkufizimi --
Informacione shtesë mbi lidhjen e domeinit.
[I detyrueshëm: PO]
3.1.3.4 Kapaciteti i monitorimit
-- Emri --
Kapaciteti i monitorimit
-- Përkufizim --
Aftësitë e ObjektiIMonitorimit.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Agreguar nga «featureType» KapacitetiIMonitorimi tek «featureType» ObjektiMonitorimit
ATRIBUTET
BurimetOnline: URL
Shumëllojshmëria: [0..1]
-- Emri --
Burimet online
-- Përkufizimi --
Lidhja me dokumentet e jashtme që ofrojnë informacione të mëtejshme në lidhje me një model të të dhënave në përputhje me ISO 19156 “Vëzhgime dhe Matje”, i përdorur për të ruajtur ose shkëmbyer vëzhgimet dhe matjet e marra.
[I detyrueshëm: PO]
LlojiIProcesit: VleraELlojitTëProcesit
Shumëllojshmëria: [1]
-- Emri --
Lloji i procesit
-- Përkufizimi --
Lloji i objektit që përdoret për përshkrimin e procesit.
[I detyrueshëm: PO]
KohaEMonitorimi: Objekt
Shumëllojshmëria: [1]
-- Emri --
Koha e monitorimit
-- Përkufizimi --
Përshkruan periudhën kohore që vëzhgimet mund të ndërlidhen nga ObjektiIMonitorimit. Mund të jetë vetëm një kohë fillimi për ekzekutimin e matjeve ose një interval.
[I detyrueshëm: PO]
NatyraERezultatit: VleraENatyrësSëRezultatit
Shumëllojshmëria: [1]
-- Emri --
Natyra e rezultatit
-- Përkufizimi --
Gjendja e rezultatit të dhënë.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Burimi -> Destinacioni) Domein
Burimi: Publike (Class) KapacitetiIMonitorimit «featureType»
Objektivi: Publike «voidable» TipologjiaEInteresit (Class) TipologjiaEGFI «FeatureType»
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Kjo tipologji në realitet është objekt, pronat e të cilit janë nën vëzhgim, ose është një tipar i synuar për të provuar objektin në realitet.
Lidhja (Drejtimi: Burimi -> Destinacioni) Fenomen
Burimi: Publike (Class) KapacitetiIMonitorimit «featureType»
Objektivi: KarakteristikatEVrojtimit (Metaclass) LlojitITipitGF «metaclass»
Shumëllojshmëria: [1]
-- Përkufizimi --
Karakteristikat e vëzhgimit ose matjet në ObjektiIMonitorimit.
Lidhja (Drejtimi: Burimi -> Destinacioni) ProcesetEPërdorimit
Burimi: Publike (Class) KapacitetiIMonitorimit «featureType»
Objektivi: Procedurat (Class) Procesi «FeatureType»
Shumëllojshmëria: [1]
-- Përkufizimi --
Lidhja me procesin e përdorur për të gjeneruar rezultatin. Procesi do të jetë i përshtatshëm për karakteristikat e vëzhguara. Si përfundim, detajet e karakteristikave të vëzhguara kufizohen nga procedurat e përdorura.
3.1.3.5 Objekti i monitorimit
-- Emri --
Objekti i monitorimit
-- Përkufizim --
Klasa bazë për objektet e monitorimit mjedisor.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga «featureType» ProgramiIMonitorimitTëMjedisit tek «featureType» ObjektiIMonitorimit
Gjeneralizuar nga «featureType» TipologjiaEMonitorimit tek «featureType» ObjektiIMonitorimit
Agreguar nga «featureType» KapacitetiIMonitorimit tek «featureType» ObjektiIMonitorimit
ATRIBUTET
BurimeOnline: URL
Shumëllojshmëria: [0..*]
-- Emri --
Burime online
-- Përkufizimi --
Lidhja me dokumentet e jashtme që ofrojnë informacione të mëtejshme mbi ObjektiIMonitorimit.
[I detyrueshëm: PO]
Emri: CharacterString
Shumëllojshmëria: [0..*]
-- Emri --
Emri
-- Përkufizim --
Kuptimi i saktë i tekstit të ObjektiIMonitorimit.
[I detyrueshëm: PO]
Gjeometria: Objekt
Shumëllojshmëria: [0..1]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria e lidhur me ObjektiIMonitorimit.
-- Përshkrimi --
Për pajisjet e shërbimit gjeometria paraqet sipërfaqen në të cilën pritet të matet objekti.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
-- Emri --
InspireId
-- Përkufizimi --
Identifikuesi i objektit të jashtëm gjeohapësinor.
[I detyrueshëm: PO]
ElementiIMonitorimit: VleraEMedias
Shumëllojshmëria: [1..*]
-- Emri --
Elementi i monitorimit
-- Përkufizimi --
Monitorimi i treguesit mjedisor.
[I detyrueshëm: PO]
PalëtPërgjegjëse: Palët përgjegjëse
Shumëllojshmëria: [0..*]
-- Emri --
Palët përgjegjëse
-- Përkufizimi --
Palët përgjegjëse për ObjektiIMonitorimit.
[I detyrueshëm: PO]
PërshkrimiShtesë: CharacterString
Shumëllojshmëria: [0..1]
-- Emri --
Përshkrimi shtesë
-- Përkufizimi --
Përshkrimi i informacionit shtesë që nuk përshtatet me atributet.
[I detyrueshëm: PO]
PrejardhjaLigjore: CitimiILegjislacionit
Shumëllojshmëria: [0..*]
-- Emri --
Prejardhja ligjore
-- Përkufizimi --
Konteksti ligjor në të cilin përcaktohet menaxhimi dhe rregullimi i ObjektiIMonitorimit.
[I detyrueshëm: PO]
Qëllimi: VleraEQëllimitTëGrumbullimit
Shumëllojshmëria: [0..*]
-- Emri --
Qëllimi
-- Përkufizimi --
Arsyeja për të cilën është krijuar ObjektiIMonitorimit.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Dy-Drejtime) Hierarkia
Burimi: Publike «voidable» IPlotë (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Një lidhje që tregon një ObjektiIMonitorimit më të gjerë (një nivel më i lartë në një strukturë hierarkike). Lidhjet kanë karakteristika shtesë siç përcaktohen në klasën e hierarkisë së lidhjeve.
Objektivi: Publike «voidable» IKufizuar (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Një lidhje që tregon një ObjektiIMonitorimit më të ngushtë (një nivel më i ulët në një strukturë hierarkike). Lidhjet kanë karakteristika shtesë siç përcaktohen në klasën e hierarkisë së lidhjeve.
Lidhje (Drejtimi: Dy-Drejtime) Gjenealogjia
Burimi: Publike «voidable» Zëvendëson (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Në një gjenealogji, ObjektiIMonitorimit që ka (kanë) është çaktivizuar/zëvendësuar nga një tjetër.
Objektivi: Publike «voidable» ZëvendësuarNga (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Në një gjenealogji, ObjektiIMonitorimit i ri aktiv që zëvendëson atë të mëparshmin.
Lidhje (Drejtimi: Dy-Drejtime) Hierarki
Burimi: Publike «voidable» IPlotë (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..1]
-- Përkufizimi --
Një lidhje që tregon një ObjektiIMonitorimit më të gjerë (një nivel më i lartë në një strukturë hierarkike). Lidhjet kanë karakteristika shtesë siç përcaktohen në klasën e hierarkisë së lidhjeve.
Objektivi: Publike «voidable» IKufizuar (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Një lidhje që tregon një ObjektiIMonitorimit më të ngushtë (një nivel më i ulët në një strukturë hierarkike). Lidhjet kanë karakteristika shtesë siç përcaktohen në klasën e hierarkisë së lidhjeve.
Lidhje (Drejtimi: Dy-Drejtime) Gjenealogjia
Burimi: Publike «voidable» Zëvendëson (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Në një gjenealogji, ObjektiIMonitorimit që ka (kanë) është çaktivizuar/zëvendësuar nga një tjetër.
Objektivi: Publike «voidable» ZëvendësuarNga (Class) ObjektiIMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Në një gjenealogji, ObjektiIMonitorimit i ri aktiv që zëvendëson atë të mëparshmin.
3.1.3.6 Periudha e aktivitetit operacional
-- Emri --
Periudha e aktivitetit operacional
-- Përkufizim --
Korrespondon me një periudhë gjatë së cilës InfrastrukturaEMonitorimitTëMjedisit ka qenë duke funksionuar, periudhe kohore 1-vjeçare.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Agreguar nga «featureType» PeriudhaEAktivitetitOperacional tek «featureType» InfrastrukturaEMonitorimitTëMjedisit
ATRIBUTET
PeriudhaEMonitorimit: Objekt
Shumëllojshmëria: [1]
-- Emri --
Periudha e monitorimit
-- Përkufizimi --
Jetëgjatësia e PeriudhaEAktivitetitOperacional.
[I detyrueshëm: PO]
3.1.3.7 Programi i monitorimit të mjedisit
-- Emri --
Programi i monitorimit të mjedisit
-- Përkufizim --
Dokumentet e bazuara në strukturën përkatëse të politikave që përcaktojnë objektivin dhe grumbullimin e vëzhgimeve dhe/ose shpërndarjen e TipologjiaEMonitorimit në terren. Zakonisht Programi i monitorimit të mjedisit ka një perspektivë afatgjatë për të paktën disa vjet.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» ProgramiIMonitorimitTëMjedisit tek «featureType» ObjektiIMonitorimit
LIDHJE
Lidhja (Drejtimi: Burimi -> Destinacioni)
Burimi: Publike (Class) NgjarjaAbstrakteEVëzhguar «featureType»
Objektivi: Publike «voidable» MonitorohetNga (Class) ProgramiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Programi që monitoron ngjarjen e vëzhguar.
Lidhje (Drejtimi: Dy-Drejtime)
Burimi: Publike «voidable» Shkakton (Class) AktivitetiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
AktivitetiIMonitorimitTëMjedisit shkaktuar nga ProgramiIMonitorimitTëMjedisit.
Objektivi: Publike «voidable» VendosurPër (Class) ProgramiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
ProgramiIMonitorimitTëMjedisit për të cilën AktivitetiIMonitorimitTëMjedisit është ndërtuar.
3.1.3.8 Rrjeti i monitorimit të mjedisit
-- Emri --
Rrjeti i monitorimit të mjedisit
-- Përkufizim --
Grupimi administrativ ose organizativ i InfrastrukturaPërMonitoriminEMjedisit ka menaxhuar të njëjtën mënyrë për një qëllim specifik, duke synuar një zonë specifike. Çdo rrjet respekton rregullat e zakonshme që sigurojnë koherencën e vëzhgimeve, veçanërisht për qëllime të InfrastrukturaPërMonitoriminEMjedisit, përzgjedhjen e detyrueshme të parametrave të metodës së matjes dhe regjimit të matjes.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» RrjetiIMonitorimitTëMjedisit tek «featureType» TipologjiaEMonitorimit
ATRIBUTET
NiveliIOrganizimit: VleratENivelitTëLegjislacionit
Shumëllojshmëria: [1]
-- Emri --
Niveli i organizimit
-- Përkufizimi --
Niveli i organizimit juridik (kombëtar, rajonal, etj.) me të cilin është lidhur RrjetinEMonitorimitTëMjedisit.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Dy-Drejtime)
Burimi: Publike «voidable» IPërket (Class) RrjetiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Një lidhje që tregon për RrjetiIMonitorimitTëMjedisit që i përket InfrastrukturaPërMonitoriminEMjedisit.
Lidhja ka karakteristika shtesë siç përcaktohen në klasën e lidhjes RrjetiIInfrastrukturës.
Objektivi: Publike «voidable» Përmban (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Një lidhje që tregon që InfrastrukturaPërMonitoriminEMjedisit përfshihet në RrjetiIMonitorimitTëMjedisit.
Lidhja ka karakteristika shtesë siç përcaktohen në klasën e lidhjes RrjetiIInfrastrukturës.
3.1.3.9 Raportimi në aktin ligjor
-- Emri --
Raportimi në aktin ligjor
-- Përkufizim --
Informacioni që përfshihet në raportin e TipologjiaEMonitorimit. Informacioni është specifik për raportimet e paraqitura dhe jo për detyrim marrëveshje.
-- Përshkrim --
Me anë të raportimit të aktit ligjor, bëhet raportimi i gjendjes së mjedisit.
-- Tipi i elementit --
DataType
ATRIBUTET
AktiLigjor: CitimiILegjislacionit
Shumëllojshmëria: [1]
-- Emri --
Akti ligjor
-- Përkufizimi --
Akti ligjor për të cilin raportohet.
[I detyrueshëm: PO]
DataERaportimit: Data
Shumëllojshmëria: [1]
-- Emri --
Data e raportimit
-- Përkufizimi --
Koha e raportimit.
[I detyrueshëm: PO]
KapacitetiIKërkuarIMonitorimit: Boolean
Shumëllojshmëria: [1]
-- Emri --
Kapaciteti i kërkuar i monitorimit
-- Përkufizimi --
Tregon nëse KapacitetiIMonitorimit është i nevojshëm për TipologjiaEMonitorimit.
[I detyrueshëm: PO]
VëzhgimiINevojshëm: Boolean
Shumëllojshmëria: [1]
-- Emri --
Vëzhgimi i nevojshëm.
-- Përkufizimi --
Tregon nëse kërkohet një vëzhgim për TipologjiaEMonitorimit.
[I detyrueshëm: PO]
Përshkrimi: CharacterString
Shumëllojshmëria: [0..1]
-- Emri -
Përshkrimi
-- Përkufizimi --
Informacione plotësuese për të dhënat aktuale të raportuara.
[I detyrueshëm: PO]
RaportiPërmbledhës: URI
Shumëllojshmëria: ( [0..1]
-- Emri --
Raporti përmbledhës
-- Përkufizimi --
Lidhja me të dhënat e raportuara përcaktohet në bazë të datës së treguar në raportin e atributeve.
[I detyrueshëm: PO]
3.1.3.10 Infrastruktura për monitorimin e mjedisit
-- Emri --
Infrastruktura për monitorimin e mjedisit
-- Përkufizimi --
Një objekt gjeografik që mbledh ose përpunon të dhëna në lidhje me objektet (p.sh., aspektet fizike, kimike, biologjike ose aspektet e tjera të kushteve mjedisore) që janë parë ose matur në mënyrë të përsëritur. Një strukturë e monitorimit mjedisor mund të përqasë edhe objekte të tjera të monitorimit mjedisor.
-- Përshkrimi --
Shënim 1. InfrastrukturaPërMonitoriminEMjedisit nuk është një strukturë në kuptimin e përbashkët të INSPIRE, por vjen e realizuar nga modelit konceptual i klasës së AktivitetitKompleks.
Shënim 2. Laboratorët nuk janë InfrastrukturaPërMonitoriminEMjedisit nga perspektiva INSPIRE pasi vendndodhja e saktë e laboratorit nuk shton informacione të mëtejshme në matje. Metodologjia e përdorur në laborator duhet të sigurohet me të dhëna periodike.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» InfrastrukturaPërMonitoriminEMjedisit tek «featureType» TipologjiaEMonitorimit
LIDHJE STRUKTURORE TË BRENDSHME
Agreguar nga «featureType» PeriudhaEAktivitetit tek «featureType» InfrastrukturaPërMonitoriminEMjedisit
ATRIBUTET
LlojiISpecializuarIInfrastruktuësPërMonitoriminEMjedisit VleraESpecializuarELlojitInfrastrukturaPërMonitoriminEMjedisit
Shumëllojshmëria: [0..1]
-- Emri --
Lloji i specializuar i Infrastrukturës për monitorimin e mjedisit.
-- Përkufizimi --
Kategorizimi i InfrastrukturaPërMonitoriminEMjedisit që përgjithësisht përdoret nga domeini në mjediset kombëtare.
-- Përshkrimi --
Shembull: Platformë, zonë, stacion, sensor...
[I detyrueshëm: PO]
StacionILëvizshëm: Boolean
Shumëllojshmëria: [1]
-- Emri --
Stacion i lëvizshëm
-- Përkufizimi --
InfrastrukturaPërMonitoriminEMjedisit tregon se është i riprodhueshëm gjatë përvetësimit të vëzhgimit.
[I detyrueshëm: PO]
RezultatiNëBurim: VleraEBurimitTëRezultatit
Shumëllojshmëria: [0..*]
-- Emri --
Rezultati në burim
-- Përkufizimi --
Burimi i përvetësimit të rezultatit
[I detyrueshëm: PO]
PikaPërfaqësuese: Pikë
Shumëllojshmëria: [0..1]
-- Emri --
Pika përfaqësuese
-- Përkufizimi --
Përfaqësimi i vendndodhjes për InfrastrukturaPërMonitoriminEMjedisit.
[I detyrueshëm: PO]
RegjimiIMatjes: VleratEMatjesSëRegjimit
Shumëllojshmëria: [1]
-- Emri --
Regjimi i matjes
-- Përkufizimi --
Regjimi i matjes (frekuenca).
[I detyrueshëm: PO]
LIDHJA
Lidhje (Drejtimi: Burimi -> Destinacioni)
Burimi: Publike (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Objektivi: Publike «voidable» LidhurMe (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Çdo lidhje teknike në Infrastrukturën për monitorimin e mjedisit. Lidhjet kanë karakteristika shtesë siç përcaktohen në klasën LidhjetMeDomein.
Lidhje (Drejtimi: Burimi -> Destinacioni)
-- Përkufizim --
Lidhet me monitorimin e objekteve mjedisore
Burimi: mobile (Class) PusAktiv «featureType»
Objektivi: Publike «voidable» MonitorimiIObjekteveMjedisore (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..1]
-- Emri -
Monitorimi i aftësisë mjedisore
-- Përkufizimi --
Lidhet me monitorimin e aftësive mjedisore
-- Përshkrim --
Pusi i vëzhgimit nëntokësor është një objekt monitorimi.
Lidhje (Drejtimi: Dy-Drejtime)
Burimi: Publike «voidable» IPërket (Class) RrjetiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Lidhje që tregon që RrjetiIMonitorimitTëMjedisit që i përket InfrastrukturaPërMonitoriminEMjedisit.
Lidhja ka karakteristika shtesë siç përcaktohen në klasën e lidhjes RrjetiIInfrastrukturës.
Objektivi: Publike «voidable» Përmban (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Një lidhje që tregon që InfrastrukturaPërMonitoriminEMjedisit përfshihet në RrjetiIMonitorimitTëMjedisit.
Lidhja ka karakteristika shtesë siç përcaktohen në klasën e lidhjes RrjetiIInfrastrukturës.
Lidhja (Drejtimi: Burimi -> Destinacioni)
Burimi: Publike (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Objektivi: Publike «voidable» LidhurMe (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Çdo lidhje tematike me InfrastrukturaPërMonitoriminEMjedisit.
Lidhja ka karakteristika shtesë siç përcaktohen në klasën e lidhjes RrjetiIInfrastrukturës.
Lidhja (Drejtimi: Burimi -> Destinacioni)
Burimi: Publike (Class) TrupiUjorëNëntokësorë «featureType»
Objektive: Publike «voidable» PusMonitorues (Class) InfrastrukturaPërMonitoriminEMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizim --
Pusi që monitoron trupin e ujit nëntokësor
3.1.3.11 Rrjeti i infrastrukturës
-- Emri --
Rrjeti i infrastrukturës
-- Përkufizim --
Lidhja midis RrjetiIMonitorimitTëMjedisit dhe InfrastrukturaPërMonitoriminEMjedisit.
-- Tipi i elementit --
DataType (AssociationClass)
ATRIBUTET
KohaELidhjes: Objekt
Shumëllojshmëria: [1]
-- Emri --
Periudha e lidhjes
-- Përkufizimi --
Periudha kohore e lidhjes.
[I detyrueshëm: PO]
3.1.3.12 Tipologjia e monitorimit
-- Emri --
Tipologjia e monitorimit
-- Përkufizimi --
Karakteristikat e klasës bazë për monitorimin mjedisor në realitet (RrjetiIMonitorimitTëMjedisit, InfrastrukturaPërMonitoriminEMjedisit).
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» TipologjiaEMonitorimit tek «featureType» ObjektiIMonitorimit
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga «featureType» InfrastrukturaPërMonitoriminEMjedisit tek «featureType» TipologjiaEMonitorimit
Gjeneralizuar nga «featureType» RrjetiIMonitorimitTëMjedisit tek «featureType» TipologjiaEMonitorimit
ATRIBUTET
RaportimiPër: RaportimiNëAktinLigjor
Shumëllojshmëria: [0..*]
-- Emri --
Raportuar për
-- Përkufizimi --
Informacion mbi përfshirjen e raportimit të TipologjiaEMonitorimit.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Dy-Drejtime)
Burimi: Publike «voidable» Përdorues (Class) TipologjiaEMonitorimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Grup i veçantë i TipologjiaEMonitorimit të përfshirë në një AktivitetiIMonitorimitTëMjedisit.
Objektivi: Publike «voidable» PërfshirëNë (Class) AktivitetiIMonitorimitTëMjedisit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
AktivitetiIMonitorimitTëMjedisit në cilin TipologjiaEMonitorimit përfshihet.
Lidhja (Drejtimi: Burimi -> Destinacioni)
Burimi: Publike (Class) TipologjiaEMonitorimit «featureType»
Objektivi: Publike «voidable» KaVëzhgim (Class) Vëzhgim «FeatureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Vëzhgimi i emetimeve, gjendja e medieve mjedisore dhe parametrave të tjerë të ekosistemit (biodiversiteti, kushtet ekologjike të bimësisë, etj.) nga ose në emër të autoriteteve publike në këtë TipologjiaEMonitorimit.
3.1.3.13 Vlerat e elementeve të monitorimit
-- Emri --
Elementet e monitorimit
-- Përkufizim --
Kategoritë për lloje të ndryshme të elementeve të monitorimit.
-- Tipi i elementit --
Kodlistë
3.1.3.14 Vlerat e qëllimit të grumbullimit
-- Emri --
Qëllimi i grumbullimit
-- Përkufizim --
Kategoritë për qëllime të ndryshme të grumbullimit.
-- Tipi i elementit --
Kodlistë
3.1.3.15 Vlerat e llojit të procesit
-- Emri --
Lloji i procesit
-- Përkufizim --
Kategoritë për llojet e ndryshme të procesit.
-- Tipi i elementit --
Kodlistë
3.1.3.16 Vlerat e rezultatit në burim
-- Emri --
Rezultati në burim
-- Përkufizim --
Kategoritë e llojeve të ndryshme të BurimitTëPërmirsimitTëRezultatit.
-- Tipi i elementit --
Kodlistë
3.1.3.17 Vlerat e natyrës së rezultatit
-- Emri --
Natyra e rezultatit
-- Përkufizim --
Gjendja e rezultatit të një vëzhgimi.
-- Tipi i elementit --
Kodlistë
3.1.3.18 Vlerat e specializuara të llojit të Infrastrukturës për monitorimin e mjedisit
-- Emri --
Lloji i specializuar i Infrastrukturës për monitorimin e mjedisit
-- Përkufizim --
Kategoritë e llojeve të ndryshme për InfrastrukturaPërMonitoriminEMjedisit.
-- Tipi i elementit --
Kodlistë
3.1.3.19 Vlerat e matjes së regjimit
-- Emri --
Matja e regjimit
-- Përkufizim --
Kategoritë për lloje të ndryshme të RegjimitTëMatjes.
-- Tipi i elementit --
Kodlistë
3.2 Metadata
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3 Kodi EPSG për KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare (KRGJSH), miratuar me vendimin e Këshillit të Ministrave nr. 669, datë 7.8.2013, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë” ndryshuar me vendimin nr. 322, datë 27.4.2016 dhe vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është EPSG - 6870.
3.4 Cilësia e të dhënave
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur, për të vlerësuar dhe dokumentuar cilësinë për grupet e të dhënave gjeohapësinore të temës Infrastruktura për monitorimin e mjedisit.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- Vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku pronat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit.
- Vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore.
Specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore, që lidhen me temën Infrastruktura për monitorimin e mjedisit.
Tabela e mëposhtme, paraqet të gjitha elementet dhe nënelementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, datasetit ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën “Sfera e vlerësimit”.
Masat që do të përdoren për secilin nga nënelementet e listuara të cilësisë së të dhënave janë përcaktuar në nënseksionet e mëposhtme.
Tabela: Elementet e cilësisë së të dhënave të përdorura në temën “Infrastruktura për monitorimin e mjedisit”
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
3.6.1
Përputhja ligjore
Përputhja konceptuale
Zbatimi i rregullave në skemën konceptuale.
Grup të dhënash;
Llojet e objektit gjeohapësinor; Objekti gjeohapësinor
3.6.2
Përputhja ligjore
Përputhja në domein
Zbatimi i vlerave në vlerat e domeinit.
Grup të dhënash; Llojet e objektit gjeohapësinor; Objekti gjeohapësinor
3.4.1 Përputhja ligjore - Përputhja konceptuale (Logical consistency - Conceptual consistency)
Rekomandim
Për testet në përputhjen konceptuale është e rekomanduar të përdoret Përputhja ligjore - Përputhja konceptuale e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me rregullat e skemës konceptuale sikurse është specifikuar në tabelën e mëposhtme:
Emri
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja konceptuale
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i të gjitha elementeve në grupin e të dhënave që nuk janë në përputhje me rregullat e skemës konceptuale.
Përshkrimi
Nëse skema konceptuale përshkruan shprehimisht ose në mënyrë absolute rregullat, këto rregulla duhet të ndiqen. Shkeljet ndaj rregullave të tilla mund të jenë, për shembull, vendosjen e pavlefshme të karakteristikave brenda një tolerance të definuar, dyfishimin e karakteristikave dhe mbivendosjen e pavlefshme të karakteristikave.
Fusha e vlerësimit
Objektet Gjeohapësinore/Llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
-
Cilësia e të dhënave të strukturës së vlerave
Integer
Burimi referencë
ISO/DIS 19157 Informacioni Gjeografik - Cilësia e të dhënave
Shembulli
-
Masa identifikuese
10
3.4.2 Përputhja ligjore - Përputhja me domeinin (Logical consistency - Domain consistency)
Rekomandim
Për testet në përputhje me domeinin, është e rekomanduar të përdoret Përputhja ligjore - Përputhja në domein e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me vlerën e domeinit sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i artikujve që nuk janë në përputhje me vlertat e domeinit të tyre
Emri alternativ
-
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Përputhje me domeinin
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i të gjitha elementeve në grupin e të dhënave që nuk janë në përputhje vlerat e domeinit të tyre
Përshkrimi
-
Fusha e vlerësimit
Objektet gjeohapësinore/Llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjive
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
Infrastruktura për monitorimin e mjedisit
3.1.3.1
EnvironmentalMonitoringActivity
AktivitetiIMonitorimitTëMjedisit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.2
Hierarchy
Hierarkia
InfrastrukturaPërMonitoriminEMjedisit
AssociationClass
3.1.3.3
AnyDomainLink
LidhjetMeDomein
InfrastrukturaPërMonitoriminEMjedisit
AssociationClass
3.1.3.4
ObservingCapability
KapacitetiIMonitorimit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.5
AbstractMonitoringObject
ObjektiIMonitorimit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.6
OperationalActivityPeriod
PeriudhaEAktivitetitOperacional
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.7
EnvironmentalMonitoringProgramme
ProgramiIMonitorimitTëMjedisit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.8
EnvironmentalMonitoringNetwork
RrjetiIMonitorimitTëMjedisit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.9
ReportToLegalAct
RaportimiNëAktinLigjor
InfrastrukturaPërMonitoriminEMjedisit
DataType
3.1.3.10
EnvironmentalMonitoringFacility
InfrastrukturaPërMonitoriminEMjedisit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.11
NetworkFacility
RrjetiIInfrastrukturës
InfrastrukturaPërMonitoriminEMjedisit
AssociationClass
3.1.3.12
AbstractMonitoringFeature
TipologjiaEMonitorimit
InfrastrukturaPërMonitoriminEMjedisit
FeatureType
3.1.3.13
MediaValue
VleratEElementitTëMonitorimit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.14
PurposeOfCollectionValue
VleratEQëllimitTëGrumbullimit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.15
ProcessTypeValue
VleratELlojitTëProcesit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.16
ResultAcquisitionSourceValue
VleratERezultatitNëBurim
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.17
ResultNatureValue
VleratENatyrësSëRezultatit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.18
SpecialisedEMFTypeValue
VleratESpecializuaraTëLlojitTëInfrastrukturësPërMonitoriminEMjedisit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
3.1.3.19
MeasurementRegimeValue
VleratEMatjesSëRegjimit
InfrastrukturaPërMonitoriminEMjedisit
CodeList
4.2 ANEKSI C - Kodlistat
4.2.1 Skema e aplikimit për temën Infrastruktura për monitorimin e mjedisit
KODLISTAT
VleratEMatjesSëRegjimit
VleratEElementitTëMonitorimit
VleratELlojitTëProcesit
VleratERezultatitNëBurim
VleratENatyrësSëRezultatit
4.2.1.1 Vlerat e matjes së regjimit
-- Emri --
Matja e regjimit
-- Përkufizimi --
Kategoritë për lloje të ndryshme të MatjesSëRegjimit.
-- Identifikuesi --
http://inspire.ec.europa.eu/codeList/MeasurementRegimeValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përmbajnë çdo vlerë të përcaktuar nga prova e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
KODLISTË
-- Emri --
Mbledhja e vazhdueshme e të dhënave.
-- Përkufizimi -
Të dhënat grumbullohen në mënyrë të vazhdueshme, zakonisht nuk ka datë përfundimi pasi mblidhen të dhëna në mënyrë të vazhdueshme.
-- Emri --
Mbledhja e të dhënave të detyruara nga kërkesat.
-- Përkufizimi --
Të dhënat e mbledhura që janë të detyruara nga kërkesa.
-- Emri --
Mbledhja e veçantë e të dhënave
-- Përkufizimi--
Të dhënat mblidhen vetëm një herë në këtë konfigurim dhe nuk mund të priten vëzhgime të tjera.
-- Emri --
Mbledhja periodike e të dhënave
-- Përkufizimi --
Të dhënat grumbullohen në interval të rregullta. Asnjë informacion nuk është në dispozicion në intervalin e mbledhjes së të dhënave.
4.2.1.2 Vlerat e elementit të monitorimit
-- Emri --
Vlerat e elementit të monitorimit
-- Përkufizimi --
Kategoritë për lloje të ndryshme të elementit të monitorimit.
-- Identifikuesi --
http://inspire.ec.europa.eu/codeList/MediaValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përmbajnë çdo vlerë të përcaktuar nga provat e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
KODLISTË
-- Emri --
Ajri
-- Emri --
Zhvillimi i jetës së kafshëve dhe bimëve në një territor të caktuar në periudha të ndryshme gjeologjike.
-- Emri --
Peizazh
-- Emri --
Sedimente
-- Emri --
Tokë/terren
-- Emri --
Mbeturina
-- Emri --
Ujë
4.2.1.3 Vlerat e llojit të procesit
-- Emri --
Lloji i procesit
-- Përkufizimi --
Kategoritë për lloje të ndryshme të procesit.
-- Identifikuesi --
http://inspire.ec.europa.eu/codeList/ProcessTypeValue
-- Vlerat -
Vlerat e lejuara për këtë kodlistë përmbajnë çdo vlerë të përcaktuar nga prova e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
KODLISTË
-- Emri --
Procesi
-- Përkufizimi -
Tregon se kategoria e përdorur për përshkrimin e informacionit metodologjik të vrojtimit është kategoria e procesit e përcaktuar në GCM.
-- Emri --
Sensori ML
-- Përkufizimi --
Tregon se kategoria e përdorur për përshkrimin e informacionit metodologjik të vrojtimit vjen nga Sensorët.
4.2.1.4 Vlerat e rezultatit në burim
-- Emri --
Rezultatet në burim
-- Përkufizimi --
Kategoritë për lloje të ndryshme të përvetësimit të burimit të rezultatit (p.sh. Ph)
-- Identifikuesi --
http://inspire.ec.europa.eu/codeList/ResultAcquisitionSourceValue
-- Vlerat -
Vlerat e lejuara për këtë kodlistë përmbajnë çdo vlerë të përcaktuar nga prova e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
KODLISTË
-- Emri --
Jo në burim
-- Përkufizimi -
Tipologjia e interesit është një specie e marrë nga tipologjia e fundit e interesit (d.m.th. tipari i provuar).
-- Emri --
Në burim
-- Përkufizimi --
Tipologjia e interesit është një veçori e marrjes së mostrave, e cila është e bashkangjitur me tipologjinë e fundit të interesit (d.m.th. Tipari i provuar).
-- Emri --
Remote-sensing
-- Përkufizimi -
Tipologjia e interesit është një veçori e marrjes së mostrave e cila është, gjithashtu, tipologjia e fundit e interesit (d.m.th. tipari i provuar).
-- Emri --
Historike
-- Përkufizimi -
Vlera historike që janë trashëguar.
4.2.1.5 Vlerat e natyrës së rezultatit
-- Emri --
Natyra e rezultatit
-- Përkufizimi --
Gjendja e rezultatit të vrojtimit.
-- Identifikuesi --
http://inspire.ec.europa.eu/codeList/ResultNatureValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përmbajnë çdo vlerë të përcaktuar nga prova e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
KODLISTË
-- Emri -
Parësor
-- Përkufizimi -
Rezultati i ofruar nga vrojtimi është rezultat i drejtpërdrejtë i një vlerësimi të një karakteristike në TipologjinëEInteresit. Asnjë përpunim i mëtejshëm nuk është kryer. Përpunimi mund të ketë ndodhur, por vetëm në kuptimin e vetë të metodologjisë së matjes, d.m.th. konvertimi i mili voltit është kthyer nga një sensor në përqendrimin e një lënde.
-- Emri -
Të përpunuara
-- Përkufizimi --
Rezultati i dhënë, zakonisht bazohet në matjet parësore, për tu përpunuar në mënyrë thelbësore. Ky përpunim mund të jetë i natyrave të ndryshme, në disa situata sigurohen agregate komplekse, në situata të tjera vlerat ekzistuese janë futur që në fillim.
-- Emri --
Të simuluara
-- Përkufizimi -
Rezultati i dhënë zakonisht bazohet në matjet parësore, bazohet në një model interpretimi dhe siguron një simulim të gjendjeve të kaluara ose të ardhshme të medieve që analizohen. Në këtë rast vlerat ekzistuese zakonisht rriten në të ardhmen.
