# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI - TEMA: DEMOGRAFIA
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Demografia
3.1.1 Parathënie
3.1.2 Skemat e aplikimit dhe diagrami UML për temën: “Demografia”
3.1.3 Katalogu i tipologjisë
3.1.3.1 Shpërndarja statistikore
3.1.3.2 Vlerat statistikore
3.1.3.3 Klasifikimet
3.1.3.4 Elementet e klasifikimit
3.1.3.5 Dimensionet
3.1.3.6 Vlerat e llojeve të klasifikimit të elementeve
3.1.3.7 Vlerat e moshës sipas vitit
3.1.3.8 Vlerat e moshës nga 5 vjet
3.1.3.9 Vlerat e grupmoshave
3.1.3.10 Vlerat e kodeve NACE
3.1.3.11 Vlerat e llojeve të klasifikimit
3.1.3.12 Vlerat e ndryshueshme
3.1.3.13 Vlerat e metodës së matjes së statistikave
3.1.3.14 Vlerat e statusit të të dhënave statistikore
3.1.3.15 Vlerat e veçanta
3.2 Metadatat
3.3 Kodi EPSG për KRGJSH-në
3.4 Cilësia e të dhënave
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
4.2 Aneksi B - Kodlistat
4.2.1 Skema e aplikimit “Demografia’’ (Shpërndarja e popullsisë)
4.2.1.1 Vlerat e moshës nga 5 vjet
4.2.1.2 Vlerat e moshës sipas vitit
4.2.1.3 Vlerat e grupmoshave
4.2.1.4 Vlerat e llojeve të klasifikimit të elementeve
4.2.1.5 Vlerat e llojeve të klasifikimit
4.2.1.6 Vlerat e veçanta
4.2.1.7 Vlerat e statusit të të dhënave statistikore
4.2.1.8 Vlerat e metodës së matjes së statistikave
4.2.1.9 Vlerat e ndryshueshme
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG) në bashkëpunim me Institutin e Statistikave (INSTAT), i cili është autoriteti publik përgjegjës për temën “Demografia”.
Data e publikimit të versionit nr. 1 është korrik 2018. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2018_ DE_v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit;
Standard - Lloji i dokumentit;
NSDI - Qëllimi i dokumentit;
2018 - Viti i krijimit;
DE - Tema për të cilën është krijuar standardi: “Demografia” (shpërndarja e popullsisë), e cila i referohet temës “Population Distribution - Demography” në direktivën INSPIRE.
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 Qëllimi
Ky dokument përcakton specifikimet teknike, të harmonizuara konform direktivës INSPIRE, për të dhënat gjeohapësinore të temës “Demografia” (shpërndarja e popullsisë), temë e cila është përcaktuar në nenin 11, pika 2/r, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse për mbledhjen përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë e tyre.
2.2 Si lexohet dokumenti
2.2.1 Struktura e dokumentit
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema: Në këtë pjesë jepen specifikimet teknike për temën “Demografia”.
4. Anekse: Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës dhe se si është e ndarë kjo temë.
3.2 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3. Sistemi koordinativ referencë - Këtu përcaktohet sistemi koordinativ referencë (KRGJSH-ja).
3.4 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 Diagramet UML dhe katalogu i tipologjisë
Diagramat UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesorë të specifikimeve dhe marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në ’Katalogun e tipologjive’ (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive, mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave dhe në katalogun e tipologjive.
Tabelat nr. 1, 2, me anë shembujsh, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit në tabelën e kodlistës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi sipas direktivës INSPIRE për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
«featureType» - një element që mund të jetë real, në terren, apo një dukuri abstrakte
«dataType» - një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër
«enumeration» “KodList» - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
«union» - një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet që bien brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse.
«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të dhënat e importuara”
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë, poligon.
Abstrakt: kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
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
Në tabelën e lidhjeve “Rol shoqërimet” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve.
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin.
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh. PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh. Ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE, i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh. Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE, i elementeve.
2.2.3 Karakteristikat e voidable dhe shumëllojshmëria
Stereotipi voidable përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera ’void’. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
- E panjohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” e një liqeni të caktuar, nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E panjohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj, kjo e dhënë mund të ekzistojë.
-- Përshkrimi --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E pa populluar”.
Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull: Të dhënat personale të popullsisë të cilat ekzistojnë por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi voidable nuk jep asnjë informacion nëse ekziston një karakteristikë në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh. nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh. nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 Mbulimet - Coverages
Funksionet e mbulimit “Coverages” përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe /ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domein-et tipike gjeohapësinore janë grupe pikash (p.sh. vendndodhja e sensorëve), kurbat përcaktuese (p.sh. izolinjat), rrjetet (p.sh: ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si vetitë e llojeve të objekteve gjeohapësinore ku lloji i vlerës së kësaj karakteristike është një realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh: ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptues të Përgjithshëm “Generic Conceptual Model”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domein-i i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, djathtas, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domein-i i të cilit përbëhet nga një rrjet referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje të mbulimit (ose një nëntip i tyre) në skemat e aplikimit në INSPIRE.
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 Numërtimet dhe kodlistat (Enumeration and Kodlistë)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, ’vlera të tjera’ përcaktojnë llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht, si më poshtë:
- ’jo’ përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
- ’të kufizuara’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave;
- ’të hapura’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave;
- ’po’ përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo”, pra të specifikuara në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 Paraqitja e dimensionit kohor
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
Shënim i rëndësishëm.
Disa terma në katalogun e tipologjive, si p.sh. featureType, dataType, void, coverages etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të direktivës INSPIRE.
2.3 Detyrimet ligjore
Në bazë të ligjit nr. 72/2012, neni 16, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM-ja nr. 1077, datë 23.12.2015);
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 Fusha e veprimit
Të gjithë autoritetet publike, kompani private apo individë që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2: Proceset e ciklit jetësor
Planifikimi - Është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave;
Vlerësimi - Është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit;
Procesimi (Përpunimi) - Është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar;
Shpërndarja - Është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit;
Zbulimi - Është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara;
Analiza - Është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar;
Përditësimi - Është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara;
Arkivimi - Është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të pa aksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike;
Shkatërrimi - Është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 Demografia
3.1.1 Parathënie
Tema “Demografia” (Shpërndarja e popullsisë) përkufizohet si “grup i të dhënave statistikore” që përshkruan fenomene që kanë të bëjnë me popullsinë dhe janë shpërndarë në një pjesë të hapësirës dy dimensionale - 2D”. Ky dokument paraqet specifikimet e të dhënave për shpërndarjen e popullsisë dhe bazohet në parimet e mëposhtme:
-Ndarja ndërmjet të dhënave statistikore dhe njësive statistikore
Të dhënat statistikore përkufizohen si “çdo përfaqësim numerik i një fenomeni”. Një njësi statistikore jep informacion për vendndodhjen e të dhënave. Ky dokument trajton vetëm specifikimet e të dhënave statistikore. Specifikimi i njësive statistikore është jashtë qëllimit të këtij dokumenti. Të dhënat statistikore, i referohen njësive statistikore nëpërmjet identifikuesit të tyre të përbashkët, p.sh. kodet NUTS (Nomenklatura e Njësive Territoriale Statistikore). Bashkimi i të dhënave statistikore me objektin gjeohapësinor nuk është vetëm bashkimi i një objekti të dhënash me një tjetër. Qëllimi është përmirësimi i ndërveprimit midis statistikave dhe sistemeve të informacionit gjeografike GIS. Ky dokument ka për qëllim përmirësimin e rekomandimeve, integrimin e analizave gjeohapësinore dhe statistikore. Rezultati i integrimit e bën grupin e të dhënave statistikore të disponueshëm për sistemet e informacionit gjeografik GIS, në kontekstin e një infrastrukture të të dhënave gjeohapësinore të shtetit.
- I përgjithshëm
Ka disa lloje të ndryshme të të dhënave statistikore, këto në lidhje me popullsinë njerëzore: për njerëzit, banesat, për vendin e tyre të punës etj. Ky dokument nuk ka për qëllim të ofrojë specifikime për të gjitha këto të dhëna. Karakteristikat e përbashkëta janë nxjerrë dhe janë paraqitur në një model të përgjithshëm të dhënash. Duke përdorur modelin e të dhënave të përshkruara në këtë specifikim, të gjitha të dhënat statistikore janë organizuar në formë tabelore ose të “data cube”, mund të sigurohen në kuadrin e INSPIRE.
Përkufizimi: Shpërndarja gjeografike e popullsisë, duke përfshirë karakteristikat e popullsisë dhe nivelet e aktiviteteve, të grumbulluara sipas rrjetit, rajonit, njësisë administrative ose njësive të tjera analitike [direktiva 2007/2/EC].
Përshkrimi: Popullsia = Popullsia njerëzore
Një popullatë është çdo grup njerëzish, kafshësh, bimësh ose elementet për të cilat ne mund të mbledhim të dhëna. Është grupi për të cilin jemi të interesuar, të cilin dëshirojmë ta përshkruajmë ose të nxjerrim konkluzione. Në këtë specifikim të të dhënave, popullsia i referohet qenieve njerëzore, d.m.th. (1) njerëzve si individë ose (2) njerëz/individë që jetojnë së bashku në familje (Njësi Ekonomike Familjare). Informacioni mbi njerëzit ku dhe si jetojnë ose qëndrojnë është thelbësor për pothuajse të gjitha temat e tjera të direktivës INSPIRE, në veçanti për temat “Shëndeti i Njerëzve dhe Siguria e tij”, “Ndërtesat” dhe “Zonat me Rreziqe Natyrore”.
Tema mund të ndahet tematikisht në disa komponentë apo nëntema specifike, si:
- popullsia njerëzore sipas karakteristikave individuale (gjinia, mosha, gjendja martesore, kombësia, etj.);
- popullsia sipas llojit të aktiviteteve (arsimi, profesioni, etj.);
- qeniet njerëzore që jetojnë së bashku në grupe për arsye të ndryshme (familje, jetimore, azile, etj.).
- Diapazon i gjerë statistikash për popullsinë
Tërësia e informacionit që lidhet me popullsinë, mund të përfshijë: popullsinë e përgjithshme, moshën, gjininë, kombësinë ose vendin e lindjes, vdekshmërinë, jetëgjatësinë dhe migracionin (flukset migratore). Interesi mund të jetë popullsia, duke iu referuar një periudhe kohore dhe aktivitetit të saj. Rastet e përdorimit të statistikave mbi popullsinë tregojnë për shembull nevojën për të bërë një dallim ndërmjet numrit të popullsisë gjatë ditës dhe numrit të popullsisë gjatë mbrëmjes dhe natës për një njësi të caktuar gjeografike/administrative/statistikore, si një qytet ose një njësi tjetër. Ndoshta është e vështirë të përcaktohet se sa njerëz janë në një vend të caktuar (vendbanim, apartament apo shtëpi) dhe se cilëve grupe i përkasin. Sipas aktiviteteve, njerëzit mund të jenë në punë ose në aktivitete të ndryshme gjatë kohës së lirë (kinema, teatër etj.) ose mund të jenë duke përdorur mjetet e transportit. Për njerëzit në punë, mund të tregohet se në cilin sektor ekonomik ata janë të angazhuar, referuar klasifikimit të aktiviteteve NACE (Klasifikimi Statistikor i Aktiviteteve Ekonomike në Komunitetin Evropian) në një vend të caktuar, rajon ose pjesë të tij, ose ku njerëzit e një grupi social jetojnë, për shembull në qytete ose në zona kufitare. Për të minimizuar mbivendosjen me burime të tjera të rëndësishme evropiane të harmonizuara si baza e të dhënave rajonale e Eurostatit (Zyra Statistikore Evropiane), vetëm disa të dhëna mbi shpërndarjen e popullsisë janë të detyrueshme.
- Pa karakteristika gjeohapësinore
Tema “Demografia” (Shpërndarja e popullsisë) përmban atribute që lidhen me njësitë statistikore. Kjo do të thotë se kjo temë nuk ka karakteristika të drejtpërdrejta gjeohapësinore siç janë shumë tema të tjera si “Ndërtesat”, “Shëndeti i njerëzve dhe siguria e tij” etj. Kjo duhet të lidhet me këto karakteristika ndërmjet përdorimit të njësive statistikore, për shembull kodet NUTS (Nomenklatura e Njësive Territoriale për Statistika) ose identifikuesit e rrjetit të qelizave.
- Të dhëna e grumbulluara dhe konfidencialiteti
Përkufizimi i mësipërm specifikon të gjitha llojet e karakteristikave të përshtatshme për demografinë. Ajo përfshin termin “grumbullim”, që do të thotë se të dhënat jo të grumbulluara (individuale) për popullsinë përjashtohen për shkak të konfidencialitetit. Sigurimi i të dhënave në nivele të ndryshme rajonale varet nga situata kombëtare në lidhje me disponueshmërinë dhe privatësinë. Ekziston një lidhje midis madhësisë së njësive statistikore dhe diferencimit të vlerave të atributeve. Modeli i të dhënave mbulon të gjitha mundësitë, por kufizimet ligjore mund të ndalojnë sigurimin e tyre.
- Demografia/shpërndarja e popullsisë në kontekstin INSPIRE
Demografia (Shpërndarja e popullsisë) është një fenomen shumë i gjerë që mund të përshkruhet nëpërmjet të dhënave sasiore nga burime të ndryshme, si në nivel kombëtar dhe në atë evropian. Ky specifikim i të dhënave ofron një model të përgjithshëm të të dhënave, që mbulon fusha të ndryshme statistikore. Rastet e përdorimit tregojnë se statistikat mbi popullsinë e përgjithshme, në rrjetet ose zonat e tjera të vogla, mund të përdoren gjerësisht së bashku me tema të tjera të INSPIRE.
Përfitimet nga kjo temë në kontekstin e INSPIRE duhet të jetë fillimisht, aksesi në statistikat ekzistuese që nuk janë publikuar ende në bankën e të dhënave rajonale të ofruara nga Eurostat ose shtetet anëtare. Statistikat e ofruara sipas kësaj teme të INSPIRE duhet të jenë më së shumti një shtesë për statistikat që aktualisht publikohen në bazë të legjislacionit dhe marrëveshjeve të rëna dakord. Statistikat kombëtare ose ato në bankën e të dhënave rajonale evropiane shpesh janë shumëdimensionale në atë mënyrë që shërbimet INSPIRE nuk mund të përputhen. Përgjithësimi i modelit shprehet me përdorimin e kodlistave të ndryshme për klasifikimin e secilës vlerë statistikore të ofruar. Kjo qasje përfshin fleksibilitetin për të reaguar ndaj kërkesave të mëtejshme që mund të vijnë nga legjislacionet e reja apo arsye të tjera.
3.1.2 Skemat e aplikimit dhe diagrami UML për temën: “Demografia”
Shpërndarja statistikore e të dhënave përshkruan strukturën e një “zone të shpërndarjes/publikimit” bazuar në një set matjesh të një fenomeni të caktuar. Qëllimi i “Shpërndarjes së popullsisë” mund të kuptohet më së miri me shembullin e mëposhtëm. Pamja e shfaqur në figurën 3 përfaqëson mënyrën se si është shpërndarë popullsia në Tiranë dhe bashkitë e tjera, që këtu përshkruhet si një drejtkëndësh gjeografik. Kjo zonë është fotografuar me një sërë pikselash me përmasa të paktën 1000 m gjerësi të qelizave të rrjetit.
Për çdo qelizë është prodhuar numri i popullsisë: “vlera” është vetëm një numër njerëzish/individësh. Pikselat e bardha tregojnë rastet kur popullsia është zero dhe ndryshojnë nuancën deri në të kafe të errët kur numri i popullsisë rritet. Por i gjithë seti i pikselave - i gjithë grupi i qelizave - ofrojnë një pamje të plotë të zonës.
Figura 3: Shembull i shpërndarjes së popullsisë
Qëllimi i modelit të propozuar është të ofrojë mundësinë e shkëmbimit të të dhënave që qëndrojnë pas pamjeve të tilla. Në këtë shembull, i gjithë grupi i të dhënave që lidhen me çdo qelizë janë të nevojshme për të ndërtuar një tablo të përgjithshme që do të përfaqësojë fushën e shpërndarjes. Modeli në fjalë nuk është i kufizuar vetëm në një formë të shpërndarjes, nuk është i kufizuar vetëm në rrjetin e qelizave si komponent elementar i shpërndarjes - njësitë statistikore (zonat e Censusit, njësitë administrative), por janë gjithashtu të mundshme dhe nuk kufizohen vetëm në numërimin e thjeshtë të popullsisë. Ky është një model i përgjithshëm për të lejuar/mundësuar shkëmbimin e të dhënave statistikore.
Një pjesë e modelit është një lloj përshkrimi i metadatave, që nuk mbulohen nga metadatat e standardit SSH EN ISO 19115-1:2014 dhe që duhet të shtohen në krye të grupit të të dhënave.
Shembull:
Atributet
Vlerat
Domein-i
“Demografia”
Masat
“PopullsiaNëNjëVendbanim”
Klasifikimi
“Gjinia”
NjësitEMatjeve
“Persona”
ZonaEShpërndarjes
“Rrethinat e Tiranës”
Domein-i - përshkruan fushën e njohurive statistikore të cilave ju takon vlera dhe masa, përmban afat të shkurtër të fenomenit që po llogaritet.
Klasifikimet - përshkruajnë llojin e klasifikimit të përdorur për të llogaritur ose bashkuar vlerat. ZonaEShpërndarjes - përshkruan zonën për të cilën disponohen të dhënat statistikore dhe/ose zonën e zgjedhur nga përdoruesi.
Dimensioni kohor i shpërndarjes së popullsisë konsiderohet në tri aspekte: periudha aktuale e matjes, periudha referuese teorike e matjes dhe periudha që të dhënat mbeten të vlefshme.
Pjesa e dytë e modelit përmban vlerat elementare të të dhënave dhe përshkrimin sipas përmasave. Çdo vlerë karakterizohet nga një kombinim i caktuar i dimensioneve tematike dhe gjeohapësinore. Kjo pjesë aplikohet aq shpesh sa vlerat janë në dispozicion për zonën e shpërndarë/kërkuar.
Atributet
Vlerat
Vlerat
<numrat>
ElementetEKlasifikimit
“mashkull”
ReferencatGjeohapësinore
<NjësiaStatistikore>
Shënim. Ky shembull është thjeshtuar dhe nuk përfaqëson të gjitha atributet e modelit.
Modeli konceptual i të dhënave të “Demografia” (Shpërndarja e popullsisë) është përcaktuar në një mënyrë shumë të përgjithshme dhe pothuajse çdo vlerë statistikore që përshkruan një fenomen të matur statistikor, p.sh. popullsia, mund të konsiderohet pjesë e saj. Rastet e përdorimit tregojnë nevojën për variabla të tjera statistikore si: “popullsia në vendin e banimit, popullsia në vendin e punës dhe dendësia e popullsisë”. Këto statistika duhet të paraqiten në një nivel më të detajuar territorial sesa ajo që është e mundur të arrihet tashmë përmes databazës së Eurostat-it, preferohen njësi statistikore si rrjeti i qelizave apo zonat e Censusit.
Institutet Kombëtare të Statistikave nuk duhet të detyrohen që të ofrojnë shërbime INSPIRE për të gjitha statistikat që mbulojnë popullsinë, duke qenë se ndërtimi i dy sistemeve paralele (statistikat rajonale tashmë të ofruara nga Eurostat dhe statistikat rajonale të ofruara nga shtetet anëtare përmes INSPIRE) do të jenë të kushtueshme dhe konsumojnë kohë.
Një përmbledhje e paketës së “Demografia” (Shpërndarja e popullsisë) dhe paketave të referuara është dhënë në figurën 4. Paketa e “Demografia” i referohet paketës së “Tipave Bazë” për llojin e të dhënave të identifikuesit dhe disa lloje të bazave të përgjithshme që do të përdoren në përputhje me GCM (Modeli i Përgjithshëm Konceptual). Përveç kësaj, tipologjia NjësisaStatistikore i temës “Njësitë Statistikore” është referuar për të mbështetur pozicionimin indirekt të të dhënave statistikore në lidhje me vendndodhjen në Tokë.
Figura 4: Përmbledhja e paketës
Shembulli i aplikimit për temën “Demografia” (shpërndarja e popullsisë) është paraqitur në figurën 4 dhe përshkruhet më poshtë.
Skema është e strukturuar me tri lloje të klasave: “ShpërndarjaStatistikore”, “VleratStatistikore”, “VleratStatistikore. Dimensionet” dhe dy grupe të kodlistave.
Figura 5: Diagrami i klasifikimit të “Demografia” (shpërndarja e popullsisë)
Figura 6: Llojet e funksioneve të shpërndarjes statistikore
ShpërndarjaStatistikore është përcaktuar si një “feature type - tipologji” për arsye praktike, për të qenë në gjendje të gjenerohet në formatin e GML-së (Geography Markup Language). Ky tip vepron kryesisht si një çelës/kod për të mbajtur informacionin e përgjithshëm në lidhje me shpërndarjen dhe përmban veçoritë e përbashkëta të secilit komponent të shpërndarjes.
Sigurimi i InspireId nuk është i detyrueshëm. Ai mund të jetë i dobishëm për përdorim të brendshëm organizativ, ndaj ofruesit të të dhënave, nëse kërkesa ose rezultati do të ruhen për përdorim të mëvonshëm.
ZonaEShpërndarjes: Fushat e shpërndarjes janë pjesë e botës 2D që përshkruan ShpërndarjaETëDhënaveStatistikore, e përfaqësuar si një sipërfaqe.
Figura 7: Njësitë statistikore, vlerat dhe zonat e shpërndarjes
Atributi Domein-i jep informacion në lidhje me domein-in e fushës së njohurive statistikore. Emërtimi i domein-eve nuk është i harmonizuar në të gjithë Evropën. Çdo ofrues duhet të përdorë emërtimin sipas strukturës së tij ekzistuese.
Shembull: Lista e domein-eve nga databaza e Eurostatit:
- Popullsia dhe kushtet sociale;
- Ekonomia dhe financa;
- Bujqësia, pylltaria dhe peshkimi;
- Industria, tregtia dhe shërbimet;
- Tregtia e jashtme;
- Transporti;
- Mjedisi dhe energjia;
- Shkenca dhe teknologjia.
Atributi ’Tërësia’ jep një informacion, nëse statistikat nuk mund të caktohen në një domein dhe në njësinë e tyre. Ky është rasti nëse statistikat janë prodhuar për një arsye të caktuar, me kërkesë të përdoruesit, dhe duhet që të dokumentohen këtu.
Shembull: “Punësimi në bujqësi” mund të llogaritet si raport ndërmjet numrit të personave të punësuar në bujqësi dhe numrit të përgjithshëm të personave të punësuar të grup moshës 18-64 vjeç.
Atributi ’Matjet’ përmban vlerën e variablit të kodlistave dhe përshkruan shkurtimisht fenomenin për të cilin ofrohen të dhënat.
Atributet ’NjësitëEMatjes’ dhe ’MetodatEMatjes’ mbështesin përshkrimin e llojit të matjeve të siguruara nga shpërndarja. Vlerat e mundshme merren nga kodlistat përkatëse VleratENdryshme dhe VleratEMetodësSëMatjesSëStatistikave.
Sipas qasjes së përbashkët në INSPIRE, për të përshkruar cilësinë e përmbajtjes së një grupi të të dhënave, disa konsiderata për cilësinë e të dhënave shfaqen përmes atributit ’NukLlogaritetProporcioni’ që tregon numrin relativ të popullsisë, në një zonë interesi, por që nuk është paraqitur në asnjë prej elementeve të tij gjeohapësinorë.
Sipas rregullores nr. 1205/2008/EC, por dhe për shkak se dimensioni kohor është një komponent i rëndësishëm i informacionit statistikor, modeli përfshin tre atribute për adresimin e kësaj çështjeje:
PeriudhaEReferencës
Është periudha kur të dhënat supozohen të japin një pamje apo një përshkrim të zonës së interesit. Periudha e referencës në “Demografia” (Shpërndarja e popullsisë) mund të jetë një periudhë ose një datë e caktuar, datë fikse. Në rastin e fundit duhet të përdorim të njëjtën datë për fillimin dhe përfundimin.
PeriudhaEVlefshmërisë
Në temat “Njësitë Statistikore” dhe “Demografia” (shpërndarja e popullsisë) vlefshmëria është periudha në të cilën të dhënat mbesin aktive.
Për “Demografia” (shpërndarja e popullsisë) në shumicën e rasteve kjo është e përhershme. Në këtë rast data e dytë nuk plotësohet (lihet bosh).
PeriudhaEMatjes
Ky atribut është i dobishëm vetëm në “Demografia” (shpërndarja e popullsisë).
Data/periudha e vrojtimit është tërhequr, të dhënat janë mbledhur.
Për të lehtësuar përzgjedhjen e grupeve të të dhënave/vlerave për një përditësim të diferencuar, janë dhënë atributet ’FillimiICiklitJetësor’ dhe ’PërfundimiICiklitJetësor’.
Këto atribute përdoren nga një përdorues, i cili kërkon rregullisht të dhëna, por pret të marrë vetëm ato vlera që janë ndryshuar që nga kërkimi i tij i fundit dhe jo të gjitha vlerat e të dhënave.
Atributi ’StatusiIPërgjithshëm’ përdoret për të përshkruar statusin e vlerave për të gjithë grupin e të dhënave si, përfundimtare, gjysmë-përfundimtare ose të përkohshme dhe paraprake ose finale (Shembuj nga publikimet e Eurostatit).
Atributi ’Klasifikimet’ mund të përdoret për të përfaqësuar një sërë shpërndarjesh në lidhje me mënyrën e ndarjes së vlerave statistikore, në grupe të ndryshme, duke përdorur një ose disa klasifikime të individëve sipas karakteristikave të tyre. Nuk mund të ndodhë asnjë klasifikim për vlerat ’Totale’.
Shembull:
ShpërndarjaStatistikore. Klasifikimi
Gjinia
Grupmosha nga 5vjeç
VleratStatistikore.Përmasat
ElementetEKlasifikimit (2)
ElementetEKlasifikimit(1)
Vlerat
femër
0 - 5
134
mashkull
0 - 5
141
femër
5 - 10
128
mashkull
5 - 10
111
femër
10 - 15
89
Tipi i të dhënave: VleratStatistikore
Figura 8: Tipi i të dhënave Vlerat statistikore
Tipi i të dhënave VleratStatistikore mbështet përshkrimin e vlerave individuale të shpërndarjes:
Ky përshkrim përmban referencën për të kuptuar se cilit element gjeohapësinor dhe cilit element të klasifikimit i referohet vlera. Vlera elementare mund të shihet si diçka që mund të jetë vendosur në një hapësirë n-dimensionale që përfshin klasiken dy dimensionale, por edhe dimensionet në lidhje me klasifikimet e përdorura. Për shembull, një numër i thjeshtë i popullsisë në një njësi administrative ose në një shtet të caktuar do të kërkojë vetëm një referencë për hapësirën dy dimensionale, të parë përmes listës së njësive administrative ose listës së shteteve. Por, e njëjta popullsi e ndarë sipas gjinisë do të ketë nevojë për një dimension të tretë. Në qendër të këtij artikulli është atributi Vlerat, i cili përmban numrin e llogaritur statistikisht.
Në rast se vlerat nuk mund të jepen (p.sh: për shkak të privatësisë, gabimit, konfidencialitetit) arsyeja për mungesën e vlerës duhet të shprehet, duke përdorur atributin VleratEVeçanta. Gjithsesi, në të dyja rastet duhet që Vlerat ose Vlerat e Veçanta të jepen/paraqiten.
Vlerat mund të shoqërohen me Tregues dhe koment (atributi Koment) si zakonisht në komunitetin e statistikave, duke dhënë çdo lloj informacioni të dobishëm për të përshkruar situata të veçanta.
Dy atributet të tjera shtesë, që lidhen me cilësinë e të dhënave, japin sugjerime në lidhje me saktësinë e matjes janë: ProporcioniIVendosurNëMënyrëKonvencionale dhe PërafrimiIVendosjesSëProporcionit -TëPopullësisë. Këto atribute diskutohen në seksionin që bën fjalë për cilësisë.
Atributi ’Status’ përdoret për raste përjashtimore, pra për përjashtimin e një vlere të caktuar për atë që është specifikuar në informacionin e StatusiIPërgjithshëm të ShpërndarjaStatistikore.
Për shkak se nuk ka një koncept të harmonizuar se si të përdoren kodet korrekte të atributeve ’VleratEVeçanta’ dhe ’Tregues’, kodlistat përkatëse duhet të sigurohen nga ofruesi i të dhënave. Rekomandohet që komuniteti statistikor të zhvillojë një koncept të harmonizuar të përdorimit të vlerave të veçanta, treguesve dhe statusit.
Përveç kësaj, për secilin nga VleratStatistikore mund të jepet një vulë kohore (PeriudhaEMatjes), për të lejuar përjashtime nga ajo që është përcaktuar në informacionin e përgjithshëm.
Tipi i të dhënave VleratStatistikore. Dimensionet
Figura 9: Tipi i të dhënave Vlerat statistikore, Dimensionet
Shënim. Shoqërimi midis “Dimensionet” dhe “NjësitëStatistikore: Core” do të krijohet duke përdorur atributin ’IdTematike’ në vend të ’InspireId’ (shih më poshtë: referimi i të dhënave në njësitë statistikore).
Sipas pikëpamjes së SDMX (Statistical Data - Metadata Exchange) mbi dimensionet, të gjitha dimensionet e vlerës (tematike dhe hapësinore) përmblidhen në një dimension unik të të dhënave.
Shënim. Numri kardinal i dimensioneve të atributit është 1, sepse së paku duhet të jepet referenca gjeografike.
Në rast se nevojitet një ndarje/grupim shtesë i vlerave statistikore sipas një ose më shumë klasifikimeve, do të përdoret atributi ’ElementetEKlasifikimit’.
Shembull: Për të përshkruar një vlerë që përfaqëson popullsinë rezidenciale sipas gjinisë, kombësisë dhe klasat 5 vjeçare të moshës janë përdorur tre tematika të ElementetEKlasifikimit “mashkull”, “shqiptar” dhe “25-30’, nga domein-et e kodlistat “Gjinia”, “Kombësia” dhe “GrupmoshaSipasNdarjesÇdo5Vjet”
Referimi i të dhënave
Të gjitha të dhënat statistikore janë të gjeoreferuara (të lidhura indirekt me një njësi statistikore) dhe shprehen nga një identifikues i përbashkët, që në SDMX (Statistical Data - Metadata Exchange) quhet dimension gjeografik. Në GIS këto identifikues përdoren për të identifikuar gjeometrinë përkatëse dhe për t’u lidhur me të dhënat tabelore. Këto ID ndërtojnë urën (lidhjen) midis botës statistikore dhe gjeografike. Vështirësitë janë të pranishme dhe ato shtohen, sepse përdoren rregulla të ndryshme, kur dhe si duhet të ndryshojnë këta identifikues gjatë një evolucioni.
Një kërkesë e përgjithshme e Modelit të Përgjithshëm Konceptual (GCM) në INSPIRE është, që një ID duhet të jetë në gjendje të identifikojë në mënyrë unike dhe të përhershme atë me të cilën është e lidhur [ISO 19135]. Ky është një rregull që nuk zbatohet për atributet (identifikuesit) që përdoren në komunitetin statistikor.
Prandaj përveç InspireId, një atribut shtesë identifikues tematik është dhënë në “feature type” të NjësitëStatistikoreVektoriale. Ky ID tematik mund të përdoret për lidhjen e dhënave të “Demografia” (Shpërndarja e popullsisë) dhe “Njësitë Statistikore” duke ndjekur rekomandimet e specifikimit të të dhënave të njësisë statistikore.
Në rast se rregullat e azhurnimit për identifikuesin e një njësie statistikore të caktuar ndjekin rregullat e Modelit Konceptual i Përgjithshëm (GCM) në zbatim të standardit ISO [ISO 19135], i 3dentifikuesi Inspire mund të kopjohet si identifikues tematik.
Për shkak se objekti gjeohapësinor, të cilit i është lidhur një ID tematike (p.sh. një komunë), mund të ndryshojë, pa ndryshuar ID-në tematike, kërkohet të jepet ndonjë informacion i versionit. Në mënyrë tipike dhe të lehtë për t’u përdorur është viti i referencës. Kjo është e nevojshme për të shmangur lidhjen e statistikave me të dhënat gjeometrike që kanë vit të ndryshëm reference.
Rregullat e përditësimit për identifikuesit duhet të përshkruajnë qartë përdorimin e versionit të identifikuesit. Ka disa arsye për të krijuar një version të ri të një ID por jo një njësi të re statistikore (p.sh. zona ka ndryshuar më pak se 3% ose ka ndryshuar emri i saj).
Referenca gjeohapësinore e llojit të të dhënave VleratStatistikore është identifikuesi tematik i njësisë statistikore të referuar. Është vlera e një instance specifike të tipit të funksionit të NjësitëStatistikore.
Kërkesat dhe rekomandimet e dhëna në njësitë statistikore të të dhënave të INSPIRE duhet të merren në konsideratë kur lidhen të dhënat statistikore në njësitë gjeohapësinore.
Klasifikimi i kodlistave:
Figura 10: Kodlistat
FeatureType ShpërndarjaStatistikore përdor dy grupe kodlistash, e para për të klasifikuar vlerat statistikore dhe tjetra për të përshkruar variablat, matjen dhe statusin.
Tërësia, Domein-i dhe Variabla, përdoren për të identifikuar objektin, për të cilin metoda e matjes statistikore përshkruan se si realizohen të dhënat, ndërsa statusi shpjegon pjekurinë e grupit të të dhënave në zinxhirin e prodhimit. Të gjitha atributet e këtij lloji të funksioneve janë të vlefshme për të gjithë grupin e të dhënave.
Përjashtimet nga përshkrimi i mësipërm, në nivelin e vlerës, mund të përshkruhen duke përdorur atributet e caktuar për llojin e të dhënave “VleratStatistikore”. Kodlistat duhet të përdoren për atributet ’VleratEVeçanta’, ’Tregues’ dhe ’Statusi’.
Klasifikimet e grupeve, të kodlistave, përmbajnë ElementetEKlasifikimit, të përdorura për të identifikuar çdo vlerë tematike. Nëse nuk ofrohet klasifikim, vlera e variablave në njësitë statistikore përfaqëson totalin. Të gjitha klasifikimet e përdorura duhet të tregohen në atributin Klasifikimet, në tipin e funksionit ShpërndarjaStatistikore.
Nuk ka ndonjë rekomandim specifik në lidhje me qëndrueshmërinë midis grupeve të të dhënave gjeohapësinore. Duhet të ketë një përputhje midis objekteve të temave “Demografia” (Shpërndarja e popullsisë) dhe Njësisë statistikore. Për çdo njësi statistikore të referuar në të dhënat statistikore duhet të jepet gjeometria e njësisë statistikore. Rekomandohet të përdoret një identifikim i versionit të njësisë statistikore që përdoret për të grumbulluar të dhënat e anketuara.
Tipi i funksionit ShpërndarjaETëDhënaveStatistikore ka një atribut identifikues. Duke ndjekur rregullat e përgjithshme INSPIRE (Modelit të Përgjithshëm Konceptual) çdo objekt ka një ID, por mund të ketë edhe përjashtime për temat e aneksit III. Nga pikëpamja e përdorimit të të dhënave ndërvepruese, nuk nevojitet identifikues për temën “Demografia” (shpërndarja e popullsisë). ID mund të përdoret ndoshta edhe për shpërndarjen e të dhënave statistikore, nëse ofruesi i të dhënave do të ruajë përzgjedhjen e të dhënave ose pyetjen për një përdorim të mëtejshëm. Në këtë rast përdoruesi duhet të jetë në gjendje të gjejë të dhënat statistikore (ose ndoshta një version të përditësuar) duke përdorur InspireId.
Identifikuesi do të përbëhet nga dy pjesë: hapësira e emrave dhe një ID lokale. Hapësira e emrave është identifikimi unik i një regjistri kombëtar ku është i regjistruar identifikuesi, ndërsa IdLokale është identifikimi unik i një objekti brenda këtij emri. Qasja pragmatike për ta bërë atë unik në nivel ndërkombëtar është të shtohet një prefiks të identifikuesit të Shtetit Anëtar së bashku me një identifikues të temës specifike për hapësirën e emrave.
Meqenëse objektivat e INSPIRE i referohen vetëm shkëmbimit të të dhënave, mirëmbajtja dhe menaxhimi i identifikuesve unik INSPIRE është jashtë fushës së INSPIRE dhe është në përgjegjësinë e shteteve anëtare. Nëse nuk përfshihet ID, duhet të sigurohen disa të dhëna të tjera për ofruesin dhe bazën e të dhënave. Kjo duhet të jetë institucioni sigurues dhe nëse është e aplikueshme nga legjislacioni.
Figura 11: Struktura e temës “Demografia”
3.1.3 Katalogu i tipologjisë
3.1.3.1 Shpërndarja statistikore
-- Emri --
Shpërndarja statistikore
-- Përkufizimi --
Një sërë masash që përshkruajnë se si një fenomen është shpërndarë brenda një hapësire të caktuar.
-- Tipi i elementit --
FeatureType
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga «dataType» VleratStatistikore te «featureType» ShpërndarjaStatistikore
ATRIBUTET
Domein-i: PT_TekstILirë
Shumëllojshmëria: [1]
-- Emri --
Domein-i
-- Përkufizimi --
Pjesa e njohurive statistikore së cilës i referohen të dhënat.
-- Përshkrimi --
Shembull: Demografia, aktivitetet, etj.
[I detyrueshëm: PO]
FillimiICiklitJetësor: Datë - orë
Shumëllojshmëria: [1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data dhe ora në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore.
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [0..1]
-- Emri --
Inspire Id
-- Përkufizimi --
Identifikuesi i jashtëm i objektit gjeohapësinor.
-- Përshkrimi --
Një identifikues i jashtëm i objektit, është një identifikues unik i tij dhe i publikuar nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme për të referuar objektin gjeohapësinor. Identifikuesi është, një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit në realitet.
[I detyrueshëm: PO]
Matjet: VleratENdryshueshme
Shumëllojshmëria: [1]
-- Emri --
Matjet
-- Përkufizimi --
Matjet e përfshirë nga shpërndarja e popullsisë.
-- Përshkrimi --
Shembull: Popullsia sipas moshës dhe gjinisë, familjet sipas madhësisë etj.
[I detyrueshëm: PO]
MetodatEMatjes: VleratEMetodësSëMatjesSëStatistikave
Shumëllojshmëria: [1]
-- Emri --
Metodat e matjes
-- Përkufizimi --
Përshkrimi i metodës së matjes statistikore.
[I detyrueshëm: PO]
NjësitëEMatjes: NjësitëEMatjes
Shumëllojshmëria: [1]
-- Emri --
Njësitë e matjes
-- Përkufizimi --
Njësitë e matjes statistikore.
[I detyrueshëm: PO]
NukLlogaritetProporcioni: Numër
Shumëllojshmëria: [0..1]
-- Emri --
Nuk llogaritet proporcioni
-- Përkufizimi --
Përqindja e popullsisë në zonën e interesit e cila nuk llogaritet në asnjë nga përbërësit gjeohapësinorë të saj.
-- Përshkrimi --
Shembull: Kjo situatë mund të ndodhë kur popullsia totale e zonës së interesit mblidhet nga ndonjë proces (p.sh. regjistri administrativ), ndërsa popullsia në komponentët gjeohapësinorë të zonës së interesit nga një proces tjetër (p.sh. vlerësimi).
[I detyrueshëm: PO]
PërfundimiICiklitJetësor: Datë-orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i ciklit jetësor
-- Përkufizimi--
Data dhe ora në të cilën ky version i objektit gjeohapësinor është zëvendësuar ose tërhequr nga grupi i të dhënave gjeohapësinore.
[I detyrueshëm: PO]
PeriudhaEMatjes: TM_Periudhë
Shumëllojshmëria: [1]
-- Emri --
Periudha e matjes
-- Përkufizimi --
Data ose periudha kur janë mbledhur të dhënat/është kryer vrojtimi.
[I detyrueshëm: PO]
PeriudhaEReferencës: TM_Periudhë
Shumëllojshmëria: [1]
-- Emri --
Periudha e referencës
-- Përkufizimi --
Periudha kur të dhënat duhet të japin një pamje të zonës së interesit.
[I detyrueshëm: PO]
PeriudhaEVlefshmërisë: TM_Periudhë
Shumëllojshmëria: [0..1]
-- Emri --
Periudha e vlefshmërisë
-- Përkufizimi --
Periudha në të cilën të dhënat mbeten të përshtatshme.
-- Përshkrimi --
Jashtë kësaj periudhe të dhënat nuk do të përdoren dhe duhet të zëvendësohen me të dhëna të reja. Në shumicën e rasteve kjo është përgjithmonë dhe data e dytë mbetet bosh.
[I detyrueshëm: JO]
StatusiIPërgjithshëm: VleratEStatusitTëTëDhënaveStatistikore
Shumëllojshmëria: [1]
-- Emri --
Statusi i përgjithshëm
-- Përkufizimi --
Statusi i shpërndarjes së të dhënave statistikore.
[I detyrueshëm: PO]
Tërësia: PT_TekstILirë
Shumëllojshmëria: [0..1]
-- Emri --
Tërësia
-- Përkufizimi --
Kur shpërndarja është e lidhur me një nëngrup të popullsisë dhe jo me popullsinë në tërësinë e saj, jepet përshkrimi i drejtpërdrejtë i mënyrës së përcaktimit të këtij nëngrupi.
Shembull: Një grup i të dhënave mund të japë shpërndarjen e popullsisë të personave të papunë nën moshën 25 vjeçare. Variabli do të jetë “i papunë-popullimi’, masa një “numërim” dhe njësia e matjes “person”. E vetmja mënyrë për të shprehur se shpërndarja nuk mbulon të gjithë popullsinë e papunë do të ishte për të përshkruar atë situatë në atributin ’Tërësia’.
[I detyrueshëm: PO]
ZonaEShpërndarjes: GM_Spërfaqe
Shumëllojshmëria: [1]
-- Emri --
Zona e shpërndarjes
-- Përkufizimi --
Pjesa dy dimensionale (2D) që përshkruan ShpërndarjaETëDhënaveStatistikore.
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtimi: Burimi -> përcaktimi)
Burimi: (Class) ShpërndarjaStatistikore «featureType»
Objektivi: Klasifikimi (Class) Klasifikimet «dataType»
Shumëllojshmëria: [0..*]
-- Emri --
Klasifikimi
-- Përkufizimi --
Klasifikimet shtesë përdoren për të ndarë një vlerë totale të fenomenit të përshkruar. Objekti i Shpërndarjes Statistikore do të ofrojë në të vërtetë disa shpërndarje, një për secilin element të klasifikimit të përdorur.
NB: Kur nuk ofrohet klasifikim, vlera statistikore është popullata e përgjithshme.
3.1.3.2 Vlerat statistikore
-- Emri --
Vlerat statistikore
-- Përkufizimi --
Pjesët e datumit të shpërndarjes.
-- Tipi i elementit --
DataType
LIDHJE STRUKTURORE TË JASHTME
Mbledhur nga «dataType» VleratStatistikore te «featureType» ShpërndarjaStatistikore
ATRIBUTET
Tregues: PT_TekstILirë
Shumëllojshmëria: [0..1]
-- Emri --
Tregues
-- Përkufizimi --
Një grup komentesh me karakter të koduar për të dhënat, që tregon rëndësinë e tyre.
[I detyrueshëm: PO]
Komentet: PT_ TekstILirë
Shumëllojshmëria: [0..1]
-- Emri --
Komentet
-- Përkufizimi --
Koment pa stil për vlerat.
[I detyrueshëm: PO]
PërafrimiIVendosjesSëProporcionitTëPopullsisë: Numër
Shumëllojshmëria: [0..1]
-- Emri --
Përafrimi i vendosjes së proporcionit të popullsisë
-- Përkufizimi --
Përqindja e numrit të popullsisë që nuk ndjek rregullin e përbashkët për vendndodhjen. “Popullsia” mund të jetë persona nëse numërohen personat, banesa nëse shpërndarja e të dhënave statistikore ka të bëjë me banesat etj.
Shembull: Një shpërndarje statistikore e popullsisë supozohet se është prodhuar pasi njerëzit janë vendosur në parcelën kadastrale ku jetojnë. Për disa pasaktësi në regjistrat e përdorur, lokacioni aktual i parcelës kadastrale nuk u gjet për disa prej tyre dhe u llogarit një vend i vlerësuar. Numri i njerëzve në këtë rast duhet të raportohet në atribut.
[I detyrueshëm: PO]
PeriudhaEMatjes: TM_Periudhë
Shumëllojshmëria: [0..1]
-- Emri --
Periudha e matjes
-- Përkufizimi --
Periudha e mbledhjes së vlerës statistikore. Kjo periudhë anashkalon periudhën e përcaktuar në shpërndarjen statistikore të lidhur.
[I detyrueshëm: PO]
ProporcioniIVendosurNëMënyrëKonvencionale: Numër
Shumëllojshmëria: [0..1]
-- Emri --
Proporcioni i vendosur në mënyrë konvencionale
-- Përkufizimi --
Përqindja e popullsisë llogaritet në pjesë të të dhënave, por që nuk mund të gjendet fizikisht kudo brenda zonës së interesit.
Shembull: Ky proporcion do të përfshijë njerëz të pastrehë, të cilët kanë adresën e organizatës që shpërndan përfitimet sociale për ta.
[I detyrueshëm: PO]
Statusi: VleratEStatusitTëTëDhënaveStatistikore
Shumëllojshmëria: [1]
-- Emri --
Statusi
-- Përkufizimi --
Statusi i të dhënave statistikore.
[I detyrueshëm: PO]
Vlerat: Numër
Shumëllojshmëria: [0..1]
-- Emri --
Vlerat
-- Përkufizimi --
Vlera për pjesën e datumit.
[I detyrueshëm: PO]
VleratEVeçanta: VleratEVeçanta
Shumëllojshmëria: [0..1]
-- Emri --
Vlerat e veçanta
-- Përkufizimi --
Disa vargje konvencionale kur vlera për pjesën e datumit nuk mund të sigurohet: vlera e humbur, vlera e fshehur për shkak të konfidencialitetit.
[I detyrueshëm: PO]
LIDHJE
Lidhja (Drejtimi: Burimi -> përcaktimi)
Burimi: (class) VleratStatistikore «dataType»
Objektivi: Dimensions (class) dimensionet «dataType»
Shumëllojshmëria: [1]
-- Emri --
Dimensionet
-- Përkufizimi --
Pjesa e botës i referohet pjesës së datumit. Dimensionet përmbajnë një përshkrim të vendndodhjes gjeografike (përmasë 2D) së bashku me dimensionet e mundshme shtesë kur numrat e popullsisë prodhohen njëkohësisht për karakteristika të ndryshme individuale.
Shembull: Një numër i thjeshtë i popullsisë për secilën pjesë të zonës së shpërndarjes do të nevojitet vetëm identifikimi i këtyre pjesëve, ndërsa numri i popullsisë sipas gjinisë do të kërkojë dhe dimension shtesë (gjinor) për të bërë dallimin mes mashkullit dhe femrës.
3.1.3.3 Klasifikimet
-- Emri --
Klasifikimi
-- Përkufizimi --
Një klasifikim i përdorur për një shpërndarje statistikore.
-- Përshkrimi --
Kjo kodlistë përshkruan klasifikimin e vlerave statistikore të dhëna. Është përbërja e artikujve të klasifikimit.
-- Tipi i elementit --
DataType
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga «dataType» ElementetEKlasifikimit te «dataType» klasifikimet
ATRIBUTET
Lloji: VleratELlojeveTëKlasifikimit
Shumëllojshmëria: [1]
-- Emri --
Lloji
-- Përkufizimi --
Llojet e klasifikimit
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtimi: Burimi -> përcaktimi)
Burimi: (Class) ShpërndarjaStatistikore «featureType»
Objektivi: Klasifikimi (Class) klasifikimet «dataType»
Shumëllojshmëria: [0..*]
-- Emri --
Klasifikimi
-- Përkufizimi--
Klasifikimet shtesë përdoren për të ndarë një vlerë totale të fenomenit të përshkruar. Objekti i Shpërndarjes statistikore do të ofrojë në të vërtetë disa shpërndarje, një për secilin artikull të klasifikimit të përdorur.
NB: Kur nuk ofrohet klasifikim, vlera statistikore është popullata e përgjithshme.
3.1.3.4 Elementet e klasifikimit
-- Emri--
Elementet e klasifikimit
-- Përkufizimi --
Një artikull që përbën një klasifikim.
-- Përshkrimi --
Shembull: Klasifikimi i tipit “gjinia” përbëhet nga artikulli “femër”, “mashkull” dhe “i panjohur”.
-- Tipi i elementit --
DataType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizim nga «dataType» ElementetEKlasifikimit te «dataType» Klasifikimet
ATRIBUTET
Lloji: VleratELlojeveTëKlasifikimitTëArtikujve
Shumëllojshmëria: [1]
-- Emri --
Lloji
-- Përkufizimi --
Lloji i artikullit të klasifikimit
[I detyrueshëm: PO]
LIDHJE
Lidhje (Drejtim: Burimi -> Përcaktimi)
Burimi: (Class) Dimensionet «dataType»
Objektivi: Tematika (Class) ElementetEKlasifikimit «dataType»
Shumëllojshmëria: [0..*]
-- Emri --
Tematika
-- Përkufizimi --
Dimensionet tematike të vlerave statistikore
3.1.3.5 Dimensionet
-- Emri --
Dimensionet
-- Përkufizimi --
Identifikimi i asaj pjese të të dhënave që i përkasin vendndodhjes gjeografike ose karakteristikave individuale.
-- Tipi i elementit --
DataType
LIDHJE
Lidhje (Drejtimi: Burimi -> përcaktimi)
Burimi: (Class) Dimensionet «dataType»
Objektivi: Tematika (Class) ElementetEKlasifikimit «dataType»
Shumëllojshmëria: [0..*]
-- Emri --
Tematika
-- Përkufizimi --
Dimensionet tematike të vlerave statistikore.
Lidhje (Drejtimi: Burimi -> përcaktimi) «Versioni»
Burimi: (Class) Dimensionet «dataType»
Objektivi: Hapësirë (Class) NjësiaStatistikore «featureType»
Shumëllojshmëria: [1]
-- Emri --
Hapësirë
-- Përkufizimi --
Dimensionet gjeohapësinore të vlerave statistikore.
Lidhje (Drejtimi: Burimi-> përcaktimi)
Burimi: (Class) VleratStatistikore «dataType»
Objektivi: Dimensions (Class) Dimensionet «dataType»
Shumëllojshmëria: [1]
-- Emri --
Dimensionet
-- Përkufizimi --
Pjesa e botës i referohet pjesës së datumit. Dimensionet përmbajnë një përshkrim të vendndodhjes gjeografike (në dimensionin 2D) së bashku me dimensionet e mundshme shtesë kur numrat e popullsisë prodhohen njëkohësisht për karakteristika të ndryshme individuale.
Shembull: Një numër i thjeshtë i popullsisë, ku për secilën pjesë të fushës së shpërndarjes do të duhet vetëm identifikimi i këtyre pjesëve, ndërsa numri i popullsisë sipas gjinisë do të kërkojë dhe dimension shtesë (gjini) për të bërë dallimin mes meshkujve dhe femrave.
3.1.3.6 Vlerat e llojeve të klasifikimit të elementeve
-- Emri --
Vlerat e llojeve të klasifikimit të elementeve
-- Përkufizimi --
Vlerat e kodeve për elementet e klasifikimit.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË BRENDSHME
Gjeneralizuar nga «codeList» VleratEGrupMoshave te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
Gjeneralizuar nga «codeList» VleratEKodeveNACE te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
Gjeneralizuar nga «codeList» VleratEMoshësSipasVitit te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
Gjeneralizuar nga «codeList» VleratEMoshësNga5Vjet te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
3.1.3.7 Vlerat e moshës sipas vitit
-- Emri --
Vlerat e moshës sipas vitit
-- Përkufizimi --
Klasifikimi i artikujve sipas vlerave të kodeve të moshës sipas vitit.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «codeList» VleratEMoshësSipasVitit te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
3.1.3.8 Vlerat e moshës nga 5 vjet
-- Emri --
Vlerat e moshës nga 5 vjet
-- Përkufizimi --
Klasifikimi i artikujve sipas vlerave të kodeve të moshës nga 5 vjet.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «codeList» VleratEMoshësNga5Vjet te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
3.1.3.9 Vlerat e grupmoshave
-- Emri --
Vlerat e grupmoshave
-- Përkufizimi --
Vlerat e kodeve për artikujt e klasifikimit të grupmoshave.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «codeList» VleratEGrupMoshave te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
3.1.3.10 Vlerat e kodeve NACE
-- Emri --
Vlerat e kodeve NACE
-- Përkufizimi --
Vlerat e kodeve për artikujt e klasifikimit të NACE.
-- Tipi i elementit --
Kodlistë
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizuar nga «codeList» VleratEKodeveNACE te «codeList» VleratELlojeveTëKlasifikimitTëArtikujve
3.1.3.11 Vlerat e llojeve të klasifikimit
-- Emri --
Vlerat e llojeve të klasifikimit
-- Përkufizimi --
Vlerat e kodeve për llojet e klasifikimit.
-- Tipi i elementit --
Kodlistë
3.1.3.12 Vlerat e ndryshueshme
-- Emri --
Vlerat e ndryshueshme
-- Përkufizimi --
Vlerat e kodeve për vlerat e ndryshueshme.
-- Tipi i elementit --
Kodlistë
3.1.3.13 Vlerat e metodës së matjes së statistikave
-- Emri --
Vlerat e metodës së matjes së statistikave
-- Përkufizimi --
Vlera e kodeve për metodën e matjes së statistikave.
-- Tipi i elementit --
Kodlistë
3.1.3.14 Vlerat e statusit të të dhënave statistikore
-- Emri --
Vlerat e statusit të të dhënave statistikore
-- Përkufizimi --
Vlerat e kodeve nga statusi i të dhënave statistikore.
-- Tipi i elementit --
Kodlistë
3.1.3.15 Vlerat e veçanta
-- Emri --
Vlerat e veçanta
-- Përkufizimi --
Vlerat e kodeve të vlerave të veçanta. Shiko aneksin B.
-- Tipi i elementit --
codeList
3.2 Metadatat
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3 Kodi EPSG për KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare sipas vendimit të Këshillit të Ministrave nr. 669, datë 7.8.2013, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë”, ndryshuar me vendimin nr. 322, datë 27.4.2016 dhe vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është EPSG - 6870.
3.4 Cilësia e të dhënave
Matja e cilësisë së të dhënave për temën “Demografia” (shpërndarja e popullsisë) , kryesisht nuk lidhet me elementet e cilësisë së të dhënave të përmendura në “ISO/DIS 19157” (Cilësia e të Dhënave të Informacionit Gjeografik).
Matja e cilësisë statistikore duhet të harmonizohet me ESMS - Euro SDMX struktura e metadata-s (Statistical Data - Metadata Exchange), duke respektuar strukturën e raportimit të cilësisë (ESQR), të cilat përdoren nga agjencitë statistikore kombëtare dhe EUROSTAT. Ky raport synon të dokumentojë metodologjitë, cilësinë dhe proceset e prodhimit statistikor në përgjithësi. Ai përdor 21 koncepte të nivelit të lartë, me një zbërthim të kufizuar të nën-artikujve, që rrjedhin në mënyrë rigoroze nga lista e koncepteve të ndërlidhura në udhëzimet e orientuara drejt përmbajtjes (SDMX - Statistical Data - Metadata Exchange) (2009).
Harmonizimi i SSH EN ISO 19157 me SDMX (Statistical Data - Metadata Exchange) është përtej fushëveprimit të këtij dokumenti. Ky harmonizim është pjesë e misionit të ardhshëm që të konvergojë hapësirën gjeografike dhe statistikore dhe të mundësojë përputhshmërinë mes INSPIRE dhe EUROSTAT.
4. ANEKSE
4.1 Aneksi A - Katalogu i tipologjisë
Nr.
Emri i elementit Anglisht
Emri i elementit Shqip
Nëntema
Tipi
DEMOGRAFIA
3.1.5.1
Dimensions
Dimensionet
Demografia
DataType
3.1.5.2
ClassificationItem
ElementetEKlasifikimit
Demografia
DataType
3.1.5.3
Classification
Klasifikimet
Demografia
DataType
3.1.5.4
StatisticalDistribution
ShpërndarjaStatistikore
Demografia
FeatureType
3.1.5.5
AgeGroupValue
VleratEGrupmoshave
Demografia
Kodlistë
3.1.5.6
NACECodeValue
VleratEKodeveNACE
Demografia
Kodlistë
3.1.5.7
ClassificationTypeValue
VleratELlojeveTëKlasifikimit
Demografia
Kodlistë
3.1.5.8
ClassificationItemTypValue
VleratELlojeveTëKlasifikimitTëElementeve
Demografia
Kodlistë
3.1.5.9
StatisticsMeasurementMethodValue
VleratEMetodësSëMatjesSëStatistikave
Demografia
Kodlistë
3.1.5.10
AgeBy5YearsValue
VleratEMoshësNga5Vjet
Demografia
Kodlistë
3.1.5.11
AgeByYearValue
VleratEMoshësSipasVitit
Demografia
Kodlistë
3.1.5.12
VariableValue
VleratENdryshueshme
Demografia
Kodlistë
3.1.5.13
StatisticalDataStatusValue
VleratEStatusitTëTëDhënaveStatistikore
Demografia
Kodlistë
3.1.5.14
SpecialValue
VleratEVeçanta
Demografia
Kodlistë
3.1.5.15
StatisticalValue
VleratStatistikore
Demografia
DataType
4.2 Aneksi B - Kodlistat
4.2.1 Skema e aplikimit “Demografia’’ (Shpërndarja e popullsisë)
Kodlistat
VleratEMoshësNga5Vjet
VleratEMoshësSipasVitit
VleratEGrupMoshave
VleratELlojeveTëKlasifikimitTëArtikujve
VleratELlojeveTëKlasifikimit
VleratEVeçanta
VleratEStatusitTëTëDhënaveStatistikore
VleratEMetodësSëMatjesSëStatistikave
VleratENdryshueshme
4.2.1.1 Vlerat e moshës nga 5 vjet
-- Emri --
Vlerat e moshës nga 5 vjet
-- Përkufizimi --
Vlerat e kodit për elementet e klasifikimit për moshën nga 5 vjet.
-- Kohëzgjatja --
Asgjë
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/AgeBy5YearsValue
-- Vlerat --
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
KodListë
-- Emri --
0 - 5
-- Përkufizimi --
Nga 0 në më pak se 5.
-- Emri --
5 - 10
-- Përkufizimi --
Nga 5 në më pak se 10.
-- Emri --
10 - 15
-- Përkufizimi --
Nga 10 në më pak se 15.
-- Emri --
15 - 20
-- Përkufizimi --
Nga 15 në më pak se 20.
-- Emri --
20 - 25
-- Përkufizimi --
Nga 20 në më pak se 25.
-- Emri --
25 - 30
-- Përkufizimi --
Nga 25 në më pak se 30.
-- Emri --
30 - 35
-- Përkufizimi --
Nga 30 në më pak se 35.
-- Emri --
35 - 40
-- Përkufizimi --
Nga 35 në më pak se 40.
-- Emri --
40 - 45
-- Përkufizimi --
Nga 40 në më pak se 45.
-- Emri --
45 - 50
-- Përkufizimi --
Nga 45 në më pak se 50.
-- Emri --
50 - 55
-- Përkufizimi --
Nga 50 në më pak se 55.
-- Emri --
55 - 60
-- Përkufizimi --
Nga 55 në më pak se 60.
-- Emri --
60 - 65
-- Përkufizimi --
Nga 60 në më pak se 65.
-- Emri --
65 - 70
-- Përkufizimi --
Nga 65 në më pak se 70.
-- Emri --
70 - 75
-- Përkufizimi --
Nga 70 në më pak se 75.
-- Emri --
75 - 80
-- Përkufizimi --
Nga 75 në më pak se 80.
-- Emri --
80 - 85
-- Përkufizimi --
Nga 80 në më pak se 85.
-- Emri --
85 - 90
-- Përkufizimi --
Nga 85 në më pak se 90.
-- Emri --
90+
-- Përkufizimi --
Më shumë se 90.
-- Emri --
95 - 100
-- Përkufizimi --
Nga 95 në më pak se 100.
-- Emri --
100+
-- Përkufizimi --
Më shumë se 100.
4.2.1.2 Vlerat e moshës sipas vitit
-- Emri --
Vlerat e moshës sipas vitit
-- Përkufizimi --
Vlerat e kodit për elementet e klasifikimit të moshës sipas vitit.
-- Kohëzgjatja --
Asgjë
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/AgeByYearValue
-- Vlerat --
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
KodListë
-- Emri --
0_1
-- Përkufizimi --
Nga 0 në më pak se 1.
-- Emri --
1_2
-- Përkufizimi --
Nga 1 në më pak se 2.
-- Emri --
2_3
-- Përkufizimi --
Nga 2 në më pak se 3.
-- Emri --
3_4
-- Përkufizimi --
Nga 3 në më pak se 4.
-- Emri --
4_5
-- Përkufizimi --
Nga 4 në më pak se 5.
-- Emri --
5_6
-- Përkufizimi --
Nga 5 në më pak se 6.
-- Emri --
6_7
-- Përkufizimi --
Nga 6 në më pak se 7.
-- Emri --
7_8
-- Përkufizimi --
Nga 7 në më pak se 8.
-- Emri --
8_9
-- Përkufizimi --
Nga 8 në më pak se 9.
-- Emri --
9_10
-- Përkufizimi --
Nga 9 në më pak se 10.
-- Emri --
10_11
-- Përkufizimi --
Nga 10 në më pak se 11.
-- Emri --
11_12
-- Përkufizimi --
Nga 11 në më pak se 12.
-- Emri --
12_13
-- Përkufizimi --
Nga 12 në më pak se 13.
-- Emri --
13_14
-- Përkufizimi --
Nga 13 në më pak se 14.
-- Emri --
14_15
-- Përkufizimi --
Nga 14 në më pak se 15.
-- Emri --
15_16
-- Përkufizimi --
Nga 15 në më pak se 16.
-- Emri --
16_17
-- Përkufizimi --
Nga 16 në më pak se 17.
-- Emri --
18_19
-- Përkufizimi --
Nga 18 në më pak se 19.
-- Emri --
19_20
-- Përkufizimi --
Nga 19 në më pak se 20.
-- Emri --
20_21
-- Përkufizimi --
Nga 20 në më pak se 21.
-- Emri --
21_22
-- Përkufizimi --
Nga 21 në më pak se 22.
-- Emri --
22_23
-- Përkufizimi --
Nga 22 në më pak se 23.
-- Emri --
23_24
-- Përkufizimi --
Nga 23 në më pak se 24.
-- Emri --
24_25
-- Përkufizimi --
Nga 24 në më pak se 25.
-- Emri --
25_26
-- Përkufizimi --
Nga 25 në më pak se 26.
-- Emri --
26_27
-- Përkufizimi --
Nga 26 në më pak se 27.
-- Emri --
27_28
-- Përkufizimi --
Nga 27 në më pak se 28.
-- Emri --
28_29
-- Përkufizimi --
Nga 28 në më pak se 29.
-- Emri --
29_30
-- Përkufizimi --
Nga 29 në më pak se 30.
-- Emri --
30_31
-- Përkufizimi --
Nga 30 në më pak se 31.
-- Emri --
31_32
-- Përkufizimi --
Nga 31 në më pak se 32.
-- Emri --
32_33
-- Përkufizimi --
Nga 32 në më pak se 33.
-- Emri --
33_34
-- Përkufizimi --
Nga 33 në më pak se 34.
-- Emri --
34_35
-- Përkufizimi --
Nga 34 në më pak se 35.
-- Emri --
35_36
-- Përkufizimi --
Nga 35 në më pak se 36.
-- Emri --
36_37
-- Përkufizimi --
Nga 36 në më pak se 37.
-- Emri --
37_38
-- Përkufizimi --
Nga 37 në më pak se 38.
-- Emri --
38_39
-- Përkufizimi --
Nga 38 në më pak se 39.
-- Emri --
39_40
-- Përkufizimi --
Nga 39 në më pak se 40.
-- Emri --
40_41
-- Përkufizimi --
Nga 40 në më pak se 41.
-- Emri --
41_42
-- Përkufizimi --
Nga 41 në më pak se 42.
-- Emri --
42_43
-- Përkufizimi --
Nga 42 në më pak se 43.
-- Emri --
43_44
-- Përkufizimi --
Nga 43 në më pak se 44.
-- Emri --
44_45
-- Përkufizimi --
Nga 44 në më pak se 45.
-- Emri --
45_46
-- Përkufizimi --
Nga 45 në më pak se 46.
-- Emri --
46_47
-- Përkufizimi --
Nga 46 në më pak se 47.
-- Emri --
47_48
-- Përkufizimi --
Nga 47 në më pak se 48.
-- Emri --
48_49
-- Përkufizimi --
Nga 48 në më pak se 49.
-- Emri --
49_50
-- Përkufizimi --
Nga 49 në më pak se 50.
KodListë
-- Emri --
50_51
-- Përkufizimi --
Nga 50 në më pak se 51.
-- Emri --
51_52
-- Përkufizimi --
Nga 51 në më pak se 52.
-- Emri --
52_53
-- Përkufizimi --
Nga 52 në më pak se 53.
-- Emri --
53_54
-- Përkufizimi --
Nga 53 në më pak se 54.
-- Emri --
54_55
-- Përkufizimi --
Nga 54 në më pak se 55.
-- Emri --
55_56
-- Përkufizimi --
Nga 55 në më pak se 56.
-- Emri --
56_57
-- Përkufizimi --
Nga 56 në më pak se 57.
-- Emri --
57_58
-- Përkufizimi --
Nga 57 në më pak se 58.
-- Emri --
58_59
-- Përkufizimi --
Nga 58 në më pak se 59.
-- Emri --
59_60
-- Përkufizimi --
Nga 59 në më pak se 60.
-- Emri --
60_61
-- Përkufizimi --
Nga 60 në më pak se 61.
-- Emri --
61_62
-- Përkufizimi --
Nga 61 në më pak se 62.
-- Emri --
62_63
-- Përkufizimi --
Nga 62 në më pak se 63.
-- Emri --
63_64
-- Përkufizimi --
Nga 63 në më pak se 64.
-- Emri --
64_65
-- Përkufizimi --
Nga 64 në më pak se 65.
-- Emri --
65_66
-- Përkufizimi --
Nga 65 në më pak se 66.
-- Emri --
66_67
-- Përkufizimi --
Nga 66 në më pak se 67.
-- Emri --
68_69
-- Përkufizimi --
Nga 68 në më pak se 69.
-- Emri --
69_70
-- Përkufizimi --
Nga 69 në më pak se 70.
-- Emri --
70_71
-- Përkufizimi --
Nga 70 në më pak se 71.
-- Emri --
71_72
-- Përkufizimi --
Nga 71 në më pak se 72.
-- Emri --
72_73
-- Përkufizimi --
Nga 72 në më pak se 73.
-- Emri --
73_74
-- Përkufizimi --
Nga 73 në më pak se 74.
-- Emri --
74_75
-- Përkufizimi --
Nga 74 në më pak se 75.
-- Emri --
75_76
-- Përkufizimi --
Nga 75 në më pak se 76.
-- Emri --
76_77
-- Përkufizimi --
Nga 76 në më pak se 77.
-- Emri --
77_78
-- Përkufizimi --
Nga 77 në më pak se 78.
-- Emri --
78_79
-- Përkufizimi --
Nga 78 në më pak se 79.
-- Emri --
79_80
-- Përkufizimi --
Nga 79 në më pak se 80.
-- Emri --
80_81
-- Përkufizimi --
Nga 80 në më pak se 81.
-- Emri --
81_82
-- Përkufizimi --
Nga 81 në më pak se 82.
-- Emri --
82_83
-- Përkufizimi --
Nga 82 në më pak se 83.
-- Emri --
83_84
-- Përkufizimi --
Nga 83 në më pak se 84.
-- Emri --
84_85
-- Përkufizimi --
Nga 84 në më pak se 85.
-- Emri --
85_86
-- Përkufizimi --
Nga 85 në më pak se 86.
-- Emri --
86_87
-- Përkufizimi --
Nga 86 në më pak se 87.
-- Emri --
87_88
-- Përkufizimi --
Nga 87 në më pak se 88.
-- Emri --
88_89
-- Përkufizimi --
Nga 88 në më pak se 89.
-- Emri --
89_90
-- Përkufizimi --
Nga 89 në më pak se 90.
-- Emri --
90_91
-- Përkufizimi --
Nga 90 në më pak se 91.
-- Emri --
91_92
-- Përkufizimi --
Nga 91 në më pak se 92.
-- Emri --
92_93
-- Përkufizimi --
Nga 92 në më pak se 93.
-- Emri --
93_94
-- Përkufizimi --
Nga 93 në më pak se 94.
-- Emri --
94_95
-- Përkufizimi --
Nga 94 në më pak se 95.
-- Emri --
95_96
-- Përkufizimi --
Nga 95 në më pak se 96.
-- Emri --
96_97
-- Përkufizimi --
Nga 96 në më pak se 97.
-- Emri --
97_98
-- Përkufizimi --
Nga 97 në më pak se 98.
-- Emri --
98_99
-- Përkufizimi --
Nga 98 në më pak se 99.
-- Emri --
99_100
-- Përkufizimi --
Nga 99 në më pak se 100.
-- Emri --
100+
-- Përkufizimi --
Më shumë se 100.
4.2.1.3 Vlerat e grupmoshave
-- Emri --
Vlerat e grupmoshave
-- Përkufizimi --
Vlerat e kodit për elementet e klasifikimit për grupmoshat.
-- Kohëzgjatja --
Hapur
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/AgeGroupValue
-- Vlerat --
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
KodListë
-- Emri --
0_15
-- Përkufizimi --
Nga 0 në më pak se 15.
-- Emri --
15_65
-- Përkufizimi --
Nga 15 në më pak se 65.
-- Emri --
65+
-- Përkufizimi --
Më shumë se 65.
4.2.1.4 Vlerat e llojeve të klasifikimit të elementeve
-- Emri --
Vlerat e llojeve të klasifikimit të elementeve
-- Përkufizimi --
Vlerat e kodit për elementet e klasifikimit.
-- Kohëzgjatja --
Asgjë
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/ClassificationItemTypeValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë dhe vlerat shtesë në çdo nivel të përcaktuar nga ofruesit e të dhënave.
KodListë
-- Emri --
0-5
-- Përkufizimi --
Nga 0 në më pak se 5.
-- Emri --
10 maj
-- Përkufizimi --
Nga 5 në më pak se 10.
-- Emri --
15 tetor
-- Përkufizimi --
Nga 10 në më pak se 15.
-- Emri --
15 - 20
-- Përkufizimi --
Nga 15 në më pak se 20.
-- Emri --
20 - 25
-- Përkufizimi --
Nga 20 në më pak se 25.
-- Emri --
25 - 30
-- Përkufizimi --
Nga 25 në më pak se 30.
-- Emri --
30 - 35
-- Përkufizimi --
Nga 30 në më pak se 35.
-- Emri --
35 - 40
-- Përkufizimi --
Nga 35 në më pak se 40.
-- Emri --
40 - 45
-- Përkufizimi --
Nga 40 në më pak se 45.
-- Emri --
45 - 50
-- Përkufizimi --
Nga 45 në më pak se 50.
-- Emri --
50 - 55
-- Përkufizimi --
Nga 50 në më pak se 55.
-- Emri --
55 - 60
-- Përkufizimi --
Nga 55 në më pak se 60.
-- Emri --
60 - 65
-- Përkufizimi --
Nga 60 në më pak se 65.
-- Emri --
65 - 70
-- Përkufizimi --
Nga 65 në më pak se 70.
-- Emri --
70 - 75
-- Përkufizimi --
Nga 70 në më pak se 75.
-- Emri --
75 - 80
-- Përkufizimi --
Nga 75 në më pak se 80.
-- Emri --
80 - 85
-- Përkufizimi --
Nga 80 në më pak se 85.
-- Emri --
85 - 90
-- Përkufizimi --
Nga 85 në më pak se 90.
-- Emri --
90+
-- Përkufizimi --
Më shumë se 90.
-- Emri --
95 - 100
-- Përkufizimi --
Nga 95 në më pak se 100.
-- Emri --
100+
-- Përkufizimi --
Më shumë se 100.
4.2.1.5 Vlerat e llojeve të klasifikimit
-- Emri --
Vlerat e llojeve të klasifikimit
-- Përkufizimi --
Vlerat e kodit për llojet e klasifikimit.
-- Kohëzgjatja --
Hapur
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/ClassificationTypeValue
-- Vlerat --
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, duhet të kontrollohet nëse njëri prej tyre mund të përdoret.
KodListë
-- Emri --
Mosha për 5 vjet
-- Përkufizimi --
Mosha për periudhën 5-vjeçare.
-- Emri --
Grupmoshat
-- Përkufizimi --
Grupmoshat.
-- Emri --
Mosha sipas vitit
-- Përkufizimi --
Mosha sipas vitit.
-- Emri --
Gjinia
-- Përkufizimi --
Femër, mashkull ose e panjohur
-- Emri --
NACE
-- Përkufizimi --
Klasifikimi i aktivitetit ekonomik NACE 2 (Klasifikimi i Aktiviteteve Ekonomike në Komunitetin Evropian).
4.2.1.6 Vlerat e veçanta
-- Emri --
Vlerat e veçanta
-- Përkufizimi --
Vlerat e kodit për vlerat e veçanta.
-- Kohëzgjatja --
Hapur
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/SpecialValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë dhe vlerat shtesë në çdo nivel të përcaktuar nga ofruesit e të dhënave.
KodListë
-- Emri --
I fshehtë/konfidencial
-- Përkufizimi --
Vlera nuk jepet për arsye konfidencialiteti.
-- Emri --
I panjohur
-- Përkufizimi --
Vlera mund të jetë matur, por nuk publikohet.
-- Emri --
Nuk aplikohet
-- Përkufizimi --
Vlera nuk do të kishte ndonjë kuptim.
4.2.1.7 Vlerat e statusit të të dhënave statistikore
-- Emri --
Vlerat e statusit të të dhënave statistikore
-- Përkufizimi --
Vlerat e kodit për statusin e të dhënave statistikore.
-- Kohëzgjatja --
Hapur
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/StatusValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë dhe vlerat shtesë në çdo nivel të përcaktuar nga ofruesit e të dhënave.
KodListë
-- Emri --
Përfundimtar
-- Përkufizimi --
Një vlerë e të dhënave statistikore përfundimtare.
-- Emri --
I fundit
-- Përkufizimi --
Vlera e fundit e të dhënave statistikore.
-- Emri --
Paraprake
-- Përkufizimi --
Një vlerë paraprake statistikore.
-- Emri --
Përkohshëm
-- Përkufizimi --
Një vlerë e përkohshme e të dhënave statistikore.
-- Emri --
Gjysmë përfundimtare
-- Përkufizimi --
Një vlerë gjysmë përfundimtare e të dhënave statistikore.
4.2.1.8 Vlerat e metodës së matjes së statistikave
-- Emri --
Vlerat e metodës së matjes së statistikave
-- Përkufizimi --
Vlera e kodit për metodën e matjes së statistikave.
-- Kohëzgjatja --
Hapur
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/StatisticsMeasurementMethodValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë dhe vlerat shtesë në çdo nivel të përcaktuar nga ofruesit e të dhënave.
KodListë
-- Emri --
Çështje/Numërim
-- Përkufizimi --
Një çështje/numërim i thjeshtë.
-- Përshkrimi --
Shembull: Numri i personave.
-- Emri --
Numërimi relativ
-- Përkufizimi --
Një raport që kombinon dy lloje të ndryshme të popullsisë statistikore.
-- Përshkrimi --
Shembull: Numri mesatar i makinave për banesë.
-- Emri --
Përqindje
-- Përkufizimi --
Një proporcion/përqindje i shprehur si një raport me emëruesin e të cilit është 100.
-- Përshkrimi --
Shembull: Përqindja e të papunëve.
-- Emri --
Mesatar
-- Përkufizimi --
Mesatar.
-- Përshkrimi --
Shembull: Shkalla e rritjes së popullsisë.
4.2.1.9 Vlerat e ndryshueshme
-- Emri --
Vlerat e ndryshueshme
-- Përkufizimi --
Vlerat e kodit për emrat e ndryshueshëm.
-- Kohëzgjatja --
Ndonjë
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/VariableValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë çdo vlerë të përcaktuar nga ofruesit e të dhënave.
Tabela më poshtë përfshin vlerat e rekomanduara që mund të përdoren nga ofruesit e të dhënave. Para krijimit të kushteve të reja, kontrolloni nëse njëri prej tyre mund të përdoret.
KodListë
-- Emri --
Lindjet
-- Përkufizimi --
Numri i lindjeve.
-- Emri --
Të ardhura
-- Përkufizimi --
Të ardhurat.
-- Emri --
Popullsia në vendin e banimit
-- Përkufizimi --
Numri i njerëzve të matur në vendin ku ata flenë.
-- Emri --
Popullsia në vendin e punës
-- Përkufizimi --
Numri i njerëzve të matur në vendin ku ata punojnë.
-- Emri --
Popullsisë së papunë
-- Përkufizimi --
Popullsisë që rezulton e papunë.
-- Emri --
Të punësuar
-- Përkufizimi --
Popullsisë që rezulton e punësuar.
