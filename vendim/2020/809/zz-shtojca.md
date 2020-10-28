# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI - TEMA: MBULESA E TOKËS
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Mbulesa e tokës
3.1.1 Parathënie
3.1.2 Terma dhe përkufizime
3.1.3 Skemat e aplikimit dhe diagrami UML për temën “Mbulesa e tokës”
3.2 Përshkrimi i nëntemës “Nomenklatura e mbulesës së tokës”
3.2.1 Parathënie
3.2.2 Skema e aplikimit dhe diagrami UML për nëntemën “Nomenklatura e Mbulesës së tokës”
3.2.3 Katalogu i tipologjisë
3.2.3.1 Nomenklatura e mbulesës së tokës
3.2.3.2 Vlerat CORINE
3.2.3.3 Vlerat e klasës së mbulesës së tokës
3.3 Përshkrimi i nëntemës “Të dhënat vektor të mbulesës së tokës”
3.3.1 Parathënie
3.3.2 Skema e aplikimit dhe diagrami UML për nëntemën “Të dhënat vektor të mbulesës së tokës”
3.3.3 Katalogu i tipologjisë
3.3.3.1 Grupi i të dhënave të mbulesës së tokës
3.3.3.2 Vlerat e mbulesës së tokës
3.3.3.3 Vlerat e kategorisë së mbulesës së tokës
3.3.3.4 Vrojtimi i mbulesës së tokës
3.3.3.5 Njësia e mbulesës së tokës
3.4 Përshkrimi i nëntemës “Të dhënat raster të mbulesës së tokës”
3.4.1 Parathënie
3.4.2 Skema e aplikimit dhe diagrami UML për nëntemën “Të dhënat raster të mbulesës së tokës”
3.4.3 Katalogu i tipologjisë
3.4.3.1 Rrjeti i mbulimit të mbulesës së tokës
3.5 Metadata
3.6 Kodi EPSG për KRGJSH-në
3.7 Cilësia e të dhënave
3.7.1 Kompletimi - Autorizimi (Completness-Commission)
3.7.2 Kompletimi - Përjashtimi (Completness-Ommission)
3.7.3 Përputhja ligjore - Përputhja konceptuale (Logical consistency - Conceptual consistency)
3.7.4 Përputhja ligjore - Përputhja me domeinin (Logical consistency - Domain consistency)
3.7.5 Përputhja ligjore - Përputhja e formatit (Logical consistency - Format consistency)
3.7.6 Përputhja ligjore - Përputhja topologjike (Logical consistency - Topological consistency)
3.7.7 Cilësia e të dhënave - Saktësia e pozicionimit - Saktësia absolute ose e jashtme (Data quality - Positional accuracy - Absolute or extrenal accuracy)
3.7.8 Cilësia e të dhënave - Saktësia e pozicionimit - Saktësia relative ose e brendshme (Data quality - Positional accuracy - Relative or internal accuracy)
3.7.9 Cilësia e të dhënave - Saktësia tematike - Korrektësia e klasifikimit (Data quality - Thematic accuracy - Classification correctness)
3.7.10 Cilësia e të dhënave - Saktësia tematike - Saktësia e atributeve josasiore (Data quality - Thematic accuracy - Non-quantative attribute accuracy)
3.7.11 Cilësia e të dhënave - Saktësia tematike - Saktësia e atributeve sasiore (Data quality - Thematic accuracy - Quantative attribute accuracy)
4. ANEKSE
4.1. Aneksi A - Katalogu i tipologjisë
4.2. Aneksi B - Kodlistat
4.2.1. KodLista “Nomenklatura e mbulesës së tokës”
4.2.1.1 Vlerat CORINE
4.2.2 Vlerat e kategorisë së mbulesës së tokës
4.2.3 Kodlista për arsyet e pavlefshmërisë - Voidable
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG) në bashkëpunim me Ministrinë e Mjedisit (Agjencia Kombëtare e Mjedisit) dhe Qendrën e Transferimit të Teknologjive Bujqësore (QTTB). Data e publikimit të versionit nr. 1 është 11 prill 2018. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2018_ MT_v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit
Standard - Lloji i dokumentit
NSDI - Qëllimi i dokumentit
2018 - Viti i krijimit
MT - Tema për të cilën është krijuar standardi “Mbulesa e tokës”, e cila i referohet temës “Land Cover” të direktivës INSPIRE.
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 QËLLIMI
Ky dokument përcakton specifikimet teknike, për të dhënat gjeohapësinore të temës “Mbulesa e tokës”, temë e cila është përcaktuar në nenin 11, pika 2/h, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse për mbledhjen përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë e tyre.
2.2 SI LEXOHET DOKUMENTI
2.2.1 STRUKTURA E DOKUMENTIT
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: - Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: - Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë.
3. Tema: - Në këtë pjesë jepen specifikimet teknike për secilën temë “Mbulesa e tokës”.
4. Anekse: - Në këtë pjesë jepen informacione shtesë shpjeguese në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 7 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës dhe se si është ndarë kjo temë.
3.2 Përshkrimi i nëntemës së parë - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e nëntemës “Nomenklatura e mbulesës së tokës”, si dhe detajohen: Diagramet UML dhe Katalogu i tipologjive.
3.3 Përshkrimi i nëntemës së dytë - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e nëntemës “Të dhënat vektor të mbulesës së tokës”, si dhe detajohen: Diagramet UML dhe Katalogu i tipologjive.
3.4 Përshkrimi i nëntemës së tretë - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e nëntemës “Të dhënat raster të mbulesës së tokës”, si dhe detajohen: Diagramet UML dhe Katalogu i tipologjive.
3.5 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.6 Sistemi Koordinativ Referencë- Këtu përcaktohet sistemi koordinativ referencë (KRGJSH).
3.7 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet mes tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në “Katalogun e tipologjive” (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit në tabelat e të dhënave në Katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të një shembulli, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit në tabelën e kodlistës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi sipas direktivës INSPIRE për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
“FeatureType”, një element që mund të jetë real në terren apo një dukuri abstrakte.
“DataType”, një element tabelor që shërben vetëm si tabelë atributesh për t’u lidhur me një element tjetër.
“Enumeration” “codeList” - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
“Union”, një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet që bien brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse.
“Imported”, të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të dhënat e importuara”
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë ose poligon.
“Abstrakt”, kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
Shumëllojshmëria
Lloji dhe numri i vlerave që mund të marrë atributi:
0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë.
1..* - mund të marrë minimumi 1 vlerë ose shumë vlera.
0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme.
1 - duhet të marrë detyrimisht 1 vlerë.
I detyrueshëm
Po - nëse atributi është i detyrueshëm të plotësohet.
Jo - nëse atributi nuk është i detyrueshëm të plotësohet.
Rol shoqërimi
Në tabelën e lidhjeve “Rol-shoqërimet” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Atributet
“Atribut” janë informacione të bashkëngjitura në format tabelor te tipologjitë gjeohapësinore.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve.
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh., PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh., ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh., joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve.
2.2.3 KARAKTERISTIKAT E VOIDABLE DHE SHUMËLLOJSHMËRIA
Stereotipi voidable përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave) ose vlera void. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
- E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
SHEMBULL. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E papopulluar”
- Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull. Të dhënat personale të popullsisë, të cilat ekzistojnë, por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi voidable nuk jep asnjë informacion nëse ekziston një karakteristikë në realitet. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në realitet, vlera minimale do të përcaktohet si 0. P.sh., nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në realitet, vlera minimale do të përcaktohet si 1. P.sh., nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe /ose në hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, precipitimet, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh., vendndodhja e sensorëve), kurbat përcaktuese (p.sh., izolinjat), rrjetet (p.sh., ortoimazheria, modelet e lartësisë) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si vetitë e llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është një realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh., ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptues të Përgjithshëm “Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje të mbulimit (ose një nëntipi të tyre) në skemat e aplikimit në INSPIRE.
Figura 1. Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 NUMËRTIMET DHE KODLISTAT (ENUMERATION AND KODLISTE)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, “vlera të tjera” përcaktojnë llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht si më poshtë:
- “Jo” përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument.
- “Të kufizuara” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave.
- “Të hapura” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave.
- “Po” përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera jo të përmbajtura në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që dhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “Fillimi i Ciklit Jetësor” dhe “Përfundimi i Ciklit Jetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “ FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
Shënim i rëndësishëm
Disa terma në Katalogun e tipologjive, si p.sh., featureType, dataType, void, coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të Direktivës INSPIRE.
2.3 DETYRIMET LIGJORE
Në bazë të ligjit nr. 72/2012, neni 16, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatës në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë këtë direktivë.
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë, të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 FUSHA E VEPRIMIT
Të gjitha autoritetet publike, kompani private apo individë që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2. Proceset e ciklit jetësor
“Planifikimi” është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
“Vlerësimi” është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
“Procesimi” është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
“Shpërndarja” është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
“Zbulimi” është procesi i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
“Analiza” është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
“Përditësimi” është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
“Arkivimi” është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen, duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
“Shkatërrimi” është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 MBULESA E TOKËS
3.1.1 PARATHËNIE
Tema “Mbulesa e tokës” përfshin mbulimin fizik dhe biologjik të sipërfaqes së tokës, duke përfshirë sipërfaqet artificiale, sipërfaqet bujqësore, pyjet, zonat natyrore, ujërat.
Mbulesa e tokës është veshja e dukshme (bio) e sipërfaqes së tokës. Të dhënat e temës “Mbulesa e tokës” japin një përshkrim të sipërfaqes së tokës, sipas karakteristikave biofizike të saj. Hartimi dhe mbikëqyrja e mbulesës së tokës bëhet përmes iniciativave të vrojtimit të saj. Programi EEA Cover CORINE, studimi LUCAS i kryer nga Eurostat dhe shumë programe kombëtare/rajonale të mbulesës së tokës, janë baza e iniciativave për temën “Mbulesa e tokës”. Shumëllojshmëria e nismave të studimit, tregon se mbulesa e tokës mund të përshkruhet, klasifikohet dhe hartografohet në shumë mënyra të ndryshme, me anë të një sërë aplikacionesh dhe kërkesash të përdoruesve.
Sipërfaqja e përshkruar si mbulesë toke, në realitet është e populluar me elemente peizazhi. Elementet e peizazhit janë tipare fizike, si: ndërtesat, rrugët, pemët, bimët, trupat e ujit etj. Brenda një njësie toke, karakteristikat biofizike të këtyre elementeve të peizazhit kombinohen për të formuar mbulesën e tokës të asaj njësie. Hartografimi dhe përshkrimi i mbulesës së tokës ndryshon nga hartografimi i elementeve të peizazhit individual, që është i lidhur me portretizimin e një sipërfaqeje të vazhdueshme dhe jo me elementet individuale që përbëjnë këtë sipërfaqe. Në këtë kuptim, tema “Mbulesa e tokës” duhet të kuptohet si një abstraksion (jo konkret ndoshta) i sipërfaqes së tokës.
Koncepti i mbulesës së tokës ndryshon nga ai i përdorimit të tokës, ku mbulesa e tokës tregon llojet fizike të tokës ndërsa përdorimi i tokës paraqet se si njerëzit po e përdorin sipërfaqen e tokës. Të dhënat e dokumentuara të mbulesës së tokës tregojnë se sa një rajon mbulohet nga pyjet, ligatinat, sipërfaqet e papërpunuara, bujqësia dhe llojet e tjera të tokës dhe ujit. Përdorimi i tokës tregon se si njerëzit përdorin peizazhin qoftë për zhvillim, për ruajtje ose për përdorim të përzier. Llojet e ndryshme të mbulimit të tokës mund të menaxhohen ose përdoren krejtësisht ndryshe.
Sidoqoftë, temat “Mbulesa e tokës” dhe “Përdorimi i tokës” janë të ndërlidhura me njëra-tjetrën dhe shpesh të kombinuara në aplikimet praktike. Të dhënat që kombinojnë përdorimin e tokës dhe informacionin e mbulesës së tokës shpesh theksojnë aspektet e përdorimit të tokës në zonat e përdorura intensivisht (p.sh., zonat e ndërtuara ose industriale, tokat artificiale) dhe aspektet e mbulesës së tokës në zonat e përdorura gjerësisht (p.sh., vegjetacioni natyror, zonat pyjore).
Zhvillimi i specifikimit teknik i të dhënave është mbështetur dhe bazuar sipas specifikimeve të mëposhtme:
- Informacion për mbulesën e tokës që përdoret në monitorimin dhe që lidhet me politikën bujqësore të BE-së (IACS).
- Informacion për mbulesën e tokës që përdoret në monitorimin e karbonit (LULUCF).
- Informacion për mbulesën e tokës, në lidhje me tokën dhe ekosistemin, bazuar këto në mbulesën e tokës CORINE (LEAC),
Ky specifikim i të dhënave për temën “Mbulesa e tokës”, në kuadrin e direktivës INSPIRE është i ndarë në dy modele bazë dhe një model shtesë.
Dy modelet kryesore në koncept janë të ngjashëm, por për arsye teknike janë ndarë në një model bazë për të dhënat vektoriale dhe një model (disi më i thjeshtëzuar) bazë për të dhënat raster. Këto modele janë propozuar si pjesë e rregullave zbatuese të INSPIRE. Koordinimi i Informacionit për Mjedisin e Mbulesës së tokës (CORINE), si dhe shumica e grupeve të të dhënave për mbulesën e tokës rajonale dhe kombëtare, mund të përfaqësohen duke përdorur një nga modelet kryesore.
Të dhënat e temës “Mbulesa e tokës”, që përfshijnë klasifikime të shumëfishta ose parametra të mbulimit të tokës, përveç klasifikimeve tradicionale mund të përfaqësohen, duke përdorur modelin e zgjeruar shtesë. Dy modelet kryesore janë pjesë e modelit shtesë, pra përdoruesit që implementojnë modelin shtesë janë në përputhje me rregullat e direktivës INSPIRE.
Modeli i përbashkët, thelbësor konceptual për të dhënat e temës “Mbulesa e tokës” ka strukturën e mëposhtme:
- Një grup i të dhënave për mbulesën e tokës përbëhet nga një koleksion i njësive të mbulesës së tokës. Këto njësi mund të jenë pikat, poligonet ose qelizat raster (duke rezultuar në dy modele bazë, një për të dhënat vektoriale dhe një për të dhënat raster).
- Skedari i mbulesës së tokës lidhet, gjithashtu, me një kodlistë (p.sh., kodlistat e mbulesës së tokës CORINE). Kodlista është një nomenklature e klasave të mbulesës së tokës ku çdo klasë përfaqësohet nga një kod dhe një emër. Në çdo njësi të saj, mbulesa e tokës është vrojtuar në një ose më shumë data vëzhgimi. Shumëllojshmëria e datave të vrojtimit është e dhënë në mënyrë që të jetë në gjendje të përshkruajë ndryshimin e mbulesës së tokës. Për secilën datë të vrojtimit të bashkangjitur në njësinë e mbulesës së tokës, vëzhgimi përfaqësohet nga një ose më shumë kode, të marra nga kodlistat (që përfaqësojnë klasa të mbulesës së tokës). Gjithashtu është e mundur të shtoni një përqindje që tregon praninë relative të secilës klasë brenda njësisë së mbulesës së tokës.
- Versioni raster (Coverage) i modelit kryesor është thjesht një nënkategori ku hiqet data e vrojtimit, përqindja e mbuluar dhe për çdo njësi të mbulesës së tokës (qeliza raster) lejohet vetëm një kod për mbulesën e tokës.
Mbulesa e tokës është konceptualisht një ndarje e sipërfaqes së tokës. Modeli gjeometrik i duhur i një ndarjeje është një mbulim (Coverage). Megjithatë, përvoja ka treguar se shumë përdorues të dhënash në Evropë nuk janë në gjendje t’i trajtojnë mbulimet. Prandaj specifikimi i të dhënave, mbulon modelin e tokës, duke përdorur poligone të thjeshta të funksioneve dhe koleksioneve të pikave përveç rasterit. Poligonet, pikat dhe të dhënat raster korrespondojnë me metodat e zakonshme të vrojtimit të përdorura në hartimin dhe monitorimin e mbulesave, të vendeve evropiane, si p.sh., programi EEA CORINE Cover.
Specifikimi i të dhënave përshkruan dhe rekomandon një nomenklaturë (klasifikim) të veçantë të temës “Mbulesa e tokës”. Ekzistojnë, gjithashtu, edhe shumë mënyra të ndryshme për të përshkruar mbulesën e tokës të cilat specifikohen nga autoritetet përgjegjëse për prodhimin e të dhënave. Kjo, për shkak të spektrit të gjerë të aspekteve të mjedisit të përfshira nga tema “Mbulesa e tokës”, por edhe për shkak të përdorimeve të ndryshme të të dhënave të mbulesës së tokës.
Kjo mënyrë e specifikimit të të dhënave lejon shumë nomenklatura të ndryshme të mbulesës së tokës të bashkëjetojnë në kontekstin e INSPIRE. Zotëruesit e kodlistave të ndryshme, dokumentojnë këto lista duke përdorur ISO 19144-2 Standard - Land Cover Meta Language (LCML) ose duke përdorur një katalog të tipareve dhe sigurojnë kështu një bazë për ndërveprim në katalogun e veçorive. Ky proces ndodh përmes një linku në web. Ky lloj dokumentacioni krijon një lidhje ndemjet përkthimit semantik dhe nomenklaturës, duke bërë që të dhënat të jenë të krahasueshme në aspektin e shkallës dhe detajeve.
Figura 3. Modeli thelbësor konceptual i temës “Mbulesa e tokës” (përfaqësimi joformal)
3.1.2 TERMA DHE PËRKUFIZIME
- “Ekosistemi” është një kompleks dinamik komunitetesh: bimë, kafshë, mikrobe dhe mjedisi jo i gjallë, që ndërveprojnë si një njësi funksionale.
- “Legjenda”, aplikimi i një klasifikimi në një zonë të caktuar kryhet duke përdorur një shkallë hartografimi të përcaktuar, si dhe të dhëna të përcaktuara [UNFAO LCCS 2: 2005]. Një legjendë është aplikimi i një klasifikimi në një zonë të caktuar, duke përdorur një shkallë hartografimi të përcaktuar dhe një grup të dhënash të caktuara. Gjithsesi, një legjendë mund të përmbajë vetëm një pjesë ose nënkategori nga të gjitha klasat e mundshme të klasifikimit. Legjenda do të varet nga shkalla dhe burimi i të dhënave.
- “Mbulimi diskret”, mbulimi kthen vlerat e atributeve të njëjta për çdo pozicion të drejtpërdrejtë brenda çdo objekti gjeohapësinor të vetëm, i cili mund të jetë objekti i përkohshëm ose objekti gjeohapësinor në domenin (domein) e tij, kjo në përputhje me SSH EN ISO 19123:2007. Shënim. Domeni (domein) i një mbulimi diskret përbëhet nga një grup i caktuar objektesh gjeohapësinore ose të përkohshme.
- “Mozaiku”, grupi i klasave të mbulesës së tokës që përcakton të njëjtën copë toke në të njëjtën kohë.
- “Nomenklatura”, një kodlistë, emrash dhe përkufizimesh përkatëse për të gjitha klasat e vlefshme që rezultojnë nga një sistem klasifikimi.
- “Njësia minimale e hartografimit”, madhësia më e vogël e zonës së një poligoni që i lejohet të përfaqësohet nga një grup i caktuar të dhënash për mbulesën e tokës.
- “Objekti i mbulesës së tokës”, objekti gjeohapësinor (pikë, piksel ose poligon), ku është kryer vëzhgimi i mbulesës së tokës.
- “Pyll” është sipërfaqja e tokës më e madhe se 0.5 ha, e mbuluar me drurë më të lartë se 5 metra dhe me shkallë mbulimi mbi 10 për qind ose me drurë të aftë për të arritur këto pragje.
- “Sistemi i klasifikimit”, sistem për ndarjen e objekteve në klasa, në përputhje me ISO 19144-1:2012. Klasifikimi është një përfaqësim abstrakt i fenomeneve të realitetit (d.m.th., gjendja në fushë), duke përdorur klasifikuesit. Një klasifikim është një kornizë sistematike që përbëhet nga emrat e klasave, përkufizimet për secilën dhe lidhjen mes klasave. Klasifikimi përfshin domosdoshmërisht përcaktimin e kufijve të klasës, të cilat duhet të jenë të qarta dhe të bazuara në kritere objektive.
- “Situata”, gjendja e një objekti të veçantë të mbulesës së tokës në një pikë të caktuar në kohë. Shënim. Çdo poligon i veçantë mund të mbështesë më shumë se një klasë klasifikimi, ku secila korrespondon me një vrojtim specifik në një pikë të caktuar në kohë.
- “Simulimi”, ndarja e një hapësire në një grup nënhapësirash, që lidhen dhe kanë dimension të njëjtë me hapësirën që ndahet [SSH EN ISO 19123:2007]. Shënim. Një shtrirje në një hapësirë 2D përbëhet nga një sërë poligonesh që nuk mbivendosen, por që mbulojnë tërësisht një rajon të përcaktuar.
- “Toka” është shtresa e sipërme e kores së tokës, që përfshin lëndën minerale, lëndën organike, pjesën e lëngshme, pjesën e gaztë, pjesën biotike dhe që përmbush funksionet e përcaktuara, si: funksionet natyrore, funksionet si arkiv i historisë së natyrës në të kaluarën dhe funksione të tjera në dobi të njeriut.
3.1.3 SKEMAT E APLIKIMIT DHE DIAGRAMI UML PËR TEMËN “MBULESA E TOKËS”
Në vend të gjuhës UML, për të pasur më të qartë konceptin e të dhënave të temës “Mbulesa e tokës”, përdorim disa ilustrime të thjeshta dhe diagrame. Këto ilustrime janë të shoqëruara me shpjegime. Kjo kryhet me qëllim që informacioni të jetë i kuptueshëm, pasi diagramet UML kanë vështirësi në interpretim.
Të dhënat e mbulesës së tokës sigurojnë një përshkrim rreth sipërfaqes së tokës me karakteristikat biofizike. Në botën reale, kjo sipërfaqe është e populluar me elemente fizike të peizazhit (p.sh., ndërtesat, rrugët, pemët, bimët etj.). Shumë nga këto elemente janë tipare gjeohapësinore, të trajtuara dhe në tema të tjera të INSPIRE. Kombinimi i tërësisë së karakteristikave të elementeve fizike të peizazhit formojnë mbulesën e tokës. Koncepti i mbulesës së tokës është abstrakt, por do të perceptohet si një sipërfaqe dhe jo si një koleksion tiparesh. Hartografimi dhe përshkrimi i mbulesës së tokës, ndryshon nga hartografimi i elementeve të peizazhit.
Pika fillestare konceptuale e modelit të të dhënave të mbulesës së tokës është bota reale dhe sipërfaqja biofizike e tokës. Vëzhgimi, hartografimi dhe monitorimi i kësaj sipërfaqeje organizohet përmes iniciativës së vëzhgimeve të mbulesës së tokës. Një studim i mbulesës së tokës është një aktivitet, zakonisht një program afatgjatë, i kryer nga një organizatë e mandatuar. Shembuj të sondazheve të mbulesës së tokës janë programi i Koordinimit të informacionit për mjedisin e mbulesës së tokës (CLC) i zbatuar nga Agjencia Evropiane e Mjedisit (EEA) dhe sondazhi i kornizës së zonës LUCAS të zbatuar nga Eurostat. Shumëllojshmëria e sondazheve tregon se mbulesa e tokës mund të përshkruhet, klasifikohet dhe hartografohet në disa mënyra të ndryshme, në bazë të kërkesës së përdoruesve.
Figura 4. Hartografimi dhe mbikëqyrja e mbulesës së tokës bëhet përmes iniciativave të vrojtimit të saj. Kjo është e ndryshme nga hartografimi i elementeve të peizazhit
Iniciativat e sondazhit (vëzhgimeve) për mbulesën e tokës sigurojnë një lidhje midis aspekteve të tjera të modelit: Bota reale, përdoruesit, dokumentacioni dhe të dhënat. “Përdoruesit” janë institucionet, agjencitë, organizatat ose njerëzit që kërkojnë informacion në lidhje me mbulesën e tokës, duke justifikuar përpjekjet për të kryer një vëzhgim për mbulesën e tokës.
Figura 5. Një iniciativë për sondazhin (vëzhgimin) e mbulesës së tokës është korniza për hartimin e hartave të tokës, që lidh aktivitetin me përdoruesit, dokumentacionin dhe të dhënat aktuale që prodhohen
- Strategjitë e hartografimit
Klasifikimi është strategjia më e zakonshme dhe më e përdorur e hartografimit. Sipërfaqja e tokës është e ndarë në një grup të njësive të mbulesës së tokës, në mënyrë uniforme në aspektin e mbulesës së tokës, ku një klasë e mbulesës së tokës caktohet në secilën njësi.
Një strategji alternative janë “atributet”. Njësia e mbulesës së tokës në këtë rast përshkruhet nga atribute të ndryshme, që sigurojnë informacionin përkatës për gjendjen e mbulesës së tokës. Shembujt janë numri i ndërtesave ose gjatësia e rrugëve të shtruara.
Strategjia e tretë është përcaktimi i parametrave “parametrizimi”. Kjo strategji thekson një aspekt të veçantë të mbulesës së tokës, duke e përshkruar këtë aspekt si një parametër. Njësitë e mbulesës së tokës zakonisht janë parametrat apo qeliza raster, por jo domosdoshmërisht. Kjo strategji është përdorur për shtresat me rezolucion të lartë GMES.
Zhvillimi aktual në hartografimin dhe monitorimin e mbulesës së tokës është një lëvizje drejt integrimit të këtyre tri strategjive. Njësitë e mbulesës së tokës të krijuara sipas klasifikimit zotërojnë informacione shtesë të nxjerra nga burimet e të dhënave dytësore, të cilat mund të krijohen si rezultat i qasjes parametrike. Shtresat me rezolucion të lartë GMES janë shembuj të burimeve të të dhënave parametrike të përdorura për të populluar (sipas atributeve) njësitë e grupeve të të dhënave të mbulesës së tokës.
- Dokumentacioni i mbulesës së tokës dhe kodlistat
Dokumentacioni është tërësia e dokumenteve teknike që përshkruajnë metodat e grumbullimit të të dhënave, përkufizimet, rregullat për matjen dhe klasifikimin, si dhe çështje të tjera të lidhura që shpjegojnë përmbajtjen e studimit të mbulesës së tokës. Një shembull është dokumentacioni teknik i Koordinimit të informacionit për mjedisin e mbulesës së tokës (CORINE Land Cover). Dokumentacionet zakonisht paraqiten si dokumente tekstesh, që përmbajnë informacione të domosdoshme, të kërkuara për përdorimin e duhur të të dhënave.
Një pjesë veçanërisht e rëndësishme e dokumentacionit është një listë kodesh e Nomenklaturës së mbulesës së tokës. Kjo listë kodesh përfshihet në modelin bazë dhe për këtë arsye është i detyrueshëm në INSPIRE. Lista e kodeve mund të ketë çdo lloj formati që përdoruesit i duket e përshtatshëm. Funksioni primar që ka një kodlistë është të kontrollojë që një kod i gjetur në grupin e të dhënave të mbulimit të tokës është i vlefshëm dhe të përdori listën e kodeve si një tabelë ku gjendet legjenda tekstuale lidhur me këtë kod. Rekomandohen listat e kodeve shumëgjuhëshe për të mbështetur ripërdorimin e të dhënave në të gjithë Evropën.
Figura 6. Dokumentacioni i një iniciative të vrojtimit të mbulesës së tokës përbëhet nga përkufizimet (ndoshta duke përfshirë një sistem klasifikimi), udhëzimet e anketimit dhe një nomenklaturë. Nomenklatura duhet të shprehet si një kodlistë dhe të vihet në dispozicion në INSPIRE
Figura 7. Diagrami UML: Struktura e temës “Mbulesa e tokës”
3.2 PËRSHKRIMI I NËNTEMËS “NOMENKLATURA E MBULESËS SË TOKËS”
3.2.1 PARATHËNIE
Nomenklatura e mbulesës së tokës është një komponent i përbashkët i dy skemave të tjera të aplikimit: Mbulesa e tokës vektor dhe raster.
Kjo nomenklaturë shërben, për një ndarje dhe një kategorizim sipas tipologjisë kryesore mbulesë-përdorim, duke mundësuar kështu një vlerësim shumëdimensional, për karakteristikat natyrore të mbulesës dhe mënyrën e menaxhimit të saj në një hapësirë të caktuar. Këto karakteristika të ndryshme shfaqen në shumëllojshmërinë e tyre, sipas shtrirjes në rajonet gjeografike natyrore dhe karakteristika të tjera specifike të menaxhimit, sipas vendeve të ndryshme. Të gjitha këto janë përmbledhur në një klasifikim të unifikuar i cili shprehet në nomenklaturën specifike të CORINE LC. Asnjë prej elementeve të territorit nuk mbetet pa u përshkruar, gjithashtu, shkalla e përgjithësimit të çdo klase bën një përmbledhje të saktë të karakteristikave të ndryshme, duke formuar klasa uniforme të mundshme për t’u aplikuar në nivel vendi dhe për t’u mozaikuar në nivel evropian. Nomenklatura jep një përshkrim të çdo klase dhe elementeve të territorit që përfshihen në secilën prej këtyre klasave.
Megjithatë nomenklatura mund të pësojë modifikime në përcaktimin e disa klasave, si rezultat i futjes së formave të reja të menaxhimit të territorit, dhe zhvillimit metodologjik, të cilat nuk kanë qenë parashikuar që nga koha e krijimit të CORINE. Të tilla mund të jenë në të ardhmen, klasifikimi dhe emërtimi i impianteve të energjisë së rinovueshme etj.
3.2.2 SKEMA E APLIKIMIT DHE DIAGRAMI UML PËR NËNTEMËN “NOMENKLATURA E MBULESËS SË TOKËS”
NomeklaturaEMbulesësSëTokës specifikon informacionet e siguruara me qëllim kuptimin e saktë dhe interpretimin e kodeve të klasifikimeve që përmban grupi i të dhënave. Në vetvete kjo bazë të dhënash (dataType) përbëhet nga:
- KodlistaENomenklaturës - ky atribut i referohet një kodliste që i bashkëngjitet nomenklaturës. Kjo kodlistë në lidhjen ndërmjet kodlistave dhe vlerave të tyre.
- PalaPërgjegjëse - ky atribut specifikon cili është autoriteti përgjegjës për nomenklaturën. Gjithashtu lejon të paraqitet kontakti dhe/ose emërtimi i autoritetit.
- PërshkrimIBrendshëm - ky atribut përshkruan sistemin e klasifikimit referuar ISO 19144 (LCML metalanguage).
- PërshkrimiJashtëm - ky atribut lejon të sigurohet një link URL, me qëllim evidentimin e dokumentacionit që përshkruan sistemin e klasifikimit që përdoret për nomenklaturën.
Figura 8. NomenklaturaEMbulesësSëTokës
Kodlista VleratEKlasaveTëMbulesës së tokës është një kodlistë bosh, e cila lejon prodhuesin e të dhënave të përcaktojë kodlistat, sipas klasifikimit që ai autoritet përgjegjës përdor. Një rast i kësaj kodliste është dhe kodlista VleratCorine.
Figura 9. VlerateKlasavetëMbulesëssëTokës - VleratCorine
3.2.3 KATALOGU I TIPOLOGJISË
3.2.3.1 NOMENKLATURA E MBULESËS SË TOKËS
-- Emri--
Nomenklatura e mbulesës së tokës
--Përkufizimi--
NomenklaturaEMbulesësSëTokës jep informacion mbi referencën kombëtare, institucionale ose lokale.
--Përshkrimi--
NomeklaturaEMbulesësSëTokës lejon të referohet dokumentacioni i nomenklaturave dhe kodlistave shoqëruese, si dhe të përcaktojë ato nëpërmjet një referimi të jashtëm ose të përfshihet në të dhënat sipas ISO 19144-2.
-- Tipi i elementit --
DataType
ATRIBUTET
InspireId: Identifikues
Shumëllojshmëria: [1]
--Emri--
Inspire ID
--Përkufizimi--
Identifikuesi i objektit të jashtëm për një objekt gjeohapësinor.
--Përshkrimi--
Shënim. Një identifikues i objektit të jashtëm është një identifikues unik i objektit, i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
KodlistaENomeklaturës: URI
Shumëllojshmëria: [1]
--Emri--
Kodlista e nomenklaturës
--Përkufizimi--
Një URI http që tregon kodlistën bashkëlidhur nomenklaturës së përdorur.
[I detyrueshëm: PO]
PalaPërgjegjëse: AutoritetiPërgjegjës
Shumëllojshmëria: [1]
--Emri--
Pala përgjegjëse
--Përkufizimi--
Pala përgjegjëse për zhvillimin dhe/ose mirëmbajtjen e nomenklaturës.
--Përshkrimi--
Pala përgjegjëse mund të jetë një agjenci hartash kombëtare ose lokale.
[I detyrueshëm: PO]
PërshkrimiIBrendshëm: SistemiIKlasifikimitTëMbulesësSëTokës
Shumëllojshmëria: [0..1]
--Emri--
Përshkrimi i brendshëm
--Përkufizimi--
Një kodim i brendshëm i sistemit të klasifikimit sipas ISO 19144-2.
[I detyrueshëm: PO]
PërshkrimiIJashtëm - CitimiIDokumentit
Shumëllojshmëria: [0..*]
--Emri--
Përshkrimi i jashtëm
--Përkufizimi--
Dokument që përshkruan nomenklaturën e përdorur në këtë grup të dhënash.
[I detyrueshëm: JO]
LIDHJE
Lidhje (Drejtimi: Burimi ->Objektivi)
-- Emri --
Lidhje e nomenklaturës së mbulesës së tokës
-- Përkufizimi --
Lidhja ndërmjet vrojtimit të mbulesës së tokës me një nomenklaturë specifike.
-- Përshkrimi --
Nomenklatura e mbulesës së tokës lejon t’i referohet dokumentacionit të nomenklaturës dhe kodlistave të lidhura dhe t’i përcaktojë ato përmes referencës në internet ose të përfshihet në të dhënat sipas ISO 19144-2. Nomenklatura duhet vetëm të referohet.
Burimi: Vrojtim (Class) VrojtimiIMbulesësSëTokës “dataType”
Shumëllojshmëria: [1..*]
-- Emri --
Vrojtim
-- Përkufizimi --
Një vëzhgim/vrojtim i cili lidhet me një nomenklaturë të veçantë.
Objektivi: Nomenklatura E Mbulesës Së Tokës
Class) NomeklaturaEMbulesësSëTokës “dataType” Shumëllojshmëria: [1]
-- Emri --
Nomenklatura e mbulesës së tokës
-- Përkufizimi --
Nomenklatura e mbulesës së tokës e referuar nga një vëzhgim i zgjatur.
3.2.3.2 VLERAT CORINE
-- Emri--
Vlerat CORINE
-- Përkufizimi--
Kodlista CORINE e mbulesës së tokës menaxhuar nga EEA. Referohu aneksit B.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga “codeList” VleraCorine te “codeList” VleratEKlasaveTëMbulesësSëTokës
3.2.3.3 VLERAT E KLASËS SË MBULESËS SË TOKËS
-- Emri--
Vlerat e klasave të mbulesës së tokës
-- Përkufizimi--
Kodlista ose klasifikimi i mbulesës së tokës.
-- Përshkrimi--
Një kodlistë boshe që vepron si një mbajtës për kodlistën CORINE, një tjetër kodlistë evropiane, kombëtare ose lokale për nomeklaturën e mbulesës së tokës.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga “codeList” VleraCorine te “codeList” VleratEKlasësSëMbulesësSëTokës
3.3 PËRSHKRIMI I NËNTEMËS “TË DHËNAT VEKTOR TË MBULESËS SË TOKËS”
3.3.1 PARATHËNIE
Kjo skemë e aplikimit përcakton se si të dhënat e mbulesës së tokës mund të mbështeten nga një përfaqësim vektori. Prandaj, të gjitha kërkesat e këtij seksioni zbatohen në rastin e të dhënave të mbulesës së tokë sduke u mbështetur në pika ose poligone.
Tipologjia Grupi i tëDhënaveTëMbulesësSëTokës
Skema e aplikimit te Të dhënat vektor të mbulesës së tokës modelon grupet e të dhënave të mbulesës së tokës si koleksione të Njësisë së mbulesës së tokës. Një njësi e mbulesës së tokës ka një gjeometri (e kufizuar në pikë ose sipërfaqe) dhe mbështet informacionin e mbulesës së tokës nëpërmjet atributit të vrojtimit të mbulesës së tokës.
Shënim. Termi “sipërfaqe” përdoret në vend të “poligonit” për konformitet me standardin SSH EN ISO 19107:2005. Një poligon gjeometrik nuk mund të ekzistojë më vete dhe do të jetë pjesë e një sipërfaqeje gjeometrike. Objekti i përgjithshëm 2D gjeometrik për një sipërfaqe 2D (sipërfaqe gjeometrike), sipas ISO Standard.
Atributi gjeometrik i një njësie të mbulesës së tokës është një objekt gjeometrik, i cili është i tipit SSH EN ISO 19107:2005. Ky atribut është i kufizuar me pikën gjeometrike (GM_Pikë) ose në sipërfaqen gjeometrike (GM_Sipërfaqe), varet sipas kërkesës. Përveç kësaj, në këtë bërthamë është e lejuar vetëm një nomenklaturë (nomeklatura e dokumentacionit) për çdo grup të dhënash.
Tipologjia NjësiaEMbulesësSëTokës
Njësia e mbulesës së tokës përfaqëson një pjesë të hapësirës që klasifikohet. Mund të korrespondojë, për shembull, me një poligon CORINE.
Çdo njësi e mbulesës së tokës përcaktohet nga:
- Gjeometria e cila është e kufizuar me pika (për shembull, pikat e mostrës së LUCAS) ose sipërfaqet (për shembull një poligon i CORINE LC), përmes kufizimit të OCL.
- Një ose disa vrojtime të mbulesës së tokës që lejojnë përshkrimin e njësisë nga pikëpamja e mbulesës së tokës.
Tipologjia VrojtimiiMbulesësSëTokës
Vrojtimi i mbulesës së tokës përshkruhet nga vetë Klasa e vrojtimit të mbulesës së tokës:
Klasa e vrojtimit të mbulesës së tokës përcakton atributet e mëposhtme:
- Atributi Klasa lejon një kod klasifikimi që rezulton nga një proces klasifikimi. Ajo mund të jetë kodi CORINE (111, 112, 223, ...), kodi IGBP ose ndonjë kod tjetër që korrespondon me një sistem kombëtar ose një nomenklaturë institucionale. Vlerat përcaktohen në listën e kodeve të përcaktuara nga Klasa e vlerës së mbulesës së tokës.
- Data e vrojtimit siguron informacion të përkohshëm, në lidhje me kohën kur janë përfituar të dhënat.
- Mozaiku lejon përshkrimin më të saktë të mbulesës së tokës përmes një koleksioni të klasifikimit të vlerave, ku secila është e lidhur me një përqindje (secila duke u shprehur me numra të plotë midis 0 dhe 100). Shuma e të gjitha këtyre përqindjeve do të jetë më e ulët se 100.
- Data e vrojtimit dhe mozaiku janë të vlefshme si vlera voidable, d.m.th. këto vlera mund të plotësohen në rast se ekzistojnë.
Të gjitha informatat për mbulesën e tokës (klasa dhe mozaiku) janë përcaktuar sipas nomenklaturës së përshkruar dhe referuar nga atributet e DokumentacionitTëNomenklaturës siguruar ky në nivel të caktuar të të dhënave.
Llojet e ndryshme të të dhënave
Një aspekt i rëndësishëm i informacionit për mbulesën e tokës është ndryshimi i cilësisë së informacionit me kalimin e kohës. Megjithatë kjo i referohet një situate të veçantë. Aspekti i dytë dhe i veçantë për mbulesën e tokës është se brenda një viti, pamja mund të ndryshojë, kjo varet nga subjekti sezonal. Kjo varësi mund të ndikojë në interpretimin e saktë tematik dhe klasifikimin e klasave të veçanta në një grup të caktuar të të dhënave.
Duke pasur parasysh dy çështjet e sipërpërmendura ekzistojnë disa lloje të të dhënave që duhet të merren parasysh në përshkrimin e peizazhit nga pikëpamja e mbulimit të tokës. Disa nga këto lloje të dhënash janë të rëndësishme, kur bëhet fjalë për krahasimin e dy ose më shumë situatave të ndryshme të mbulimit të tokës. Në bazë të llojeve të ndryshme të të dhënave në dispozicion, përdoruesi i të dhënave është në gjendje të nxjerrë dhe të vlerësojë informacionin e ndryshimit të mbulimit të tokës nga imazhet ose burimet e tjera të të dhënave. Më poshtë paraqitet një listë e llojeve të të dhënave përgjatë procesit të kapjes dhe dorëzimit të të dhënave të mbulimit të tokës.
- Data e ngjarjes
Pika e kohës ose periudha e shkurtër, kur një lloj i caktuar mbulesash tokësore ndodh në realitet, shihet si data e ngjarjes (p.sh., dëmtimi nga stuhitë ose prerja e qartë në zonat pyjore, fillimi i një vendi ndërtimi, përfundimi i një vendi ndërtimi). Data e ngjarjes do të ishte informacioni më i saktë në momentin kur një ndryshim i caktuar i mbulimit të tokës do të shfaqet në realitet. Monitorimi i mbulimit të tokës ka qëllim të përdorë disa afate kohore të ndryshme. Në shumicën e rasteve, informacioni i datës së ngjarjeve për objektet e mbulimit të tokës nuk është. Ruajtja e datës së ngjarjes për çdo rast të veçantë, mund të duket si e pamundur dhe prandaj konsiderohet si jo e detyrueshme, por voidable.
Nëse kërkohet, data e ngjarjes mund të modelohet si atribut voidable:
- EVlefshmeNga: Pika e kohës kur fenomeni filloi të ekzistonte në botën reale.
- EVlefshmeDeri: Pika e kohës që kur fenomeni nuk ekziston më në botën reale.
- Data e vrojtimit
Data e vrojtimit konsiderohet si pikë e kohës ose e situatës, kur burimi i informacionit mbi burimin e tokës, i cili përdoret për kapjen e të dhënave të mbulimit të tokës regjistrohet. Zakonisht data e vrojtimit është data e blerjes së imazhit ajror ose satelitor (të dhënat nga remote sensing) të përdorur për hartografimin e një njësie të veçantë hapësinore (poligoni). Për shkak se për secilin sondazh përdoren shumë imazhe, të dhënat aktuale mund të ndryshojnë nga një poligon në tjetrin brenda të njëjtit grup të dhënash. Data e blerjes së imazheve të regjistruara do të lidhet me çdo njësi gjeohapësinore të vetme (pikë/poligoni). Data e vrojtimit mund të jetë, gjithashtu, pikë e kohës, kur informacioni i mbulimit të tokës kapet në terren nga një inspektor i terrenit. Objekti i mbulesës të tokës në një grup të caktuar të të dhënave mund të ketë të dhëna të ndryshme të vrojtimit, nëse disa burime informacioni janë kombinuar për të kapur informacionin e mbulesës së tokës. Data e vrojtimit zakonisht ndryshon nga data e ngjarjes.
- Data e referencës
Një vit referencë ose datë referimi është momenti (pak a shumë i saktë) i një periudhe kohe ose një hapësire kohore kur informacioni, në një grup të dhënash të plotë, supozohet të jetë i vlefshëm. Afati kohor për blerjen e një numri pamjesh satelitore ose imazheve ajrore brenda një periudhe reference varion nga disa ditë, muaj apo dhe vite.
Ndryshimet e mbulesës së tokës
Modeli aktual shpreh mbulimet, të cilat në vetvete përmbajnë disa njësi gjeohapësinore. Me kalimin e kohës, këto njësi gjeohapësinore mund të ndryshojnë gjeometrinë e tyre në krahasim me njëri-tjetrin nga të dhënat e përcaktuara ose mund të fiksohen dhe mbajnë zgjerimin e tyre gjeometrik (rrjetin e rregullt) dhe vetëm të ndryshojnë informacionet e tyre tematike të mbulesës së tokës. Për të paraqitur ndryshimet e mbulesës së tokës ka dy mënyra.
- Mënyra analitike: Përdoruesi bën një shtresë diferenciale ndërmjet dy datave të mbulimeve të ndryshme, ai krijon ndryshimin e mbulesës së tokës si rezultat i kësaj mbulese.
- Mënyra historike: Për secilën njësi gjeohapësinore fikse, informacioni i mbulesës së tokës merret sipas një ose më shumë datash të vrojtimit në kohë dhe i caktohet njësisë hapësinore. Pikat e LUCAS ose qelizat e rrjetit në përgjithësi janë shembuj të njësive gjeohapësinore fikse ku të dhënat e mbulesës së tokës mund të “vërehen” ose të “maten” në pika të ndryshme në të njëjtën kohë në të njëjtin vend.
Një rast i veçantë është një grup i të dhënave që përmban informacione që ndryshojnë, p.sh., baza e të dhënave të ndryshimit të tokës CORINE të ndryshuar 2000-2006. Pra nuk ka një vit referimi. Ajo mund të shihet si një mbulim me njësi hapësinore fikse dhe dy situata të veçanta (datat e vrojtimit), një që i referohet datës së parë dhe e dyta datës së mëvonshme të vrojtimit, e cila përfaqësohet në nivelin e poligonit.
3.3.2 SKEMA E APLIKIMIT DHE DIAGRAMI UML PËR NËNTEMËN “TË DHËNAT VEKTOR TË MBULESËS SË TOKËS”
Figura 10. Të dhënat vektoriale të temës “Mbulesa e tokës” - Lidhjet e jashtme
Figura 11. Të dhënat vektoriale të të temës “Mbulesa e tokës”, DataType-et dhe Kodlistat
3.3.3 Katalogu i tipologjisë
3.3.3.1 Grupi i të dhënave të mbulesës së tokës
--Emri--
Grupi i të dhënave të mbulesës së tokës
--Përkufizimi--
Një prezantim vektorial për të dhënat e mbulesës së tokës.
--Përshkrimi--
Ky prezantim lejon që të dhënat e mbulesës së tokës të mbështeten nga një gjeometri vektoriale.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË BRENDSHME
Agreguarnga “featureType” NjësiaEMbulesësSëTokëSë te “featureType” GrupiITëDhënaveTëMbulesësSëTokës
ATRIBUTE
DokumentacioniINomeklaturës: NomeklaturaEMbulesësSëTokës
Shumëllojshmëria: [1]
--Emri--
Dokumentacioni i nomeklaturës
--Përkufizimi--
Informacion rreth nomenklaturës së përdorur në këtë grup të dhënash.
[I detyrueshëm: PO]
Emërtimi: Text (CharacterString)
Shumëllojshmëria: [1]
--Emri--
Emërtimi
--Përkufizimi--
Emërtimi i grupit të të dhënave të mbulesës së tokës.
[I detyrueshëm: PO]
EVlefshmeDeri: Datë
Shumëllojshmëria: [1]
--Emri--
E vlefshme deri
--Përkufizimi--
Koha kur fenomeni mbaron së ekzistuari në realitet.
[I detyrueshëm: PO]
EVlefshmeNga: Datë
Shumëllojshmëria: [1]
--Emri--
E vlefshme nga
--Përkufizimi--
Koha kur fenomeni fillon të ekzistojë në realitet.
[I detyrueshëm: PO]
FillimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [1]
--Emri--
Fillimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
--Emri--
Inspire ID
--Përkufizimi--
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
--Përshkrimi--
Shënim. Një identifikues i objektit të jashtëm është një identifikues unik i objektit, i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
MbarimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
--Emri--
Përfundimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u largua, në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: JO]
Shtrirja: EX_Shtrirje
Shumëllojshmëria: [1]
--Emri--
Shtrirja
--Përkufizimi--
Përmban shtrirjen e grupit të të dhënave.
--Përshkrimi--
Shënim. Shtrirja mund të specifikohet në hapësirë, kohë ose hapësirë-kohë.
[I detyrueshëm: PO]
3.3.3.2 VLERAT E MBULESËS SË TOKËS
-- Emri --
Vlerat e mbulesës së tokës
-- Përkufizimi --
Klasa e përgjithshme që mbështet vlerën dhe përqindjen e mbulesës së tokës.
-- Tipi i elementit --
DataType
ATRIBUTE
Klasa: VleratEKlasësSëMbulesësSëTokës
Shumëllojshmëria: [1]
-- Emri --
Klasa
-- Përkufizimi --
Caktimi i një objekti gjeohapësinor të mbuluar me tokë në një klasë të mbulimit të tokës nëpërmjet një identifikuesi të kodifikuar klasifikimi.
-- Përshkrimi --
Identifikuesi, p.sh., 1.1.1, 1.1.2 ... (për klasat e CORINE MT) lejon qasje në vlerën dhe përkufizimin ose përshkrimin narrativ të klasës korresponduese.
[I detyrueshëm: PO]
PërqindjaEMbuluar: Integer
Shumëllojshmëria: [1]
-- Emri --
Përqindja e mbuluar
-- Përkufizimi --
Pjesa e Njësisë të mbulesës së tokës e lidhur me vlerën e klasifikimit.
[I detyrueshëm: PO]
3.3.3.3 Vlerat e Kategorisë së mbulesës së tokës
-- Emri --
Vlerat e kategorisë të mbulesës së tokës
-- Përkufizimi --
Kategoritë e mbulesës së tokës, sipas klasifikimit aktual. Shiko aneksin B.
-- Tipi i elementit --
Kodlistë
3.3.3.4 Vrojtimi i mbulesës së tokës
--Emri--
Monitorimi i mbulesës së tokës
--Përkufizimi--
Informacioni i mbulesës së tokës i interpretuar në një kohë dhe vend të caktuar.
-- Tipi i elementit --
DataType
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuarnga “dataType” VrojtimiIMbulesësSëTokës te “dataType” MonitorimiIMbulesësSëTokës - VrojtimiIMbulesësSëTokës
ATRIBUTE
DataEMonitorimit: Datë-Orë
Shumëllojshmëria: [1]
--Emri--
Data e monitorimit
--Përkufizimi--
Data e monitorimit e lidhur me një monitorim.
--Përshkrimi--
Përcakton datën e vrojtimit të vlerës së klasifikimit. Mund të jetë data e një imazhi ajror/satelitor ose një përditësim zone. Data e vrojtimit i lejon përdoruesit të ketë të dhëna të sakta se kur çdo vlerë është vërejtur realisht. Në një bazë të dhënash, jo të gjitha informacionet e poligonit përditësohen domosdoshmërisht në të njëjtën kohë.
[I detyrueshëm: PO]
Klasa: VleratEKlasësSëMbulesësSëTokës
Shumëllojshmëria: [1]
--Emri--
Klasa
--Përkufizimi--
Caktimi i një klase të mbulesës së tokës, në njësinë e mbulesës së tokës nëpërmjet një identifikuesi të kodit të klasifikimit.
--Përshkrimi--
Identifikuesi, p.sh., 1.1.1, 1.1.2, ... (për klasat e CORINE MT) lejon qasje në vlerën dhe përkufizimin ose përshkrimin narrativ të klasës korresponduese.
[I detyrueshëm: PO]
Kategoria: VleratEKategorisëSëMbulesësSëTokës
Shumëllojshmëria: [1]
--Emri--
Kategoria
--Përkufizimi--
Vlera e kategorisë së mbulesës së tokës sipas klasifikimit aktual.
[I detyrueshëm: PO]
Mozaikimi: VleratEMbulesësSëTokës
Shumëllojshmëria: [1..*]
--Emri--
Mozaikimi
--Përkufizimi--
Lista e vlerave të klasifikimit që përshkruajnë në detaje njësinë e mbulesës së tokës, e lidhur me përqindjet.
[I detyrueshëm: PO]
3.3.3.5 Njësia e mbulesës së tokës
--Emri--
Njësia e mbulesës së tokës
--Përkufizimi--
Një element individual i grupit të të dhënave të mbulesës së tokës i përfaqësuar nga një pikë ose poligon.
--Përshkrimi--
Çdo njësi mbështet informacionin e mbulesës së tokës
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Agreguarnga “featureType” NjësiaEMbulesësSëTokës te “featureType” GrupiITëDhënaveTëMbulesësSëTokës
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuarnga “featureType” NjësiaEMbulesësSëTokës te “featureType” NjësiaEMbulesësSëTokës
ATRIBUTE
FillimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [1]
--Emri--
Fillimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
Gjeometria: GM_Object
Shumëllojshmëria: [1]
--Emri--
Gjeometria
--Përkufizimi--
Përfaqësimi gjeohapësinor i njësisë së mbulesës së tokës.
--Përshkrimi--
Shënim. Gjeometria e kufizuar: pikë ose sipërfaqe.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
--Emri--
Inspire ID
--Përkufizimi--
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
--Përshkrimi--
Shënim. Një identifikues i objektit të jashtëm është një identifikues unik i objektit, i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit realitet.
[I detyrueshëm: PO]
PërfundimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
--Emri--
Përfundimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u largua në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: JO]
MonitorimiIMbulesësSëTokës: MonitorimiIMbulesësSëTokës
--Emri--
Monitorimi i mbulesës së tokës
--Përkufizimi--
Informacioni i mbulesës së tokës në një kohë dhe vend të caktuar.
[I detyrueshëm: PO]
3.4 PËRSHKRIMI I NËNTEMËS “TË DHËNAT RASTER TË MBULESËS SË TOKËS”
3.4.1 PARATHËNIE
Kjo skemë e aplikimit përcakton se si të dhënat e temës “Mbulesa e tokës” mund të mbështeten nga një përfaqësim raster (coverage). Të gjitha kërkesat e këtij seksioni zbatohen, prandaj në rastin e të dhënave të mbulesës së tokës mbështeten në mbulimin e rrjetit të korrigjuar, siç përcaktohet nga standardi SSH EN ISO 19123:2007.
Tipologjia RrjetiIMbulimitTëMbulesësSëTokës
Skema e aplikimit Të dhënat taster të mbulesës së tokës paraqet të dhënat MT si një rrjet mbulimi i rektifikuar (sipas SSH EN ISO 19123:2007). Ky mbulim mbart thuajse të njëjtin set atributesh si GrupiITëDhënaveTëMbulesësSëTokës, por ka disa kufizime në krahasim me modelin e vektorit. Nuk përmban të gjitha informacionet semantike të ofruara nga informacioni i mbulimit të tokës në rastin e skemës së të dhënave vektor:
- Nuk ka asnjë datë vëzhgimi.
- Nuk ka mozaikim.
Informacioni i vetëm ekuivalent që gjendet në këtë përfaqësim raster është VleratEKasësSëMbulesësSëTokës. LlojiIGamës lejon lidhjen e një kodi të vetëm klasifikimi, që rezulton nga një proces klasifikimi, në çdo qelizë raster. Këto mund të jenë kodet CORINE, kodet IGBP ose kodet e tjera që korrespondojnë me një nomenklaturë kombëtare, institucionale ose vendore.
Këto kufizime lidhen me formatet e përdorura të rrjetit të mbulimit të rektifikuar (si Geotiff) që mbështesin vetëm një vlerë për piksel.
3.4.2 Skema e aplikimit dhe diagrami UML për nëntemën “Të dhënat raster të mbulesës së tokës”
Figura 12. Paketa e të dhënave raster për të temës mbulesa e tokës”
Figura 13. Të dhënat raster për temën “Mbulesa e tokës” - Lidhjet strukturore të jashtme dhe të brendshme
3.4.3 Katalogu i tipologjisë
3.4.3.1 Rrjeti i mbulimit të mbulesës së tokës
--Emri--
Rrjeti i mbulimit të mbulesës së tokës
--Përkufizimi--
Një imazh që prezanton të dhënat e mbulesës së tokës.
--Përshkrimi--
Ky prezantim lejon që të dhënat e mbulesës së tokës të mbështeten nga rrjeti i mbulimit i rektifikuar (SSH EN ISO 19123:2007).
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuarnga “featureType” RrjetiIMbulimitTëMbulesësSëTokëste “featureType” RrjetiKoordinativIRektifikuar (Transformuar)
ATRIBUTE
DokumentacioniINomeklaturës: NomeklaturaEMbulesësSëTokës
Shumëllojshmëria: [1]
--Emri--
Dokumentacioni i nomenklaturës
--Përkufizimi--
Informacion rreth nomenklaturës së përdorur në këtë mbulim.
[I detyrueshëm: PO]
Emërtimi: Text (CharacterString)
Shumëllojshmëria: [1]
--Emri--
Emërtimi
--Përkufizimi--
Emërtimi i rrjetit të mbulimit të mbulesës së tokës.
[I detyrueshëm: PO]
EVlefshmeDeri: Datë
Shumëllojshmëria: [1]
--Emri--
E vlefshme deri
--Përkufizimi--
Koha kur fenomeni mbaron së ekzistuari në realitet.
[I detyrueshëm: PO]
EVlefshmeNga: Datë
Shumëllojshmëria: [1]
--Emri--
E vlefshme nga
--Përkufizimi--
Koha kur fenomeni fillon të ekzistoj në realitet.
[I detyrueshëm: PO]
FillimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [1]
--Emri--
Fillimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
--Emri--
Inspire ID
--Përkufizimi--
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
--Përshkrimi--
Shënim. Një identifikues i objektit të jashtëm është një identifikues unik i objektit i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit të botës reale.
[I detyrueshëm: PO]
PërfundimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
--Emri--
Përfundimi i ciklit jetësor
--Përkufizimi--
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u largua në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: JO]
Shtrirja: EX_Shtrirje
Shumëllojshmëria: [1]
--Emri--
Shtrirja
--Përkufizimi--
Përmban shtirjen e grupit të të dhënave.
--Përshkrimi--
Shënim. Shtrirja mund të specifikohet në hapësirë, kohë ose hapësirë-kohë.
[I detyrueshëm: PO]
3.5 METADATA
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.6 Kodi EPSG për KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare, sipas vendimit nr. 669, datë 7.8.2013, të Këshillit të Ministrave “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë” ndryshuar me vendimin nr. 322, datë 27.4.2016 dhe vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është EPSG-6870.
3.7 CILËSIA E TË DHËNAVE
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së tyre, që duhen përdorur për të vlerësuar dhe për të dokumentuar cilësinë e të dhënave për grupet e të dhënave që lidhen me të dhënat gjeohapësinore të temës “Mbulesa e tokës”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret, për të:
- vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku karakteristikat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit;
- vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore;
- për të specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore, që lidhen me temën “Mbulesa e tokës”.
Rekomandim
Kur është e pamundur të shprehet vlerësimi i elementit të cilësisë së të dhënave në një mënyrë sasiore, vlerësimi i elementit duhet të shprehet me një deklaratë tekstuale si rezultat përshkrues i cilësisë së të dhënave.
Tabela - Elementet e cilësisë së të dhënave që janë përdorur për të dhënat gjeohapësinore në temën “Mbulesa e tokës”
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
7.1.1
Kompletimi
Komision
Të dhëna të tepërta të pranishme në grupin e të dhënave, siç përshkruhet nga fushëveprimi
Llojet e objekteve gjeohapësinore
7.1.2
Kompletimi
Përjashtimi
Të dhënat që mungojnë nga grupi i të dhënave, siç përshkruhet nga fushëveprimi
Llojet e objekteve gjeohapësinore
7.1.3
Përputhja ligjore
Përputhja konceptuale
Zbatimin i rregullave të skemës konceptuale
Llojet e objekteve gjeohapësinore, grupet e të dhënave
7.1.4
Përputhja ligjore
Përputhja në domeinin
Zbatimin e vlerave, në vlerat e domeinit
Objekt gjeohapësinor
7.1.5
Përputhja ligjore
Përputhja e formatit
Cilësia në të cilën ruhen të dhënat në përputhje me strukturën fizike të grupit të të dhënave, siç përshkruhet nga fushëveprimi
Llojet e objekteve gjeohapësinore, grupet e të dhënave
7.1.6
Përputhja ligjore
Përputhja topologjike
Korrektësia e topologjisë së koduar në mënyrë të qartë, karakteristikat e grupeve të të dhënave, siç përshkruhet nga fushëveprimi
Objekt gjeohapësinor
7.1.7
Saktësia pozicionale
Saktësa absolute ose e jashtme
Aftësia e vlerave të koordinatës së raportuar, për vlerat e pranuara si ose të qenit të vërteta
Objekt gjeohapësinor
7.1.8
Saktësia pozicionale
Saktësia relative ose e brendshme
Afërsia e karakteristikave relative të pozicionit, në kuadër të pozicioneve përkatëse relative që pranohen ose që janë të vërteta.
Objekt gjeohapësinor
7.1.9
Saktësia tematike
Korrektësia e klasifikimit
Krahasimi i klasave bazuar në karakteristikat ose atributet e një bashkësie ligjëratash
Objekt gjeohapësinor
7.1.10
Saktësia tematike
Korrektësia e atributeve josasiore
Korrektësia e atributeve josasiore
Objekt gjeohapësinor
7.1.11
Saktësia tematike
Korrektësia e atributeve sasiore
Saktësia e atributeve sasiore
Objekt gjeohapësinor
3.7.1 KOMPLETIMI - AUTORIZIMI (COMPLETNESS-COMMISSION)
Rekomandim
Autorizimi duhet të vlerësohet dhe dokumentohet, duke përdorur artikujt e tepërt siç specifikohet në tabelat e mëposhtme
Emri
Artikuj të tepërt
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletuar
Cilësia e të dhënave të nënelementeve
Komision
Cilësia e të dhënave të matjeve themelore
Treguesi i gabimit
Përkufizim
Tregon se një artikull është gabimisht i pranishëm në të dhënat
Përshkrimi
-
Fusha vlerësimit
Objekt gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha raportimit
TëDhënatEMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Boolean (e vërteta që tregon se artikulli është i tepërt)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Paraqitja e artikujve të tepërt në një grup të dhënash:
Dy ose më shumë pika të mbledhura njëra sipër tjetrës.
Dy ose më shumë sipërfaqe të mbledhura njëra sipër tjetrës.
Masa identifikuese
1
3.7.2 KOMPLETIMI - PËRJASHTIMI (COMPLETNESS-OMMISSION)
Rekomandim
Përjashtimi duhet të vlerësohet dhe të dokumentohet duke përdorur artikujt e tepërt të përcaktuara në tabelat e mëposhtme:
Emri
Mungon artikulli
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletuar
Cilësia e të dhënave të nënelementeve
Përjashtimi
Cilësia e të dhënave të matjeve themelore
Treguesi i gabimit
Përkufizimi
Tregon se si shfaqet një artikull i veçantë që mungon te të dhënat
Përshkrimi
-
Fusha e vlerësimit
Objekt gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Boolean (e vërteta që tregon se artikulli mungon)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembulli
Gjetja e artikullit që mungon:
-Mospërputhja e pakontrolluar në grupin e të dhënave.
Masa identifikuese
5
3.7.3 PËRPUTHJA LIGJORE - PËRPUTHJA KONCEPTUALE (LOGICAL CONSISTENCY - CONCEPTUAL CONSISTENCY)
Rekomandim
Përputhja konceptuale duhet të vlerësohet dhe të dokumentohet duke përdorur mospërputhjen e skemës konceptuale të përcaktuar në tabelën e mëposhtme:
Emri
Skema konceptuale e përcaktuar
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja konceptuale
Cilësia e të dhënave të matjeve themelore
Treguesi i gabimit
Përkufizim
Tregon se një artikull nuk është në përputhje me rregullat e skemës konceptuale
Përshkrimi
-
Fusha e vlerësimit
Objekt gjeohapësinor: NjësiaEMbulesësSëTokës
Llojet e objekteve gjeohapësinore: NjësiaEMbulesësSëTokës
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës, RrjetiIMbulimitTëMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës, RrjetiIMbulimitTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Boolean (e vërteta që tregon se një artikull nuk është në përputhje me rregullat e skemës konceptuale)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Paraqitja e artikujve në mbulesën që shkel përputhjen konceptuale:
- Mbulimi përmban vija/pika në vend të poligonit.
- Poligonet e mbivendosura gjenden në mbulesë, ndërsa koncepti nuk lejon mbivendosje.
- Në mbulesë janë të pranishëm poligone më të vogla se njësia e përcaktimit të hartave minimale të paracaktuara.
Masa identifikuese
8
3.7.4 PËRPUTHJA LIGJORE - PËRPUTHJA ME DOMEININ (LOGICAL CONSISTENCY - DOMAIN CONSISTENCY)
Rekomandim
Përputhja me domeinin duhet të vlerësohet dhe dokumentohet duke përdorur vlerën e moskonformitetit të domeineve të përcaktuar në tabelën e mëposhtme:
Emri
Vlera e moskonformitetit të domeinit
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja me domeinin
Cilësia e të dhënave të matjeve themelore
Treguesi i gabimit
Përkufizimi
Tregon se një artikull nuk është në përputhje me domeinin e vlerës së tij
Përshkrimi
-
Fusha e vlerësimit
Objekt gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës, RrjetiIMbulimitTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Boolean (e vërteta që tregon se një artikull nuk është në përputhje me vlerat e domeinit)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Paraqitja e artikujve në mbulesën që mbivendoset me domeinin:
- Mbulimi përmban pika/poligone me atribute jashtë atributeve të domeinit (p.sh., kodet e klasës joekzistuese)
Masa identifikuese
14
3.7.5 PËRPUTHJA LIGJORE - PËRPUTHJA E FORMATIT (LOGICAL CONSISTENCY - FORMAT CONSISTENCY)
Rekomandim
Përputhja formative duhet të vlerësohet dhe dokumentohet duke përdorur mospërputhjen e strukturës fizike të përcaktuar në tabelën e mëposhtme:
Emri
Struktura fizike e përcaktuar
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja formative
Cilësia e të dhënave të matjeve themelore
Treguesi i gabimit
Përkufizimi
Tregon se një artikull ruhet në kundërshtim me strukturën fizike të grupit të të dhënave
Përshkrimi
-
Fusha e vlerësimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës, RrjetiIMbulimitTëMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës, RrjetiIMbulimitTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Boolean (e vërteta që tregon mospërputhjen e strukturës fizike)
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Paraqitja e artikujve në mbulesën që shkel përputhjen formative:
- Formati i skedarit, skedar ose emrat e atributeve ose llojet e atributeve nuk korrespondojnë me specifikimet
Masa identifikuese
119
3.7.6 PËRPUTHJA LIGJORE - PËRPUTHJA TOPOLOGJIKE (LOGICAL CONSISTENCY - TOPOLOGICAL CONSISTENCY)
Rekomandim
Përputhja topologjike duhet të vlerësohet dhe dokumentohet duke përdorur numrin e gabimeve të pavlefshme që vetëndërpriten të cilat janë përcaktuar në tabelën e mëposhtme:
Emri
Numri i gabimeve të pavlefshme që vet-ndërpriten
Emri alternativ
Unazorë
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja topologjike
Cilësia e të dhënave të matjeve themelore
Numri i gabimit
Përkufizimi
Numëron të gjithë artikujt me të dhënat që ndërhyjnë në mënyrë jo të rregullt me veten e tyre
Përshkrimi
-
Fusha e vlerësimit
Grupi i të dhënave: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
- Numri i unazave (“figura tetë” që formojnë poligone të mbuluara të tokës) janë të pranishme
Masa identifikuese
26
3.7.7 CILËSIA E TË DHËNAVE - SAKTËSIA E POZICIONIMIT - SAKTËSIA ABSOLUTE OSE E JASHTME (DATA QUALITY - POSITIONAL ACCURACY - ABSOLUTE OR EXTRENAL ACCURACY)
Rekomandim
Saktësia absolute ose e jashtme duhet të vlerësohet dhe dokumentohet duke përdorur gabimin mesatar kuadratik të planimetrisë, të specifikuar në tabelën e mëposhtme:
Emri
Gabimi mesatar kuadratik i planimetrisë
Emri alternativ
RMSEP
Cilësia e të dhënave të elementeve
Saktësia e pozicionimit
Cilësia e të dhënave të nënelementeve
Saktësia absolute ose e jashtme
Cilësia e të dhënave të matjeve themelore
-
Përkufizimi
1. Është rrënja katrore e mesatares së ndryshimeve në katror ndërmjet vlerave të koordinatave të një grupi të dhënash të matura dhe vlerave të koordinatave nga një burim i pavarur të saktësisë më të lartë për pikat identike. GMK-ja dallon dy raste:
Rasti 1 - Kur llogariten gabimet e mundshme vi
: :
Ku:
vi - gabimi i mundshëm që llogaritet si diference e vlerës përfaqësuese me vlerën e matur
- vlera përfaqësuese që merret si vlera mesatare e vlerave të matura xi
n - numri i matjeve
Rasti 2 - Kur llogariten gabimet e vërteta
:
Ku:
n - është numri i matjeve
X- vlera e vërtetë e vlerës së matur xi
- gabimet e vërteta dhe përcaktohen si diferencë e vlerës së vërtetë me vlerën e matur
Përshkrimi
Rrezja e rrethit rreth pikës së dhënë, në të cilën vlera e vërtetë shtrihet me probabilitetin P
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Vërtet
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Saktësia absolute ose e jashtme e pozicionit të të dhënave të mbulimit të tokës zakonisht përcaktohet nga saktësia absolute e pozicionit të imazheve në vëzhgimet e tokës, që shërben si bazë për nxjerrjen e të dhënave MT.
Masa identifikuese
47
3.7.8 CILËSIA E TË DHËNAVE - SAKTËSIA E POZICIONIMIT - SAKTËSIA RELATIVE OSE E BRENDSHME (DATA QUALITY - POSITIONAL ACCURACY - RELATIVE OR INTERNAL ACCURACY)
Rekomandim
Saktësia relative ose e brendshme duhet të vlerësohet dhe dokumentohet duke përdorur gabimin mesatar kuadratik të planimetrisë të specifikuar në tabelën e mëposhtme:
Emri
Gabimi mesatar kuadratik i planimetrisë
Emri alternativ
RMSEP
Cilësia e të dhënave të elementeve
Saktësia e pozicionimit
Cilësia e të dhënave të nënelementeve
Saktësia relative ose e brendshme
Cilësia e të dhënave të matjeve themelore
-
Përkufizimi
2. Është rrënja katrore e mesatares së ndryshimeve në katror ndërmjet vlerave të koordinatave të një grupi të dhënash të matura dhe vlerave të koordinatave nga një burim i pavarur të saktësisë më të lartë për pikat identike. GMK-ja dallon dy raste:
Rasti 1 - Kur llogariten gabimet e mundshme vi
: :
Ku:
vi - gabimi i mundshëm që llogaritet si diference e vlerës përfaqësuese me vlerën e matur
- Vlera përfaqësuese që merret si vlera mesatare e vlerave të matura xi
n - Numri i matjeve
Rasti 2 - Kur llogariten gabimet e vërteta
:
Ku:
n - është numri i matjeve
X- vlera e vërtetë e vlerës së matur xi
- gabimet e vërteta dhe përcaktohen si diferencë e vlerës së vërtetë me vlerën e matur
Përshkrimi
Rrezja e rrethit rreth pikës së dhënë, në të cilën vlera e vërtetë shtrihet me probabilitetin P.
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
E vërtetë
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Saktësia relative ose e brendshme e pozicionit të të dhënave të mbulimit të tokës zakonisht përcaktohet si saktësi e përcaktimit të kufijve të njësive të mbulesës së tokës, në lidhje me imazhet themelore të vëzhgimeve të tokës që shërben si bazë për nxjerrjen e të dhënave MT.
Masa identifikuese
47
3.7.9 CILËSIA E TË DHËNAVE - SAKTËSIA TEMATIKE - KORREKTËSIA E KLASIFIKIMIT (DATA QUALITY - THEMATIC ACCURACY - CLASSIFICATION CORRECTNESS)
Rekomandim
Korrektësia e klasifikimit duhet të vlerësohet dhe të dokumentohet duke përdorur shkallën e mosklasifikimit ose matricën e mosklasifikimit siç specifikohet në tabelën e mëposhtme:
Emri
Gabimi i mosklasifikimit
Emri alternativ
-
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Korrektësia e klasifikimit
Cilësia e të dhënave të matjeve themelore
-
Përkufizimi
Zona e klasifikuar gabimisht në lidhje me zonën e vërtetë të vendit klasës së mbulesës të synuar
Përshkrimi
-
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Real
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Shkalla e mosklasifikimit zakonisht vlerësohet me vëzhgim dhe raportohet në lidhje me një zonë të mbulimit të tokës. Parametrat sasiorë duhet të publikohen së bashku me vlerësimin e pasigurisë në një nivel domethënës të paracaktuar.
Shkalla e gabimit të komisionit të klasës është 12.1% ± 2.8%
Shkalla e gabimit të përjashtimit të klasës është 16.4% ± 3.5%
Niveli i rëndësisë: 68.3%
Masa identifikuese
61
Emri
Gabimi i mosklasifikimit
Emri alternativ
Matrica e konfuzionit
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Korrektësia e klasifikimit
Cilësia e të dhënave të matjeve themelore
-
Përkufizimi
Matricë që tregon klasën e zonës (i) klasifikuar si klasë (j). Në praktikë këto zona vlerësohen nga numri i mostrave të rastësishme që bien në klasën (i) dhe klasën (j)
Përshkrimi
Matrica e mosklasifikimit (MCM) është një matricë katrore me n kolona dhe n rreshta, n nënkupton numrin e klasave në shqyrtim.
MCM (i,j) = [ # artikuj të klasës (i) klasifikuar si klasa (j) ]
Elementet e diagonales së matricës së mosklasifikimit përmbajnë artikuj të klasifikuar mirë dhe elementet jashtë diagonaleve përmbajnë numrin e gabimeve të mosklasifikimit.
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
Emri: n
Përkufizimi: numri i klasave që shqyrtohen.
Lloji i vlerës: Integer
Cilësia e të dhënave të llojeve të vlerave
Integer
Cilësia e të dhënave të strukturës së vlerave
Matricë (n*n)
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Congalton, R. (1991) Shqyrtimi i vlerësimit të saktësisë së klasifikimeve të të dhënave të ndjeshme nga distanca. Ndjeshmëria në distancë, e mjedisit 37: 35-46.
Shembull
Shkalla e mosklasifikimit zakonisht vlerësohet me vëzhgim dhe raportohet në lidhje me një zonë të mbulimit të tokës. Parametrat sasiorë duhet të publikohen së bashku me vlerësimin e pasigurisë në një nivel domethënës të paracaktuar.
Shkalla e gabimit të komisionit të klasës është 12.1% ± 2.8%
Shkalla e gabimit të përjashtimit të klasës është 16.4% ± 3.5%
Niveli i rëndësisë: 68.3%
Masa identifikuese
62
Emri
Matrica e mosklasifikimit
Emri alternativ
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Korrektësia e klasifikimit
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Zona e klasifikuar gabim në lidhje me zonën e vërtetë të klasës së mbulimit të tokës
Përshkrimi
-
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Vërtet
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
Caktimi i një artikulli në një klasë të caktuar mund të jetë i saktë ose i pasaktë. Si të dhëna të përshtatshme të mbulesës së tokës janë të disponueshme rrallë, klasifikimi i mbulimit të tokës zakonisht krahasohet në vendndodhjet e mostrës me interpretim reference bazuar në imazhet e OE-së ose kontrolli në terren.
Masa identifikuese
61
3.7.10 CILËSIA E TË DHËNAVE - SAKTËSIA TEMATIKE - SAKTËSIA E ATRIBUTEVE JOSASIORE (DATA QUALITY - THEMATIC ACCURACY - NON-QUANTATIVE ATTRIBUTE ACCURACY)
Rekomandim
Saktësia e atributeve josasiore duhet të vlerësohet dhe dokumentohet duke përdorur shkallën e vlerave të atributeve të pasakta, siç specifikohet në tabelën e mëposhtme:
Emri
Shkalla e vlerave të atributeve të pasakta
Emri alternativ
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Saktësia e atributeve josasiore
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numri i vlerave të atributeve ku vlerat e gabuara janë caktuar në lidhje me numrin e përgjithshëm të vlerave të atributeve
Përshkrimi
-
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulesësSëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Vërtet
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembull
-
Masa identifikuese
67
3.7.11 CILËSIA E TË DHËNAVE - SAKTËSIA TEMATIKE - SAKTËSIA E ATRIBUTEVE SASIORE (DATA QUALITY - THEMATIC ACCURACY - QUANTATIVE ATTRIBUTE ACCURACY)
Rekomandim
Saktësia e atributeve sasiore duhet të vlerësohet dhe dokumentohet duke përdorur grafikun e llojit “scatter plot” siç specifikohet në tabelën e mëposhtme:
Emri
Grafiku “Scatter plot”
Emri alternativ
Cilësia e të dhënave të elementeve
Saktësia tematike
Cilësia e të dhënave të nënelementeve
Saktësia e atributeve sasiore
Cilësia e të dhënave të matjeve themelore
-
Përkufizimi
Krahasimi grafik i vlerave të densitetit të mbulesës së tokës referente me vlerat e densitetit të siguruara nga produkti
Përshkrimi
-
Fusha e vlerësimit
Objekti gjeohapësinor: NjësiaEMbulimitTëTokës
Fusha e raportimit
Grupi i të dhënave: GrupiITëDhënaveTëMbulesësSëTokës
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Grafik
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
http://sia.eionet.europa.eu/EAGLE/EAGLE_5rdMeeting_g2_MONINA_FFM/EL_
Validation_of_HR_layers_finaldraft.pdf
Shembull
Masa identifikuese
-
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
MBULESA E TOKËS
3.2.2.1
LandCoverNomenclature
NomenklaturaEMbulesësSë
Tokës
LandCover Nomenclature
DataType
3.2.2.2
CorineValue
VleratCorine
LandCoverNomenclature
Kodlistë
3.2.2.3
LandCoverClassValue
VleratEKlasaveTëMbulesësSë
Tokës
LandCoverNomenclature.
Kodlistë
3.3.2.1
LandCoverDataSet
GrupiiTëDhënaveTëMbulesësSë Tokës
Land CoverVector
FeatureType
3.3.2.2
LandCoveValue
VleratEMbulesësSëTokës
LandCoverVector
DataType
3.3.2.3
LandCoverValue
VleratEKategorisëSëMbulesesSë Tokës
LandCoverVector
DataType
3.2.3.4
LandCoverObservation
VrojtimiIMbulesësSëTokës
LandCoverVector
Kodlistë
3.2.3.5
LandCoverUnit
NjësiaEMbulesësSëTokës
LandCoverVector
FeatureType
3.4.2.1
LandCoverGridCoverage
RrjetiiMbulimitTëMbulesësSë Tokës
LandCoverRaster
FeatureType
4.2 Aneksi B - Kodlistat
4.2.1 KodLista “Nomenklatura e mbulesës së tokës”
4.2.1.1 Vlerat CORINE
Emërtimi: KodlistatCORINE të mbulesës së tokës
Përcaktimi: KodlistatCORINE të mbulesës së tokës drejtuar nga EEA
Identifikimi: http://www.eea.europa.eu/data-and-maps/data/corine-land-cover-2006-raster-1/corine-land-cover-classes-and/clc_legend.csv/at_doënload/file
*Shënim. Vlerat e lejuara për këtë listë kodesh përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Kodi i kategorisë
Category Name
Emërtimi i kategorisë
Kodi i klasës
Emërtimi i klasës
Përkufizimi
1
Surface with Constructions and other Artificial Spaces
Sipërfaqe me ndërtime dhe hapësira të tjera artificiale
111
Struktura urbane e vazhdueshme
Pjesa më e madhe e sipërfaqes mbulohet nga ndërtesa, rrugë dhe zona me sipërfaqe artificiale, që mbulojnë pothuajse të gjithë tokën. Janë të përjashtuara zonat jolineare të vegjetacionit dhe tokat e zhveshura.
112
Struktura urbane e ndërprerë
Pjesa më e madhe e tokës mbulohet nga strukturat. Ndërtesat, rrugët dhe zonat me sipërfaqe artificiale të lidhura me zonat pa bimësi dhe tokat e zhveshura, të cilat zënë sipërfaqe të pavazhdueshme, por të rëndësishme.
121
Njësitë industriale ose tregtare
Zonat me sipërfaqe artificiale (me beton, asfalt ose tokë e rrafshuar) pa vegjetacion, zënë pjesën më të madhe të zonës në fjalë, e cila, gjithashtu, përmban ndërtesa dhe/ose zona të vegjetuara.
122
Rrjetet rrugore, hekurudhore dhe lidhja me tokën
Autostradat, hekurudhat, duke përfshirë instalimet përkatëse (stacione, platforma, argjinatura). Gjerësia minimale përfshirë: 100 m.
123
Zonat e portit
Infrastruktura e zonave të porteve, duke përfshirë kalatat, kantieret dhe portet e turistëve.
124
Aeroporti
Instalimet e aeroportit, pistën, rrugët, ndërtesat së bashku me tokën.
131
Vendet e nxjerrjes së mineraleve
Zonat me gropa të hapura për nxjerrjen e mineraleve industriale (gërmuesit, guroret) ose minerale të tjera (miniera të hapura).
132
Vendet e hedhjes së mbeturinave
Landfillet ose vendet e depozitimit të mbeturinave minerare, industriale ose publike.
133
Vendet në ndërtim
Hapësirat në zhvillim të ndërtimit, gërmimet e tokës ose të themelit, punime tokësore.
141
Zona të gjelbëruara brenda hapësirës urbane
Zonat me bimësi brenda strukturave urbane. Këtu përfshihen parqet dhe varrezat me bimësi.
142
Mjedise sportive dhe kampinge, piknike etj.
Kampet sportive, terrenet sportive, parqet, fushat e golfit, pista për gara etj. Këtu përfshihen parqe qe nuk janë në zonat urbane.
2
Cultivated Agricultural Areas
Sipërfaqe të kultivuara bujqësore
211
Tokë arë e paujitshme
Drithëra, bishtajore, bimë foragjere dhe frutrrënjorët. Këtu përfshihen kultivimi i luleve dhe fidanishteve si në terren të hapur dhe në serra me (plastmasë ose xham).
212
Tokë arë e ujitshme
Kulturat ujiten përgjithmonë dhe periodikishte, duke përdorur një infrastrukturë të përhershme (kanale ujitës dhe rrjetet vaditëse). Shumica e këtyre kulturave nuk mund të kultivohen pa vaditjen në mënyrë artificiale. Këtu nuk përfshihen tokat e ujitura në mënyrë sporadike.
213
Orizoret
Tokat e përshtatura për kultivimin e orizit. Sipërfaqe të sheshta me kanale ujitës. Sipërfaqe që përmbyten në mënyrë të rregullt.
221
Vreshtat
Zonat e mbjella me vreshta.
222
Pemë frutore
Parcela të mbjella me pemë frutore ose shkurre: të përbëra nga një lloj i vetëm ose të përziera, pemë frutore të shoqëruara me sipërfaqe të përhershme me bar. Këtu përfshihen arrat dhe gështenjat.
223
Ullishtet
Zona të mbjella me ullinj. Përfshi dhe zonat mikse me vreshta.
231
Livadhe
Mbulesa e dendur, kryesisht me bar dhe me lule, jashtë skemave të rrotacionit. Kryesisht përdoret për kullotje, por foragjeret mund të korren mekanikisht. Këtu përfshihen zonat me rrethim bimësie.
241
Kultura njëvjeçare të bashkëshoqëruara me bimë shumëvjeçare
Bimë njëvjeçare të shoqëruara me bimë shumëvjeçare në të njëjtën parcelë.
242
Modele kultivimi komplekse
Parcela të vogla të vendosura pranë njëra-tjetrës, me bimë njëvjeçare të ndryshme, kullota ose bimë shumëvjeçare.
243
Tokë e zënë kryesisht me bujqësi e kombinuar me bimësi natyrore.
Tokë e zënë kryesisht nga bujqësia, me zona të rëndësishme të bimësisë natyrore. Zonat e zëna kryesisht nga bujqësia, të ndërthurura me zona të rëndësishme natyrore ose gjysmë natyrore (duke përfshirë ligatinat, trupat e ujit, nxjerrjet e mineraleve).
244
Zonat agropyjore
Kulturat vjetore ose tokat e kullotjes nën mbulesën e pyllëzuar të specieve pyjore.
3
Areas with Natural and Semi - Natural Forests
Sipërfaqe me Pyje natyrore dhe gjysmë natyrore
311
Pyjet gjethegjerë
Formimi i vegjetacionit i përbërë kryesisht nga pemë, duke përfshirë bimët e shkurreve dhe shkurret, ku mbizotërojnë speciet me gjethe të gjelbra.
312
Pyje halore
Formimi i vegjetacionit i përbërë kryesisht nga pemë, duke përfshirë edhe shkurret, ku mbizotërojnë speciet halore.
313
Pyje të përzier
Formimi i vegjetacionit i përbërë kryesisht nga përzierje e llojeve fletorë dhe halorë, duke përfshirë edhe shkurret.
321
Kullota natyrore
Kullotat me produktivitet të ulët. Shpesh ndodhen në zonat e ulëta ku përfshihen gjithashtu edhe disa zona shkëmbore, ose sipërfaqe toke të një bimësie tjetër (gjysmë) natyrore.
322
Shqopishte
Bimësia me mbulesë të ulët dhe të mbyllur, të dominuar nga bimët e shkurreve, shkurret, (shqopishte, driza, gjineshtra etj.). dhe bimë barishtore, duke formuar një fazë kulmore të zhvillimit.
323
Vegjetacion sklerofil
Vegjetacioni i sklerofilit në një fazë kulmore të zhvillimit, përfshirë këtu makien dhe garrigen.
324
Pyje dhe shkurre tranzitore
Shkurre kalimtare dhe bimësi barishtore me pemë të shpërndara rastësisht. Mund të përfaqësojë degradimin e pyjeve ose rigjenerimin/rikolonizimin e pyjeve.
331
Plazhe, duna, ranishte
Shtrirja natyrore e papërpunuar e rërës ose guralecëve/zhavorrit, në vende bregdetare ose kontinentale, si: plazhet, dunat apo brigjet me guralecë; duke përfshirë shtretërit e kanaleve të rrymës në formë rrëkeje.
332
Sipërfaqe shkëmbore
Rrëpirë me gurë të rrëzuar, shkëmbinj, formacione të shkëmbinjve, duke përfshirë zonat e erozionit aktiv, shkëmbinj dhe laguna që ndodhen mbi nivelin e ujit, në brendësi të fushave me kripë.
333
Sipërfaqe me bimësi të rrallë
Zonat me vegjetacion të rrallë, duke mbuluar 10-50% të sipërfaqes. Përfshirë, tundrën, stepën dhe terrenet e larta alpine.
334
Sipërfaqe të djegura
Sipërfaqe të përshkuara nga zjarri.
335
Akullnajat bora e përhershme
Toka të mbuluara nga akujt dhe borë e përhershme.
4
Wetland Areas
Sipërfaqe
ligatinore
411
Këneta në toka të ulëta
Zakonisht shtrihet në toka të ulëta të përmbytura në dimër dhe pak të saturuara me ujë gjatë gjithë vitit.
412
Këneta me torfë
Toka torfike që përmbajnë kryesisht masa të dekompozuara dhe mbeturina bimore.
421
Kënetat e kripura
Zona të ulëta me vegjetacion mbi linjën e baticës të influencuara nga përmbytja e ujit të detit. Shpesh në procesin e mbushjes, gradualisht mbushen nga bimët alifilike.
422
Kripore
Kripore aktive ose në proces abandonimi. Kanale me ujëra të kripura të përdorura për prodhimin e kripës pas avullimit. Ato dallohen nga kënetat nga parcelizimi i tyre.
423
Sheshe ndërbaticore
Hapësira në përgjithësi pa vegjetacion, me llucë, rërë ose shkëmbinj që shtrihen midis kufirit të sipërm dhe të poshtëm të ujit. Kontur 0 m në hartë.
5
Water Area
Sipërfaqe ujore
511
Rrjedhat ujore
Rrjedhat ujore natyrale ose artificiale që shërbejnë si kanale për drenazhimin e ujit. Minimumi i gjerësisë për përfshirjen 100 m.
512
Trupa ujorë
Shtrirja natyrore ose artificiale e ujit.
521
Laguna bregdetare
Shtresat pa bimësi me kripë ose ujëra të njelmëta të ndara nga deti me rrip toke ose me një topografi të ngjashme. Këto trupa uji mund të lidhen me detin në pika të kufizuara, të cilat mund të kenë lidhje të përhershme ose vetëm në një pjesë të vitit.
522
Grykëderdhje
Grykëderdhja e lumit brenda së cilës batica tërhiqet dhe shtyhet.
523
Deti dhe oqeani
Sipërfaqja ujore e detit në pjesën më të ulët të baticës.
4.2.2 Vlerat e kategorisë së mbulesës së tokës
-- Emri --
Vlerat e kategorisë së mbulesës së tokës
-- Përkufizimi --
Kategoritë e mbulesës së tokës sipas klasifikimit aktual.
ATRIBUTE
Kategoria I
--Emri--
Kategoria I
-- Përkufizimi --
Sipërfaqe me ndërtime dhe hapësira të tjera artificiale, kategoria e parë e klasifikimit të mbulesës së tokës.
Kategoria II
--Emri--
Kategoria II
-- Përkufizimi --
Sipërfaqe të kultivuara bujqësore, kategoria e dytë e klasifikimit të mbulesës së tokës.
Kategoria III
--Emri--
Kategoria III
-- Përkufizimi --
Sipërfaqe me pyje natyrore dhe gjysmënatyrore, kategoria e tretë e klasifikimit të mbulesës së tokës.
Kategoria IV
--Emri--
Kategoria IV
-- Përkufizimi --
Sipërfaqe moçalore, kategoria e katërt e klasifikimit të mbulesës së tokës.
Kategoria V
--Emri--
Kategoria V
-- Përkufizimi --
Sipërfaqe ujore, kategoria e pestë e klasifikimit të mbulesës së tokës.
4.2.3 Kodlista për arsyet e pavlefshmërisë - Voidable
--Emri--
Vlerat e pavlefshmërisë - Voidable
-- Përkufizimi --
Kjo karakteristikë paraqet arsyet e përdorimit të vlerës void. Kur e ndeshim këtë, i japim në përdorim një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
ATRIBUTE
E panjohur - (Unknwonn)
--Emri--
E panjohur
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” të një liqeni nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
E papopulluar (Unpopulated)
--Emri--
E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj, kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E papopulluar”.
Konfidenciale - (Withheld)
--Emri--
Konfidencial
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
