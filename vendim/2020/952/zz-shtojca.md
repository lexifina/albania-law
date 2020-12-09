# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI - TEMA: IMAZHI I HARTËS BAZË
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Imazhi i hartës bazë
3.1.1 Parathënie
3.1.2 Skemat e aplikimit dhe diagrami UML për temën: “Imazhi i hartës bazë”
3.2 Përshkrimi i nëntemës: “Harta bazë mbulim”
3.2.1 Skemat e aplikimit dhe diagramit UML për nëntemën: “Harta bazë mbulim”
3.2.2 Katalogu i tipologjisë
3.2.2.1 Harta bazë mbulim
3.2.2.2 Autoriteti përgjegjës
3.2.2.3 Elementet matematikore të hartës
3.2.2.4 Nomenklatura
3.2.2.5 Viti i krijimit ose i përditësimit
3.2.2.6 Vlerat e llojit të teknologjisë
3.3 Përshkrimi i nëntemës: “Harta bazë vektor”
3.3.1 Skemat e aplikimit dhe diagramit UML për nëntemën: “Harta bazë vektor”
3.3.2 Katalogu i tipologjisë
3.3.2.1 Harta bazë vektor
3.3.2.2 Emërtimet gjeografike
3.3.2.3 Kufijtë e njësive administrative
3.3.2.4 Rrjetet e transportit
3.3.2.5 Hidrografia
3.3.2.6 Modeli digjital i terrenit
3.3.2.7 Mbulesa e tokës
3.3.2.8 Ndërtesat
3.3.2.9 Elementet e tjera
3.4 Metadata
3.5 Kodi EPSG për KRGJSH-në
3.6 Cilësia e të dhënave
3.6.1 Kompletimi - Komisioni (Completeness - Commission)
3.6.2 Kompletimi - Përjashtimi (Completeness - Omission)
3.6.3 Përputhja ligjore - Përputhja konceptuale (Logical consistency - Conceptual consistency)
3.6.4 Përputhja ligjore - Përputhja me domein-in (Logical consistency - Domain consistency)
3.6.5 Përputhja ligjore - Përputhja me formatin (Logical consistency - Format consistency)
3.6.6 Përputhja ligjore - Përputhja topologjike (Logical consistency - Topological consistency)
3.6.7 Saktësia pozicionale - Saktësia absolute (Positional accurancy - Absolute accuracy)
3.6.8 Saktësia tematike - Korrektësia e klasifikimit (Thematic accurancy - Classification correcteness)
3.6.9 Saktësia tematike - Korrektësia e atributeve jo sasiore (Thematic accurancy - Nonquantitative attribute correcteness)
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
4.2 Aneksi B - Kodlistat
4.2.1 Skema e aplikimit. Harta bazë mbulim
4.2.1.1 Vlerat e llojit të teknologjisë
4.3 Aneksi C - Simbologjia e hartës bazë
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG).
Data e publikimit të versionit nr.1 është prill 2019. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2019_ IHB_v.1 ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit;
Standard - Lloji i dokumentit;
NSDI - Qëllimi i dokumentit;
2019 - Viti i krijimit;
IHB - Tema për të cilën është krijuar standardi: “Imazhi i hartës bazë”.
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 Qëllimi
Ky dokument përcakton specifikimet teknike, për të dhënat gjeohapësinore të temës: “Imazhi i hartës bazë”, temë e cila është përcaktuar në nenin 11, pika 2/ç, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse, për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë midis tyre.
2.2 SI LEXOHET DOKUMENTI
2.2.1 STRUKTURA E DOKUMENTIT
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema: Në këtë pjesë jepen specifikimet teknike për temën: “Imazhi i hartës bazë”.
4. Anekse: Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 6 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës, si dhe detajohen: Diagramit UML dhe katalogu i tipologjive.
3.2 Përshkrimi i nëntemës: “Harta bazë mbulim” - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e nëntemës, si dhe detajohen: Diagrami UML dhe katalogu i tipologjive.
3.3 Përshkrimi i nëntemës: “Harta bazë vektor” - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e nëntemës, si dhe detajohen: Diagrami UML dhe katalogu i tipologjive.
3.4 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.5 Sistemi koordinativ referencë - Këtu përcaktohet sistemi koordinativ referencë që është miratuar me vendimin nr. 669, datë 7.8.2013, të Këshillit të Ministrave, i ndryshuar, me vendimin nr. 322, datë 27.4.2016, dhe vendimin nr. 359, datë 29.5.2019.
3.6 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në ’Katalogu i tipologjive’ (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në Katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të shembujve, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit në tabelën e kodlistës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
«featureType» - një element që mund të jetë real, në terren, apo një dukuri abstrakte;
«dataType» - një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër;
«enumeration» “Kodlist» - listë e parapërgatitur vlerash, ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”;
«union» - një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet, të cilat bien brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse;
«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të dhënat e importuara”.
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
Rol shoqërimi
Në tabelën e lidhjeve “Rol shoqërime” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshëm në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi i elementeve.
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin.
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh: PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh: ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh: joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
2.2.3 KARAKTERISTIKAT E VOIDABLE DHE SHUMËLLOJSHMËRIA
Stereotipi voidable përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat, e përcaktuara për objektet gjeohapësinore, duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera ’void’. Një vlerë ’void’ nënkupton që nuk ekziston një vlerë përkatëse, në grupet e të dhënave gjeohapësinore, që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës ’void’ duhet të paraqitet kurdo që të jetë e mundur, duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
- E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni të caktuar, nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull. Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E papopulluar”.
- Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull. Të dhënat personale të popullsisë të cilat ekzistojnë por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi <<voidable>> nuk jep asnjë informacion nëse ekziston një karakteristikë në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh: nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1;
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh: nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohoro-gjeohapësinor. Domein-et tipike gjeohapësinore janë grupe pikash (p.sh. vendndodhja e sensorëve), kurbat përcaktuese (p.sh. izolinjat), rrjetet (p.sh: ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si veti të llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh: ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik, për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptual të Përgjithshëm “Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domein-i i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domein-i i të cilit përbëhet nga një rrjet referimi, një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje mbulimi (ose një nëntip i tyre) në skemat e aplikimit në INSPIRE.
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 NUMËRTIMET DHE KODLISTAT (ENUMERATION AND CODE LIST)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, ’vlera të tjera’ përcaktojnë llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht, si më poshtë:
- ’jo’ përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
- ’të kufizuara’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara, të përcaktuara nga ofruesi i të dhënave;
- ’të hapura’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave;
- ’po’ përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë, të përcaktuara nga ofruesit e të dhënave, nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo”, pra të specifikuara në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
Shënim i rëndësishëm:
Disa terma në Katalogun e tipologjive, si p.sh. featuretype, datatype, void, coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të direktivës INSPIRE.
2.3 DETYRIMET LIGJORE
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është institucioni përgjegjës për krijimin e standardeve, për secilën nga temat e përcaktuara në nenin 11 të këtij ligji, në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (sikurse është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM-ja nr. 1077, datë 23.12.2015);
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 FUSHA E VEPRIMIT
Të gjithë autoritetet publike, kompanitë private apo individët që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2: Proceset e ciklit jetësor
Planifikimi - Është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave;
Vlerësimi - Është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit;
Procesimi (Përpunimi) - Është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar;
Shpërndarja - Është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit;
Zbulimi - Është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara;
Analiza - Është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar;
Përditësimi - Është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara;
Arkivimi - Është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendit ku implementohet standardi. Rezultat i këtij procesi janë të dhënat që bëhen të pa aksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen, për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike;
Shkatërrimi - Është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 IMAZHI I HARTËS BAZË
3.1.1 PARATHËNIE
Harta bazë i referohet një grupi të dhënash GIS dhe/ose imazheve të ortorektifikuara, që formojnë një hartë mbështetëse bazë, e cila përmban të dhëna gjeohapësinore thelbësore dhe përdoret për të mbështetur punime të ndryshme hartografike. Të dhënat tipike vektor dhe/ose imazhet, që përbëjnë shtresat për një hartë bazë mund të jenë: rrugët, kufijtë administrativë (vendi, qarku, njësia vendore), rrugët ujore, ortoimazheria, imazhet satelitore etj. Në varësi të llojit të hartës, mund të përdoret çdo kombinim i këtyre shtresave. Harta bazë krijohet si kornizë me funksion përpunimi. Të dhënat e një harte bazë, janë të dhëna minimale që duhet të ketë çdo hartë që krijohet (nga institucione shtetërore/private/apo dhe përdorues të thjeshtë), sipas tematikave të ndryshme.
Përkufizimi:
Një hartë bazë është paraqitja grafike, në një shkallë të caktuar, e informacioneve kryesore të përzgjedhura, që përdoret si një kornizë, mbi të cilën mund të përpunohen të dhëna gjeohapësinore të tjera, të një natyre të specifikuar.
Përshkrimi:
Hartat bazë mund të ndryshojnë nga lloji, shkalla dhe informacioni i trajtuar. Mund të përmendim këtu hartat bazë mbulim (HartaBazëMbulim) dhe hartat bazë vektor (HartaBazëVektor). Secila nga këto lloje hartash bazë paraqet informacionin minimal gjeohapësinor.
Për të filluar procesin e ndërtimit të hartës bazë kryhet fillimisht një vlerësim i materialeve burimore nga harta bazë ekzistuese. Gjithashtu kryhet dhe përcaktimi i shtresave bazë, të domosdoshme, që shërbejnë për të paraqitur informacionin gjeohapësinor. Harta bazë kombinon të dhënat ekzistuese tematike duke kryer përpunimin e të dhënave dhe modelit gjeohapësinor të zbatuar, që ndikojnë në produktin përfundimtar.
Aplikimet e mundshme alternative të hartës bazë janë të shumta. Për më tepër, në të ardhmen, të dhëna të tjera mund të përfshihen p.sh: si të dhëna administrative apo të dhëna të hartave kadastrale.
Harta bazë u siguron përdoruesve një kontekst gjeografik dhe vizual për të dhënat. Zgjedhja e hartës bazë ndikon në mënyrën se si përdoruesit interpretojnë dhe përdorin hartën.
Qëllim tjetër i hartës bazë është sigurimi i transparencës së plotë të metodologjisë së zhvilluar. Kjo përfshin përshkrimet e hollësishme të të dhënave hyrëse, të përpunimit të këtyre të dhënave dhe të modelimit gjeohapësinor të aplikuar. Transparenca e metodologjisë së aplikuar, në një të ardhme, do të lehtësojë krijimin e versioneve të reja të hartave bazë, bazuar në të dhënat e përditësuara. Për më tepër, modelimi gjeohapësinor dhe të dhënat hyrëse mund të përshtaten me qëllimet alternative dhe nevojat për hulumtim.
Harta bazë kombinon informacionet ekzistuese tematike dhe kryen përpunimin e të dhënave me modelin gjeohapësinor të zbatuar, që ndikojnë në produktin përfundimtar. Ekzistojnë dy forma themelore që mund të përdoren për të paraqitur informacionin e hartës: HartaBazëMbulim (Raster) dhe HartaBazëVektor.
3.1.2 SKEMAT E APLIKIMIT DHE DIAGRAMI UML PËR TEMËN: “IMAZHI I HARTËS BAZË”
Skema e aplikimit për ImazhiIHartës, jepet përmes dy paraqitjeve: HartaBazëMbulim dhe HartaBazëVektor, ku secili nga këto objekte përfaqësohet nga tipologji të ndryshme.
Figura 3: Skema e përgjithshme e aplikimit për temën “Imazhi i hartës bazë”
3.2 PËRSHKRIMI I NËNTEMËS “HARTA BAZË MBULIM”
Hartabazëmbulim (raster) është një nga format e paraqitjes themelore hartografike. Për të kryer paraqitjen e saj, kryhet vlerësimi i të dhënave paraprake dhe hartat ekzistuese. Këtu përfshihen hartat ekzistuese, topografike dhe/ose ortoimazheria.
Në hartat topografike përfshihen:
- Harta topografike të viteve të ndryshme;
- Harta topografike të shkallëve të ndryshme (p.sh: 10 000, 25 000, 50 000 etj.).
Përveç hartave topografike, si hartëbazëmbulim (raster) kemi dhe ortoimazherinë (pavarësisht se bën pjesë në një temë tjetër), ku paraqitet në një formë të thjeshtë informacioni gjeografik. Vlerat e atributeve të një rastër-i janë përshtatur duke përdorur gjeometrinë e një rrjeti kuadratik të rregullt në dy dimensione.
Ortoimazheria përfshin ortofotot e prodhuara në vite të ndryshme, që janë:
- Ortofoto të viteve të ndryshme (p.sh: 2007, 2015, 2018 etj.);
- Ortofoto të rezolucioneve të ndryshme (p.sh: 8 cm, 20 cm etj.).
Figura 4: Paraqitja e të dhënave me metodën e mbulimit (raster) për nëntemën HartaBazëMbulim
3.2.1 SKEMAT E APLIKIMIT DHE DIAGRAMET UML PËR NËNTEMËN: “HARTA BAZË MBULIM”
Skema e aplikimit të HartaBazëMbulim paraqet elementet bazë që duhet të përmbajë një hartë bazë raster. Kjo realizohet ndërmjet kombinimit të feature-it kryesor që ndërlidhet me datatype-et përkatëse.
Figura 5: Skema e aplikimit për HartaBazëMbulim
3.2.2 KATALOGU I TIPOLOGJISË
3.2.2.1 HARTA BAZË MBULIM
-- Emri-
Harta bazë mbulim (raster)
-- Përkufizimi --
Harta bazë mbulim (raster) përbëhet nga të dhënat të paraqitura në formë pikseli (ose qelize), ku çdo pikseli ka një vlerë të lidhur. Pra, gjithë këto të dhëna, përfaqësohen si një rrjet (zakonisht katror) qelizash.
-- Tipi i elementit --
FeatureType
ATRIBUTE
Autoritetet: AutoritetetPërgjegjëse
Shumëllojshmëria: [1..*]
-- Emri --
Autoritetet përgjegjëse
-- Përkufizimi --
Autoritetet përgjegjëse për krijimin, mirëmbajtjen dhe përditësimin e hartave.
[ I detyrueshëm: PO]
Emërtimi: EmërtimiGjeografik
Shumëllojshmëria: [1]
-- Emri --
Emërtimi
-- Përkufizimi --
Emërtimi i llojit të hartës.
-- Përshkrimi -
Shembull. Llojet e hartave topografike, ortofoto etj.
[ I detyrueshëm: PO]
FillimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data dhe ora në të cilën, versioni i grupit të të dhënave të përdorimit ekzistues të tokës është bashkëngjitur ose krijuar në grupin e të dhënave.
[ I detyrueshëm: PO]
ParametratEHartës: ElementetMatematikorëTëHartës
Shumëllojshmëria: [1..*]
-- Emri --
Parametrat e hartës
-- Përkufizimi --
Parametrat matematikë, të sistemit koordinativ, të krijimit të hartës topografike si: elipsoidi, projeksioni etj.
[ I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [0..1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i objektit të jashtëm është një identifikues unik i objektit, i publikuar nga autoriteti përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme, për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[ I detyrueshëm: PO]
LlojiITeknologjisë: VleratELlojitTëTeknologjisë
Shumëllojshmëria:[0..1]
-- Emri --
Lloji i teknologjisë
-- Përkufizimi --
Teknologjia e përdorur për të krijuar hartën bazë.
[ I detyrueshëm: PO]
Nomenklatura: Nomenklatura
Shumëllojshmëria: [1]
-- Emri --
Nomenklatura
-- Përkufizimi --
Emërtesa e hartës, e cila i referohet një sistemi shkronjash dhe numrash të renditura sipas një rregulli të përcaktuar.
[ I detyrueshëm: PO]
PërfundimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i ciklit jetësor
-- Përkufizimi --
Data dhe koha në të cilën, ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq në grupin e të dhënave gjeohapësinore.
[ I detyrueshëm: JO]
Shkalla: Numër
Shumëllojshmëria: [1]
-- Emri --
Shkalla
-- Përkufizimi --
Shkalla e hartës i referohet raportit, midis distancës së matur në hartë dhe distancës përkatëse në tokë, p.sh në një hartë në shkallën 1: 10 000, 1cm në hartë është i barabartë me 10 000 cm (100 m) në tokë.
[ I detyrueshëm: PO]
Viti: VitiIKrijimit/Përditësimit
Shumëllojshmëria: [1..*]
-- Emri --
Viti
-- Përkufizimi --
Viti i krijimit ose përditësimit të hartës.
[ I detyrueshëm: JO]
LIDHJE
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) ImazhiIHartësBazë «featureType»
Shumëllojshmëria: [1]
-- Emri --
ImazhiIHartësBazë
-- Përkufizimi --
Harta bazë është paraqitja grafike në një shkallë të caktuar e
informacioneve kryesore të përzgjedhura. Ajo përdoret si
një kornizë mbi të cilën mund të përpunohen
të dhëna gjeohapësinore të tjera, të një natyre më të specializuar.
Objektivi: (Class) HartaBazëMbulim «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
HartaBazëMbulim
-- Përkufizimi --
Një nga paraqitjet themelore të hartave bazë, është ajo me mbulim (raster). Të dhënat e mbulimit përbëhen nga piksela (ose qeliza), dhe çdo piksel ka një vlerë të lidhur. Pra, gjithë këto të dhëna përfaqësohen si një rrjet (zakonisht katror) qelizash.
3.2.2.2 AUTORITETI PËRGJEGJËS
-- Emri --
Autoriteti përgjegjës
-- Përkufizimi --
Autoriteti përgjegjës për krijimin, mirëmbajtjen dhe publikimin e hartës.
-- Tipi i elementit --
DataType
ATRIBUTE
AutoritetiIMirëmbajtjes: Text
Shumëllojshmëria: [0..1]
-- Emri --
Autoriteti i mirëmbajtjes
-- Përkufizimi --
Autoriteti përgjegjës për mirëmbajtjen e hartës.
[ I detyrueshëm: PO]
AutoritetiKrijues: Text
Shumëllojshmëria: [0..1]
-- Emri --
Autoriteti krijues
-- Përkufizimi --
Autoriteti përgjegjës për krijimin e hartës.
[ I detyrueshëm: PO]
AutoritetiPublikues: Text
Shumëllojshmëria: [0..1]
-- Emri --
Autoriteti publikues
-- Përkufizimi --
Autoriteti përgjegjës për publikimin e hartës.
[ I detyrueshëm: PO]
3.2.2.3 ELEMENTET MATEMATIKORE TË HARTËS
-- Emri --
Elementet matematikore të hartës.
-- Përkufizimi --
Elementet matematikor të hartës përfshijnë projeksionet hartografike, shkallën e hartës dhe kufijtë e hartës.
-- Tipi i elementit --
DataType
ATRIBUTE
Elipsoidi: Tekst
Shumëllojshmëria: [1]
-- Emri --
Elipsoidi
-- Përkufizimi --
Elipsoidi i përcaktuar në sistemin koordinativ.
[ I detyrueshëm: PO]
EPSG: Tekst
Shumëllojshmëria: [1]
-- Emri --
EPSG
-- Përkufizimi --
EPSG kodi gjeodezik ndërkombëtar për identifikimin e sistemit koordinativ.
-- Përshkrim --
Shënim.
6870 është EPSG për KRGJSH-në (Korniza Referuese Gjeodezike Shqiptare);
32634 është EPSG për UTM, zona 24;
2462 është EPSG për Albanian 1986/Gaus-Kryger.
[ I detyrueshëm: PO]
Link: NT_Link
Shumëllojshmëria: [1]
-- Emri --
Link
-- Përkufizimi -
Link (lidhje) që gjeneron hartën topografike.
[ I detyrueshëm: PO]
OrigjinaELartësive: Tekst
Shumëllojshmëria: [0..*]
-- Emri --
Origjina e lartësive
-- Përkufizimi --
Datumi gjeodezik në të cilin është përcaktuar origjina e lartësive p.sh. niveli mesatar i Detit Adriatik.
[ I detyrueshëm: PO]
Përshkrimi: Tekst
Shumëllojshmëria: [0..1]
-- Emri --
Përshkrimi
-- Përkufizimi --
Përshkrimi i elementeve matematikorë të hartës.
[ I detyrueshëm: JO]
Projeksioni: Tekst
Shumëllojshmëria: [0..1]
-- Emri --
Projeksioni
-- Përkufizimi --
Projeksioni i përcaktuar në sistemin koordinativ.
[ I detyrueshëm: PO]
3.2.2.4 NOMENKLATURA
-- Emri --
Nomenklatura
-- Përkufizimi --
Emërtesa e hartës, e cila i referohet një sistemi shkronjash dhe numrash të renditura sipas një rregulli të përcaktuar.
-- Tipi i elementit --
DataType
ATRIBUTE
EmërtimiINomenklaturës: EmërtimiGjeografik
Shumëllojshmëria: [1]
-- Emri --
Emërtimi i nomenklaturës
-- Përkufizimi --
Emërtesa e hartës, e cila i referohet një sistem shkronjash dhe numrash të renditura sipas një rregulli të përcaktuar p.sh nomenklatura e hartës K-34-126-B-a.
[I detyrueshëm: PO]
IdELidhur: Identifikuesi
Shumëllojshmëria: [0..1]
-- Emri --
Id e lidhur
-- Përkufizimi --
Identifikuesi (ID) që lidhet me nomenklaturën, identifikon lidhjen unike me nomenklaturën.
[ I detyrueshëm: PO]
3.2.2.5 VITI I KRIJIMIT OSE I PËRDITËSIMIT
-- Emri --
Viti i krijimit ose i përditësimit
-- Përkufizimi --
Viti kur harta është krijuar ose përditësuar.
-- Tipi i elementit --
DataType
ATRIBUTE
VitiIPërditësimit: Datë
Shumëllojshmëria: [0..1]
-- Emri --
Viti i përditësimit
-- Përkufizimi --
Viti kur është kryer përditësimi i hartës.
[ I detyrueshëm: JO]
VitiIBotimit: Datë
Shumëllojshmëria: [0..1]
-- Emri --
Viti i botimit
-- Përkufizimi --
Viti kur është botuar harta.
[ I detyrueshëm: JO]
VitiIRealizimitTëMatjeve: Datë
Shumëllojshmëria: [0..1]
-- Emri --
Viti i realizimit të matjeve
-- Përkufizimi --
Viti kur janë realizuar matjet për krijimin e hartës.
[ I detyrueshëm: JO]
3.2.2.6 VLERAT E LLOJIT TË TEKNOLOGJISË
-- Emri --
Vlerat e llojit të teknologjisë
-- Përkufizimi --
Teknologjitë e përdorura gjatë krijimit të hartës bazë. Shiko aneksin B.
-- Tipi i elementit --
Kodlistë
3.3 PËRSHKRIMI I NËNTEMËS: “HARTA BAZË VEKTOR”
Ka disa mënyra të ndryshme për të paraqitur përfaqësimin e Hartave bazë, pasi ato mund të modelohen si dukuri diskrete ose të vazhdueshme në varësi të konceptimit në realitet. Skema e aplikimit të HartaBazëVektor mundëson paraqitjen e disa shtresave që janë objekte gjeohapësinore, që paraqiten me vijë ose pikë. Qëllimi parësor është të mbështesë shkëmbimin e të dhënave planare për HartaBazëVektor. HartaBazëVektor do të përfshijë disa objekte gjeohapësinore, featureType shoqëruar me atribute, ku secili nga këto objekte do të paraqitet si shtresë, duke u mbivendosur me njëra-tjetrën. Shtresat paraqesin të dhëna bazë të domosdoshme, të cilat duke u mbivendosur me njëra - tjetrën, formojnë hartën bazë vektor. Shtresat e përdorura te HartaBazëVektor janë tërësia e elementeve (tipologjive) të marrë nga tema të ndryshme të gjeoinformacionit, si dhe elemente të tjera shtesë (ElementetETjera), të identifikuar si të domosdoshëm, të cilët nuk janë pjesë e temave të gjeoinformacionit.
Shtresat e përdorura për këtë hartë vektor, të identifikuara sipas temave, janë radhitur si më poshtë:
- Emërtimet gjeografike (EGJ);
- Kufijtë e njësive administrative (KNJA);
- Rrjetet e transportit (RRT);
- Hidrografia (HID);
- Modeli digjital i terrenit (MDT);
- Mbulesa e tokës (MT);
- Ndërtesat (ND);
- ElementeTëTjera.
Figura 6: Paraqitja e shtresave në hartën bazë vektor
Të gjitha temat e mësipërme, përveç ElementetETjera, kanë specifikimet e tyre të të dhënave, të përshtatura sipas direktivës INSPIRE. Secila ka një paraqitje sipas standardit përkatës, por te standardi ImazhiIHartësBazë do të trajtohen vetëm objektet gjeohapësinore të nevojshëm për të krijuar një hartë bazë, duke paraqitur lidhjen midis temave dhe tipologjive (feature-ave) të secilës temë.
Vlen të theksohet që paraqitja vizive e të dhënave, në këtë hartë bazë, realizohet nga të dhëna vektor, të cilat nuk plotësohen me të dhëna atributesh por i referohen klasifikimeve të kodlistave, të secilës temë të gjeoinformacionit. Klasifikimi i të dhënave mbështetet në ndarjet dhe nënndarjet e kodlistave por të paraqitura sipas një simbologjie komplekse (kode, ngjyra dhe simbole - specifikuar në aneksin C). Për informacione të detajuara për tipologjitë dhe klasifikimet specifike, të temave, duhet t’i referohemi standardeve përkatëse të gjeoinformacionit.
3.3.1 SKEMAT E APLIKIMIT DHE DIAGRAMET UML PËR NËNTEMËN: “HARTA BAZË VEKTOR”
Skema e aplikimit të HartaBazëVektor është krijuar nga kombinimi i disa feature-ave, ku atributet e secilës tipologji janë përzgjedhur për të paraqitur të dhënat gjeohapësinore bazë.
Figura 7: Skema e aplikimit e HartaBazëVektor
3.3.2 KATALOGU I TIPOLOGJISË
3.3.2.1 HARTA BAZË VEKTOR
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore në format vektor, me anë të elementeve të secilës shtresë.
-- Tipi i elementit --
FeatureType
LIDHJE
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) Ndërtesat «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Ndërtesat
-- Përkufizimi --
Një ndërtesë është një konstruksion i mbyllur mbi dhe/ose nëntokë, i përdorur ose destinuar për strehimin e njerëzve, kafshëve, sendeve ose për prodhimin e mallrave ekonomike.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) KufijtëENjësiveAdministrative «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Kufijtë e njësive administrative
-- Përkufizimi --
Janë njësitë e ndarjeve administrative të sipërfaqeve ku shteti ka dhe/ose ushtron të drejtat juridike për qeverisjen lokale, rajonale dhe kombëtare.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor
«featureType» Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) MbulesaETokës «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Mbulesa e tokës
-- Përkufizimi --
Mbulesa e tokës përbën mbulimin fizik dhe biologjik të sipërfaqes së tokës, duke përfshirë sipërfaqet artificiale, sipërfaqet bujqësore, pyjet, zonat natyrore, ujërat.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) ModeliDixhitalITerrenit «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Modeli digjital i terrenit
-- Përkufizimi --
Sipërfaqja që përshkruan formën tri dimensionale të sipërfaqes së zhveshur të tokës, duke përjashtuar aq sa është e mundur çdo tipar tjetër të vendosur mbi të.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) EmërtimetGjeografike «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Emërtimet gjeografike
-- Përkufizimi --
Emërtimi i duhur që i përket entitetit në realitet.
Lidhje (drejtim: Objektivi-burimi
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) RrjetetETransportit «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Rrjetet e transportit
-- Përkufizimi -
Grup i elementeve të rrjetit që i përkasin një lloji të vetëm transporti.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) Hidrografia «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Hidrografia
-- Përkufizimi --
Hidrografia në kontekstin e specifikimit të të dhënave përfshin përshkrimet mbi elementet hidrografike: detet, liqenet, lumenjtë, ujërat etj.
Lidhje (drejtim: Objektivi-burimi)
Burimi: (Class) HartaBazëVektor «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Harta bazë vektor
-- Përkufizimi --
Harta bazë vektor është paraqitja e kombinuar e të dhënave gjeohapësinore me anë të elementeve të secilës shtresë.
Objektivi: (Class) ElementetETjera «featureType»
Shumëllojshmëria: [1..*]
-- Emri --
Elementet e tjera
-- Përkufizimi --
Elementet e tjera, janë element të shtuara nga autoriteti përgjegjës, për plotësimin e paraqitjes së të dhënave gjeohapësinore bazë.
3.3.2.2 EMËRTIMET GJEOGRAFIKE
-- Emri --
Emërtimet gjeografike
-- Përkufizimi --
Emërtimi i duhur që i përket entitetit në realitet.
-- Tipi i elementit --
FeatureType
ATRIBUTE
EmërtimiIVendit
Shumëllojshmëria: [1..*]
-- Emri --
Emërtimi i vendit
-- Përkufizimi --
Çdo entitet (subjekt) në realitet, të cilit i referohet një ose më shumë emra të përveçëm.
[ I detyrueshëm: PO]
3.3.2.3 KUFIJTË E NJËSIVE ADMINISTRATIVE
-- Emri --
Kufijtë e njësive administrative
-- Përkufizimi -
Janë njësitë e ndarjeve administrative të sipërfaqeve ku shteti ka dhe/ose ushtron të drejtat juridike për qeverisjen lokale, rajonale dhe kombëtare.
-- Tipi i elementit --
FeatureType
ATRIBUTE
KufijtëAdministrativë
Shumëllojshmëria: [1..*]
-- Emri --
Kufijtë administrativë
-- Përkufizimi --
Një vijë ndarëse ndërmjet dy njësive administrative.
[ I detyrueshëm: PO]
KufijtëDetarë
Shumëllojshmëria: [1..*]
-- Emri --
Kufijtë detarë
-- Përkufizimi --
Një linjë që përshkruan ndarjen e çdo lloji të juridiksionit detar.
[ I detyrueshëm: PO]
3.3.2.4 RRJETET E TRANSPORTIT
-- Emri --
Rrjetet e transportit
-- Përkufizimi --
Një grup elementesh të rrjetit që i përkasin një lloji të vetëm transporti.
-- Përshkrimi --
Shënim 1: Transporti ajror, hekurudhor, ujor, kabllor, rrugor merren gjithmonë parasysh si lloje të ndara transporti. Këto katër kategori, mund të ndahen në shumë nënlloje transporti, bazuar në infrastrukturë, llojet e automjeteve, sistemin e shtytjes, operimit dhe/ose karakteristika të tjera përcaktuese.
Shembull. Të gjitha transportet rrugore mund të konsiderohen një lloj transporti për disa aplikime. Për disa aplikime të tjera, mund të jetë i nevojshëm dallimi mes rrjeteve të ndryshme të transportit rrugor publik. Brenda transportit ujor, transporti detar dhe ujor i brendshëm mund të konsiderohen si lloje të veçanta transporti për disa aplikime, sepse përdorin lloje të ndryshme anijesh.
-- Tipi i elementit --
FeatureType
ATRIBUTE
ZonëAreodromi
Shumëllojshmëria: [1..*]
-- Emri --
Zonë aerodromi
-- Përkufizimi --
Një zonë e përcaktuar mbi tokë ose ujë (përfshi ndërtesa, instalime dhe pajisje), e cila synon të përdoret ose plotësisht ose pjesërisht për mbërritjen, nisjen dhe lëvizjen sipërfaqësore të aeroplanëve/helikopterëve.
-- Përshkrimi --
Një objekt zone gjeohapësinore, i cili përdoret për të përfaqësuar kufijtë fizikë të të gjitha pajisjeve që përbëjnë një aerodrom në brendësi të tokës.
[ I detyrueshëm: PO]
LinjëHekurudhore
Shumëllojshmëria: [1..*]
-- Emri --
Linjë hekurudhore
-- Përkufizimi --
Një koleksion përkimesh të lidhjes hekurudhore dhe/ose lidhjeve individuale hekurudhore që karakterizohen nga një ose më shumë identifikues tematikë dhe/ose karakteristika.
-- Përshkrimi --
Shembull. Linja hekurudhore të karakterizuara nga një kod specifik identifikimi dhe që përdoret nga kompani hekurudhore ose hekurudha për turistë, identifikuar nga një emër specifik.
[ I detyrueshëm: PO]
SipërfaqjaHekurudhore
Shumëllojshmëria: [1..*]
-- Emri --
Sipërfaqja hekurudhore
-- Përkufizimi --
Sipërfaqe e zënë nga një shinë(binar) hekurudhe, përfshirë balastin.
[ I detyrueshëm: PO]
ZonaEPortit
Shumëllojshmëria: [1..*]
-- Emri --
Zona e portit
-- Përkufizimi --
Një objekt gjeohapësinor (sipërfaqe), i cili përdoret për të përfaqësuar kufijtë fizikë të të gjitha objekteve që përbëjnë zonën tokësore të një deti apo porti në brendësi të tokës.
[ I detyrueshëm: PO]
LidhjaETransportitKabllor
Shumëllojshmëria: [1..*]
-- Emri --
Lidhja e transportit kabllor
-- Përkufizimi --
Një objekt linear gjeohapësinor që përshkruan gjeometrinë dhe lidhjen e një rrjeti kabllor mes dy pikash në rrjet të transportit kabllor.
-- Përshkrimi --
Transporti kabllor është një formë transporti bazuar në një kabllo të varur normalisht nga një grup konstruksionesh metalike të njëpasnjëshme.
[ I detyrueshëm: PO]
SipërfaqjaRrugore
Shumëllojshmëria: [1..*]
-- Emri --
Sipërfaqja rrugore
-- Përkufizimi --
Sipërfaqja ndërtimore e rrugës e cila përfshin karrexhatën dhe pjesë të tjera të saj.
[ I detyrueshëm: PO]
ZonaEShërbimitRrugor
Shumëllojshmëria: [1..*]
-- Emri --
Zonë shërbimi rrugor
-- Përkufizimi --
Zonë shtesë e trupit të rrugës e destinuar për të ofruar shërbime të caktuara.
-- Përshkrimi --
Shembull. Pikë karburanti, zonë pushimi, zonë tarifimi.
[ I detyrueshëm: PO]
3.3.2.5 HIDROGRAFIA
-- Emri --
Hidrografia
-- Përkufizimi --
Hidrografia në kontekstin e specifikimit të të dhënave përfshin përshkrimet mbi: detet, liqenet, lumenjtë, ujërat etj.
-- Tipi i elementit --
FeatureType
ATRIBUTE
ObjekteTëNdërtuaraNgaNjeriu
Shumëllojshmëria: [1..*]
-- Emri --
Objekte të ndërtuara nga njeriu
-- Përkufizimi --
Një objekt artificial që shtrihet në brendësi të trupit ujor dhe ka një nga llojet e funksionit, si më poshtë:
- Mban ujë;
- Rregullon sasinë e ujit;
- Ndryshon rrjedhjen e ujit;
- Lejon kryqëzimin e rrjedhjes ujore.
[ I detyrueshëm: PO]
PellgUjëmbajtës
Shumëllojshmëria: [1..*]
-- Emri --
Pellg ujëmbajtës
-- Përkufizimi --
Një trup ujor që është i rrethuar plotësisht nga toka.
-- Përshkrimi --
Kjo mund të ndodhë, në një deformim natyror të terrenit në të cilin mblidhet uji, ose mund të bllokohet nga një digë, apo i formuar në shtratin e tij nga rrënimi i tokës ose i formuar nga bllokimi dhe/ose digat natyrore. Ajo mund të jetë e lidhur me hyrjen/rrjedhën ujore ose me ujëra të tjera jo të rrjedhshëm.
[ I detyrueshëm: PO]
RrjedhaUjore
Shumëllojshmëria: [1..*]
-- Emri --
Rrjedha ujore
-- Përkufizimi --
Rrjedha ujore mund të jetë; natyrore, artificiale ose lumë.
-- Përshkrimi --
Mund të përfshijë edhe ishuj, të përfaqësuara si ’vrima’ në gjeometrinë e saj. Ishujt mundet të jenë të rrethuar nga një breg dhe/ose kufi toke.
Shembull. Liqen, pellg, rezervuar, lumë, etj.
[ I detyrueshëm: PO]
3.3.2.6 MODELI DIGJITAL I TERRENIT
-- Emri --
Modeli digjital i terrenit (DTM)
-- Përkufizimi --
Sipërfaqja që përshkruan formën tri dimensionale të sipërfaqes së zhveshur të tokës duke përjashtuar, aq sa është e mundur, çdo tipar tjetër të vendosur mbi të.
-- Përshkrimi --
Shembull. Ndërtesat, urat ose bimësia nuk formojnë pjesë të një DTM-je.
Shënim1: Për sipërfaqet DTM që përshkruajnë shtratin e trupave ujorë (p.sh. shtrati i detit) dhe karakteristika të vendosura mbi to, trupat ujorë nuk konsiderohen si pjesë të sipërfaqes së zhveshur të tokës, si rrjedhojë, ato përjashtohen nga DTM-ja.
Shënim 2. Për sipërfaqet DTM ku çdo karakteristikë, në sipërfaqen e zhveshur të tokës, nuk është filtruar dhe përjashtuar plotësisht, devijimet duhet të shpjegohen në metadata.
-- Tipi i elementit --
FeatureType
ATRIBUTE
Izoipse
Shumëllojshmëria: [1..*]
-- Emri --
Izoipse
-- Përkufizimi --
Vija që bashkojnë pika me kuotë të njëjtë.
-- Përshkrim --
Shënim1. Në rastin e izoipseve, kur atributi PoshtëDjathtas është ’i vërtetë’ kjo tregon se gjatësia e sipërfaqes është më e ulët në krahun e djathtë të vijës.
Shënim 2. Në rastin e izoipseve të thellësisë, kur atributi PoshtëDjathtas është ’i vërtetë’ kjo tregon se thellësia e sipërfaqes është më e ulët në krahun e djathtë të vijës.
[ I detyrueshëm: PO]
RrjetiIMbulimitTëTëDhënaveTëLartësive
Shumëllojshmëria: [1..*]
-- Emri --
Rrjeti i mbulimit të të dhënave të lartësive
-- Përkufizimi --
Mbulim i vazhdueshëm që përdor një mozaik sistematik bazuar në një rrjet të rregullt të rektifikuar katërkëndëshash për të mbuluar domein-in e tij, ku vlera e karakteristikës së lartësisë zakonisht njihet për secilën prej pikave të rrjetit që formojnë këtë domein.
-- Përshkrimi --
Burimi është adaptuar nga [SSH EN ISO 19123:2007].
[ I detyrueshëm: PO]
3.3.2.7 MBULESA E TOKËS
-- Emri --
Mbulesa e tokës
-- Përkufizimi --
Mbulesa e tokës përbën mbulimin fizik dhe biologjik të sipërfaqes së tokës, duke përfshirë sipërfaqet artificiale, sipërfaqet bujqësore, pyjet, zonat natyrore, ujërat.
-- Tipi i elementit --
FeatureType
ATRIBUTE
NjësiaEMbulesësSëTokës
Shumëllojshmëria: [1..*]
-- Emri --
Njësia e mbulesës së tokës
-- Përkufizimi --
Një element individual i grupit të të dhënave të mbulesës së tokës i përfaqësuar nga një pikë ose poligon.
-- Përshkrimi --
Çdo njësi mbështet informacionin e mbulesës së tokës.
[ I detyrueshëm: PO]
3.3.2.8 NDËRTESAT
-- Emri --
Ndërtesat
-- Përkufizimi --
Një ndërtesë është një konstruksion i mbyllur mbi dhe/ose nëntokë, i përdorur ose destinuar për strehimin e njerëzve, kafshëve, sendeve ose për prodhimin e mallrave ekonomike.
-- Tipi i elementit --
FeatureType
ATRIBUTE
Ndërtesat
Shumëllojshmëria: [1..*]
-- Emri --
Ndërtesat
-- Përkufizimi --
Një ndërtesë është një konstruksion i mbyllur mbi dhe/ose nëntokë, i përdorur ose destinuar për strehimin e njerëzve, kafshëve, sendeve ose për prodhimin e mallrave ekonomike.
[ I detyrueshëm: PO]
PjesëNdërtese
Shumëllojshmëria: [1..*]
-- Emri --
Pjesë ndërtese
-- Përkufizimi --
Pjesë ndërtese quhet një nënndarje e ndërtesës e cila mund të konsiderohet si ndërtesë më vete.
-- Përshkrimi --
Shënim 1. Një pjesë ndërtese është homogjene lidhur me aspektin fizik, funksional dhe kohor.
Shënim 2. Ndërtesë dhe PjesëNdërtese ndajnë të njëjtat grupe të dhënash. Një ndërtesë mund të jetë e përbërë nga pjesë ndërtese me lartësi të ndryshme mbi tokë.
[ I detyrueshëm: PO]
3.3.2.9 ELEMENTET E TJERA
-- Emri --
Elementet e tjera
-- Përkufizimi --
Elementet e tjera, janë elemente të shtuara nga autoriteti përgjegjës (ASIG), të identifikuara si të domosdoshëm, për plotësimin e paraqitjes së hartës me të dhënat gjeohapësinore bazë.
-- Tipi i elementit --
FeatureType
ATRIBUTE
NdërtimeReligjioze
Shumëllojshmëria: [1..*]
-- Emri --
Ndërtime Religjioze
-- Përkufizimi --
Objekte dhe ndërtime të cilat kanë si funksion apo qëllim shërbimet religjioze si: kisha, xhami, sinagoga etj.
[ I detyrueshëm: PO]
PikatERrjeteveGjeodezike
Shumëllojshmëria: [1..*]
-- Emri --
Pikat e rrjeteve gjeodezike
-- Përkufizimi --
Pikat e bazamentit të Kornizës Referuese Gjeodezike të Republikës së Shqipërisë.
[ I detyrueshëm: PO]
ElementeTopografikë
Shumëllojshmëria: [1..*]
-- Emri --
Elemente topografikë
-- Përkufizimi --
Elemente topografikë të identifikuar në dy gjeometri:
1-Pikë: ku mund të përmendim elemente topografike që kanë në përmbajtjen e tyre simbologjinë shpellë, shkëmb, humnerë dhe karst.
2-Lineare: ku mund të përmendim elemente topografike lineare që kanë në përmbajtjen e tyre simbologjinë e rrëzimeve deri 2m, rrëzimeve mbi 2m, rrëpirë shkëmbore, rrëshqitje dhe kreshtë.
[ I detyrueshëm: PO]
ElementTransportiTëTjerë
Shumëllojshmëria: [1..*]
-- Emri --
Elemente të tjerë transporti
-- Përkufizimi --
Elemente transporti të identifikuar në dy gjeometri:
1-Linear: elementet e transportit që kanë në përmbajtjen e tyre simbologjinë urë, urë e ngritshme, pasarelë, mbikalim, nënkalim, barrierë gjatë trasesë, platformë për ngarkim, platformë, tunel, trotuar, bankinë.
2-Sipërfaqe: Elemente transporti që kanë në përmbajtjen e tyre simbologjinë mbikalim këmbësorësh, nënkalim këmbësorësh, shesh, shkallë.
[ I detyrueshëm: PO]
ElementLinearKufizues
Shumëllojshmëria: [1..*]
-- Emri --
Elemente lineare kufizues
-- Përkufizimi --
Elemente lineare që kanë në përmbajtjen e tyre simbologjinë gardh, mur, gardh natyror, varg pemësh gjetherënëse, varg pemësh konifere, rrethim varrezash, mur historik etj.
[ I detyrueshëm: PO]
ElementTëNdërtesaveTëTjerë
Shumëllojshmëria: [1..*]
-- Emri --
Elemente të tjerë të ndërtesave
-- Përkufizimi --
Elemente lineare që kanë në përmbajtjen e tyre simbologjinë ndërtesa në ndërtim, rrënoja, konstruksione të çmontueshme etj.
[ I detyrueshëm: PO]
3.4 METADATA
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.5 KODI EPSG PËR KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare (KRGJSH), miratuar me vendimin nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë” ndryshuar me vendimin nr. 322, datë 27.4.2016, dhe vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është: EPSG - 6870.
3.6 CILËSIA E TË DHËNAVE
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur, për të vlerësuar dhe dokumentuar cilësinë për grupet e të dhënave gjeohapësinore të temës “Imazhi i hartës bazë”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- Vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku pronat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit.
- Vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore.
- Për të specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore që lidhen me temën “Imazhi i hartës bazë”.
Tabela e mëposhtme, paraqet të gjithë elementet dhe nënelementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, datasetit ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën “Sfera e vlerësimit”.
Masat që do të përdoren për secilin nga nënelementet e listuar të cilësisë së të dhënave janë përcaktuar në nënseksionet e mëposhtme.
Tabela - Elementet e cilësisë së të dhënave të përdorura në temën: “Imazhi i hartës bazë”
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
3.6.1
Kompletimi
Autorizimi
Të dhëna të tepërta të pranishme në grupin e të dhënave, sikurse përshkruhet nga fushëveprimi.
Koleksion të dhënash,
grupet e të dhënave,
llojet e objektit gjeohapësinor
3.6.2
Kompletimi
Përjashtimi
Të dhënat që mungojnë nga grupi i të dhënave, sikurse përshkruhet nga fushëveprimi.
Koleksion të dhënash, Grupet e të dhënave, Llojet e objektit gjeohapësinor, Objekti gjeohapësinor
3.63
Përputhja ligjore
Përputhja konceptuale
Zbatimi i rregullave të skemës konceptuale.
Grupet e të dhënave
3.6.4
Përputhja ligjore
Përputhja në domein
Zbatimi i vlerave, në vlerat e domein-it.
Grupet e të dhënave
3.6.5
Përputhja ligjore
Përputhja e formatit
Shkalla në të cilën ruhen të dhënat në përputhje me strukturën fizike të grupit të të dhënave, sikurse përshkruhet nga fushëveprimi.
Grupet e të dhënave
3.6.6
Përputhja ligjore
Përputhja topologjike
Korrektësia e topologjisë së koduar në mënyrë të qartë, karakteristikat e grupeve të të dhënave, sikurse përshkruhet nga fushëveprimi
Objekti gjeohapësinor
3.6.7
Saktësia pozicionale
Saktësia absolute ose e jashtme.
Afërsia e vlerave të koordinatës së raportuar, për vlerat e vërteta ose vlerat e pranuara si të tilla.
Objekti gjeohapësinor
3.6.8
Saktësia tematike
Korrektësia e klasifikimit
Karakteristikat e krahasimit të klasave të caktuara ose atributet e tyre në një univers ligjërimi.
Objekti gjeohapësinor
3.6.9
Saktësia tematike
Korrektësia e atributeve jo sasiore
Korrektësia e atributeve jo sasiore
Objekti gjeohapësinor
3.6.1 KOMPLETIMI - KOMISIONI (COMPLETENESS - COMMISSION)
Rekomandim.
Komisioni duhet të vlerësohet dhe dokumentohet duke përdorur normën e artikujve të tepërt sikurse specifikohet në tabelën e mëposhtme:
Emri
Norma e artikujve të tepërt
Cilësia e të dhënave të elementeve
Kompletimi.
Cilësia e të dhënave të nënelementeve
Autorizimi.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë E Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjera).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (përqindja).
Kriteret e vlerësimit të cilësisë së të dhënave
Krahasohet çdo feature i grupit të të dhënave, me të dhëna referuese për të llogaritur shkallën e gabimit (%).
- Në rast se një feature nuk korrespondon në hartën bazë, duhet të ketë një gabim.
- Shkalla e gabimit (%) = Numri i tepërt/numri total i rasteve * 100.
3.6.2 KOMPLETIMI - PËRJASHTIMI (COMPLETENESS - OMISSION)
Rekomandim.
Përjashtimi mund të vlerësohet dhe dokumentohet duke përdorur normën e artikujve të munguar sikurse specifikohet në tabelën e mëposhtme.
Emri
Norma e artikujve të tepërt
Cilësia e të dhënave të elementeve
Kompletimi.
Cilësia e të dhënave të nënelementeve
Përjashtimi.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjera).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (përqindja).
Kriteret e vlerësimit të cilësisë së të dhënave
Krahasoni çdo feature të grupit të të dhënave, me të dhëna referuese për të llogaritur shkallën e gabimit (%):
- Në rast se, një feature nuk korrespondon në hartën bazë, duhet të ketë një gabim.
- Shkalla e gabimit (%) = Numri i tepërt/numri total i rasteve * 100.
3.6.3 PËRPUTHJA LIGJORE - PËRPUTHJA KONCEPTUALE (LOGICAL CONSISTENCY - CONCEPTUAL CONSISTENCY)
Rekomandim.
Për testet në përputhje konceptuale, është e rekomanduar të përdoret Përputhja ligjore - Përputhja konceptuale e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me rregullat e skemës konceptuale sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i artikujve që nuk janë në përputhje me rregullat e skemës konceptuale (Vlefshmëria e modelit të të dhënave)
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja konceptuale.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative)+;
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjera/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Krahaso gjithë bazën e të dhënave me diagramin UML që përcakton strukturën e modelit të të dhënave dhe tregon çdo lloj parregullsie të UML:
- Çdo lloj parregullsie në UML duhet të jetë gabim.
Shkalla e gabimit = Numri i gabimeve.
Emri
Numri i mbivendosjeve të pavlefshme të sipërfaqeve (mbivendosjet e pavlefshme)
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja konceptuale.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Nuk përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjera/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Aplikimi varet nga përcaktimi i sipërfaqeve që mund të mbivendosen ose jo. Por jo të gjitha sipërfaqet që mund të mbivendosen janë domosdoshmërisht të gabuara.
Kur kryhet matja e cilësisë së të dhënave, llojet e feature-ave të klasave që korrespondojnë me sipërfaqet e mbivendosura të paligjshme duhet të raportohen me hollësi.
HID:
- Digë nuk duhet të mbivendoset mes tyre dhe me, Rreke ose Ujëvarë;
- SipërfaqeUjore nuk duhet të mbivendoset mes tyre dhe me RrjedhaUjore;
- Ligatinat nuk duhet të mbivendosen midis tyre dhe me RrjedhaUjore, SipërfaqeUjore;
- RrjedhaUjore nuk duhet të mbivendoset ndërmjet tyre dhe me Detin e Adriatikut.
MT:
- Të gjitha njësitë e mbulimit të tokës nuk duhet të mbivendosen mes tyre;
- Të gjitha njësitë e mbulimit të tokës duhet të mbulojnë të gjithë masën pa lënë hapësira.
3.6.4 PËRPUTHJA LIGJORE - PËRPUTHJA ME DOMEIN-IN (LOGICAL CONSISTENCY - DOMAIN CONSISTENCY)
Rekomandim.
Për testet në përputhje me domein-in, është e rekomanduar të përdoret Përputhja ligjore - Përputhja në domein e nënelementeve të cilësisë së të dhënave dhe masa e numrit të artikujve që nuk janë në përputhje me vlerën e domein-it sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i artikujve që nuk janë në përputhje me vlerën e domein-it
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja në domein.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjera/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Numërimi i të gjithë elementeve në grupin e të dhënave që nuk janë në përputhje me domein-in e vlerave të tyre.
3.6.5 PËRPUTHJA LIGJORE - PËRPUTHJA ME FORMATIN (LOGICAL CONSISTENCY - FORMAT CONSISTENCY)
Rekomandim.
Përputhja me formatin duhet të vlerësohet dhe dokumentohet duke përdorur shkallën e konfliktit të strukturës fizike sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i të dhënave me formate të pavlefshme
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nënelementeve
Përputhja me formatin
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Të dhënat mund të ekspozohen nga një format të dhënash bazë, pa shfaqur asnjë gabim në ekspozim.
3.6.6 PËRPUTHJA LIGJORE - PËRPUTHJA TOPOLOGJIKE (LOGICAL CONSISTENCY - TOPOLOGICAL CONSISTENCY)
Rekomandim.
Përputhja topologjike duhet të vlerësohet dhe dokumentohet duke përdorur numrin e lidhjeve të munguara për shkak të nënshkrimit, numrin e lidhjeve të munguara për shkak të mbivendosjeve, numrin e gabimeve të vetëvendosjes së pavlefshme sikurse është specifikuar në tabelën e mëposhtme:
Emri
Numri i lidhjeve të gabuara pikë-kurbë (konsistenca e nyjës së harkut)
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja topologjike.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Nuk përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Ekziston një lidhje pikë kurbash ku përfshihen kurba të ndryshme. Këto kurba kanë një marrëdhënie të brendshme topologjike që do të reflektojë paraqitjen e vërtetë.
Emri
Numri i lidhjeve që mungojnë për shkak të nënndarjeve (nënndarjeve)
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja topologjike.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Mungesa masive e lidhjeve ndikon në Tolerancën e Lidhshmërisë, duke i konsideruar ato si gabime, gjithnjë nëse feature reale janë të lidhura në rrjetin hidrografik.
Emri
Numri i lidhjeve që mungojnë për shkak të mbivendosjeve
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja topologjike.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Numërimi i artikujve në grupin e të dhënave që nuk përputhen për shkak të mbivendosjes, duke pasur parasysh tolerancën e lidhjes së parametrave.
Tolerancë: Njësia minimale e regjistrimit të të dhënave = 1mm.
Emri
Numri i gabimeve të paligjshme që vetë kryqëzohen
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja topologjike.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (numër).
Kriteret e vlerësimit të cilësisë së të dhënave
Numërimi i elementeve të të dhënave, që vetë kryqëzohen në mënyrë të paligjshme.
Emri
Numri i gabimeve të vetë mbivendosjes së pavlefshme (Mbivendosjet e vetes)
Cilësia e të dhënave të elementeve
Përputhja ligjore.
Cilësia e të dhënave të nënelementeve
Përputhja topologjike.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
N/A
Kriteret e vlerësimit të cilësisë së të dhënave
Numërimi i elementeve të të dhënave, që vetë-mbivendosen në mënyrë të paligjshme.
3.6.7 SAKTËSIA POZICIONALE - SAKTËSIA ABSOLUTE (POSITIONAL ACCURANCY - ABSOLUTE ACCURACY)
Rekomandim.
Saktësia absolute ose pozicionale duhet të vlerësohet dhe dokumentohet duke përdorur vlerën mesatare të pasigurive pozicionale, shkallën e gabimeve pozicionale, mbi një prag të caktuar, sikurse është specifikuar në tabelën e mëposhtme:
Emri
Gabimi mesatar kuadratik në planimetri (RMSEP)
Cilësia e të dhënave të elementeve
Saktësia pozicionale.
Cilësia e të dhënave të nënelementeve
Saktësia absolute.
Cilësia e të dhënave trajtohet për:
Nuk përfshihet: EGJ (Emërtimet Gjeografike);
Nuk përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Nuk përfshihet: ZM (Zonat e Mbrojtura);
Nuk përfshihet: MDT (Modeli Digjital i Terrenit);
Nuk përfshihet: MT (Mbulesa e Tokës);
Nuk përfshihet: ND (Ndërtesa);
Nuk përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Vlera.
Kriteret e vlerësimit të cilësisë së të dhënave
Gabimi Mesatar Kuadratik (GMK = RMSE në anglisht) - Është rrënja katrore e mesatares së ndryshimeve në katror ndërmjet vlerave të koordinatave të një grupi të dhënash të matura dhe vlerave të koordinatave nga një burim i pavarur i saktësisë më të lartë për pikat identike. GMK dallon dy raste:
Rasti 1 - Kur llogariten gabimet e mundshme vi
Ku:
vi - gabimi i mundshëm që llogaritet si diferencë e vlerës përfaqësuese me vlerën e matur;
- Vlera përfaqësuese që merret si vlera mesatare e vlerave të matura xi;
n - Numri i matjeve;
Saktësia pozicionale e përcaktuar nga të dhënat e kontrolluara:
Saktësia Horizontale
ku:
janë koordinatat horizontale të pikave të kontrolluara në grupin e të dhënave;
- janë koordinatat e pikave të kontrolluara nga burime të pavarura të një saktësie më të lartë;
- është numri i pikave të testuara;
- është numri përkatës i pikës.
Gabimi horizontal i pikës përcaktohet nga:
Nëse nga llogaritjet kemi ,
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale dhe të pavarura në secilin komponent (x, z) një koeficient (faktor) 2.4477 përdoret për të llogaritur saktësinë horizontale me nivel besimi 95% (Greenwalt and Schultz 1968). Kur zbatohen kushtet e mësipërme,, vlera e saktësisë horizontale referuar NSSDA duhet të llogaritet nga formula:
Saktësia Vertikale
ku:
janë koordina vertikale e pikave të kontrolluara në grupin e të dhënave;
- janë koordinatat vertikale të pikave të kontrolluara nga burime të pa varura të një saktësie më të lartë;
- është numri i pikave të testuara;
- është numri përkatës i pikës.
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale, një koeficient (faktor) 1.9600 përdoret për të llogaritur saktësinë vertikale me nivel besimi 95% (Greenwalt and Schultz 1968). Nga kjo, saktësia vertikale, e raportuar sipas NSSDA-së duhet të llogaritet nga formula:
3.6.8 SAKTËSIA TEMATIKE - KORREKTËSIA E KLASIFIKIMIT (THEMATIC ACCURANCY - CLASSIFICATION CORRECTENESS)
Rekomandim.
Korrektësia e klasifikimit duhet të vlerësohet dhe dokumentohet duke përdorur shkallën e klasifikimit të gabuar, sikurse është specifikuar në tabelën e mëposhtme:
Emri
Shkalla e klasifikimit të gabuar
Cilësia e të dhënave të elementeve
Saktësia tematike.
Cilësia e të dhënave të nënelementeve
Korrektësia e klasifikimit.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (përqindja).
Kriteret e vlerësimit të cilësisë së të dhënave
Krahasohen manualisht të gjitha feature-at e dukshme në zonë, duke iu referuar ortofotos.
3.6.9 SAKTËSIA TEMATIKE - KORREKTËSIA E ATRIBUTEVE JO SASIORE (THEMATIC ACCURANCY - NONQUANTITATIVE ATTRIBUTE CORRECTENESS)
Rekomandim.
Korrektësia e atributeve jo sasiore duhet të vlerësohet dhe dokumentohet duke përdorur shkallën e atributeve të sakta, sikurse është specifikuar në tabelën e mëposhtme:
Emri
Vlerat e shkallës së atributeve të sakta
Cilësia e të dhënave të elementeve
Saktësia tematike.
Cilësia e të dhënave të nënelementeve
Korrektësia e atributeve josasiore.
Cilësia e të dhënave trajtohet për:
Përfshihet: EGJ (Emërtimet Gjeografike);
Përfshihet: KNJA (Kufijtë e Njësive Administrative);
Përfshihet: RRT (Rrjetet e Transportit);
Përfshihet: HID (Hidrografia);
Përfshihet: ZM (Zonat e Mbrojtura);
Përfshihet: MDT (Modeli Digjital i Terrenit);
Përfshihet: MT (Mbulesa e Tokës);
Përfshihet: ND (Ndërtesa);
Përfshihet: ET (Elementet e Tjerë/ASIG).
Cilësia e të dhënave të llojeve të vlerave
Shkalla e gabimit (përqindja).
Kriteret e vlerësimit të cilësisë së të dhënave
Krahasohen manualisht të gjitha feature-at e dukshme në zonë, duke iu referuar ortofotos.
4. ANEKSE
4.1 ANEKSI A - KATALOGU I TIPOLOGJISË
Nr
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
Imazhi i hartës bazë
3.2.2.1
BasemapCoverage
HartaBazëMbulim
HartaBazëMbulim
FeatureType
3.2.2.2
ResponsibleAuthority
AutoritetetPërgjegjës
HartaBazëMbulim
DataType
3.2.2.3
MathematicParametersOfTheMap
ElementetMatematikorëTëHartës
HartaBazëMbulim
DataType
3.2.2.4
Nomenclature
Nomenklatura
HartaBazëMbulim
DataType
3.2.2.5
YearOfCreation/Updating
VitiIKrijimit/Përditësimit
HartaBazëMbulim
DataType
3.2.2.6
TechnologyTypeValue
VleratELlojitTëteknologjisë
HartaBazëMbulim
Kodlistë
3.3.2.1
BasemapVector
HartaBazëVektor
HartaBazëVektor
FeatureType
3.3.2.2
OtherElements
ElementetETjera
HartaBazëVektor
FeatureType
3.3.2.3
GeographicalNames
NamedPlace
EmërtimetGjeografike
EmërtimiIVendit
HartaBazëVektor
FeatureType
3.3.2.4
Hydrography
ManMadeObject
Standingwater
Watercourse
Hidrografia ObjekteTëNdërtuaraNgaNjeriu
PellgUjëmbajtës
RrjedhaUjore
HartaBazëVektor
FeatureType
3.3.2.5
Administrative Units
AdministrativeBoundary
MaritimeBoundary
KufijtëENjësiveadministrative
KufijtëAdministrativë
KufijtëDetarë
HartaBazëVektor
FeatureType
3.3.2.6
LandCover
LandCoverUnit
MbulesaEoTkës
NjësiaEMbulesësSëTokës
HartaBazëVektor
FeatureType
3.3.2.7
Digital Terrain Model
CounturLine
ElevationGridCoverage
ModeliDixhitalITerrenit
Izoipse
RrjetiIMbulimitTëTëDhënaveTëLartësive
HartaBazëVektor
FeatureType
3.3.2.8
Buildings
Building
BuildingPart
Ndërtesat
Ndërtesa PjesëNdërtese
HartaBazëVektor
FeatureType
3.3.2.9
TransportNetworks
AerodromeArea
RailwayLine
RailwayArea
PortArea
CablewayLink
RoadArea
RoadServiceArea
RrjetetETransportit
ZonëAreodromi
LinjëHekurudhore
SipërfaqjaHekurudhore
ZonaEPortit
LidhjaETransportitKabllor
SipërfaqjaRrugore
ZonaEShërbimitRrugor
HartaBazëVektor
FeatureType
4.2 ANEKSI B - KODLISTAT
4.2.1 SKEMA E APLIKIMIT HARTA BAZË MBULIM
Kodlistat
VleratELlojitTëTeknologjisë
4.2.1.1 VLERAT E LLOJIT TË TEKNOLOGJISË
-- Emri --
Vlerat e llojit të teknologjisë
-- Përkufizimi --
Teknologjia e përdorur për krijimin e hartës bazë.
-- Vlerat -
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse ndonjëra prej tyre mund të përdoret.
Kodlistë
-- Emri --
Fotogrametri/Remote Sensing
-- Përkufizimi --
Metoda e matjes së të dhënave me anë të procesit të fotografimit ajror.
-- Emri --
Gjeneralizimi
-- Përkufizimi --
Metoda e matjes së të dhënave me anë të procesit të gjeneralizimit.
-- Emri --
Kombinuar
-- Përkufizimi --
Kombinimi i disa metodave teknologjike (p.sh. kombinimi i metodës së fotogrametrisë dhe rilevimit).
-- Emri --
Takiometri/Rilevimi
-- Përkufizimi --
Metoda me rilevim e marrjes së të dhënave në terren.
-- Emri --
Tjera
-- Përkufizimi --
Llojet të tjera të teknologjisë së përdorur.
4.3 ANEKSI C - SIMBOLOGJIA E HARTËS BAZË
Një ndër aspektet kryesore të paraqitjes vizive të hartës bazë është krijimi dhe ndërtimi i një modeli klasifikimi të simbologjisë së elementeve hartografik. Për këtë arsye ASIG, si autoritet publik përgjegjës për temën “Imazhi i hartës bazë”, harton manualin “Katalogu i simbologjisë së shkallës 1:2000”. Ky manual përcakton rregullat dhe mënyrën e përdorimit të simboleve, teksteve dhe klasifikimin e ngjyrave në hartën bazë. Manuali hartohet dhe publikohet në faqen zyrtare të ASIG, brenda 3 muajve nga miratimi i këtij dokumenti.
