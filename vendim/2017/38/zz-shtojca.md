# Shtojca
RREGULLAT
E NDËRVEPRUESHMËRISË
TË TË DHËNAVE, GRUPEVE TË TË DHËNAVE DHE SHËRBIMEVE GJEOHAPËSINORE
KREU I
FUSHA E VEPRIMIT DHE PËRKUFIZIME
Fusha e veprimit
Ky dokument përcakton rregullat dhe kërkesat për përgatitjet teknike për ndërveprimin dhe, kur është e mundur, harmonizimin e të dhënave, grupeve të të dhënave dhe shërbimeve gjeohapësinore, që i përkasin temave të nenit 11, të ligjit nr. 72, datë 28.6.2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”.
Përkufizime
Për qëllime të këtij dokumenti, do të përdoren përkufizimet e mëposhtme:
“Tipi abstrakt” nënkupton një element i cili nuk është element real në terren, por konsiderohet vetëm si fenomen. (Ka të njëjtin kuptim me atë të përdorur në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për temat e nenit 11, të ligjit nr. 72/2012).
“Rol shoqërimi” nënkupton një vlerë ose objekt, me të cilët një tip ka një lidhje, siç referohet në nenin 18, të ligjit nr. 72/2012.
“Atribut” nënkupton një karakteristikë të një tipi, siç referohet në nenin 18, të ligjit nr. 72/2012.
“Kod - listë” nënkupton një listë vlerash të përcaktuara. Në dokument gjenden të shqipëruara si “Numërtimet dhe kod-listat”. (Ka të njëjtin kuptim me atë të përdorur në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për temat e nenit 11, të ligjit nr. 72/2012).
“Data - type” nënkupton një element tabelor i cili shërben vetëm si tabelë atributesh për t’u lidhur me një element tjetër. (Ka të njëjtin kuptim me atë të përdorur në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për temat e nenit 11, të ligjit nr. 72/2012). Në përputhshmëri me ISO/TS 19103:2005.
“Numërtimet” nënkupton një renditje vlerash. Listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. (Ka të njëjtin kuptim me atë të përdorur në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për temat e nenit 11, të ligjit nr. 72/2012).
“Identifikues i jashtëm i objektit” nënkupton një identifikues unik objektesh, i cili krijohet nga autoriteti përgjegjës, që mund të përdoret nga aplikimet e jashtme për të referuar objektin gjeohapësinor.
“Identifikues” nënkupton një vijimësi të pavarur karakteresh të aftë për të identifikuar në mënyrë unike një element të caktuar.
“Ilustrim me shembull konkret” nënkupton të krijosh një objekt që është në përputhje me përkufizimin, atributet, rolet e shoqërimit dhe kufizimet e specifikuara për tipin e ilustruar me shembull konkret.
“Shtresë” nënkupton njësinë themelore të informacionit gjeografik që mund të kërkohet në hartë nga një server. (Ka të njëjtin kuptim me atë të përdorur në “Rregullat për shërbimet e rrjetit”.)
“Cikli jetësor” nënkupton historinë e një grupi të dhënash, ciklin e jetës së tyre nga mbledhja, përdorimi dhe përditësimi i tyre deri në formën aktuale, në përputhje me EN ISO 19101. (Ka të njëjtin kuptim me atë të përdorur në vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për miratimin e rregullores “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”).
“Element i metadatave” nënkupton një njësi diskrete të metadatës, në përputhje me EN ISO 19115. (Ka të njëjtin kuptim me atë të përdorur në vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për miratimin e rregullores “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”).
“Paketë” nënkupton një grup elementesh me karakteristika të përbashkëta me qëllim organizimin e tyre.
“Regjistër” nënkupton një grup skedarësh që përmbajnë identifikues të caktuar për artikujt, shoqëruar me përshkrime të tyre.
“Tipi i objektit gjeohapësinor” nën-kupton një klasifikim të objekteve gjeohapësinore sipas një tipologjie të caktuar.
“Stil” nënkupton veçori të objekteve gjeohapësinore dhe kufizimeve në simbole të parametrizuara, që përdoren në hartë.
17. “Tip” nënkupton tipin e objektit gjeo-hapësinor ose të të dhënave gjeohapësinore.
18. “Nëntip” nënkupton një marrëdhënie mes një tipi specifik e një tipi më të përgjithshëm, ku tipi specifik është plotësisht në përputhshmëri me tipin e përgjithshëm dhe përmban informacion shtesë.
19. “I shmangshëm” (voidable) nënkupton që një atribut ose rol shoqërimi me vlerë ’e shmangshme’ (void) mund të bëhet e disponueshme, nëse përfshihet një vlerë korresponduese në grupet e të dhënave gjeohapësinore, përcaktuar nga autoritetet përgjegjëse. Nëse një atribut ose rol shoqërimi nuk është i shmangshëm, kuadrati i tabelës që specifikon të qenit i shmangshëm lihet bosh.
20. “Karakteristika” nënkupton atribut ose rol shoqërimi (association role).
21. “Tip bashkimi” nënkupton një tip që përbëhet nga një ose vetëm një nga disa alternativa (listuar si atribute pjesëmarrëse), në përputhje me ISO/TS 19103:2005.
22. “Kategori shoqërimi” nënkupton një tip që përcakton tipare shtesë në një marrëdhënie mes dy tipash të tjerë.
23. “Mbulim” (Coverage), funksionet “Coverage” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe/ose hapësirë. Shembuj tipikë janë temperaturat, lartësitë, precipitimet, imazheria etj. Një “Coverage” përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-hapësinor, në përputhje me ISO 19123:2007.
24. “Domain” nënkupton një bashkësi vlerash të mirëpërcaktuara, në përputhje me ISO/TS 19103:005.
25. “Gamë” nënkupton një grup vlerash, atributesh e tiparesh të shoqëruara nga një funksion me elemente të domain-it.
26. “Rrjet koordinativ i rektifikuar (transformuar)” nënkupton një rrjet koordinativ për të cilin ka një transformim afin përkatës mes koordinatave të rrjetit dhe koordinatave të një sistemi referimi koordinativ.
27. “Rrjet koordinativ referues” nënkupton një rrjet, të shoqëruar me një transformim, që mund të përdoret për të shndërruar vlerat e rrjetit të koordinatave në vlera koordinatash referuar një sistemi të jashtëm referimi, sipas EN ISO 19123:2007.
28. “Mozaik” nënkupton një ndarje të hapësirës në një grup nënhapësirash fqinje duke pasur të njëjtin dimension në hapësirën e ndarë. Një mozaik në një hapësirë 2D përbëhet nga një grup shumëkëndëshash pa mbivendosje, që mbulojnë krejtësisht një rajon interesash.
29. “Vlera paraardhëse” nënkupton një vlerë që ka marrëdhënie hierarkike me një vlerë mëmë më të përgjithshme.
30. “Offset” nënkupton mbivendosje të vlerës së një atributi, kryesisht i shprehur në sistemin binar 1/0. 1 tregon vlerat negative ndërsa zero vlerat pozitive. Gjithmonë i referohet një vlere të mëparshme.
31. “Tipologji” nënkupton një element i cili mund të jetë real në terren apo një fenomen abstrakt. (Ka të njëjtin kuptim me atë të përdorur në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për temat e nenit 11, të ligjit nr. 72/2012).
KREU II
RREGULLA TË PËRGJITHSHME
Tipat e zakonshëm
Tipat që janë të zakonshëm për një numër temash të nenit 11, të ligjit nr. 72/2012, duhet të përputhen me përkufizimet, kufizimet dhe duhet të përfshijnë atributet dhe rolet e shoqërimit, të përcaktuara në kreun III.
Tipat për shkëmbimin dhe klasifikimin e objekte gjeohapësinore
a) Për shkëmbimin dhe klasifikimin e objekteve gjeohapësinore nga grupet e të dhënave që plotësojnë kushtet e nenit 2, të ligjit nr.72/2012, autoritetet përgjegjëse do të përdorin tipat e objekteve gjeohapësinore dhe data-type-ve të shoqërimit, numërtimet dhe kod-listat, që janë të përcaktuara në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor për çdo temë të nenit 11, të ligjit nr. 72/2012, për motivet me të cilat lidhen grupet e të dhënave.
b) Tipat e objekteve gjeohapësinore dhe data-type-ve do të përputhen me përkufizimet dhe kufizimet dhe do të përfshijnë atributet e rolet e shoqërimit, të përcaktuara në këto standarde.
c) Numërtimet dhe kod-listat e përdorura në atributet apo rolet e shoqërimit të tipave të objekteve gjeohapësinore ose data-type-ve, do të përputhen me përkufizimet dhe do të përfshijnë vlerat e përcaktuara në standardin përkatës për çdo temë.
ç) Renditja dhe vlerat e kod-listës identifikohen në mënyrë unike nga kodet unike të gjuhës së programimit për kompjuterat. Vlerat mund edhe të përfshijnë një emër të një gjuhe specifike për t’u përdorur nga përdoruesit e thjeshtë.
3. Tipat
a) Për të gjitha tipat e përcaktuar në këto rregulla jepet një emër neutral për gjuhën kompjuterike mes thonjëzave në titullin e pjesës ku specifikohen kërkesat për këtë tip. Ky emër i gjuhës kompjuterike do të përdoret për t’iu referuar tipit korrespondues në përkufizimin e një atributi ose roli shoqërimi.
b) Tipat që janë një nëntip i një tipi tjetër do të përfshijnë gjithashtu të gjitha atributet e këtij tipi dhe rolet e tij të shoqërimit.
c) Tipat abstrakte nuk do të ilustrohen me shembuj konkretë.
4. Numërtimet dhe kod-listat
4.1 Kod-listat do të jenë njëra nga tipat vijues, siç janë specifikuar në “Standardet shtetërore për specifikimet teknike të informacionit gjeohapësinor në Shqipëri” për çdo temë të nenit, 11, të ligjit nr. 72/2012.
a) Kod-listat, vlerat e lejuara të të cilave përbëhen vetëm nga vlerat e specifikuara në këto rregulla;
b) Kod-listat, vlerat e lejuara të të cilave përbëhen nga vlerat e specifikuara në këto rregulla dhe vlerat më të rëndësishme, të përcaktuara nga ofruesit e të dhënave;
c) Kod-listat, vlerat e lejuara të të cilave përbëhen nga vlerat e specifikuara në këto rregulla dhe vlerat shtesë të çdo niveli, të përcaktuara nga ofruesit e të dhënave;
ç) Kod-listat, vlerat e lejuara të të cilave përbëhen nga çdo vlerë e përcaktuar nga ofruesit e të dhënave.
4.2 Kod-listat mund të jenë hierarkike. Vlerat hierarkike të kod-listave mund të kenë një vlerë mëmë më të përgjithshme. Aty ku vlerat e vlefshme të një kod-liste specifikohen në një tabelë në këto rregulla, vlerat mëmë janë listuar në shtyllën e fundit.
4.3 Aty ku për një atribut, tipi i të cilit është një kod-listë, siç referohet në shkronjat “b”, “c” ose “ç”, të nënpikës 4.1, një ofrues të dhënash jep një vlerë, që nuk është specifikuar në këto rregulla, ajo vlerë dhe përkufizimi i saj do të bëhen të disponueshme në një regjistër.
4.4 Atributet ose rolet e shoqërimit të tipave të një objekti gjeohapësinor ose data-type-ve, tipi i të cilave është një kod-listë, mund të marrë vetëm vlera që lejohen në përputhje me specifikimin në kod-listë.
4.5 Atributet ose rolet e shoqërimit të tipave të një objekti gjeohapësinor ose të data-type-ve, që kanë një tip numërtimi mund të marrin vlera vetëm nga listat e specifikuara për tipin e numërtimit.
5. Kodimi
a) Çdo rregull kodimi, i përdorur për të koduar të dhënat gjeohapësinore, duhet të jetë konform EN ISO 19118. Në veçanti, duhet të specifikojë rregullat e shndërrimit të skemës për të gjithë tipat e objekteve gjeohapësinore dhe të gjitha tiparet e rolet e shoqërimit, si dhe strukturën e përdorur të të dhënave si output.
b) Do të vihet në dispozicion çdo rregull kodimi i përdorur për të koduar të dhënat gjeohapësinore.
6. Përditësimet
Autoritetet përgjegjëse, për çdo temë, do të vënë në dispozicion të ASIG-ut rregullisht përditësimet e të dhënave.
b) Të gjitha përditësimet duhet të kryhen të paktën 6 muaj pas aplikimit të ndryshimit të grupeve të të dhënave burimore, pavarësisht se për përditësimet e të dhënave gjeohapësinore specifike janë caktuar periudha të ndryshme në standardet përkatëse të temës.
7. Menaxhimi i identifikuesit
a) Identifikuesi i data-type-ve, përcaktuar në pikën 2.1 të (kreut III), do të përdoret si një tip për identifikuesin e jashtëm të objektit si një objekt gjeohapësinor.
b) Identifikuesi i jashtëm i objektit për identifikimin unik të objekteve gjeohapësinore nuk do të ndryshojë gjatë ciklit të jetës së një objekti gjeohapësinor.
8. Cikli i jetës së objekteve gjeohapësinore
a) Versionet e ndryshme të të njëjtit objekt gjeohapësinor do të jenë gjithmonë shembuj të të njëjtit tip të objektit gjeohapësinor.
b) Tiparet e hapësirës së emrit dhe ID lokale të identifikuesit të objektit të jashtëm do të mbeten të njëjtë për versione të ndryshme të një objekti gjeohapësinor.
c) Aty ku përdoren tiparet, fillimi i ciklit jetësor dhe përfundimi i ciklit jetësor, vlera e përfundimi i ciklit jetësor nuk do të vendosen para vlerës së fillimi të ciklit jetësor.
9. Referenca kohore
a) Do të përdoret referenca kohore e përzgjedhur, referuar në vendimit nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë” nëse nuk janë specifikuar sisteme të tjera reference kohore për një motiv specifik të dhënash, në standardet përkatëse sipas temave.
b) Nëse përdoren sisteme të tjera reference kohore, këto do të specifikohen në metadatat e grupit të të dhënave të temës përkatëse.
10. Kërkesa dhe rregulla të tjera
a) Të gjitha vlerat e matjeve do të shprehen duke përdorur njësitë e sistemit SI ose njësitë jo-SI, të pranuara për përdorim në Sistemin Ndërkombëtar të Njësive, nëse nuk është specifikuar ndryshe për një motiv ose tip specifik të dhënash gjeohapësinore.
b) Aty ku përdoren tiparet, fillimi i ciklit jetësor dhe përfundimi i ciklit jetësor, vlera e përfundimi i ciklit jetësor nuk do të vendosen para vlerës së fillimit të ciklit jetësor.
c) Për më tepër, do të përdoren të gjitha kërkesat me motive specifike të përcaktuara në standardet përkatëse për çdo temë.
11. Metadatat e kërkuara për ndërveprimin
Metadatat përshkruajnë një grup të dhënash gjeohapësinore të cilat do të përfshijnë elementet e mëposhtme të metadatave, që kërkohen për ndërveprimin:
a) Sistemi koordinativ i referimit: Përshkrimi i sistemit/eve koordinativ/e të referimit të përdorura për grupin e të dhënave;
b) Sistemi i referencës kohore: Përshkrimi i sistemit/eve kohor/e të referimit të përdorura në grupin e të dhënave.
Ky element është i detyrueshëm vetëm nëse grupi i të dhënave gjeohapësinore përmban informacion kohor, që nuk i referohet sistemit të referencës kohore, të zgjedhur më parë.
a) Shërbim kodimi: Shërbim që ofron implementimin e rregullave të kodimit dhe ofron një ndërfaqe për funksionalitetet e kodimit dhe dekodimit. (Sipas vendimit nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për miratimin e rregullores “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”).
b) Konsistenca topologjike: Korrektësia e karakteristikave të koduara topologjike në mënyrë të qartë të grupit të të dhënave, siç përshkruhet nga domain.
Ky element është i detyrueshëm vetëm nëse grupi i të dhënave përfshin tipa nga modeli i përgjithshëm i rrjetit dhe nuk garanton topologji qendrore (lidhje me qendrat) për rrjetin.
a) Kodimi i karakterit: Kodimi i karakterit të përdorur në grupin e të dhënave. Ky element është i detyrueshëm vetëm nëse një kodim përdoret dhe nuk bazohet në UTF-8.
b) Tipi i prezantimit gjeohapësinor: Metoda e përdorur për të prezantuar në mënyrë gjeohapësinore informacionin gjeografik.
12. Paraqitja
Për paraqitjen e grupeve të të dhënave gjeohapësinore, që përdorin një shërbim rrjeti sipas “Rregullave të shërbimeve të rrjetit” do të vihen në dispozicion:
a) shtresat (layers), të specifikuara në standardet përkatëse për çdo temë për motivin ose motivet me të cilat lidhet grupi i të dhënave;
b) për secilën shtresë të paktën një stil paraqitjeje me parazgjedhje, duke pasur minimumi një titull shoqërimi dhe një identifikues unik.
12.2 Për secilën shtresë, standardi përkatës i temës përcakton:
a) një titull të lexueshëm nga njeriu, i shtresës për t’u përdorur për shfaqje në ndërfaqen e përdoruesit:
b) Tipi /et i objektit gjeohapësinor ose nëntipi, që përbën/jnë përmbajtjen e shtresës.
12.3 Për tipat e objekteve gjeohapësinore, objektet e të të cilave mund të klasifikohen më tej duke përdorur një atribut si kod-listë, mund të përcaktohen disa shtresa. Secila nga këto shtresa do të përfshijë objektet gjeohapësinore, që korrespondojnë me njërën nga vlerat specifike të kod-listës. Në përkufizimin e grupeve të shtresave në standardet përkatëse sipas temave do të përmbushen të gjitha kërkesat e mëposhtme:
a) variabli <Vlera e kod-listës> përfaqëson vlerat e kod-listës përkatëse, ku shkronja e parë është kapitale;
b) variabli <Lexueshmëria e emrit> përfaqëson emrin e lexueshëm nga njeriu të vlerave të kod-listës;
c) tipi i objektit gjeohapësinor përfshin atributin përkatës dhe kod-listën, në thonjëza;
ç) do të jepet një shembull i shtresës.
KREU III
TIPAT E ZAKONSHËM, PËRKUFIZIMET DHE KËRKESAT
1. TIPAT E PËRCAKTUAR NË STAN-DARDET EVROPIANE DHE NDËR-KOMBËTARE
Tipat e mëposhtëm, të përdorur më shpesh si atribute apo role shoqërimi të tipave, të objekteve gjeohapësinore ose të tipave të të dhënave gjeohapësinore, përkufizohen si vijon:
Për tipat: Kënd, sipërfaqe, tipi boolean, varg karakteresh, datë, data-ora, tipi decimal, distancë, tipi integer, gjatësi, matje, numër, probabilitet, real, tipi i regjistrimit, nënshkrim, njësi matëse, shpejtësi dhe volum do të zbatohen përkufizimet e dhëna në ISO/TS 19103:2005.
1.2 Për tipat: (Direct Position), (GM_Boundary), (GM_Curve), (GM_MultiCurve), (GM_Multi-Surface), (GM_Object), (GM_Point), (GM_Primitive), (GM_Solid), (GM_Surface) dhe (GM_Tin) do të përdoren përkufizimet e dhëna në standardet përkatëse sipas temave.
1.3 Për tipat: (TM_Duration), (TM_Geometric -Primitive), (TM_Instant), (TM_Object), (TM_Period) dhe (TM_Position) do të zbatohen përkufizimet e dhëna në EN ISO 19108:2005 /AC:2008.
1.4 Për tipin (GF_PropertyType) do të zbatohen përkufizimet e dhëna në EN ISO 19109:2006.
1.5 Për tipat: (CI_Citation), (CI_Date), (CI_RoleCode), EX_Extent, EX_VerticalExtent, MD_Distributor, MD_Resolution dhe URL do të zbatohen përkufizimet e dhëna në EN ISO 19115:2005/AC:2008.
1.6 Për tipin (CV_SequenceRule) do të zbatohen përkufizimet e dhëna në EN ISO 19123:2007.
1.7 Për tipat: (AbstractFeature), (Quantity and Sign) do të zbatohen përkufizimet e dhëna në EN ISO 19136:2009.
1.8 Për tipat: (LocalisedCharacterString), (PT_FreeText) dhe URI do të zbatohen përkufizimet e dhëna në EN ISO/TS 19139:2009.
1.9 Për tipin LC_LandCoverClassificationSystem do të zbatohen përkufizimet e dhëna në ISO 19144-2:2012.
1.10 Për tipat: (GFI_Feature), (Location), (OM_Observation), (OM_Process), Sampling-Coverage Observation, SF_SamplingCurve, SF_Sampling Point, SF_SamplingSolid, SF_SamplingSurface dhe SF_Spatial SamplingFeature do të zbatohen përkufizimet e dhëna në ISO 19156:2011.
1.11 Për tipat: Kategori, sasi, gamë e sasisë dhe kohë do të zbatohen përkufizimet e dhëna sipas standardeve INSPIRE.
1.12 Për tipat TimeValuePair dhe Timeseries shpjegimi jepet sipas përkufizimeve të standardeve INSPIRE.
1.13 Për tipat CGI_LinearOrientation dhe CGI_PlanarOrientation shpjegimi jepet sipas përkufizimeve të standardeve INSPIRE.
2. DATA-TYPE TË PËRBASHKËTA
2.1 Identifikuesi
Identifikuesi i jashtëm i një objekti unik, të publikuar nga autoriteti përgjegjës, që mund të përdoret nga aplikimet e jashtme, referuar objektit gjeohapësinor.
Atributet e identifikuesit të data-type-ve
Atributi
Përkufizimi
Tipi
Shmangia
ID lokale
Një identifikues lokal, caktuar nga ofruesi i të dhënave. Identifikuesi lokal është unik brenda emrit, kjo do të thotë se nuk ka objekt tjetër gjeohapësinor që mbart të njëjtin identifikues unik.
Vargu i karaktereve
Emri i krijuesit
Emri që identifikon në mënyrë unike burimin e të dhënave të objektit gjeohapësinor.
Vargu i karaktereve
ID e versionit
Identifikuesi i versionit të veçantë të objektit gjeohapësinor, me një gjatësi maksimale prej 25 karakteresh. Nëse specifikimi i një tipi të objektit gjeohapësinor me një identifikues të jashtëm objekti përfshin informacionin e ciklit të jetës, versioni identifikues përdoret për të dalluar mes versioneve të ndryshme të një objekti gjeohapësinor. Brenda grupit të të gjitha versioneve të një objekti gjeohapësinor, versioni identifikues është unik.
Vargu i karaktereve
i shmangshëm
Palët përgjegjëse (RelatedParty)
Një autoritetit përgjegjës ose një person me një status të caktuar, që lidhet me një burim.
Atributet e identifikuesit të data-type-ve
Atributi
Përkufizimi
Tipi
Shmangia
Emri individual
Emri i personit përkatës.
Tekst i lirë PT
i shmangshëm
Autoriteti përgjegjës
Emri i autoritetit përgjegjës sipas vendimit të ASIG-ut.
Tekst i lirë PT
i shmangshëm
Titulli i pozicionit
Pozicioni i palës pjesëmarrëse në lidhje me një burim, siç është kreu i departamentit.
Tekst i lirë PT
i shmangshëm
Kontakti
Informacioni i kontaktit për palën pjesëmarrëse përkatëse.
Kontakti
i shmangshëm
Roli
Rolet e palës pjesëmarrëse në lidhje me një burim, siç është pronari.
Vlera e rolit të palës
i shmangshëm
2.3 Kufizimet e të dhënave të kontaktit për palët përgjegjëse.
Të paktën do të jepet individi, autoritetit përgjegjës ose emërtimi i pozicionit.
Kontakti
Kanalet e komunikimit me të cilat është e mundur marrja e aksesit për dikë ose diçka.
Atributet e identifikuesit të tipi të të dhënave të kontaktit
Atributi
Përkufizimi
Tipi
Shmangia
Adresa
Adresë e dhënë si tekst i lirë.
Paraqitja e adresës
i shmangshëm
Udhëzimet e kontaktit
Udhëzime shtesë se si apo kur të kontaktoni një individ ose organizatë.
Tekst i lirë PT
i shmangshëm
Adresa e postës elektronike
Adresa e kutisë së postës elektronike të një organizate ose individi.
Vargu i karaktereve
i shmangshëm
Orët e shërbimit
Periudhat kohore kur autoriteti përgjegjës apo individi mund të kontaktohet.
Tekst i lirë PT
i shmangshëm
Telefoni fax-e-mail
Nr. i telefonit fax-email të autoritetit përgjegjës ose individit.
Vargu i karaktereve
i shmangshëm
Telefon
Numri i telefonit të autoritetit përgjegjës ose individit.
Vargu i karaktereve
i shmangshëm
Website zyrtar
Faqet e ofruara në web nga autoriteti përgjegjës ose individi.
URL
i shmangshëm
2.4 Citim i dokumenti (DocumentCitation)
Citim për qëllim të referimit të qartë të një dokumenti.
Atributet e data-type-ve për citimin e dokumentit
Atributi
Përkufizimi
Tipi
Shmangia
Emri
Emri i dokumentit.
Vargu i karaktereve
Emri i shkurtuar
Emër i shkurtër ose titull alternativ i dokumentit.
Vargu i karaktereve
i shmangshëm
Data
Data e krijimit, botimit ose rishikimit të dokumentit.
CI_Date
i shmangshëm
Lidhja
Lidhja e një versioni on-line të dokumentit
URL
i shmangshëm
Referencë specifike
Referencë për një pjesë specifike të dokumentit.
Vargu i karaktereve
i shmangshëm
2.5 Citimi i legjislacionit (LegislationCitation)
Citim për qëllim të referimit të qartë të një akti ligjor ose një pjese specifike të një akti ligjor.
Ky tip është një nëntip i citimit të dokumentit.
Atributet e data-type-ve të citimit të legjislacionit
Atributi
Përkufizimi
Tipi
Shmangia
Numër identifikimi
Kodi i përdorur për të identifikuar instrumentin legjislativ
Vargu i karaktereve
Nr. i dokumentit zyrtar
Numri i dokumentit zyrtar i përdorur për të identifikuar në mënyrë unike instrumentin legjislativ.
Vargu i karaktereve
Data e hyrjes në fuqi
Data e instrumentit legjislativ të hyrë në fuqi.
TM Position
Data e shfuqizimit
Data e shfuqizimit të instrumentit legjislativ
TM Position
Niveli
Niveli me të cilin është miratuar instrumenti legjislativ.
Vlera e nivelit
legjislativ
Citimi i faqes zyrtare
Citimi i faqes zyrtare me të cilën është botuar legjislacioni. (www.qbz.gov.al)
Gazeta zyrtare në
formim
Atributet e data-type-ve të citimit të legjislacionit
Nëse atributi i lidhjes është i pavlefshëm, do të ofrohet citimi nga faqja zyrtare.
2.6 Informacioni i Fletores Zyrtare
Citim i plotë i vendndodhjes së instrumentit legjislativ brenda faqes zyrtare.
Atributet e data-type-ve të informacionit në Fletoren Zyrtare
Atributi
Përkufizimi
Tipi
Shmangia
Identifikimi i faqes zyrtare
Referencë për vendndodhjen brenda gazetës zyrtare brenda së cilës është botuar instrumenti legjislativ. Kjo referencë do të përbëhet nga tre pjesë:
titulli i gazetës zyrtare
volumi dhe/ose numri i serisë
Numri(at) e faqes
Vargu i karaktereve
ISSN
Numri serial i Standardit Ndërkombëtar (ISSN) është një numër tetëshifror, që identifikon publikimin periodik në të cilën është botuar instrumenti legjislativ.
Vargu i karaktereve
ISBN
Numri i librit të Standardit Ndërkombëtar (ISBN) është një numër nëntëshifror, që identifikon në mënyrë unike librin në të cilën është botuar instrumenti legjislativ.
Vargu i karaktereve
Linku i faqes zyrtare
Lidhja me një version on-line të Fletores Zyrtare
URL
2.7 Identifikuesi tematik
Identifikuesi tematik që do të identifikojë në mënyrë unike objektin gjeohapësinor.
Atributet e data-type-ve të identifikuesit tematik
Atributi
Përkufizimi
Tipi
Shmangia
Identifikuesi
Identifikuesi unik i përdorur për të identifikuar objektin gjeohapësinor brenda skemës së specifikuar të identifikimit.
Vargu i karaktereve
Skema e identifikuesit
Identifikuesi që përcakton skemën e përdorur për të caktuar identifikuesin.
Vargu i karaktereve
3. NUMËRTIMET E PËRBASHKËTA
3.1 Vlerat e pozicionit vertikal
Vlera
Përkufizimi
Në sipërfaqen e tokës
Objekti gjeohapësinor është në nivelin e tokës
Ndërmjetëm
Objekti gjeohapësinor është pezull ose në hapësirë
Nëntokë (nën ujë)
Objekti gjeohapësinor është nëntokësor (nënujor)
Pozicioni vertikal përkatës i një objekti gjeohapësinor.
Vlerat e lejuara për numërtimet e pozicionuara vertikalisht.
4. KOD-LISTAT E PËRBASHKËTA
4.1 Vlerat e gjendjes së objektit
Gjendja e një objekti për sa i përket përfundimit dhe përdorimit të tij.
Vlerat e lejuara për këtë kod-listë përbëjnë vlerat në tabelën e mëposhtme dhe vlerat më të domosdoshme, përcaktuar nga ofruesit e të dhënave.
Vlerat për kod-listën mbi gjendjen e objektit
Vlera
Emri
Përkufizimi
Funksional
funksional
Objekti është funksional.
Projektuar
projektuar
Objekti po projektohet. Ndërtimi nuk ka filluar ende.
Proces ndërtimi
proces ndërtimi
Objekti është në ndërtim e sipër dhe nuk është ende funksional. Kjo përdoret vetëm për ndërtimin fillestar të objektit dhe jo për mirëmbajtjen e punës.
Nxjerrë nga përdorimi
nxjerrë nga përdorimi
Objekti nuk përdoret më, por nuk po hiqet dhe nuk është hequr nga shërbimi.
Hequr nga shërbimi
hequr nga shërbimi
Objekti nuk përdoret më dhe nuk po hiqet dhe nuk është hequr nga shërbimi.
4.2 Kodi i shtetit
Kodi i shtetit siç është përcaktuar në udhërrëfyesin e stilit ndërinstitucional, botuar nga Zyra e Botimeve të Bashkimit Evropian.
Vlerat e lejuara për këtë kod-listë përbëhen vetëm nga vlerat e specifikuara në tabelën e mëposhtme.
Vlerat e lejuara për këtë kod-listë janë kodet me dy shkronja të shtetit të listuar në udhërrëfyesin e stilit ndërinstitucional, botuar nga Zyra e Botimeve të Bashkimit Evropian.
4.3 Niveli i legjislacionit
Niveli me të cilin është miratuar një akt ligjor ose konventë.
Vlerat e lejuara për këtë kod-listë përbëhen nga vlerat e përcaktuara nga ofruesit e të dhënave.
Ofruesit e të dhënave mund të përdorin vlerat e specifikuara në standardet përkatëse për çdo temë, sipas udhëzuesve teknikë të INSPIRE-s.
4.4 Roli i palës përgjegjëse
Rolet e palëve pjesëmarrëse që lidhen ose janë përgjegjëse për një burim të caktuar.
Vlerat e lejuara për këtë kod-listë përbëjnë vlerat në kod-listat e mëposhtme ose kod- listat e tjera të përcaktuara nga ofruesit e të dhënave.
- Role Code (CI_RoleCode): Funksionet e kryera nga një palë përgjegjëse, e specifikuar si në EN ISO 19115:2005/AC:2008.
- Roli i një pale përgjegjëse (RelatedPartyRoleValue): Klasifikimi i roleve që lidhen me palën përgjegjëse, siç specifikohet në tabelën e mëposhtme.
Vlerat për kod-listën për rolin e palës përgjegjëse
Vlera
Emri
Përkufizimi
Autoriteti
autoriteti
Një autoritet mandatuar me ligj për të mbikëqyrur një burim dhe/ose palët lidhur me një burim të caktuar.
Operator
operator
Një autoritet i cili mbart një burim.
Pronari
pronari
Një autoritet i cili zotëron një burim, i përket një burim nga ana ligjore.
4.5 Emrat standart të klimës dhe parashikimit të motit
Përkufizimet e fenomeneve të vëzhguara në meteorologji dhe oqeanografi.
Vlerat e lejuara për këtë kod-listë përbëhen nga vlerat e përcaktuara nga ofruesit e të dhënave.
Ofruesit e të dhënave mund të përdorin vlerat e specifikuara në standardet përkatëse sipas temave në përputhje me dokumentet teknike të INSPIRE në Modelin e Përgjithshëm Konceptual të INSPIRE-s.
Gjinia
Gjinia e një personi ose grupi personash.
Vlerat e lejuara për këtë kolistë përbëhen vetëm nga vlerat e specifikuara në tabelën e mëposhtme.
Vlerat e kod-listës së gjinisë
5. MODEL I PËRGJITHSHËM I RRJETIT
Vlera
Emri
Përkufizimi
Femër
femër
Një person ose grup personash të seksit femër.
Mashkull
mashkull
Një person ose grup personash të seksit mashkull.
I pacaktuar
i pacaktuar
Një person ose grup personash të një seksi të pacaktuar.
5.1 Tipat e objektit gjeohapësinor
5.1.1 Referencë e tërthortë (CrossReference)
Përfaqëson një referencë mes dy elementeve në të njëjtin rrjet.
Rolet e shoqërimit të tipit të objektit gjeohapësinor me referencë të tërthortë
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Elementi
Elementet e referencës së tërthortë
Elementi i rrjetit
5.1.2 Lidhje e përgjithësuar (GeneralisedLink)
Tipi me bazë abstrakte përfaqëson një element rrejti linear, i cili mund të përdoret si një target në referencat lineare.
Ky tip është një nëntip i elementit të rrjetit.
Ky tip është abstrakt.
5.1.3 Kategoritë e kryqëzimeve të ndara (GradeSeparated- Crossing)
Tregon se cili nga dy ose më shumë elementet që kryqëzohen është/janë poshtë dhe cili/cilët është/janë sipër, për t’u përdorur nëse kuotat nuk janë të pranishme ose nuk janë të besueshme.
Ky tip është një nëntip i elementit të rrjetit.
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Elementi
Rendi i lidhjeve të kryqëzimit. Rendi reflekton lartësia e tyre; lidhja e parë është lidhja e poshtme.
lidhje
Rolet e shoqërimit të tipit të objektit gjeohapësinor për ndarjen në kategori të elementeve të kryqëzuara. (GradeSeparated- Crossing)
5.1.4 Lidhja
Elementet të kurbëzuara linearisht të rrjetit të cilat lidhin dy pozicione dhe që përfaqëson një rrugë homogjene në rrjet. Pikat e lidhura mund të paraqiten si nyje.
Ky tip është një nëntip i lidhjes së përgjithësuar.
Ky tip është abstrakt.
Atributet e objektit gjeohapësinor të tipit lidhje (Link)
Atributi
Përkufizimi
Tipi
Shmangia
Gjeometria e linjës qendrore (aksi)
Gjeometri që përfaqëson linjën qendrore të lidhjes.
GM_Curve
Imagjinare
Tregues që gjeometria qendrore e lidhjes është një vijë e drejtë pa pika të ndërmjetme kontrolli - nëse vija e drejtë nuk përfaqëson gjeografinë në zgjidhjen siç duhet të grupit të të dhënave.
Boolean
Rolet e shoqërimit të tipit të objektit gjeohapësinor link
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Nyja fundore
Nyja opsionale fundore për këtë lidhje. Nyja fundore mund të jetë shembulli i njëjtë si nyja e fillimit.
Nyja
Nyja fillestare
Nyja opsionale e fillimit për këtë lidhje.
Nyja
5.1.5 Lidhje sekuenciale
Një element rrjeti që përfaqëson një rrugë të vazhdueshme në rrjet pa ndonjë degëzim. Elementi ka një fillim dhe fund të përcaktuar dhe çdo pozicion në rendin e lidhjes është i identifikueshëm me njërin nga parametrat siç është gjatësia.
Ky tip është një nëntip i lidhjes së përgjithësuar.
Ky tip është abstrakt.
Atributet e objektit gjeohapësinor të tipit lidhje sekuenciale
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Lidhja
Grupi i lidhjeve dhe rendet e lidhjes që
GeneralisedLink
përbëjnë grupin e lidhjes.
5.1.6 Objekt lidhës (LinkSet)
Një koleksion i rendeve të lidhjes dhe/ose lidhjet individuale që kanë një funksion specifik ose domethënie në një rrjet.
Ky tip është një nëntip i elementit të rrjetit.
Ky tip është abstrakt.
Rolet e shoqërimit të tipit të objektit gjeohapësinor (LinkSet)
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Lidhja
Grupi i lidhjeve dhe rendet e lidhjes që
GeneralisedLink
përbëjnë grupin e lidhjes.
5.1.7 Rrjeti
Një rrjet është ndërlidhja e elementeve të rrjetit.
Atributet e tipit të objektit gjeohapësinor në rrjet
Atributi
Përkufizimi
Tipi
Shmangia
Emërtimet gjeografike
Emri gjeografik për këtë rrjet.
GeographicalName
i shmangshëm
Rolet e shoqërimit të tipit të objektit gjeohapësinor në rrjet
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Elementet
Koleksioni i elementeve që përbëjnë
Elementi i rrjetit
rrjetin.
5.1.8 Sipërfaqja e rrjetit (Network)
Element 2-dimensional në një rrjet.
Ky tip është një nëntip i elementit të rrjetit.
Ky tip është abstrakt.
Atributet e tipit të objektit gjeohapësinor (NetworkArea)
Atributi
Përkufizimi
Tipi
Shmangia
Gjeometria
Përfaqëson karakteristikat
gjeometrike të zonës
Sipërfaqja GM
5.1.9 Lidhje në rrjet
Përfaqëson një lidhje logjike mes dy ose më shumë elementeve të rrjetit në rrjete të ndryshme.
Ky tip është një nëntip i elementit të rrjetit.
Atributet e lidhjes në rrjet për tipin e objektit gjeohapësinor.
Atributi
Përkufizimi
Tipi
Shmangia
Tipi
Kategorizimi i lidhjes së rrjetit.
Lidhja-
Tipi i vlerës
i shmangshëm
Rolet e shoqërimit të tipit të objektit gjeohapësinor (NetworkConnection)
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Elementi
Elementet e rrjetit në rrjete të ndryshme
Elementi i rrjetit
Kufizimet e lidhjes së rrjetit në bazë të tipit të objektit gjeohapësinor.
Të gjitha elementet duhet të jenë në rrjete të ndryshme
5.1.10 Element rrjeti
Tipi bazik që përfaqëson një element në rrjet. Çdo element në një rrjet ofron disa funksione që janë në interes të rrjetit.
Ky tip është abstrakt.
Atributet e elementeve të rrjetit për tipin e objektit gjeohapësinor
Atributi
Përkufizimi
Tipi
Shmangia
Koha e fillimit të Versionit
Data dhe koha kur ky version i objektit gjeohapësinor u vendos ose u ndryshua në grupin e të dhënave gjeohapësinore.
data ora
i shmangshëm
Koha e përfundimit të versionit
Data dhe koha kur ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq nga grupi i të dhënave gjeohapësinore.
data ora
i shmangshëm
ID Inspire
Identifikuesi i jashtëm i objektit gjeohapësinor.
Identifikuesi
Rolet e shoqërimit të tipit të objektit gjeohapësinor për elemente të rrjetit
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Në rrjet
Rrjetet ku një element rrjeti është
pjesëtar.
Rrjeti
i shmangshëm
5.1.11 Karakteristikat e rrjetit
Tipi bazë abstrakt që përfaqëson fenomenin e gjendur në ose përgjatë elementit të një rrjeti. Ky tip bazë ofron karakteristika të përgjithshme për të shoqëruar fenomenin e lidhur me rrjet (karakteristikat e rrjetit) me elementet e rrjetit.
Ky tip është abstrakt.
Atributet e tipit të objektit gjeohapësinor në rrjet
Atributi
Përkufizimi
Tipi
Shmangia
Fillimi i ciklit jetësor
Data dhe ora kur ky version i objektit gjeohapësinor u vendos ose u ndryshua në grupin e të dhënave gjeohapësinore.
data ora
i shmangshëm
Përfundimi i ciklit jetësor
Data dhe ora kur ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq në grupin e të dhënave gjeohapësinore.
data ora
i shmangshëm
ID Inspire
Identifikuesi i jashtëm i objektit gjeohapësinor.
Identifikuesi
Rrjeti referues
Referenca gjeohapësinore e karakteristikës së lidhur me rrjetin.
Rrjeti referues
i shmangshëm
5.1.12 Nyje
Përfaqëson një pozicion në rrjet, që gjithmonë ndodh në fillim ose në fund të një lidhjeje.
Ky tip është një nëntip i elementit të rrjetit.
Ky tip është abstrakt.
Atributet e tipit të nyjave të objektit gjeohapësinor
Atributi
Përkufizimi
Tipi
Shmangia
gjeometria
Vendndodhja e nyjës
GM Point
Rolet e shoqërimit të tipit të nyjave të objektit gjeohapësinor
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Lidhjet hyrëse
Lidhjet që hyjnë në nyje
lidhjen
i shmangshëm
Lidhjet dalëse
Lidhjet që dalin nga nyje
lidhjen
i shmangshëm
5.2 Tipi i të dhënave
5.2.1 Lidhje direkte
Një lidhje në drejtim pozitiv ose negativ.
Atributet e data-type-ve të lidhjes së orientuar (DirectedLink)
Atributi
Përkufizimi
Tipi i shmangies
Shmangia
Drejtim
Tregon nëse pajtohet lidhja e drejtuar (pozitiv) ose nuk pajtohet (negativ) me drejtimin pozitiv të lidhjes.
Nënshkrim
Rolet e shoqërimit të data type-ve të DirectedLink
Rol shoqërimi
Përkufizimi
Tipi i shmangies
Shmangia
Lidhje
Lidhja
Lidhje
5.2.2 Lidhje referuese
Një rrjet referues në një element linear të rrjetit.
Ky tip është një nëntip i rrjetit referues.
Atributet të data-type-ve të lidhjes-referuese
Atributi
Përkufizimi
Tipi
Shmangia
Drejtimi i lidhjes së aplikuar
Drejtimet e lidhjes së përgjithësuar me të cilat referenca zbatohet. Në rastet ku një karakteristikë nuk aplikohet te një drejtim përgjatë një lidhjeje, por përfaqëson një fenomen, ’inDirection’ i referohet krahut të djathtë në drejtimin e lidhjes.
Vlera e drejtimit të lidhjes
i shmangshëm
Kufizimet e data-type-ve të lidhjes referuese
Objektivat e referencës lineare duhet të jenë elementet e rrjetit linear. Kjo nënkupton, nëse përdoret referenca lineare ose drejtimi është relevant, objektivi i referencës së rrjetit do të jetë lidhje ose një rend lidhjeje.
5.2.3 Rrjet referues
Një referencë e elementit të rrjetit.
Rolet e shoqërimit të data-type-ve të rrjetit referues
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Elementi
Referenca e elementit të rrjetit.
Elementi i rrjetit
5.2.4 Lidhje lineare referencë (SimplelinearReference)
Një rrjet referencë i cili kufizon për një pjesë të elementit të rrjetit linear. Pjesa është pjesë e elementit të rrjetit, mes pozicionit fillestar dhe pozicionit përfundimtar.
Ky tip është një nëntip i lidhjes referuese.
Atributet e data-type-ve të lidhjes lineare referuese
Atributi
Përkufizimi
Tipi
Shmangia
Pozicioni fillestar
(fromPosition)
Pozicioni i nisjes së elementit linear, shprehur si distanca nga nisja e elementit të rrjetit linear përgjatë gjeometrisë së tij të lakuar.
gjatësia
Offset
Një offset nga gjeometria qendrore e lidhjes së përgjithësuar, sipas rastit, një offset pozitiv është në të djathtën e drejtimit të lidhjes, një offset negativ është në të majtë.
gjatësia
i shmangshëm
Pozicioni përfundimtar
(toPosition)
Pozicioni përfundimtar i elementit linear, shprehur si distanca nga nisja e elementit të rrjetit linear përgjatë gjeometrisë së tij të lakuar.
gjatësia
5.2.5 Pikë referuese
Një referencë në rrjet e cila kufizohet në një pikë të elementit të rrjetit linear. Pika është vendndodhja në elementin e rrjetit në pozicionin përfundimtar (atPosition) përgjatë rrjetit.
Ky tip është një nëntip i lidhjes referuese.
Atributet e data-type-ve të pikës referuese
Atributi
Përkufizimi
Tipi
Shmangia
Pozicioni përfundimtar
(atPosition)
Pozicioni i pikës, shprehur si distanca nga nisja e elementit të rrjetit linear përgjatë gjeometrisë së tij të lakuar.
gjatësia
Offset
Një offset nga gjeometria qendrore e lidhjes së përgjithësuar, sipas rastit; një offset pozitiv është në të djathtën e drejtimit të lidhjes, një offset negativ është në të majtë.
gjatësia
i shmangshëm
5.3 Kod-listë
5.3.1 Vlerat e tipit të lidhjes (ConnectionTypeValue)
Tipit e lidhjeve midis rrjeteve të ndryshme.
Vlerat e lejuara për këtë kod-listë përbëhen vetëm nga vlerat e specifikuara në tabelën e mëposhtme
Vlera
Përkufizimi
Lidhja ndërkufitare joindentike
Lidhja mes dy elementeve të rrjetit në rrjete të ndryshme të të njëjtit tip, por në sipërfaqe ngjitur. Elementet e rrjetit të referuar paraqesin ndryshime, por specifikojnë fenomenin e përbashkët të lidhur me realitetin.
Lidhja ndërkufitare identike
Lidhja mes dy elementeve të rrjetit në rrjete të ndryshme të të njëjtit tip, por në sipërfaqe ngjitur. Elementet e rrjetit të referuar përfaqësojnë të njëjtin fenomen.
Lidhja ndihmëse
Nënkupton lidhjen midis dy rrjeteve (në rrjete të ndryshme), të cilat kanë një mënyrë të ndryshme transportimi të paketave të informacionit. Lidhja riprezanton një mundësi për rrjet komunikimi (të njerëzve, shërbimeve etj.), të ndryshme nga një formë komunikimi në tjetrën.
5.3.2 Vlerat e drejtimit të lidhjes (LinkDirectionValue)
Lista e vlerave për drejtimet relative të një lidhjeje.
Vlerat e lejuara për këtë kod-listë përbëhen vetëm nga vlerat e specifikuara në tabelën e mëposhtme:
Vlera
Përkufizimi
Dy drejtime
Në të dyja drejtimet.
Në drejtim
Në drejtim të lidhjes.
Në drejtim të kundërt
Në drejtim të kundërt me lidhjen.
6. MODELI I MBULIMIT (Coverage) së INSPIRE përbëhet nga paketat e mëposhtme:
- Mbulimi (Coverage) (Bazë)
- Mbulimi (Coverage) (Domain dhe varg)
6.1 Mbulimi (Coverage) (Bazë)
6.1.1 Tipat e objektit gjeohapësinor
Paketa mbulimi (Bazë) përmban tipin e objektit gjeohapësinor “Mbulesë” .
6.1.1.1 Mbulim (Coverage)
Objekti gjeohapësinor që vepron si një funksion i cili kthen vlerat, nga gama e shtrirjes të vlerave të vlefshme të tij, për çdo pozicion direkt brenda hapësirës së vet, në kohë ose në kohë dhe hapësirë.
Ky tip është abstrakt.
Atributet e tipit të objektit gjeohapësinor
Atributi
Përkufizimi
Tipi
Shmangia
Metadata
Aplikimi i mbulimit specifik të metadatave.
Çdo
Tipi i varg-ut
Përshkrimi i strukturës së vlerës së vargut.
Tipi i regjistruar
6.2 Mbulimi (Domain dhe Varg)
6.2.1 Tipat e objektit gjeohapësinor
Paketa e mbulimit (Domain dhe vargu) përmban tipat e mëposhtëm të objektit gjeohapësinor:
- Mbulimi (Domain dhe vargu përfaqësues);
- Mbulimi i rrjetit koordinativ të rektifikuar;
- Mbulimi i rrjetit të referuar.
6.2.1.1 Mbulimi (Domain dhe vlera përfaqësuese) (CoverageByDomain-AndRange)
Mbulimi që ofron shtrirje të vlerave të vlefshme dhe vargun si karakteristika të veçanta.
Ky tip është një nëntip i mbulimit.
Ky tip është abstrakt.
Atributet e objektit gjeohapësinor të tipit “Mbulim (Domain dhe vlera përfaqësuese”
Atributi
Përkufizimi
Tipi
Shmangia
Funksioni i mbulimit
Përshkrimi se si mund të fitohet gama e vlerave në vendndodhjet e domain-it të mbulimit.
Funksioni i mbulimit
Vendosja e shtrirjes të vlerave të vlefshme
Konfigurim i vlerave të vlefshme të mbulimit përshkruar në kushtet e koordinatave.
Çdo
Vendosja e vargut.
Grup vlerash të shoqëruara nga një funksion me elemente të domain-it të mbulimit.
Çdo
Kufizimet e objektit gjeohapësinor të tipit mbulim “CoverageByDomainAndRange”
Funksioni i rrjetës do të jetë i vlefshëm vetëm për shtrirjen e vlerave të vlefshme që janë në rrjet.
6.2.1.2 Mbulimi i rrjetit koordinativ të rektifikuar
Mbulimi në të cilin shtrirja e vlerave të vlefshme konsiston në një rrjet të rektifikuar.
Ky tip është një nëntip i mbulesës së rrjetit koordinativ të rektifikuar.
Kufizimet e objektit gjeohapësinor të tipit “Mbulimi i rrjetit koordinativ të rektifikuar”.
Shtrirja e vlerave të vlefshme mund të jetë një rrjet koordinativ i rektifikuar.
Pikat e rrjetit të “Mbulimi i rrjetit koordinativ të rektifikuar” (RectifiedGridCoverage) do të përputhen me qendrat e qelizave të rrjeteve gjeografike të përcaktuara në standardin përkatës për rrjetet gjeografike, në çdo nivel zgjidhjeje.
6.2.1.3 Mbulimi i rrjetit koordinativ të rektifikuar (RectifiedGridCoverage)
Shtrirja e vlerave të vlefshme përbëhet nga një mbulim rrjeti koordinativ të rektifikuar.
Ky tip është një nëntip i mbulimit nga fusha dhe vargu.
Kufizimet e tipit të objektit gjeohapësinor për mbulim të rrjetit koordinativ të rektifikuar
Fusha do të jetë një rrjet i referuar.
6.2.2 Data-type
6.2.2.1 Funksioni i mbulesës (CoverageFunction)
Përshkrimi se si mund të merren vlerat e vargut të vendndodhjes në fushën e mbulimit.
Ky është një tip bashkimi.
Atributet e një bashkimi të tipit CoverageFunction
Atributi
Përkufizimi
Tipi
Shmangia
Vargu i karaktereve
Përshkrim formal ose joformal i funksionit të mbulimit si tekst.
Vargu i karaktereve
Rregullat referuese
Përshkrim formal ose joformal i funksionit të mbulimit si tekst.
URI
Funksioni i rrjetit koordinativ
Rregulli i planifikimit për gjeometrinë e rrjetit.
Funksioni i rrjetës
6.2.2.2 Funksioni i rrjetit (GridFunction)
Rregull i qartë i planifikimit për gjeometrinë e rrjetës.
Atributet e të dhënave të tipit “Funksioni i rrjetit”
Atributi
Përkufizimi
Tipi
Shmangia
Rregullat sekuenciale
Përshkrim se si janë të renditura pikat e rrjetit për shoqërim të elementeve të vlerave në setin e vlerave të mbulimit.
CV_ Rregullat sekuenciale
Pikënisja
Pika e rrjetit për t’u shoqëruar me regjistrimin e parë në grupin e gamës së mbulimit.
Integer
7. MODELI I VROJTIMEVE
Modeli i vrojtimeve të INSPIRE-s përbëhet nga paketat e mëposhtme:
- Referencat e vrojtimit;
- Proceset karakteristike të vrojtimit;
- Vrojtimet e specifikuara.
7.1 Referencat e vrojtimit
Tipat e objektit gjeohapësinor
Paketa mbi referencat e vrojtimit përmban tipin e objektit gjeohapësinor
7.1.1 Grupi i vrojtimit (ObservationSet)
Lidh një grup vrojtimesh.
Atributet e tipit të objektit gjeohapësinor mbi grupin e vrojtimeve
Atributi
Përkufizimi
Tipi
Shmangia
Inspire ID
Identifikuesi i jashtëm i objektit gjeohapësinor.
Identifikuesi
Shtrirja
Informacioni rreth shtrirjes gjeohapësinore dhe kohore
EX Extent
Rolet e shoqërimit të tipit të objektit gjeohapësinor ObservationSet.
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Anëtar
Një anëtar i ObservationSet.
OM Observation
7.2 Proceset
7.2.1 Tipat e objektit gjeohapësinor
Paketa “Proceset” përmban proceset e tipit të objektit gjeohapësinor.
7.2.1.1 Procesi
Përshkrimi i procesit të vrojtimit.
Ky tip është një nëntip i OM_Process.
Atributet e Procesit të tipit të objektit gjeohapësinor
Atributi
Përkufizimi
Tipi
Shmangia
Inspire ID
Identifikuesi i jashtëm i objektit gjeohapësinor.
Identifikuesi
i shmangshëm
Emri
Emri i procesit.
Vargu i karaktereve
i shmangshëm
Tipi
Tipi i procesit.
Vargu i karaktereve
i shmangshëm
Dokumentacioni
Informacion i mëtejshëm (on-line/off-line) shoqëruar me procesin.
DocumentCitation
i shmangshëm
Parametrat e procesit
Parametër që kontrollon zbatimin e procesit dhe, si pasojë, edhe prodhimin e këtij procesi.
ProcessParameter
i shmangshëm
Palët përgjegjëse
Individ ose organizatë lidhur me procesin.
Palët përgjegjëse
i shmangshëm
7.2.2 Tipi i të dhënave
7.2.2.1 Parametri i procesit (ProcessParameter)
Përshkrim i parametrit të dhënë.
Atributet e data-type-it “Parametri i procesit”
Atributi
Përkufizimi
Tipi
Shmangia
Emri
Emri i parametrit të procesit.
Parametri i procesit
Vlera e emrit.
Përshkrimi
Përshkrimi i parametrit të procesit.
Vargu i karaktereve
7.2.3 Kod-listat
7.2.3.1 Vlera e emrit të parametrit të procesit
(ProcessParameterNameValue)
Një kod-listë me emra të parametrave të procesit.
Vlerat e lejuara për këtë kod-listë përbëhen nga vlerat e përcaktuara nga ofruesit e të dhënave.
7.3 Karakteristikat e vrojtimit
7.3.1 Data-type
7.3.1.1 Kufizim
Kufizim në disa karakteristika, p.sh. gjatësia e valës = 200 nm.
Atributet e kufizimit të data-type-ve
Atributi
Përkufizimi
Tipi
Shmangia
Karakteristikat dalluese
Karakteristika që kufizohet, p.sh. ’ngjyra’
Fenomeni-
kufizimi është ’ngjyrë = blu’.
vlera e tipit
Etiketa
Një titull i lexueshëm nga njeriu për të gjithë kufizimin.
Vargu i karaktereve
7.3.1.2 Kategorizimi i kufizimeve.
Kufizim i bazuar në disa kategori kualifikuese. p.sh. ngjyra = ’kuqe’.
Ky tip është një nëntip i kufizimit.
Atributet e data-type-ve të mbi kategorizimin e kufizimeve
Atributi
Përkufizimi
Tipi
Shmangia
Krahasimi
Operator krahasimi. Në rast të një kufizimi të kategorisë duhet të jetë ’i barasvlershëm me (equalTo)’ ose ’jo i barasvlershëm me (notEqualTo)’.
Krahasimi i vlerës së operatorit (Comparison OperatorValue)
Vlera
Vlera e karakteristikës, që është e kufizuar p.sh. ’blue’ (nëse karakteristika e kufizuar është ngjyra.)
Vargu i karaktereve
(CharacterString)
7.3.1.3 Kufizim i vlerës (RangeConstraint)
Kufizim numerik i vlerës për disa karakteristika p.sh. gjatësia e valës > 300 nm dhe gjatësia e valës < 600 nm.
Ky tip është një nëntip i kufizimit.
Atributet e data-type-ve mbi këtë kufizim
Atributi
Përkufizimi
Tipi
Shmangia
Vlera
Gama e vlerës numerike të
karakteristikës që është e kufizuar.
Vlerat e
kufijve
(RangeBounds)
Njësia matëse
Njësitë e matjes së përdorur në kufizim.
Njësia matëse (UnitOf-Measure)
7.3.1.4 Kufijtë e vlerave
Vlerat kufizuese të fillimit dhe mbarimit të një vlere numerike (p.sh. fillimi 50, mbarimi < 99).
Atributet e data-type-ve për këtë tipi kufizimi
Atributi
Përkufizimi
Tipi
Shmangia
Krahasimi pikënisjes
Krahasuesi i përdorur për kufirin më të ulët të vlerës (p.sh. Më e madhe se ose e barabartë me)
Krahasimi i vlerave të operatorit
(Comparison
OperatorValue)
Pikënisja
Kufiri më i ulët i gamës së vlerave
Real (Real)
Krahasimi pikë fundore
Krahasuesi i përdorur për kufirin më të lartë të gamës (p.sh. më pak se (lessThan))
Krahasimi i vlerave të operatorit
(Comparison
OperatorValue)
Pika përfundimtare
Kufiri më i lartë i gamës së vlerave
Real (Real)
7.3.1.5 Kufiri skalar (ScalarConstraint)
Një kufizim skalar numërimi në disa karakteristika p.sh. gjatësia > 1 m.
Ky tip është një nëntip i kufizimit.
Atributet e data-type-ve për këtë tipi kufizimi
Atributi
Përkufizimi
Tipi
Shmangia
Vlera
Vlera numerike e karakteristikës që është kufizuar
Real(Real)
Krahasimi
Krahasuesi që do të përdoret në kufizim p.sh. Më e madhe se (greaterThan)
Krahasimi i vlerave të operatorit
(Comparison
OperatorValue)
Njësia Matëse
Njësitë e matjes së përdorur në kufizim
Njësia matëse (UnitOf-Measure)
7.3.1.6 Kufizime të tjera
Një kufizim që nuk është modeluar në një mënyrë të strukturuar, por mund të përshkruhet duke përdorur atributin me tekst të lirë ’përshkrimi’.
Ky tip është një nëntip i kufizimit
Atributet e data type-ve për këtë tipi kufizimi
Atributi
Përkufizimi
Tipi
Shmangia
Përshkrimi
Përshkrimi i kufizimit.
Vargu i karaktereve
7.3.1.7 Matje statistikore
Një përshkrim i disa matjeve statistikore p.sh. ’arritjet maksimale’.
Atributet e tipit të të dhënave për këtë tipi kufizimi
Atributi
Përkufizimi
Tipi
Shmangia
Etiketa
Një titull i lexueshëm nga njeriu për tërë matjen statistikore.
Vargu i karaktereve
Funksionet Statistikore
Një funksion statistikor p.sh. mjet
Vlera e tipit të funksionit statistikor
Periudha kohore
Një gamë vlerash e përkohshme mbi të cilën llogaritet një statistikë p.sh. një ditë, një orë.
TM_Duration
Gjatësia
Vlerë njëdimensionale gjeohapësinore mbi të cilën llogaritet një statistikë, për shembull 1 metër.
gjatësia
Sipërfaqe
Vlerë dydimensionale gjeohapësinore mbi të cilën llogaritet një statistikë, për shembull 1 metër katror.
Sipërfaqe
Sasi Volumi
Vlerë tredimensionale gjeohapësinore mbi të cilën llogaritet një statistikë, për shembull 1 metër kub.
Volumi
Grumbullim tjetër
Çdo tip tjetër grumbullimi
Çdo
Rolet e shoqërimit të data-type-ve të matjeve statistikore
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Rrjedh nga
Një matje statistikore mund të rrjedhë nga një tjetër, p.sh. temperaturat maksimale mujore mund të rrjedhin nga temperaturat mesatare ditore.
Matje statistikore
7.3.2 Numërtimet
7.3.2.1 Operatori i krahasimit
Një numërtim i operatorëve të krahasimit (p.sh. më i madh se)
Vlerat për numërtimin e operatorëve krahasues
Vlera
Përkufizimi
E barabartë me
Ekzaktësisht baras me
Jo e barabartë me
Jo ekzaktësisht baras me
Më e vogël se
më e vogël se një vlerë e caktuar
Më shumë se
më e madhe se një vlerë e caktuar
Më e vogël ose baras me
më pak se ose fiks baras me
Më e madhe ose baras me
më shumë se ose fiks baras me
7.3.3 Kod-listat
Tipi i fenomenit
Një kod-listë me fenomene (p.sh.: temperatura, shpejtësia e erës)
Vlerat e lejuara për këtë kod-listë përbëhen nga vlerat e kod-listave vijuese ose kod- listave të tjera, përcaktuar nga ofruesit e të dhënave:
- Emrat standardë të klimës dhe parashikimit të motit (CFStandardNamesValue). Përcaktimet e fenomeneve të vëzhguara në meteorologji dhe oqeanografi, siç specifikohet në pikën 4.5 të këtij kreu.
- Emri i parametrit të elementit të profilit (ProfileElementParameterNam- eValue): Karakteristikat mund të vëzhgohen për të karakterizuar elementin e profilit, siç specifikohet në standardin e temës përkatëse.
- Emri i parametrit të objektit të prejardhur nga toka (SoilDerivedObjectParame- terNameValue): Karakteristikat që lidhen me tokën që mund të burojnë nga toka dhe të dhëna të tjera, siç specifikohet në standardin e temës përkatëse.
- Emri i parametrit të profilit të tokës (SoilProfileParameterNameValue): Karakteristikat që mund të vëzhgohen për të karakterizuar profilin e tokës, siç specifikohet në standardin e temës përkatëse.
- Emri i parametrit të vendndodhjes së tokës (SoilProfileParameterNameValue): Karakteristikat që mund të vëzhgohen të karakterizojnë vendndodhjen e tokës, siç specifikohet në standardin e temës përkatëse.
- Përbërësi evropian i referencës së cilësisë së ajrit (EU_AirQualityReference- ComponentValue): Përcaktimet e fenomenit lidhur me cilësinë e ajrit në kontekstin e raportimit sipas legjislacionit evropian, siç specifikohet në standardin e temës përkatëse.
- Kodi dhe flamujt WMO GRIB Tabela 4.2 (GRIB_CodeTable4_2Value) Përcaktimet e fenomenit vëzhguar në meteorologji, siç specifikohet në standardin e temës përkatëse.
Përdorimi i parametrit BODC P01 (BODC_P01ParameterUsageValue): Përcaktimet e fenomenit të vrojtuar në oqeanografi.
7.3.3.2 Vlera e tipit të funksionit statistikor.
Një kod-listë me funksione statistikore (p.sh. maksimumi, minimumi, mesatarja).
Vlerat e lejuara për këtë kod-listë përbëhen nga vlerat e përcaktuara nga ofruesit e të dhënave.
7.4 Vrojtimet e specializuara
Tipat e objektit gjeohapësinor
Paketa e vrojtimeve të specializuara përmban tipat e objekteve gjeohapësinore si vijon:
- Vrojtimi i rrjetit koordinativ;
- Vrojtimi i serive të rrjetit koordinativ;
- Vrojtimi i pikës;
- Koleksioni i vrojtimeve të pikës;
- Vrojtimi me shumë pika;
- Vrojtimi i serive kohore të pikës ;
- Vrojtim i profilit;
- Vrojtim i trajektores.
7.4.1.1 Vrojtim i rrjetit koordinativ (GridObservation)
Vrojtim që përfaqëson një rrjeti koordinativ të zhvilluar në një moment të vetëm.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizime të tipit “GridObservation” .
Tipologjia target do të jenë një SF_SamplingSolid ose SF_Sampling- Surface.
Fenomeni kohë do të jetë një TM_Instant.
Rezultati do të jetë një mbulim i rrjetit koordinativ të rektifikuar.
7.4.1.2 Vrojtimi i rrjeteve koordinative me seri. “GridObservation”
Vrojtim që përfaqëson një rrjet koordinativ të zhvilluar në hapësira kohe të caktuara.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizimet e tipit të objektit gjeohapësinor “SamplingCoverageObservation”
Tipologjia target do të jetë një SF_SamplingSolid.
Fenomeni kohë do të jetë një TM_Period.
Rezultati do të jetë një “RectifiedGridCoverage” ose një “RectifiedGrid-Coverage”.
7.4.1.3 Vrojtimi i pikës (Point Observation)
Vrojtim që përfaqëson një matje të një karakteristike në një pikë të vetme në kohë dhe hapësirë.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizimet e tipit të objektit gjeohapësinor “Point Observation”
Tipologjia target do të jetë një SF_SamplingSolid.
Fenomeni kohë do të jetë një TM_Instant.
7.4.1.4 Koleksioni i vrojtimeve të pikës.
Një koleksion i vrojtimeve të pikës.
Ky tip është një nëntip i ObservationSet. Kufizimet e tipit të objektit gjeohapësinor mbi koleksionin e vrojtimeve të pikës.
Çdo autoritet përgjegjës do të jetë një vrojtues pike.
7.4.1.5 Vrojtimi me shumë pika.
Vrojtimi që përfaqëson një grup matjesh të kryera pikërisht në të njëjtën kohë, por në vendndodhje të ndryshme.
Ky tip është një nëntip i SamplingCoverageObservation
Kufizimet e tipit objektit gjeohapësinor “vrojtimi me shumë pika”.
Tipologjia target do të jetë një SF SamplingCurve, SF SamplingSurface ose SF SamplingSolid.
Fenomeni kohë do të jetë një TM_Instant
Rezultati do të jetë një mbulim shumëpikësh.
7.4.1.6 Vrojtimi i serive kohore të pikës.
Vrojtimi që përfaqëson një seri kohore të matjeve të pikës të një karakteristike në një vendndodhje të fiksuar në hapësirë.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizimet e tipit të objektit gjeohapësinor “vrojtimi i serive kohore të pikës”.
Tipologjia target do të jetë një SF_SamplingSolid.
Fenomeni kohë duhet të jenë TM_Period.
Rezultatet duhet të jenë një Timeseries.
7.4.1.7 Vrojtimi i profilit.
Vrojtimi që përfaqëson matjen e një karakteristike përgjatë një profili vertikal në hapësirë në një moment të vetëm të kohës.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizimet e tipit të objektit gjeohapësinor “Vrojtimi i profilit” (ProfileObservation)
Tipologjia target do të jetë një SF SamplingCurve.
Fenomeni kohë do të jetë një TM_Instant.
Rezultati do të jetë një mbulesë rrjeti të rektifikuar.
7.4.1.8 Vrojtimi i trajektores.
Vrojtim që përfaqëson një matje të një karakteristike në një pikë të vetme në kohë dhe hapësirë.
Ky tip është një nëntip i SamplingCoverageObservation.
Kufizimet e tipit të objektit hapësinor “TrajectoryObservation”
Fenomeni kohë do të jetë një TM_Period.
Rezultati do të jetë një Timeseries.
Çdo pikë në rezultat do të jetë një TimeLocationValueTriple.
Tipologjia target do të jetë një SF_Sampling Curve”.
7.4.2 Tipi i të dhënave
Vlerë e trefishtë: Kohë, vendndodhje, vlerë (matje)
Një grup i trefishtë i kohës, vendndodhjes, vlerës (matja). Për shembull, në një pikë përgjatë trajektores.
Ky tip është një nëntip i TimeValuePair.
Atributet e tipit të të dhënave të TimeLocationValueTriple
Atributi
Përkufizimi
Tipi
Shmangia
Vendndodhja
Vendndodhja gjeografike ku vlera është e vlefshme.
GM_Position
7.5 Kërkesat për vrojtimet
Aty ku përdoret tipi OM_Observation, ose çdo nëntip i tij, për t’i bërë të dhënat të disponueshme, do të zbatohen kërkesat vijuese:
- Tipi i procesit do të përdoret për të treguar procedurën e përdorur në një OM_ Observation.
- Aty ku jepet një referencë për EnvironmentalMonitoringFacility nga një OM_Observation, do të ofrohet një atribut parametri, emri i të cilit është ’relatedMonitoringFeature’ dhe atributi i të cilit është tipi AbstractMonitoringFeature.
- Për të gjitha kodimet që përdoren për të gjithë rezultatin e OM_Obser- vation ose një pjesë të tij, do të vihet në dispozicion një ndërfaqe publike e programimit të aplikacionit (API) për të lexuar skedarin e koduar. Ky API do të jetë i aftë të ekspozojë informacionin e duhur për të kuptuar objektet gjeohapësinore të INSPIRE-s.
- Nëse atributi ProcessParameter është i pranishëm në karakteristikën e procedurës së një objekti OM_Observation, vlera e tij (një emër) do të përfshihet në atributin e parametrit të objektit OM_Observation.
8. MODELI KOMPLEKS I AKTIVITETEVE
Modeli kompleks i aktivitetit sipas INSPIRE përmban paketën “Kompleksiteti i aktivitetit”
8.1 Aktiviteti kompleks (ActivityComplex)
8.1.1 Tipi i objektit gjeohapësinor
Paketa “Kompleksiteti i aktivitetit” përmban tipin e objektit gjeohapësinor Activity Complex.
8.1.1.1 Aktiviteti kompleks (ActivityComplex)
Një njësi e vetme, si nga ana teknike dhe ekonomike, sipas kontrollit të menaxhimit të një entiteti ligjor (operator), që mbulon aktivitete si ato të listuara në klasifikimin e Eurostat NACE, vendosur nga rregullorja (KE) nr.1893/2006 e Parlamentit dhe Këshillit Evropian. Activity Complex duhet të përfaqësojë të gjithën zonën, në të njëjtën vendndodhje ose në vendndodhje tjetër, menaxhuar nga i njëjti operator, përfshi të gjithë infrastrukturën, pajisjet dhe materialet.
Atributet e tipit të objektit gjeohapësinor ActivityComplex
Atributi
Përkufizimi
Tipi
Shmangia
Inspire ID
Identifikuesi i jashtëm i objektit gjeohapësinor.
Identifikuesi
ID e tematikës
Identifikuesi tematik i kompleksitetit të aktivitetit.
Indentifikimi i tematikës (Thematic
Identifier)
Atributi
Përkufizimi
Tipi
Shmangia
Gjeometria
Gjeometria e përdorur për të përcaktuar shtrirjen ose pozicionin e kompleksitetit të aktivitetit.
GM Object
Funksioni
Aktivitetet e kryera në kuadër të “kompleksiteti i aktivitetit”. Funksioni përshkruhet nga aktiviteti dhe mundësisht të jetë i pajisur me informacion rreth input-eve dhe output-eve si rrjedhojë e tij.
Funksioni
Emri
Emri përshkrues i kompleksitetit të aktivitetit.
Vargu i karaktereve
i shmangshëm
E vlefshme nga
Koha kur kompleksiteti i aktivitetit filloi të ekzistonte në botën e vërtetë.
data ora
i shmangshëm
E vlefshme deri në
Koha kur kompleksiteti i aktivitetit nuk ekziston më në botën e vërtetë.
data ora
i shmangshëm
Fillimi i kohës së vlefshmërisë
Data dhe koha kur ky version i objektit gjeohapësinor u vendos ose u ndryshua në grupin e të dhënave gjeohapësinore.
data ora
i shmangshëm
Përfundimi i kohës së vlefshmërisë
Data dhe koha kur ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq në grupin e të dhënave gjeohapësinore.
data ora
i shmangshëm
8.1.2 Data-type-et
8.1.2.1 Funksioni
Funksioni i diçkaje shprehur si një aktivitet dhe inputi opsional dhe/ose output-i.
Atributet e data-type-ve të funksionit
Atributi
Përkufizimi
Tipi
Shmangia
Aktiviteti
Përshkrim i kategorizuar individualisht ose grup i organizuar i proceseve teknike, që kryhen nga një njësi ekonomike, private ose publike, me ose pa profil përfitues.
Vlera ekonomike Aktive.
(Economic
ActivityValue)
Inputi
Çdo material i klasifikuar ose i regjistruar, që fut një njësi teknike dhe ekonomike në përputhje me funksionin.
Vlera
Input-Output
(InputOutput-Value)
i shmangshëm
Outputi
Çdo material i klasifikuar ose i regjistruar, që del nga një njësi teknike dhe ekonomike në përputhje me funksionin.
Vlera Input-Output
(InputOutput-Value)
i shmangshëm
Përshkrimi
Një përshkrim më i detajuar i funksionit.
Tekst i lirë_PT
i shmangshëm
8.1.2.2 Kapacitet
Një kuantifikim i një aftësie aktuale ose potenciale për të kryer një aktivitet, që në mënyrë tipike nuk ndryshon, nuk ndryshon shpesh, ose nuk ndryshon në një shkallë domethënëse.
Atributet e data-type-ve të kapacitetit
Atributi
Përkufizimi
Tipi
Shmangia
Aktiviteti
Përshkrim i kategorizuar individualisht ose grup i organizuar i proceseve teknike, që kryhen nga një njësi ekonomike, private ose publike, me ose pa profil përfitues.
Vlera ekonomike aktive.
(EconomicActiv-
ityValue)
Inputi
Informacion i matshëm rreth çdo materiali të klasifikuar ose regjistruar, që fut një njësi teknike dhe ekonomike në përputhje me funksionin.
Vlera Input-Output
(InputOutput-Value)
Outputi
Informacion i matshëm rreth çdo materiali të klasifikuar ose regjistruar, që del nga një njësi teknike dhe ekonomike në përputhje me funksionin.
Vlera Input-Output
Koha
Kohëzgjatja së cilës i referohet kapaciteti i specifikuar, si 1 vit për një kapacitet vjetor.
TM_Duration
Përshkrimi
Përshkrimi i kapacitetit
Tekst i lirë PT
i shmangshëm
8.1.2.3 Shuma input ose output (InputOutputAmount)
Tipi dhe, sipas disponueshmërisë, shuma e matshme e një materiali të klasifikuar ose regjistruar, që hyn ose del nga një njësi teknike ose ekonomike.
Atributet e data-type-ve tipi “Shuma input output”
Atributi
Përkufizimi
Tipi
Shmangia
InputOutput
Çdo material i klasifikuar ose i regjistruar, që hyn ose del nga një njësi teknike dhe ekonomike në përputhje me funksionin.
vlera Input-Output
Shuma
Shuma (si volumi ose masa) e një materiali të klasifikuar ose regjistruar, që hyn ose del nga një njësi teknike ose ekonomike.
Matje
i shmangshëm
8.1.2.4 Leja (permision)
Vendimi zyrtar (pëlqimi formal) që jep autorizimin për të operuar në gjithë kompleksitetin e aktiviteteve ose një pjesë të tyre, duke iu nënshtruar kushteve të caktuara të cilat garantojnë që instalimet ose pjesë të instalimeve në të njëjtin vend, operuar nga i njëjti operator ku kërkesat janë fiksuar nga një autoritet kompetent. Një leje mund të mbulojë një ose më shumë funksione dhe parametra fiks të kapacitetit. Termi mund të zgjerohet edhe në tipa të tjerë certifikatash ose dokumentesh me përkatësi të veçantë në varësi të shtrirjes (p.sh.: EMAS, National Quality Standards, etj.).
Atributet e data-type-ve
Atributi
Përkufizimi
Tipi
Shmangia
Id
Referenca identifikuese e lejes.
ThematicIdentifier
Palët relative
Palët që lidhen me lejen e dhënë për kompleksitetin e aktivitetit të hapur për shumë role të ndryshme, siç janë Competent Authorities ose Company mes shumë të tjerave
Palët relative
i shmangshëm
Atributi
Përkufizimi
Tipi
Shmangia
Data e përcaktuar përkohësisht
Referencë kohore që plotëson përkufizimin e lejes.
data ora
i shmangshëm
Nga data
Datë që fillon nga zbatimi i lejes dhe është e vlefshme.
data ora
i shmangshëm
Deri më datën
Data deri në zbatimin e lejes dhe është e vlefshme.
data ora
i shmangshëm
Përshkrimi
Përshkrimi i lejes.
tekst i lirë PT
i shmangshëm
Funksioni i lejueshmërisë
Funksioni/et për të cilin jepet leja.
funksioni
i shmangshëm
Kapaciteti i lejuar
Sasitë maksimale të input-it ose/dhe output-it të aktivitetit në përputhje me lejen.
kapaciteti
i shmangshëm
8.1.2.5 Përshkrimi i aktiviteteve komplekse (Activity Complex)
Informacion shtesë rreth një kompleksiteti të aktivitetit, përfshi përshkrimin e tij, adresën, detajet e kontaktit dhe palët e interesuara.
Atributet e tipit të objektit gjeohapësinor “Përshkrimi i aktiviteteve komplekse”
Rol shoqërimi
Përkufizimi
Tipi
Shmangia
Përshkrimi
Një përkufizim plotësues i aktiviteteve komplekse dhe karakteristikave të tij.
Tekst i lirë PT
i shmangshëm
Adresa
Një adresë për aktivitetet komplekse, d.m.th., adresë ku ndodhin aktivitetet.
Riprezantimi i adresës.
(Address
Representation)
i shmangshëm
Kontakti
Informacioni i kontaktit për kompleksitetin e aktivitetit.
Kontakti
i shmangshëm
Pjesa relative
Informacioni mbi palët lidhur me Activity Complex. Është i hapur për shumë role të ndryshme, si pronarët, operatorët ose autoritetet kompetente.
Pjesa relative
(RelatedParty)
i shmangshëm
8.1.3 Kod listat
8.1.3.1 Aktiviteti ekonomik
Klasifikimi i aktiviteteve ekonomike.
Vlerat e lejuara për këtë kod-listë përbëjnë vlerat në kod-listat e mëposhtme ose në kod-listat e tjera të përcaktuara nga ofruesit e të dhënave:
- Klasifikimi i aktivitetit ekonomik të BE-së (EconomicActivityNAC- EValue): Aktivitetet ekonomike sipas vlerave të Eurostat NACE Classification, siç specifikohet në rregulloren (KE) nr. 1893/2006 të Parlamentit dhe Këshillit Evropian.
- Klasifikimi i aktivitetit ekonomik mbi statistikat e mbetjeve në BE (Economi- cActivityWasteStatisticsValue): Klasifikimi i aktiviteteve ekonomike në përputhje me pjesën 8 të aneksit I të rregullores (KE).
- Klasifikimi i mbetjeve të riciklueshme (WasteRecoveryDis-posalValue): Klasifikim mbetjeve të riciklueshme dhe trajtimi i tyre në përputhje me aneksin I dhe II të direktivës 2008/98/EC të Parlamentit dhe Këshillit Evropian.
8.1.3.2 Vlera input ose output (Input Output Value)
Klasifikim i input-eve dhe output-eve.
Vlerat e lejuara për këtë listë kod përbëjnë vlerat në listat e mëposhtme të kodit ose listat e tjera kod, përcaktuar nga ofruesit e të dhënave:
- Klasifikimi i produktit në BE (ProductCPAValue): Klasifikimi i produkteve nga aktiviteti ekonomik në përputhje me rregulloren (KE) nr. 451/2008 të Parlamentit dhe Këshillit Evropian.
- Klasifikimi i mbetjeve (WasteValue): Klasifikimi i mbetjeve në përputhje me vendimin 2000/532/EC.
8.2 Kërkesat për kompleksitin e aktivitetit
Nëse një ofrues të dhënash përdor një nëntip të aktiviteteve komplekse (ActivityComplex) për të bërë të disponueshme informacionin mbi statusin do të përdoren kapaciteti fizik, lejet dhe/ose informacioni shtesë, kod-listat përkatëse dhe data-type-t e përfshira në paketën “Kompleksiteti i aktiviteteve”.
