# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI-TEMA: DETET
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Detet
3.1.1 Parathënie
3.1.2 Terma dhe përkufizime
3.1.3 Skemat e aplikimit dhe diagramet UML për temën: “Detet”
3.1.4 Katalogu i tipologjisë
3.1.4.1 Zonë detare
3.1.4.2 Deti
3.1.4.3 Zona e qarkullimit detar
3.1.4.4 Zona ndërbaticore
3.1.4.5 Shtrirje detare
3.1.4.6 Vlerat e parametrave
3.1.4.7 Bregdeti/ tokë e lagur
3.1.4.8 Vija bregdetare
3.1.4.9 Segmenti bregdetar
3.1.4.10 Shtresa detare
3.1.4.11 Zonë e sipërfaqes detare
3.1.4.12 Sipërfaqja e tabanit të detit
3.1.4.13 Izolinjë detare
3.1.4.14 Konturi detar
3.1.4.15 Vlerat e klasifikimit të zonave detare
3.1.4.16 Vlerat e mbulesës së tabanit të detit
3.1.4.17 Vlerat e klasifikimit të sipërfaqes së detit
3.1.4.18 Vlerat e qëndrueshmërisë së bregdetit
3.1.4.19 Vlerat e klasifikimit të llojit të bregdetit
3.1.4.20 Vlerat e llojeve të zonave
3.2 Metadatat
3.3 Kodi EPSG për KRGJSH-në
3.4 Cilësia e të dhënave
3.4.1 Elementet e cilësisë së të dhënave
3.4.2 Përputhja logjike - përputhja konceptuale (Logical consistency - Conceptual consistency)
3.4.3 Përputhja logjike - përputhja me domeinin (Logical consistency - Domain consistency)
3.4.4 Saktësia e pozicionimit - saktësia absolute ose e jashtme (Positional accuracy - Absolute or extrenal accuracy)
3.4.5 Përdorimi (Usability)
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
4.2 Aneksi B - Kodlistat
4.2.1 Vlerat e klasifikimit të zonave detare
4.2.2 Vlerat e mbulesës së tabanit të detit
4.2.3 Vlerat e klasifikimit të sipërfaqes së detit
4.2.4 Vlera e qëndrueshmërisë së bregdetit
4.2.5 Vlerat e klasifikimit të llojeve të bregdetit
4.2.6 Vlerat e llojeve të zonave
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG) në bashkëpunim me Shërbimin Hidrografik Shqiptar (Komanda e Forcave Detare). Data e publikimit të versionit nr. 1 është Korrik 2018. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2018_ DT_v.1 ku:
ASIG - autoriteti përgjegjës për krijimin e standardit
Standard - lloji i dokumentit
NSDI - qëllimi i dokumentit
201 - viti i krijimit
DT - tema për të cilën është krijuar standardi: “Detet”, e cila i referohet temës “Sea Regions” në direktivën INSPIRE
v.1 - numri i versionit të standardit
2. HYRJE
2.1 Qëllimi
Ky dokument përcakton specifikimet teknike të harmonizuara konform direktivës INSPIRE për të dhënat gjeohapësinore të temës “Detet”, temë e cila është përcaktuar në nenin 11, pika 2/u, të ligjit nr. 72/2012 “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse për mbledhjen përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë e tyre.
2.2 SI LEXOHET DOKUMENTI
2.2.1 STRUKTURA E DOKUMENTIT
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë.
3. Tema: në këtë pjesë jepen specifikimet teknike për secilën temë.
4. Anekse: në këtë pjesë jepen informacione shtesë shpjeguese në ndihmë të lexuesve.
- Përmbajtja e kapitullit III është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - këtu detajohen: Diagramet UML dhe Katalogu i tipologjive.
3.2 Metadata - këtu jepen specifikimet teknike për metadata-t e temës përkatëse.
3.3 Sistemi Koordinativ Referencë - këtu përcaktohet sistemi koordinativ referencë për të dhënat gjeohapësinore.
3.4 Cilësia e të dhënave - këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesor të specifikimeve dhe marrëdhëniet mes tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në “Katalogun e tipologjive” (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
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
Tipi i elementit mund të jetë i këtyre llojeve:
«featureType» - një element që mund të jetë real në terren apo një dukuri abstrakte
«dataType» - një element tabelor që shërben vetëm si tabelë atributesh për t’u lidhur me një element tjetër
«enumeration» “Kodlist» - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa Codelist nënkupton “listë vlerash ose ndryshe kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
«union» - një mbulesë topologjike e dy ose më shumë grupe të dhënash gjeohapësinore, që ruan tiparet që përfshihen brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse.
«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të dhëna të importuara”
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë ose poligon.
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
Rol shoqërimi
Në tabelën e lidhjeve “Rol shoqërimet” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh: PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh: Ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve
Vlera e dytë (etj.) e listës së gatshme, p.sh.: Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE i elementeve
2.2.3 KARAKTERISTIKAT E <<VOIDABLE>> DHE SHUMËLLOJSHMËRIA
Stereotipi <<voidable>> përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera ’void’. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E pa populluar”
Konfidenciale (Withheld).
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
Stereotipi <<voidable>> nuk jep asnjë informacion nëse ekziston një karakteristikë në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh. nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh. nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe /ose në hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, precipitimet, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh. vendndodhja e sensorëve), kurbat përcaktuese (p.sh. izolinjat), rrjetet (p.sh. ortoimazheria, modelet e lartësisë) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si vetitë e llojeve të objekteve gjeohapësinore ku lloji i vlerës së kësaj karakteristike është një realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh. ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptues të Përgjithshëm “ Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë. (shih figurën 1, majtas).
RrjetiIMbulimitReferencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlera të koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje mbulimi (ose një nëntip i tyre) në skemat e aplikimit në INSPIRE.
Figura 1 - Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 NUMËRTIMET DHE KODLISTAT (ENUMERATION AND CODELIST)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistën, ’vlera të tjera’ përcaktohet lloji i përmbajtjes së kodlistës, i përkufizuar specifikisht si më poshtë:
’jo’ përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument.
’të kufizuara’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave.
’të hapura’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave.
’po’ përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera jo të përmbajtura në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që dhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo është ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
Shënim i rëndësishëm:
Disa terma në Katalogun e tipologjive, si p.sh. FeatureType, DataType, Void, Coverages etj, nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të Direktivës INSPIRE.
2.3 DETYRIMET LIGJORE
Në bazë të nenit 16, të ligjit nr.72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet Evropiane (Direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore për krijimin e NSDI në Shqipëri janë përshtatur nga specifikimet teknike të temave përkatëse në Direktivën INSPIRE si dhe nga praktikat më të mira ndërkombëtare që mbështeten dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë këtë direktivë. (VKM nr. 1077, datë 23.12.2015)
Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 FUSHA E VEPRIMIT
Të gjithë autoritetet publike, kompanitë private apo individët që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor si më poshtë:
Figura 2: Proceset e ciklit jetësor
Planifikimi - është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
Vlerësimi - është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
Procesimi - është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
Shpërndarja - është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
Zbulimi - është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
Analiza - është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
Përditësimi - është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
Arkivimi - është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të pa aksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
Shkatërrimi - është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacionin në fuqi.
3. TEMA
3.1 DETET
3.1.1 PARATHËNIE
Tema “Detet” parashikon një kornizë të përgjithshme për përshkrimin e ndarjeve, nën-ndarjeve ose bashkimin e deteve sipas vetive fizike dhe kimike (për shembull; zonat detare sipas temperaturës mesatare, ose zonat me karakteristika të ngjashme të sedimenteve). Gjithashtu, kjo temë lejon konceptin e emërtimeve të deteve (p.sh., deti Adriatik), vijës bregdetare (p.sh., vija bregdetare shqiptare) si dhe përcaktimin e bregut/vijës bregdetare në gjendje të ndryshme të baticës.
Përkufizimi: Kushtet fizike dhe/ose kimike të deteve dhe trupave ujorë të kripur, të ndarë në rajone dhe nënrajone (zona detare) me karakteristika të përbashkëta.
Përshkrimi: Një zonë detare mund të përmbajë karakteristika që janë elemente të temave të tjera të gjeoinformacionit si për shembull batimetria (tema “Modeli dixhital i terrenit”) dhe linjat e transportit detar (tema “Rrjetet e transportit”). Një zonë detare mund të jetë një grup të dhënash vektoriale (jo të dhëna të mbulimit) që paraqet një gjeometri 2D të një zone që mbulohet nga një oqean, një det ose një trup ujor i kripur i ngjashëm. Kufijtë e kësaj zone marrin atribute të proceseve fizike ose kimike si për shembull:
- kripësia;
- qarkullimi aktual;
- kufijtë e masës tokësore;
- thellësia (shelfi detar, zonat ndërbaticore, humnerat);
- mbulesa e shtratit të detit (p.sh. rërë) ose e sipërfaqes (p.sh. akull).
Zonat detare kanë disa aspekte të përkohshme dhe variacione sezonale, të cilat ndryshojnë shtrirjen e zonës në varësi të rrymave detare (MHWS, MLWS, MHWN, MLWN).
Figura 3: Llojet dhe shtrirja e detit për nivele të ndryshme të baticës (përshtatur nga IHO H20)
Specifikimet e kësaj teme mund të bazohen në karakteristikat e përcaktuara nga Organizata Hidrografike Ndërkombëtare (IHO), në veçanti nga standardi i IHO S-57. Këto specifikime përdoren në përgjithësi nga shtetet anëtare të BE.
Shembuj nga tema “Detet”
Bazuar nga sa më lart, në vijim jepen disa shembuj të elementeve gjeografik të Zonave detare:
“Deti i Veriut” (d.m.th. çdo përdorim i zakonshëm me emrin det ose oqean)
Një trup ujor me një kufi të përcaktuar, bazuar në modelet e zakonshme të qarkullimit rreth tokës dhe detit.
“Qelizë sedimentare”
Një trup ujor ose zona përgjatë vijës bregdetare dhe në zonën e afërt, ku lëvizja e materialit është kryesisht e pavarur, zakonisht i përdorur për menaxhimin e erozionit bregdetar.
“Qelizë qarkullimi”
Një trup ujor, i cili është destinacioni për të gjithë ndotësit që hyjnë në trupin e ujit, zakonisht i përdorur për menaxhimin e cilësisë së ujit bregdetar, për shembull nga Direktiva e Strukturës Ujore.
“Sipërfaqja e tabanit të detit”
Çdo zonë e detit e karakterizuar nga mbulesa e tabanit të detit ose thellësia.
Çfarë nuk përfshihet në temën “Detet”
Në temën “Detet” nuk përfshihen:
Çdo lloj ndarje me kufij, të cilat nuk janë të bazuara në kushtet fizike ose kimike; p.sh Kuadratet Marsden të përdorura nga ICES.
Batimetria (thellësia e detit).
Tipologjitë Oqeanike (tema e INSPIRE Oqeanet) si “temperatura” ose “rrymat baticore” (por analiza e një tipologjie Oqeanike mund të përcaktojë një Zonë Detare, gjithashtu Elementet Gjeografike të Oqeanit mund të jenë karakteristika (atribute) të një Zone Detare).
Zonat administrative, për shembull Zona Ekonomike Ekskluzive.
Raste përdorimi të temës “Detet”
Rastet e mëposhtme shërbejnë për të na ndihmuar të kuptojmë qëllimin e standardit me temë “Detet”.
Rast përdorimi për përcaktimin e zonës
Ky rast i përdorimit të përgjithshëm ka për qëllim që një përdorues i thjeshtë të kuptojë nëse një zonë ose objekt ndodhet në mjedisin detar:
“Alberti punon për Agjencinë Evropiane të Mjedisit. Ai do të donte të kuptonte se cilat Zona të Mbrojtura janë të vendosura në mjedisin detar. Për ta bërë këtë ai dëshiron të shohë një hartë të thjeshtë të të gjithë zonave të mbrojtura të BE-së, të mbuluara nga shtrirja e zonave detare Evropiane. Nga një kërkesë shtesë në këtë analizë, ai do të donte të kuptonte se cilat nga këto Zona të mbrojtura janë zhytur plotësisht dhe ato që janë të mbuluara nga uji si pjesë e ciklit baticor.”
Rast përdorimi i përmbytjes
Menaxhimi i Rrezikut nga Përmbytjet u sugjerua si një rast përdorimi ndërtematik. Në këtë drejtim, TWG për detet marrin në konsideratë rolin e deteve në menaxhimin e rrezikut nga përmbytjet:
“Maria punon për ECWMF dhe po përgatit një vlerësim të rrezikut të Evropës për të përballuar stuhitë dhe ngjarjet bregdetare të përmbytjeve. Për të llogaritur rrezikun, ajo kërkon shkallën e nivelit më të lartë të mundshëm të ujit rreth vijës bregdetare evropiane.”
Rasti i përdorimit të Direktivës së Strukturës Ujore
Ky rast përdorimi është vendosur për të qartësuar nevojën e deteve në mbështetje të Direktivës së Strukturës Ujore. Gjithashtu mund të përdoret si një rast i përgjithshëm i përdorimit të monitorimit të ndotjes:
“Migel duhet të ndërtojë një model ujëmbledhësi që fillon në det dhe lidhet me rrjetet e lumenjve. Zona detare e përcaktuar për këtë qëllim shërben si një gropë që mbledh ujërat e rrjetit të lumenjve. Migel duhet të jetë në gjendje të shohë se në cilat dete bëhet shkarkimi i ujëmbledhësit dhe çfarë mekanizmash ka në vend, për të monitoruar cilësinë e ujit në këto dete.”
3.1.2 TERMA DHE PËRKUFIZIME
HAT - Niveli më i lartë astronomik i baticave (Highest Astronomical Tide)
ICES - Konventa Ndërkombëtare për Eksplorimin e Deteve (International Convention for Exploration of the Seas)
IHO - Organizata Ndërkombëtare e Hidrografisë (International Hydrographic Organization)
ISO - Organizata Ndërkombëtare e Standardizimit (International Organization for Standardization)
LAT - Niveli më i ulët astronomik i zbaticave (Lowest Astronomical Tide)
MHW - Niveli mesatarë i ujit (Mean High Water)
MHWS - Niveli mesatar i baticës më të lartë në pranverë (Mean High Water Spring)
MLWS - Niveli mesatar i zbaticës më të ulët në pranverë (Mean Low Water Spring)
MHWN - Niveli mesatar i baticës më të ulët (Mean High Water Neat)
MLWN - Niveli mesatar i zbaticës më të ulët (Mean Low Water Neat)
Shërbimi Hidrografik përdorë dy nivele të ndryshme si referencë për nivelin e detit
Max Tide (Niveli maksimal i baticave) - Niveli maksimal i baticave i vëzhguar
Min Tide (Niveli maksimal i zbaticave) - Niveli minimal i zbaticave i vëzhguar
Në mënyrë skematike paraqiten termat dhe elementet kryesorë të deteve
Figura 4: Elementet fizik të detit
(A) Bregdet
Një rrip toke me gjerësi të pacaktuar (deri në disa milje) që shtrihet nga bregu i brendshëm në drejtim të ndryshimit të parë të madh në karakteristikat e tokës që nuk janë të ndikuara nga proceset bregdetare.
(B) Plazh (Breg)
Zona e rërës së lirshme, zhavorrit dhe materialeve të tjera që shtrihen në tokë nga rrymat ujore të baticës deri në vijën bregdetare.
(C) Zona pranë bregut
Zona që shtrihet në drejtim të detit nga niveli i ujit në baticë përtej zonës së thyerjes. Kjo zonë është e pacaktuar dhe ndikohet nga rrymat e zonës pranë bregdetare.
(D) Det i hapur
Drejtimi drejt detit i zonës pranë bregut.
(E) Vijë e bregdetit
Vija që formon kufirin midis bregdetit (tokës) dhe plazhit (bregut). Ajo shënohet me fillimin e bimësisë së përhershme ose kur ka një ndryshim të dukshëm në morfologjinë (formën) e substratit ose formës së tokës, për shembull, nga një plazh relativisht i sheshtë në duna kodrinore.
(F) Bregdet/Tokë e lagur
Bregdet/Tokë e lagur (shoreline) - është një rrip toke i ndërmjetëm dhe në varësi të gjendjes së detit, mund të jetë i mbuluar nga uji ose jo, përkatësisht në baticë mbulohet në zbaticë nuk mbulohet nga uji.
(G) Dunat
Kreshta ose kodra me material të dallgëzuar, zakonisht rërë. Dunat shpesh kanë bimë që rriten në to.
(H) Bregu i sipërm Zona e plazhit midis zonës para bregore dhe pjesës fundore të dunave. Kjo zonë është midis bregut dhe vijës bregdetare. Normalisht pjesa e prapme është e thatë; valët arrijnë këtë zonë vetëm gjatë stuhive.
(I) Zonë parabregore
Kjo pjesë e plazhit (breg) në mes të nivelit të ujit në baticën e ulët dhe kufirin e sipërm të valës në baticën e lartë (bregdeti).
(K) Zonë thyerje
Zona ku valët e thella të ujit prekin fundin dhe bëhen dallgë me ujë të cekët, duke ndryshuar nga valët e rrumbullakosura në valë të paqëndrueshme dhe të pjerrëta që fillojnë të thyhen.
(L) Niveli i ujit në baticë
Niveli më i lartë i ujit për çdo baticë në rritje.
(M) Rrip (rrip rëre)
Një argjinaturë e rërës, zhavorrit, ose grimcave të tjera depozitohen në ujë të cekët nga valët dhe rrymat që janë paralele me bregun. Rripat e rërës mund të zhyten ose të dalin.
(N) Niveli i ujit në zbaticë
Niveli më i ulët i ujit në çdo zbaticë.
3.1.3 SKEMAT E APLIKIMIT DHE DIAGRAMAT UML PËR TEMËN: “DETET”
Modeli konceptual i temës “Detet” mund të konsiderohet si bashkim i elementeve të mëposhtëm:
- ZonaDetare, përfshijnë Detet, ZonatEQarkullimitDetar dhe ZonaNdërbaticore
- Bregdeti dhe VijaBregdetare
- IzolinjatDetare
- SipërfaqjaEZonësDetare (p.sh. derdhjet e naftës)
- SipërfaqjaETabanitTëDetit
ZonaDetare, Detet, Zonat e Qarkullimit Detar dhe Zona Ndërbaticore
Klasa primare në modelin e temës “Detet” është ZonaDetare. ZonaDetare mund të kuptohet si një sipërfaqe e detit, në veçanti një zonë që është përcaktuar kryesisht nga karakteristikat e tij fizike apo kimike.
Meqenëse gjeometria e detit ndryshon sipas gjendjeve të baticës, ZonaDetare mund të gjendet me gjeometri të ndryshme për të njëjtin rast. Gjeometria e një ZoneDetare përshkruhet nga tipi i të dhënave ShtrirjaDetare që shoqëron një MultiSipërfaqe (një ose më shumë zona të përcaktuara gjeometrikisht) me një gjendje të caktuar baticash, e cila duhet të merret nga kodlista VleratENivelitTëUjit (kodlistë e importuar nga tema “Hidrografia”).
Një shembull i thjeshtë do të ishte një ZonëDetare me dy gjeometri, një për nivelin e baticave dhe një për nivelin e zbaticave. Në shumë aplikime në realitet efektet e baticës dhe zbaticës bëjnë pak ndryshim në gjeometri, megjithatë ka një numër rajonesh ku këto dallime janë shumë të rëndësishme kështu që skema e aplikimit plotëson të dy skenarët.
Një ZonëDetare gjithashtu mund të mbajë vlerat e parametrave që përshkruajnë vetitë fizike të ZonësDetare. Për shembull, një ZonëDetare mund të përmbajë informacion rreth Temperaturës mesatare vjetore të sipërfaqes së saj. Kjo duhet shtuar duke përdorur atributin VleratEParametraveTëZonësDetare.
ZonaDetare mund të klasifikohen sipas vlerave të kodlistës VleratEKlasifikimitTëZonësDetare. Për shembull një ZonëDetare mund të klasifikohet si grykëderdhje (ose ndonjë vlerë tjetër nga lista).
ZonaDetare është qëllimisht një tip shumë i përgjithshëm. Megjithatë ka ndarje të ZonësDetare në modelin e temës “Detet” që duhet të përdoren për qëllime specifike. Këto janë:
- Deti
- ZonaEQarkullimitDetar
Figura 4: Përmbledhja e UML për ZonaDetare
Tipologjia Deti duhet të përdoret sa herë që një ZonëDetare është identifikuar, me emrin det (ose oqean). Për shembull, Deti i Zi ose Deti i Veriut. Deti do të jetë element që përdoret në rastin e përgjithshëm ku përdoruesit kanë nevojë për një rajon detar për të kërkuar në brendësi ose për të parë shtrirjen e deteve në një hartë.
Kur përdoret termi Deti, ShtrirjaDetare e tij, duhet t’i referohet NivelitTëLartëTëUjit dhe nëse nuk ka ndonjë ndryshim të dukshëm për shkak të baticë-zbaticës, mund të përdoret NiveliMesatarIDetit.
Klasa ZonaEQarkullimitDetar duhet të përdoret sa herë që një ZonëDetare, është një zonë qarkullimi detar si një zonë përzierje ose qelizë sedimentesh. Lloji i zonës do të jepet duke përdorur atributin LlojetEZonës. Këto zona përfaqësojnë ZonaDetare që mund të jenë të dobishme për qëllimin e menaxhimit të erozionit bregdetar, monitorimit dhe raportimit të cilësisë së ujërave bregdetare.
ZonaNdërbaticore është një specialitet i llojit të bregdetit në Hidrografi. Mund të përdoret për të identifikuar pjesën e detit që është e ekspozuar (jo e mbuluar me ujë) gjatë një cikli normal të baticës. Këto janë zona të rëndësishme ekologjike.
Një ZonëNdërbaticore mund të cilësohet si pjesë e mjedisit detar që është ekspozuar (nuk mbulohet me ujë) gjatë një cikli normal të baticës dhe zbaticës; e përcaktuar si diferenca ndërmjet nivelit të lartë dhe çdo niveli të ulët të ujit. Shtrirja e përgjithshme e zonës ndërbaticore duhet të jepet duke iu referuar NivelitTëLartëTëUjit, të dy niveleve të ujit, ndërsa vlera e atributit të NiveliTëUlëtTëUjit duhet të specifikojë nivelin më të ulët të dy niveleve të ujit, që u përdor për të përcaktuar kufijtë e poshtëm të zonës ndërbaticore.
Rregullat e sakta për përcaktimin e shtrirjes së objekteve të ndryshme të ZonaDetare janë specifikuar në konventa, marrëveshje dhe legjislacione të ndryshme ndërkombëtare. Gjithashtu termi Detet mund të ketë lidhje me Elementet Gjeografike Oqeanografike që përshkruajnë elemente të tilla si temperatura, kripësia, rryma ose vala, të trajtuara në këtë temë, por kjo nuk është modeluar shprehimisht.
Referencat e objektit hidrik
Bregdeti:
Një Bregdet është kufiri ku një zonë e detit takon tokën. Megjithatë, mund të ketë bregdete të ndryshme në varësi të gjendjes së baticës. Për këtë arsye, një Bregdet duhet të ketë një vlerë për NivelinEUjërave që identifikon gjendjen e baticës që përdoret për të përcaktuar bregun. Për trupat ujorë në brendësi të tokës duhet të përdoren vetëm termat nga tema “Hidrografia”, p.sh. KufiriUjëTokë. Një Bregdet është një element specifik i ObjekteveHidrike dhe prandaj mund të ketë një emër gjeografik, p.sh. “niveli mesatar i ujit në bregdetin e Britanisë së Madhe”.
Segmenti i bregdetit:
Lloji i objektit gjeohapësinor Bregdeti është ndërtuar nga shumë SegmenteBregdetare. Secili segment bregdeti ka një gjeometri të kurbës që përcakton një pjesë të bregut. Çdo SegmentBregdetar mund të klasifikohet sipas gjendjes së stabilitetit (gërryerje, qëndrueshmëri etj.) dhe llojit të bregdetit (rërë, baltë etj).
Vija Bregdetare:
Një VijëBregdetare është një rast specifik i Bregdetit kur niveli i ujit është i barabartë me MHW. (Vija bregdetare është e ngjashme me konceptin e KufiritUjëTokë në temën “Hidrografia”, por aplikohet vetëm në rastin e deteve, d.m.th. lumenjtë dhe liqenet përjashtohen). Një bregdet zakonisht do të jetë tipi i objektit gjeohapësinor që përdoret për shumicën e aplikacioneve që duhet të tregojnë një kufi të detit/tokës.
Figura 5: Përmbledhja e UML për VijatBregdetare dhe bregdetet
Konturi detar
Lloji i objekti gjeohapësinor, KonturDetar, është një grup izolinjash që përfaqësojnë vlerën e disa fenomeneve në një kohë të caktuar. Për shembull, do të përdoret zakonisht për të shfaqur konturet e temperaturës, konturet e valëve të klimës, ose vijat baticore. Nuk duhet të përdoret për të dhënat batimetrike, të cilat duhet të përfaqësohen nga llojet e objekteve gjeohapësinore të përshkruara në temën “Modeli dixhital i terrenit - DTM”.
KonturiDetar nuk duhet të shtrihet përtej zonës që përfshinë tema “Detet”. Një KonturDetar është i përbërë nga disa izolinja, për të cilat përdoret tipi i të dhënave IzolinjatDetare. Një lloj i të dhënave të IzolinjaveDetare përcakton gjeometrinë e një konturi për një vlerë të veçantë dhe përdoren shumë lakore për ta bërë këtë siç ilustrohet në Figurën 6.
Figura 6: Përdorimi i ilustruar i Izolinjave Detare dhe Vijave të Nivelit Detar
Figura 7: Përmbledhja e UML për Vijat e Nivelit Detar
Shtresat detare / Sipërfaqet e zonës detare
Një ShtresëDetare është një klasë e përgjithshme për të përshkruar sipërfaqet me interes në det, që nuk janë ZonaDetare siç përcaktohet në këtë temë. Janë dhënë dy përkufizime, një për sipërfaqen e detit dhe një për zonat e tabanit të detit. E para, SipërfaqjaEZonësDetare, përshkruan një zonë të sipërfaqes së detit që është me interes të veçantë. Për shembull, mund të mbulohet nga një vaj i shkëlqyeshëm ose me vegjetacion. Kjo zonë do të klasifikohet sipas kodlistës së VleraveTëKlasifikimitTëSipërfaqesSëDetit. Në mënyrë të ngjashme, SipërfaqjaETabanitTëDetit përshkruan një zonë të detit të klasifikuar sipas llojit të mbulimit. Duhet pasur parasysh se një SipërfaqjaETabanitTëDetit mund të ketë më shumë se një klasifikim, për shembull, kur ekziston rërë mbi baltë.
Një ShtresëDetare mund të lidhet në mënyrë hierarkike me shtresa të tjera detare nëpërmjet marrëdhënies së NënShtresave.
Figura 8: Përmbledhja e UML-së për shtresat detare
Konsistenca (lidhja logjike) midis grupeve të të dhënave gjeohapësinore
Ka disa kufizime që vlejnë për specializimet e ndryshme të ZonësDeteve. Për shembull, Deti është përcaktuar si një ZonëDetare me MesatarenEUjraveTëLartë, kështu që vlera e atributeve të ShtrirjesDetare duhet të jetë MesatarjaEUjraveTëLartë për Detin. Në të njëjtën mënyrë vija bregdetare është përcaktuar si bregdet në MesatarenEUjraveTëLartë.
Në përgjithësi, gjeometria e zonave detare dhe llojet përkatëse duhet të pasqyrojnë kufizimet e realitetit. Për shembull, një bregdet me nivelin e ulët të ujërave duhet të ndajë një gjeometri me një ZonëDetare në të njëjtin nivel. Një izolinjë detare duhet të përshtatet brenda një zone detare (ose të shumë zonave detare). Një ShtresëDetare (shtrati apo sipërfaqja e detit) duhet të përshtatet brenda gjeometrisë së një zone detare (p.sh. do të ishte absurde që të kishim mbulesën e tabanit të detit mbi tokë).
Figura 9: Struktura e temës “Detet”
3.1.4 KATALOGU I TIPOLOGJISË
3.1.4.1 ZONË DETARE
-- Emri --
Zonë detare
-- Përkufizimi --
Një zonë e detit e përcaktuar sipas karakteristikave fizike dhe kimike të saj. Mund të ketë gjeometri të shumta (shtrirje) për të përfaqësuar gjendje të ndryshme të baticës.
-- Përshkrimi --
Një Zonë detare është një lloj i ObjektHidrografik, siç përshkruhet në temën “Hidrografia”. Ajo ka gjeometrinë e përshkruar nga një ose më shumë MultiSipërfaqe. Gjeometri të shumëfishta lejohen të mundësojnë që një zonë detare të përshkruhet sipas disa gjendjeve të ndryshme të baticës.
Specifikimet e ZonësDetare do të kufizojnë gjeometrinë në një gjendje të caktuar baticash ose në një sërë gjendjesh të baticës. ZonaDetare përfshijnë detet me emrin si “deti Baltik” dhe gjithashtu zonat e pa-emërtuara të detit që kanë karakteristika të veçanta kimike dhe fizike. ZonaDetare janë objekte 2D dhe nuk mbajnë asnjë informacion të qartë për thellësinë e detit. Kjo është specifikuar në temën “Modeli dixhital i terrenit”.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Agreguar nga «featureType» ZonaDetare tek «featureType» ZonaDetare
Gjeneralizuar nga «featureType» ZonaDetare tek «featureType» ObjektiHidrik
LIDHJE STRUKTURORE TË JASHTME
Agreguar nga «featureType» ZonaDetare tek «featureType» ZonaDetare
Gjeneralizuar nga «featureType» ZonaEQarkullimitDetar tek «featureType» ZonaDetare
Gjeneralizuar nga «featureType» Deti tek «featureType» ZonaDetare
ATRIBUTET
InspireId : Identifikues
Shumëllojshmëria: [1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikuesi i objektit të jashtëm të objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i objektit të jashtëm është një identifikues unik i objektit i publikuar nga autoriteti përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit të botës reale.
[I detyrueshëm: PO]
LlojetEZonësSëDetit : VleratEKlasifikimitTëLlojeveTëSipërfaqeveDetare
Shumëllojshmëria: [0..1]
-- Name --
Llojet e zonë së detit
-- Përkufizimi--
Lloji i ZonësDetare sipas klasifikimeve në kodlistën VleratEKlasifikimeveTëZonaveDetare. p.sh grykëderdhje e gjerë
[I detyrueshëm: PO]
Shtrirje : ShtrirjeDetare
Shumëllojshmëria: [1..*]
-- Emri --
Shtrirje
-- Përkufizimi --
Shkalla e ZonësDetare në një gjendje të caktuar baticash.
[I detyrueshëm: PO]
VleratEParametrave : BashkimiIVleraveTëParametrave
Shumëllojshmëria: [0..*]
-- Emri --
Vlerat e parametrave
-- Përkufizimi --
Një vlerë e disa parametrave të caktuar në ZonënDetare. P.sh. Temperatura mesatare vjetore e detit është 12 gradë Celsius
-- Përshkrimi --
Një ZonëDeti mund t’i atribuohet me çdo numër vlerash që janë relevante për poligonin e ZonësDetare si një e tërë. Vëzhgime më të hollësishme, të tilla si rrjetet dhe të dhënat e pikave janë objekt i specifikimeve Gjeografike të Oqeanografisë.
[I detyrueshëm: PO]
FillimiICiklitJetësor : Datë-Orë
Shumëllojshmëria: [1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data dhe koha në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
PërfundimiICiklitJetësor : Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i ciklit jetësor
-- Përkufizimi --
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq nga grupi i të dhënave gjeohapësinore.
[I detyrueshëm: JO]
LIDHJE
Lidhje (Drejtimi: Burimi -> Përcaktimi)
Burimi: (Class) ZonaDetare «featureType»
Objektivi: ZonaDetare (Class) ZonaEDetare «featureType»
3.1.4.2 DETI
--Emri --
Deti
-- Përkufizimi --
Shtrirja (sipërfaqja) e detit në nivelin e ujërave të larta (niveli i mesatar i baticave).
-- Përshkrimi--
Një sipërfaqe e detit, e kufizuar nga toka dhe zona detare të tjera ngjitur. Kjo tipologji mund të përmbajë zona detare të shkallëve të vogla. Gjithashtu gjenden modele në shkallë të gjerë të qarkullimit, të cilat ndikohen nga kufijtë me tokën. Niveli ujërat e arta merret si niveli i mesatar i baticave. Si shembuj mund të përmendim: Deti i Veriut, deti Egje etj. (Burimi: IHO S23 Detet)
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» Deti tek «featureType» ZonaDetare
ATRIBUTET
Shtrirja : ShtrirjaDetare
Shumëllojshmëria: [1]
-- Emri --
Shtrirja
-- Përkufizimi --
Shtrirja sipërfaqësore e detit në Nivelin e Mesatar të Baticave
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtimi: Paspecifikuar)
Burimi: (Class) ZonaDetare «featureType»
Objektivi: Deti (Class) Deti «featureType»
3.1.4.3 ZONA E QARKULLIMIT DETAR
-- Emri--
Zona e qarkullimit detar
-- Përkufizimi --
Një zonë e detit e përcaktuar nga modelet e tij të qarkullimit fizik dhe kimik.
-- Përshkrimi --
Përdoret në mënyrë tipike për menaxhimin dhe raportimin e mjedisit detar ose klasifikimin e mjedisit detar.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» ZonaEQarkullimitDetar tek «featureType» ZonaDetare
ATRIBUTET
LlojetEZonave : VleratELlojeveTëZonave
Shumëllojshmëria: [1]
-- Emri --
Llojet e zonave
-- Përkufizimi --
Lloji i ZonësSëQarkullimitDetar, p.sh. QelizaSedimentare (zona e sendimentit).
[I detyrueshëm: PO]
Shtrirje : ShtrirjeDetare
Shumëllojshmëria: [1]
-- Emri --
Shtrirje
-- Përkufizimi --
Shtrirja e ZonësSëQarkullimitDetar në një gjendje të veçantë baticash.
[I detyrueshëm: PO]
3.1.4.4 ZONA NDËRBATICORE
-- Emri --
Zona ndërbaticore
-- Përkufizimi --
Pjesa e mjedisit detar që është e ekspozuar (nuk është e mbuluar me ujë) gjatë një cikli normal të baticës; e përcaktuar si diferenca ndërmjet nivelit të lartë dhe çdo niveli të ulët të ujit.
-- Përshkrimi--
Pjesa e mjedisit detar që është e ekspozuar (nuk është e mbuluar me ujë) gjatë një cikli normal të baticës.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» ZonaNdërbaticore tek «featureType» Bregdet
ATRIBUTET
NiveliILartëIUjit : VleratENivelitTëUjit
Shumëllojshmëria: [1]
-- Emri --
Niveli i lartë i ujit (baticës)
-- Përkufizimi--
Niveli i lartë i ujit i cili përdoret për të përcaktuar kufirin e sipërm të zonës ndërbaticore p.sh. “Niveli Mesatar i Baticës”.
[I detyrueshëm: PO]
NiveliIUlëtIUjit : VleratENivelitTëUjit
Shumëllojshmëria: [1]
-- Emri --
Niveli i ulët i ujit (zbaticës)
-- Përkufizimi --
Niveli i ulët i ujit i cili përdoret për të përcaktuar kufirin e poshtëm të ZonësNdërbaticore p.sh. “Niveli Mesatar Zbaticës”.
[I detyrueshëm: PO]
3.1.4.5 SHTRIRJE DETARE
-- Emri --
Shtrirje detare
-- Përkufizimi --
Shtrirja e një ZoneDetare në një gjendje të caktuar baticash.
-- Përshkrimi --
Shtrirja gjeometrike 2D e një ZoneDetare për një gjendje të veçantë baticash.
-- Tipi i elementit --
DataType
ATRIBUTET
Geometri : GM_MultiSipërfaqe
Shumëllojshmëria: [1]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria e ShtrirjesDetare .
-- Përshkrimi --
Një MultiSipërfaqe përdoret në mënyrë që të paraqesë gjendje të ndryshme të baticës në shtete të ndryshme, e cila bën të mundur paraqitjen e zonave që herë pas here shfaqen si zona detare të izoluara nga toka, për shkak të vlerave të ndryshme të baticës. Kjo është prioritet për detet në shkallë lokale
[I detyrueshëm: PO]
NiveliIUjit : VleratENivelitTëUjit
Shumëllojshmëria: [0..1]
-- Emri --
Niveli i ujit
-- Përkufizimi --
Vlera e nivelit të ujit në të cilën ShtrirjaDetare është e vlefshme.
[I detyrueshëm: PO]
3.1.4.6 VLERAT E PARAMETRAVE
-- Emri --
Vlera e parametrave
-- Përkufizimi --
Një sërë parametrash që përmbajnë një vlerë të disa karakteristikave të vëzhguara, p.sh., temperatura mesatare vjetore e sipërfaqes së detit.
-- Tipi i elementit --
DataType
ATRIBUTET
Parametri : KarakteristikaEVëzhgimitAbstrakt
Shumëllojshmëria: [1]
-- Emri --
Parametri
-- Përkufizimi --
Një përkufizim i parametrit të vëzhguar (p.sh. temperatura mesatare).
[I detyrueshëm: PO]
Vlera : Matje
Shumëllojshmëria: [1]
-- Emri --
Vlera
-- Përkufizimi --
Vlera e parametrit të vëzhguar, p.sh. 12 gradë Celsius.
[I detyrueshëm: PO]
KohaEVlefshmërisë : TM_Objekt
Shumëllojshmëria: [1]
-- Emri --
Koha e vlefshmërisë
-- Përkufizimi --
Koha për të cilën vlera e atribuar është e vlefshme. Kjo mund të jetë një çast kohor ose një interval kohor.
[I detyrueshëm: JO]
3.1.4.7 BREGDETI / TOKË E LAGUR
-- Emri --
Bregdeti/Tokë e lagur
-- Përkufizimi --
Bregdet/Tokë e lagur (shoreline) - është një rrip toke i ndërmjetëm dhe në varësi të gjendjes së detit, mund të jetë i mbuluar nga uji ose jo, përkatësisht në baticë mbulohet në zbaticë nuk mbulohet nga uji.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizimi nga «featureType» Bregdeti tek «featureType» ObjektiHidrik
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» VijaBregdetare tek «featureType» Bregdeti
ATRIBUTET
Segmenti : SegmentiIBregdetit
Shumëllojshmëria: [1..*]
-- Emri --
Segmenti
-- Përkufizimi --
Një segment i bregdetit.
[I detyrueshëm: JO]
NiveliIUjit : VleratENivelitTëUjit
Shumëllojshmëria: [1]
-- Emri --
Niveli i ujit
-- Përkufizimi --
Niveli i ujit i përdorur në përcaktimin e vijës bregdetare (p.sh. NiveliMesatarIBaticës)
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtimi: Burimi -> Përcaktimi)
Burimi: (Class) ZonaDetare «featureType»
Objektivi: baseline (Class) Bregdeti «featureType»
3.1.4.8 VIJA BREGDETARE
-- Emri --
Vija bregdetare
-- Përkufizimi --
Vija që formon kufirin midis bregdetit (tokës) dhe plazhit (bregut). Ajo shënohet me fillimin e bimësisë së përhershme ose kur ka një ndryshim të dukshëm në morfologjinë (formën) e substratit ose formës së tokës, për shembull, nga një plazh relativisht i sheshtë në duna kodrinore.
-- Përshkrimi --
VijaBregdetare është një rast i veçantë i një Bregdeti, i përcaktuar si vijë bregdetare, sipas NiveliMesatarTëBaticës (MHW). Kur nuk ka ndryshime të rëndësishme në nivelin e ujit, NiveliMesatarIDetit (MSL) mund të përdoret si zëvendësim për MHW.
Ky tip funksioni është projektuar për rastin e përdorimit të përgjithshëm ku toka (kufiri i detit) nevojitet për të mbështetur shikimin dhe zbulimin e grupeve të të dhënave. Nuk është hartuar për të nxjerrë në pah kufijtë politikë. Qëllimi është të sigurojë një pasqyrë të qëndrueshme të shtrirjes detare evropiane dhe për këtë arsye zgjidhet një masë e vetme e baticës. Kjo është në përputhje me përkufizimet e IHO-57
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» VijaBregdetare tek «featureType» Bregdeti
3.1.4.9 SEGMENTI BREGDETAR
-- Emri --
Segment bregdetar
-- Përkufizimi --
Segmenti bregdetar është një pjesë e linjës bregdetare.
-- Përshkrimi --
Nëse është e mundur të sigurohen atributet për stabilitetin e bregdetit (erodimi, stabiliteti etj.) dhe/ose lloji i bregdetit (ranor, shkëmbor, port etj.).
-- Tipi i elementit --
FeatureType
ATRIBTET
Gjeometria : GM_Linjë
Shumëllojshmëria: [1]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria e Segmentit Bregdetar
[I detyrueshëm: PO]
KlasifikimiIBregdetit : VleratEKlasifikimeveTëLlojeveTëVijaveBregdetare
Shumëllojshmëria: [0..1]
-- Emri--
Lloji primar
-- Përkufizimi --
Lloji primar i segmentit të bregdetit, marrë nga kodlista VleratEKlasifikimeveTëLlojeveTëBregdetit.
[I detyrueshëm: PO]
StabilitetiIBregdetit : VleratEStabilitetitTëBregdetit
Shumëllojshmëria: [0..1]
-- Emri--
Stabiliteti i bregdetit
-- Përkufizimi --
Lloji i stabilitetit primar të SegmentitTëBregdetit, marrë nga kodlista VleratEStabilitetitTëBregdetit.
[I detyrueshëm: JO]
3.1.4.10 SHTRESA DETARE
-- Emri --
Shtresa detare
-- Përkufizimi --
ShtresaDetare përshkruan çdo shtresë që mund të mbulojë pjesë të sipërfaqes ose tabanit të detit.
-- Përshkrimi--
Shembuj të shtresave sipërfaqësore të identifikuara në materialin referues përfshijnë vajin, lulëzimin e algave dhe akullin. Shembuj të shtresës së shtratit të detit të identifikuara në materialin referues përfshijnë llojin e sendimentit dhe praninë ose mungesën e vegjetacionit.
Meqenëse këto fenomene kanë një karakteristikë dinamike, shkalla që përshkruajnë (Sipërfaqe) ka një periudhë vlefshmërie. Një ShtresëDetare nuk mund të shoqërohet me një ZonëDetare. Një ZonëDetare mund të ketë ShtresaDetare të shumëfishta, dhe këto ShtresaDetare mund të mbivendosen me njëra tjetrën.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» ZonaETabanitTëDetit tek «featureType» ShtresaDetare
Gjeneralizuar nga «featureType» SipërfaqjaEZonësDetare tek «featureType» ShtresaDetare
ATRIBUTET
Gjeometria : GM_Objekt
Shumëllojshmëria: [0..1]
-- Emri --
Gjeometria
-- Përkufizimi --
Gjeometria e shtresave detare
[I detyrueshëm: PO]
KohaEVlefshmërisë : TM_Periudhë
Shumëllojshmëria: [1]
-- Përkufizimi --
Koha e vlefshmërisë
-- Përkufizimi --
Periudha kohore për të cilën ShtresaDetare është e vlefshme.
[I detyrueshëm: JO]
LIDHJE
Lidhje (Drejtimi: Burimi -> Përcaktuar)
Burimi: (Class) ShtresaDetare «featureType»
Objektivi: NënShtresa (Class) ShtresaDetare «featureType»
Shumëllojshmëria: [1]
-- Emri --
Nënshtresa
-- Përkufizimi --
Një shtresë detare mund të ketë një nën shtresë, për shembull një shtresë nafte (rrjedhje nafte) mund të ketë një burim kryesor dhe disa pjesë të tjera të shpërndara (nënshtresa).
3.1.4.11 ZONË E SIPËRFAQES DETARE
-- Emri --
Zonë e sipërfaqes detare
-- Përkufizimi --
Një zonë e sipërfaqes së detit e mbuluar me ndonjë lloj elementi p.sh. një zonë e akullit të detit
-- Përshkrimi --
Kjo përshkruan një rajon detar sipas karakteristikave të sipërfaqes së detit në vend të karakteristikave të ujit në përgjithësi. Është analoge me konceptin e mbulesës së tokës në temën përkatëse.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» SipërfaqjaEZonësDetare tek «featureType» ShtresaDetare
ATRIBUTET
LlojiISipërfaqes : VleratEKlasifikimitTëSipërfaqesSëDetit
Shumëllojshmëria: [1]
-- Emri --
Lloji i sipërfaqes
-- Përkufizimi --
Llojet e sipërfaqeve të detit
[I detyrueshëm: PO]
3.1.4.12 SIPËRFAQJA E TABANIT TË DETIT
-- Emri --
Sipërfaqja e tabanit të detit
-- Përkufizimi --
Një sipërfaqe e tabanit të detit e mbuluar me elemente, me karakteristika të njëjta, p.sh., një zonë e vegjetacionit ose një zonë e një lloji sedimenti.
-- Përshkrimi --
Kjo përshkruan një zonë detare sipas karakteristikave të tabanit të detit në vend të karakteristikave të ujit në përgjithësi. Ajo nuk përfshin gjeologjinë (zonat nëndetare) dhe është analoge me konceptin e mbulesës së tokës.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «featureType» ZonaETabanitTëDetit tek «featureType» ShtresaDetare
ATRIBUTET
LlojetESipërfaqes : VleratEMbulesësSëTabanitTëDetit
Shumëllojshmëria: [1..*]
-- Emri --
Llojet e sipërfaqeve
-- Përkufizimi --
Llojet e sipërfaqeve të tabanit të detit
-- Përshkrimi --
Llojet e sipërfaqeve të tabanit të detit
[I detyrueshëm: PO]
3.1.4.13 IZOLINJË DETARE
--Emri --
Izolinjë detare
-- Përkufizimi --
Një izolinjë detare përfaqëson një vlerë të veçantë të një fenomeni detar fizik ose kimik të tillë si temperatura, kripësia ose lartësia e valës.
-- Përshkrimi--
Një kontur detar (linjë) që përfaqëson një vlerë të veçantë të ndonjë fenomeni. Gjeometria e konturit është një MultiLinjë, d.m.th. mund të formulohet nga disa kthesa apo harqe, të cilat përfaqësojnë të njëjtën vlerë p.sh. 15 gradë celsius.
-- Tipi i elementit --
DataType
ATRIBUTET
Gjeometria : GM_MultiLinjë
Shumëllojshmëria: [1]
-- Emri--
Gjeometria
-- Përkufizimi--
Gjeometria e izolinjës
[I detyrueshëm: PO]
Vlerat : Matje
Shumëllojshmëria: [1]
-- Emri--
Vlera
-- Përkufizimi--
Vlerat që i atribuohen izolinjës.
[I detyrueshëm: PO]
3.1.4.14 KONTURI DETAR
-- Emri --
Konturi detar
-- Përkufizimi --
Një grup izolinjash që përfaqësojnë vlerën e disa fenomeneve në një kohë të caktuar.
-- Përshkrimi --
Një përfaqësim i çdo dukurie fizike ose kimike që lidhet me ZonatDetare. LinjaDetare është një element abstrakt i “realitetit” për të ofruar një pasqyrë të kushteve të pritshme të një ZoneDetare. Shembujt do të përfshijnë konturet e kripësisë, konturet e thellësisë, lartësinë e valëve të rëndësishme.
-- Tipi i elementit --
FeatureType
ATRIBUTET
IzolinjaDetare : IzolinjaDetare
Shumëllojshmëria: [1]
-- Emri --
Izolinja detare
-- Përkufizimi --
Izolinjat detare përdoren për të përcaktuar konturet e një dukurie apo elementi me vlerë të barabartë.
[I detyrueshëm: PO]
Dukuria : KarakteristikatEVëzhgimitAbstrakt
Shumëllojshmëria: [1]
-- Emri --
Dukuria
-- Përkufizimi --
Karakteristikat e përfaqësuara nga izovija (p.sh niveli i valëve).
[I detyrueshëm: PO]
KohaEVefshme : TM_Moment
-- Emri --
Koha e vlefshme
-- Përkufizimi --
Koha në të cilën ky kontur është përfaqësuar.
[I detyrueshëm: JO]
LIDHJE
Lidhje (Drejtimi: Burimi -> Përcaktimi)
Burimi: (Class) KonturDetar «featureType»
Objektivi: VëzhgimetEBurimit (Class) Vëzhgimet «featureType»
Shumëllojshmëria: [1]
-- Emri --
Vëzhgimet e burimeve
-- Përkufizimi --
Përdoret për tu lidhur me një koleksion të Vëzhgimeve themelore të cilat janë përdorur për të përcaktuar një izovijë detare.
3.1.4.15 VLERAT E KLASIFIKIMIT TË ZONAVE DETARE
-- Emri --
Vlerat e klasifikimit të zonës detare
-- Përkufizimi --
Lloji i klasifikimit të ZonësDetare, p.sh. grykëderdhje.
Shiko Aneksin B
-- Tipi i elementit --
Kodlistë
3.1.4.16 VLERAT E MBULESËS SË TABANIT TË DETIT
-- Emri --
Vlerat e mbulesës së tabanit të detit.
-- Përkufizimi --
Llojet e gjetura të mbulesës së tabanit të detit.
-- Përshkrimi --
Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Shiko Aneksin B
-- Tipi i elementit --
Kodlistë
3.1.4.17 VLERAT E KLASIFIKIMIT TË SIPËRFAQES SË DETIT
-- Emri --
Vlerat e klasifikimit të sipërfaqes së detit.
-- Përkufizimi --
Llojet e shtresave sipërfaqësore të detit, që gjenden në sipërfaqet e detit.
-- Përshkrimi --
Kodlistat për llojet e shtresave sipërfaqësore të detit që gjenden në sipërfaqet e detit (p.sh. vaj, akull etj.).
Shiko aneksin B
-- Tipi i elementit --
Kodlistë
3.1.4.18 VLERAT E QËNDRUESHMËRISË SË BREGDETIT
-- Emri --
Vlerat e qëndrueshmërisë së bregdetit.
-- Përkufizimi --
Llojet e qëndrueshmërisë së segmenteve të bregdetit.
-- Përshkrimi --
Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Shiko Aneksin B
-- Tipi i elementit --
Kodlistë
3.1.4.19 VLERAT E KLASIFIKIMIT TË LLOJIT TË BREGDETIT
-- Emri --
Vlerat e klasifikimit të llojit të bregdetit
-- Përkufizimi --
Llojet e segmenteve të vijave bregdetare.
-- Përshkrimi --
Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Shiko aneksin B
-- Tipi i elementit --
Kodlistë
3.1.4.20 VLERAT E LLOJEVE TË ZONAVE
-- Emri --
Vlerat e llojeve të zonave
-- Përkufizimi --
Llojet e zonave të qarkullimit detar.
-- Përshkrimi--
Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Shiko Aneksin B
-- Tipi i elementit --
Kodlistë
3.2 METADATAT
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3 KODI EPSG PËR KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare sipas vendimit nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë” ndryshuar me vendimin nr. 322, datë 27.4.2016 dhe vendimin nr.359, datë. 29.05.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është: EPSG - 6870.
3.4 CILËSIA E TË DHËNAVE
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nën elementeve si dhe cilësinë e matjes së tyre, që duhen përdorur për të vlerësuar dhe dokumentuar cilësinë e të dhënave, për grupet e të dhënave që përfshihen në temën “Detet”.
Cilësia e të dhënave të elementeve, nën elementeve dhe matjeve duhet të përdoret për të:
Vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku karakteristikat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit.
Vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore.
Për të specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore që lidhen me temën “Detet”.
3.4.1 ELEMENTET E CILËSISË SË TË DHËNAVE
Tabela paraqet të gjitha elementet dhe nën elementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit gjeohapësinor, të dhëna ose grupe të dhënash. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën e fushës së vlerësimit.
Masat që do të përdoren për secilën nga nën elementet e listuar të cilësisë së të dhënave janë përcaktuar në nën seksionet e mëposhtme.
Tabela. Elementet e cilësisë së të dhënave që janë përdorur për të dhënat gjeohapësinore në temën “Detet”
Pjesa
Elementi i cilësisë së të dhënave
Nën elementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
3.4.2
Përputhja logjike
Përputhja konceptuale
Zbatimi i rregullave të skemës konceptuale.
Grup të dhënash, të dhëna, llojet e objekteve gjeohapësinore, objektet gjeohapësinore.
3.4.3
Përputhja logjike
Përputhja në domein
Zbatimi e vlerave, në vlerat e domeinit.
Grup të dhënash, të dhëna, llojet e objekteve gjeohapësinore, objektet gjeohapësinore.
3.4.4
Saktësia pozicionale
Saktësa absolute ose e jashtme.
Afërsia me vlerat e koordinuara të raportuara, me vlerat e pranuara ose që janë të vërteta.
Llojet e objekteve gjeohapësinore.
3.4.5
Përdorimi
--
Shkalla e respektimit të një grupi të të dhënave për një grup kërkesash specifike.
Të dhënat.
3.4.2 PËRPUTHJA LOGJIKE - PËRPUTHJA KONCEPTUALE. (LOGICAL CONSISTENCY - CONCEPTUAL CONSISTENCY)
Rekomandim: Për provën e përputhjes konceptuale, është rekomanduar të përdoret Përputhja Logjike - Përputhja Konceptuale e nën elementit të cilësisë së të dhënave dhe matja e numrit të artikujve që nuk janë në përputhje me rregullat e skemës konceptuale siç është specifikuar në tabelën e mëposhtme.
Emri
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nën elementeve
Përputhja konceptuale
Cilësia e të dhënave të matjeve themelore
Numëruesi i gabimit
Përkufizim
Numërimi i të gjithë elementeve në grupin e të dhënave që nuk janë në përputhje me rregullat e skemës konceptuale.
Përshkrimi
Nëse skema konceptuale përshkruan shprehimisht ose në mënyrë të qartë rregullat, këto rregulla duhet të ndiqen. Shkeljet ndaj rregullave të tilla mund të jenë, për shembull, vendosja e pavlefshme e karakteristikave brenda një tolerance të përcaktuar, dyfishimi i karakteristikave dhe mbivendosja e pavlefshme e karakteristikave.
Fusha e vlerësimit
Objekti gjeohapësinor / llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
Cilësia e të dhënave të strukturës së vlerave
-
Burimi reference
SSH EN ISO 19157:2013 Informacion Gjeografik - Cilësia e të dhënave
Shembull
Masa identifikuese
8
3.4.3 PËRPUTHJA LOGJIKE - PËRPUTHJA ME DOMEININ (LOGICAL CONSISTENCY - DOMAIN CONSISTENCY)
Rekomandim
Për provën e përputhjes me domeinin, është rekomanduar të përdoret Përputhja Logjike - Përputhja me domeinin e nën elementit të cilësisë së të dhënave dhe matja e numrit të artikujve që nuk janë në përputhje me domeinin e vlerave të tyre siç specifikohet në tabelën e mëposhtme:
Emri
Numri i artikujve që nuk janë në përputhje me domeinin e vlerës së tyre
Emri alternativ
-
Cilësia e të dhënave të elementeve
Përputhja ligjore
Cilësia e të dhënave të nën-elementeve
Përputhja me domeinin
Cilësia e të dhënave të matjeve themelore
Numëruesi i gabimit
Përkufizimi
Numërimi i të gjithë elementeve në grupin e të dhënave që nuk janë në përputhje me domeinin e vlerës së tyre.
Përshkrimi
-
Fusha e vlerësimit
Objekti gjeohapësinor / Llojet e objekteve gjeohapësinore
Fusha e raportimit
Grupi i të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Integer
3.4.4 SAKTËSIA E POZICIONIMIT - SAKTËSIA ABSOLUTE OSE E JASHTME (POSITIONAL ACCURACY - ABSOLUTE OR EXTRENAL ACCURACY)
Rekomandim
Saktësia absolute ose e jashtme duhet të vlerësohet dhe dokumentohet duke përdorur vlerën mesatare të pa qartësive pozicionale nga IOS/DIS 19157 të specifikuar në tabelën e mëposhtme:
Shënim. Është praktikë e zakonshme në domeinin e Detit për të bërë një dallim në mënyrë të qartë midis saktësisë pozicionuese horizontale dhe saktësisë vertikale pozicionale. Prandaj, duhet të sigurohen dy masa të veçanta për saktësinë e pozicionit sipas SSH EN ISO 19157:2013
Emri
Vlera mesatare e të panjohurave pozicionale - komponenti horizontal
Emri alternativ
Cilësia e të dhënave të elementeve
Saktësia e pozicionimit
Cilësia e të dhënave të nën-elementeve
Saktësia absolute ose e jashtme
Cilësia e të dhënave të matjeve themelore
Ndryshimet rastësore 2-dimensionale X dhe Y
Përkufizimi
Vlera mesatare e pasigurive pozicionale për një grup pozicionesh ku pasiguritë pozitive janë përcaktuar si distanca ndërmjet një pozicioni të matur dhe asaj që konsiderohet si pozicioni përkatës i vërtetë.
Përshkrimi
Gabimi Mesatar Kuadratik (GMK = RMSE në anglisht) - Është rrënja katrore e mesatares së ndryshimeve në katror ndërmjet vlerave të koordinatave të një grupi të dhënash të matura dhe vlerave të koordinatave nga një burim i pavarur i saktësisë më të lartë për pikat identike. GMK dallon dy raste :
Rasti 1 - Kur llogariten gabimet e mundshme vi
: :
Ku:
vi - gabimi i mundshëm që llogaritet si diferencë e vlerës përfaqësuese me vlerën e matur.
- Vlera përfaqësuese që merret si vlera mesatare e vlerave të matura xi
n - Numri i matjeve
Saktësia pozicionale e përcaktuar nga të dhënat e kontrolluara:
Saktësia Horizontale
ku:
janë koordinat horizontale e pikave të kontrolluara në grupin e të dhënave.
- janë koordinatat e pikave të kontrolluara nga burime të pa varura të një saktësie më të lartë
- është numri i pikave të testuara
- është numri përkatës i pikës.
Gabimi horizontal i pikës përcaktohet nga:
Nëse nga llogaritjet kemi ,
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale dhe të pavarura në secilin komponent (x, z) një koeficient (faktor) 2.4477 përdoret për të llogaritur saktësinë horizontale me nivel besimi 95% (Greenwalt and Schultz 1968). Kur zbatohen kushtet e mësipërme,, vlera e saktësisë horizontale referuar NSSDA duhet të llogaritet nga formula:
Saktësia Vertikale
ku:
janë koordina vertikale e pikave të kontrolluara në grupin e të dhënave.
- janë koordinata vertikale e pikave të kontrolluara nga burime të pa varuara të një saktësie më të lartë
- është numri i pikave të testuara
- është numri përkatës i pikes.
Supozohet sikur gabimet sistematike janë eliminuar në mënyrën më të mirë të mundshme. Nëse gabimet janë të shpërndara në mënyrë normale, një koeficient (faktor) 1.9600 përdoret për të llogaritur saktësinë vertikale me nivel besimi 95% (Greenwalt and Schultz 1968). Nga kjo, saktësia vertikale, e raportuar sipas NSSDA duhet të llogaritet nga formula:
Fusha e vlerësimit
Llojet e objekteve gjeohapësinore: ZonaDetare, Deti, ZonaEQarkullimitDetar, ZonaNdërbaticore, Bregdeti, VijaBregdetare, IzovijatDetare
Fusha e raportimit
Llojet e objekteve gjeohapësinore: ZonaDetare, Deti, ZonaEQarkullimitDetar, ZonaNdërbaticore, Bregdeti, VijaBregdetare, IzolinjatDetare
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Matjet
Cilësia e të dhënave të strukturës së vlerave
Vlera e vetme: një shprehje e saktësisë pozicionale për komponentin horizontal pritet vetëm këtu.
Burim reference
SSH EN ISO 19157:2013 Informacion Gjeografik - Cilësia e të dhënave
Shembull
10 metra
Masa identifikuese
28
3.4.5 PËRDORIMI (USABILITY)
Rekomandim:
Përdorshmëria duhet të vlerësohet dhe dokumentohet duke përdorur treguesin e korrektësisë nga SSH EN ISO 19157:2013 siç specifikohet në tabelën më poshtë.
Emri
Vlera mesatare e paqartësive pozicionale - komponenti vertikal
Emri alternativ
Cilësia e të dhënave të elementeve
Përdorimi
Cilësia e të dhënave të nën elementeve
-
Cilësia e të dhënave të matjeve themelore
Treguesi i korrektësisë
Përkufizimi
Një deklaratë e cilësisë së përgjithshme të të dhënave përfshin çdo informacion të rëndësishëm që mund të ndikojë në qëllimet për të cilat përdoren të dhënat.
Përshkrimi
Kjo është një masë përshkruese e cila duhet të ofrojë çdo informacion shtesë të rëndësishëm në lidhje me cilësinë e përgjithshme të të dhënave, të grupit të të dhënave.
Fusha e vlerësimit
Grup të dhënash
Fusha e raportimit
Grup të dhënash
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
DQ_RezultatiPërshkrues
Cilësia e të dhënave të strukturës së vlerave
Vlera e vetme: një varg tekstesh
Burimi referencës
SSH EN ISO 19157:2013 Informacion Gjeografik - Cilësia e të dhënave
Shembulli
“Ky grup të dhënash është certifikuar sipas miratimit të X
procedure”
Shembulli
“Dihet që ka disa të dhëna që mungojnë në rajonin X për shkak të
dështimit të instrumentit”
Masa identifikuese
Cilësia e të dhënave të strukturës së vlerave
-
Burimi referencës
SSH EN ISO 19157:2013 Informacion Gjeografik - Cilësia e të dhënave
Shembulli
Paraqitja e artikujve në mbulesën që mbivendoset me domeinin:
Mbulimi përmban pika/poligone me atribute jashtë atributeve të domeinit (p.sh. kodet e klasës jo ekzistuese)
Masa identifikuese
14
4. ANEKSE
4.1 ANEKSI A - KATALOGU I TIPOLOGJISË
Nr.
Emri i elementit Anglisht
Emri i elementit Shqip
Nëntema
Tipi
DETET
3.1.5.1
SeaArea
ZonëDetare
Detet - SeaRegions
FeatureType
3.1.5.2
Sea
Deti
Detet - SeaRegions
FeatureType
3.1.5.3
MarineCirculationZone
ZonaEQarkullimitDetar
Detet - SeaRegions
FeatureType
3.1.5.4
IntertidalArea
ZonaNdërbaticore
Detet - SeaRegions
FeatureType
3.1.5.5
MarineExtent
ShtrirjaDetare
Detet - SeaRegions
DataType
3.1.5.6
ParameterValuePair
VleraEParametrave
Detet - SeaRegions
DataType
3.1.5.7
Shoreline
Bregdeti/TokëELagur
Detet - SeaRegions
FeatureType
3.1.5.8
Coastline
VijëBregdetare
Detet - SeaRegions
FeatureType
3.1.5.9
ShoreSegment
SegmentBregdetar
Detet - SeaRegions
FeatureType
3.1.5.10
MarineLayer
ShtresëDetare
Detet - SeaRegions
FeatureType
3.1.5.11
SeaSurfaceArea
SipërfaqeEZonësDetare
Detet - SeaRegions
FeatureType
3.1.5.12
SeaBedArea
SipërfaqjaETabanitTëDetit
Detet - SeaRegions
FeatureType
3.1.5.13
MarineIsoline
IzolinjëDetare
Detet - SeaRegions
DataType
3.1.5.14
MarineContoure
KonturiDetar
Detet - SeaRegions
FeatureType
3.1.5.15
SeaAreaTypeClassificationValue
VleratEKlasifikimitTëZonaveDetare
Detet - SeaRegions
CodeList
3.1.5.16
SeaBedCoverValue
VleratEMbulesësSëTabanitTëDetit
Detet - SeaRegions
CodeList
3.1.5.17
SeaSurfaceClassificationValue
VleratEKlasifikimitTëSipërfaqesSëDetit
Detet - SeaRegions
CodeList
3.1.5.18
ShoreStabilityValue
VleratEQëndrueshmërisëSëBregdetit
Detet - SeaRegions
CodeList
3.1.5.19
ShoreTypeClassificationValue
VleratEKlasifikimitTëLlojitTëBregdetit
Detet - SeaRegions
CodeList
3.1.5.20
ZoneTypeValueCodelist
VleratELlojeveTëZonave
Detet - SeaRegions
CodeList
4.2 ANEKSI B - KODLISTAT
Kodlista
VleratEKlasifikimitTëZonësDetare
VleratEMbulesësSëTabanitTëDetit
VleratEKlasifikimitTëSipërfaqesSëDetit
VleraEQëndrueshmërisëSëBregdetit
VleratEKlasifikimitTëLlojitTëBregdetit
VleraELlojeveTëZonave
4.2.1 VLERAT E KLASIFIKIMIT TË ZONAVE DETARE
Emri: Vlerat e klasifikimit të zonës detare
Përkufizimi: Llojet e klasifikimit të ZonësDetare, p.sh grykëderdhje.
Identifikuesi: http://inspire.ec.europa.eu/codeList/SeaAreaTypeClassificationValue
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
Kodlistë
-- Emri --
Zonë thyerje
-- Përkufizimi --
Zona detare është një zonë thyerje.
-- Emri --
Deltë
-- Përkufizimi --
Zona detare është një deltë.
-- Emri --
Grykëderdhje e gjerë
-- Përkufizimi --
Zona detare është një grykëderdhje e gjerë .
-- Emri --
Oqean i hapur
-- Përkufizimi --
Zona detare është një det i hapur.
-- Emri --
Shelfi detar
-- Përkufizimi --
Zona detare është një shelf detar.
4.2.2 VLERAT E MBULESËS SË TABANIT TË DETIT
Emri: Vlerat e mbulesës së tabanit të detit
Përkufizimi: Llojet e mbulesave të gjetura në shtratin e detit
Përshkrimi: Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Kodlistë
-- Emri --
Rërë
-- Përkufizimi --
Sipërfaqe me rërë.
-- Emri --
Baltë
-- Përkufizimi --
Sipërfaqe me baltë.
-- Emri --
Argjilë
-- Përkufizimi --
Sipërfaqe me argjilë.
-- Emri --
Lym (llum)
-- Përkufizimi --
Sipërfaqe me lym
-- Emri --
Gurë
-- Përkufizimi --
Sipërfaqe me gurë.
-- Emri --
Zhavorr
-- Përkufizimi --
Sipërfaqe me zhavorr.
-- Emri --
Guralecë
-- Përkufizimi --
Sipërfaqe me guralecë.
-- Emri --
Qymyr
-- Përkufizimi --
Sipërfaqe me qymyr.
-- Emri --
Shkëmb
-- Përkufizimi --
Sipërfaqe shkëmbore.
-- Emri --
Koral
-- Përkufizimi --
Sipërfaqe me korale.
-- Emri --
Guaska
-- Përkufizimi --
Sipërfaqe me guaska.
-- Emri --
Barishte
-- Përkufizimi --
Sipërfaqe me barishte, përfshirë leshterikë.
-- Emri --
Dallgë rëre
-- Përkufizimi --
Sipërfaqe me dallgë rëre (fund i lëvizshëm).
-- Emri --
Burime ujore
-- Përkufizimi --
Sipërfaqe me burime ujore në shtratin e detit.
4.2.3 VLERAT E KLASIFIKIMIT TË SIPËRFAQES SË DETIT
Emri: Vlerat e klasifikimit të sipërfaqes së detit
Përkufizimi: Llojet e shtresave sipërfaqësore të detit që gjenden në sipërfaqet e detit.
Përshkrim: Kodlista për llojet e shtresave sipërfaqësore të detit që gjenden në sipërfaqet e detit.
Kodlistë
-- Emri --
Akull
-- Përkufizimi --
Sipërfaqja e detit është akull.
-- Emri --
Vaj (naftë)
-- Përkufizimi --
Sipërfaqja e detit është vaj/naftë.
-- Emri --
Borë
-- Përkufizimi --
Sipërfaqja e detit është borë ose borë e shkrirë.
-- Emri --
Mbeturina
-- Përkufizimi --
Sipërfaqja e detit është me mbeturina.
-- Emri --
Alga
-- Përkufizimi --
Sipërfaqja e detit është me alga.
4.2.4 VLERA E QËNDRUESHMËRISË SË BREGDETIT
Emri: Vlerat e qëndrueshmërisë së bregdetit
Përkufizimi: Llojet e qëndrueshmërisë së segmenteve të bregdetit.
Përshkrim: Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave
Identifikuesi: http://inspire.ec.europa.eu/codeList/ShoreStabilityValue
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
Kodlistë
-- Emri --
I qëndrueshëm
-- Përkufizimi --
Shtrirja e bregut është e qëndrueshme.
-- Emri --
Tendenca të mundshme të erozionit
-- Përkufizimi --
Shtrirja e bregut është me tendenca të mundshme të erozionit.
-- Emri --
Tendenca të konfirmuara të erozionit
-- Përkufizimi --
Shtrirja e bregut është me tendenca të konfirmuara të erozionit.
-- Emri --
Trendi i rritjes së mundshme
-- Përkufizimi --
Shtrirja e bregut është ndoshta duke u rritur.
-- Emri --
Trendi i konfirmuar i rritjes
-- Përkufizimi --
Shtrirja e bregut konfirmohet të jetë në rritje.
-- Emri --
I panjohur
-- Përkufizimi --
Stabiliteti i shtrirjes së bregut është i panjohur.
4.2.5 VLERAT E KLASIFIKIMIT TË LLOJEVE TË BREGDETIT
Emri: Vlerat e klasifikimit të llojeve të bregdetit
Përkufizimi: Llojet e segmenteve të bregut.
Përshkrim: Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave
Identifikuesi: http://inspire.ec.europa.eu/codeList/ShoreTypeClassificationValue
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
Kodlistë
-- Emri --
Grykëderdhje e gjerë
-- Përkufizimi --
Lloji i bregut është grykëderdhje e gjerë /grykë lumore
-- Emri --
Shkëmb
-- Përkufizimi --
Lloji i bregut është shkëmbor
-- Emri --
Rërë
-- Përkufizimi --
Lloji i bregut është ranor.
-- Emri --
Kënetë baticore
-- Përkufizimi --
Lloji i bregut është kënetë baticore.
-- Emri --
Breg i ngushtë vegjetativ
-- Përkufizimi --
Lloji ibregut është breg i ngushtë vegjetativ.
-- Emri --
Bregdet artificial
-- Përkufizimi --
Lloji i bregut është breg artificial.
-- Emri --
Zall
-- Përkufizimi --
Lloji i bregut është zall.
-- Emri --
Baltë
-- Përkufizimi --
Lloji i bregut është baltë.
4.2.6 VLERAT E LLOJEVE TË ZONAVE
Emri: Vlerat e llojeve të zonave
Përkufizimi: Llojet e zonave të qarkullimit detar
Përshkrim: Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
Kodlistë
-- Emri --
Zonë e përzier
-- Përkufizimi --
Zona është një zonë e përzier.
-- Emri --
Zonë sedimentare
-- Përkufizimi --
Zona është një zonë sedimentare.
-- Emri --
Ujëra bregdetare
-- Përkufizimi --
Zona është zonë me ujëra bregdetare.
