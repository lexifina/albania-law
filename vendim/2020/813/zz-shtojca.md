# Shtojca
STANDARDET SHTETËRORE
PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI - TEMA: SISTEMET E RRJETEVE GJEOGRAFIKE
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. TEMA
3.1 Sistemet e rrjeteve gjeografike
3.1.1 Parathënie
3.1.2 Qëllimi dhe objektivi
3.1.3 Terma dhe përkufizime
3.2 Rrjetet gjeografike
3.2.1 Projeksionet
3.2.1.1 Projeksioni TM-Zonal
3.2.1.2 Projeksioni LCC
3.2.1.3 Indeksimi i fletës së hartës
3.2.2 Skema konceptuale UML - Sistemet e rrjeteve gjeografike - Diagrame
3.2.3 Katalogu i tipologjisë
3.2.3.1 Projeksioni TM-zn
3.2.3.2 Projeksioni LCC
3.2.3.3 Përmasat e fletës
3.2.3.4 Rrjetet gjeografike
3.3 Metadata
3.4 Kodi EPSG për KRGJSH-në
3.5 Cilësia e të dhënave
3.5.1 Kompletimi - Komisioni (Completeness - Commission)
3.5.2 Kompletimi - Përjashtimi (Completeness - Omission)
4. ANEKSE
1.1 Aneksi A - Katalogu i tipologjisë
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG). Data e publikimit të versionit nr. 1 është 13 shtator 2017. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2017_ SRRGJ _v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit
Standard - Lloji i dokumentit
NSDI - Qëllimi i dokumentit
2017 - Viti i krijimit
SRRGJ - Tema për të cilën është krijuar standardi: “Sistemet e rrjeteve gjeografike”, e cila i referohet temës “Geographical Grid Systems” të direktivës INSPIRE
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 QËLLIMI
Ky dokument përcakton specifikimet teknike, për të dhënat gjeohapësinore të temës “Sistemet e rrjeteve gjeografike”, temë e cila është përcaktuar në nenin 11, pika 2/b, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse, për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë midis tyre.
2.2 SI LEXOHET DOKUMENTI
2.2.1 STRUKTURA E DOKUMENTIT
Ky dokument është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve - Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje - Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të interpretohet më lehtë ai.
3. Tema - Në këtë pjesë jepen specifikimet teknike për temën “Sistemet e rrjeteve gjeografike”.
4. Anekse - Në këtë pjesë jepen informacione shtesë, shpjeguese, në ndihmë të përdoruesve.
- Përmbajtja e kapitullit të 3-të është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës, si dhe detajohen: Diagramet UML dhe Katalogu i tipologjive.
3.2 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3 Sistemi Koordinativ Referencë - Këtu përcaktohet sistemi koordinativ referencë (KRGJSH).
3.4 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet ndërmjet tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në Katalogun i tipologjive (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave, duke u fokusuar te Katalogu i tipologjive. Për përdoruesit e aplikacioneve, Katalogu i tipologjive mund të jetë i dobishëm për të kontrolluar nëse ai përmban të dhëna të nevojshme për përdorim.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në Katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të shembujve, shpjegojnë mënyrën e organizimit të informacionit, në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shembulli, shpjegon mënyrën e organizimit të informacionit, në tabelën e kodlistës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Lloji i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
FeatureType, një element që mund të jetë real, në terren, apo një dukuri abstrakte.
“DataType”, një element tabelor, që shërben vetëm si tabelë atributesh, për t’u lidhur me një element tjetër.
“Enumeration” “codeList”, listë e parapërgatitur vlerash, ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe kodlistë. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
“Union”, një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan tiparet, të cilat bien brenda shtrirjes gjeohapësinore të të dyja grupeve të të dhënave hyrëse.
“Imported”, të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden të shqipëruara si “Të dhënat e importuara”.
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë, poligon.
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
Në tabelën e lidhjeve “Rol-shoqërime” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Atributet
“Atribut” janë informacione të bashkëngjitura në format tabelor te tipologjitë gjeohapësinore.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi i elementeve
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin.
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh., PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh., ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
Vlera e dytë (etj.) e listës së gatshme, p.sh., joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi i elementeve.
2.2.3 KARAKTERISTIKAT E VOIDABLE DHE SHUMËLLOJSHMËRIA
Stereotipi voidable përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore, edhe pse mund të ekzistojnë në realitet. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera void. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse, në grupet e të dhënave gjeohapësinore, që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur, duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
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
- Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
-- Përshkrimi --
Shembull. Të dhënat personale të popullsisë, të cilat ekzistojnë, por që nuk mund të shfaqen pasi mbrohen nga legjislacioni për mbrojtjen e të dhënave personale.
Stereotipi voidable nuk jep informacion nëse karakteristika ekziston apo jo në realitet. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në realitet, vlera minimale do të përcaktohet si 0. P.sh., nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në realitet, vlera minimale do të përcaktohet si 1. P.sh., nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit Coverages përdoren për të përshkruar karakteristikat e një fenomeni të botës reale që zhvillohet në kohë dhe/ose hapësirë. Shembuj tipikë të tyre janë temperaturat, lartësitë, imazheritë etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domeinet tipike gjeohapësinore janë grupe pikash (p.sh., vendndodhja e sensorëve), kurbat përcaktuese (p.sh., izolinjat), rrjetet (p.sh., ortoimazheria, modelet e lartësive) etj.
Në skemat e aplikimit të INSPIRE, funksionet e mbulimit janë përcaktuar si veti të llojeve të objekteve gjeohapësinore, ku lloji i vlerës së kësaj karakteristike është realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh., ISO 19136 dhe OGC Shërbimi i mbulimit në internet) dhe për të përmirësuar harmonizimin ndërtematik, për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në modelin konceptual të përgjithshëm Generic Conceptual Model.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domeini i të cilit përbëhet nga një rrjet referimi, një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje mbulimi (ose një nëntip i tyre) në skemat e aplikimit të INSPIRE.
Figura 1. Shembuj të një rrjeti të korrigjuar (majtas) dhe një rrjeti referues (djathtas)
2.2.5 NUMËRTIMET DHE KODLISTAT (ENUMERATION AND CODELIST)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, “vlera të tjera” përcakton llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht si më poshtë:
- “Jo” përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument.
- “Të kufizuara” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave.
- “Të hapura” përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave.
- “Po” përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese, të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera “jo” të përmbajtura në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që dhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në realitet.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
Shënim i rëndësishëm
Disa terma në Katalogun e tipologjive, si p.sh., FeatureType, DataType etj., nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike, sipas termave të direktivës INSPIRE.
2.3 DETYRIMET LIGJORE
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është institucioni përgjegjës për krijimin e standardeve, për secilën nga temat e përcaktuara në nenin 11, të këtij ligji, në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore, për krijimin e NSDI-së në Shqipëri, janë përshtatur nga specifikimet teknike të temave përkatës në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - Në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (sikurse është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë atë (VKM nr. 1077, datë 23.12.2015).
- Specifikimi i të dhënave - Standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 FUSHA E VEPRIMIT
Të gjitha autoritetet publike, kompani private apo individë, që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
Figura 2. Proceset e ciklit jetësor
“Planifikimi” është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
“Vlerësimi” është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
“Procesimi” është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
“Shpërndarja” është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
“Zbulimi” është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
“Analiza” është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet më të dhënat që janë evidentuar.
“Përditësimi” është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
“Arkivimi” është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen, duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendit ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
“Shkatërrimi” është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 SISTEMET E RRJETEVE GJEOGRAFIKE
3.1.1 PARATHËNIE
Përdorimi i rrjeteve gjeografike është një metodë indirekte e ruajtjes së informacionit gjeohapësinor. Rrjetet janë mjete të fuqishme për harmonizimin dhe reduktimin e kompleksitetit të grupeve të të dhënave. Rrjetet gjeografike janë, gjithashtu, mjete efektive komunikimi në raportimin e ndryshimeve gjeohapësinore të tipologjive. Teknikisht, rrjetet për të dhënat gjeografike janë struktura referimi gjeohapësinore të paracaktuara, të përbëra nga qeliza (pjesë apo fletë) të rregullta në formë ose sipërfaqe.
Një rrjet zakonisht përdor një matricë me nxm qeliza të shtrira në 2 akse, horizontale dhe vertikale. Si rezultat, rrjeti i qelizave mund të identifikohet nga një numër i plotë, i cili formohet nga numri i rreshtit dhe i kolonës së pozicionit përkatës.
Në varësi të qëllimit ekzistojnë lloje të ndryshme rrjetesh. Një rrjet i dobishëm për të gjitha qëllimet do të ishte ideal, por krijimi i tij, që të mbulojë në mënyrë uniforme të gjithë Evropën, nuk është i mundur. Çdo lloj rrjeti ka specifikime të ndryshme, në varësi të përdorimit, çka e bën atë të ketë dizavantazhe kundrejt rrjeteve të tjera.
Direktiva INSPIRE përcakton “Sistemet e rrjeteve gjeografike” si një temë e të dhënave referencë në aneksin e parë, që përbën një kornizë gjeohapësinore për të lidhur informacionet e tjera. Tema “Sistemet e rrjeteve gjeografike” është një nga temat më të rëndësishme të të dhënave në infrastrukturën e të dhënave gjeohapësinore (SDI). Principet kryesore të specifikimeve INSPIRE për sistemet e rrjetit gjeografik janë: të ndërtohen referenca të qarta dhe të identifikohet çdo qelizë e rrjetit.
Specifikimi i të dhënave për rrjetet gjeografike nga INSPIRE, përcakton dy rrjete gjeografike për përdorimin e tyre në Evropë:
- Rrjeti me Sipërfaqe të Barabarta (Equal Area Grid), i cili synon të përdoret më shumë për qëllime të raportimeve statistikore. Ky rrjet është i përcaktuar si Grid_ETRS89-LAEA.
- Rrjeti Gjeografik Zonal (Zoned Geographic Grid), i cili ka për qëllim sigurimin e informacionit të rrjetëzuar gjeohapësinor për temat e të dhënave referencë(p.sh., të dhënat raster, të dhëna të bazuara në mbulim - coverage). Ky rrjet është i përcaktuar si Grid_ETRS89-GRS80zn_res.
Sistemi i kodimit (nomenklatura) të INSPIRE identifikon madhësinë e qelizës dhe pozicionin e cepit të poshtëm, majtas. Por shumë vende e kanë mbuluar territorin e tyre me rrjete të bazuara në koordinata plane kombëtare dhe pikën e fillimit të numërimit të fletëve e kanë të ndryshme.
Hartat dhe planet topografike të territorit të Republikës së Shqipërisë do të përpilohen bazuar në vendimin nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si metadatë”, të ndryshuar me vendimet nr. 322, datë 27.4.2016 dhe nr. 359, datë 29.5.2019. Ky vendim e ka të përcaktuar mjaft qartë referencën gjeodezike që do të përdoret, si dhe mënyrën e ndarjes dhe emërtimit të fletëve të hartave.
3.1.2 QËLLIMI DHE OBJEKTIVI
Qëllimi
Ky standard përshkruan një formë unike të rregullave dhe procedurave që duhen ndjekur për të krijuar sistemet e rrjeteve gjeografike. Këtu përshkruhen konceptet bazë për rrjetet gjeografike dhe përcaktohet procedura e indeksimit të fletëve të hartave.
Objektivi
1. Sigurimi i një kornize 2-dimensionale me referencë të qartë gjeodezike, unike dhe të identifikueshme për çdo fletë (qelizë) të hartës sipas shkallës.
2. Rritja e ndërveprueshmërisë midis temave të ndryshme të përcaktuara sipas nenit 11, të ligjit 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
3. Realizimi i harmonizimit, ruajtjes së informacionit gjeohapësinor dhe reduktimit të kompleksitetit të grupeve të të dhënave.
3.1.3 TERMA DHE PËRKUFIZIME
“Brez” quhet hapësira në sferë ose elipsoid e formuar nga kufizimi i dy paraleleve.
“Ekuatori” është vijëprerja e sipërfaqes së një sfere ose elipsoidi me një rrafsh pingul me boshtin e rrotullimit të sferës ose elipsoidit që kalon në qendrën gjeometrike.
“Elipsoid” është një sipërfaqe e formuar nga rrotullimi i një elipsi rreth boshtit të tij të vogël.
“Faktori shkallë për meridianin qendror (k0)” është një koeficient numerik pa njësi, i cili shërben për të menaxhuar shformimet në projeksione. Ai jepet si raport i rrezes së cilindrit me rrezen e madhe të elipsoidit. Kur k0=1 kemi të bëjmë me cilindër tangencues, kur k0<1 kemi të bëjmë me cilindër ndërprerës.
“GRS80 (Geodetic Reference System)” është sistemi referues gjeodezik i përcaktuar në vitin 1980 dhe i pranuar ndërkombëtarisht.
“Gjerësia gjeografike (φ)” është këndi i matur në rrafshin e meridianit ndërmjet rrafshit të ekuatorit dhe normales së sipërfaqes së elipsoidit në një pikë P (figura 4).
“Gjatësia gjeografike (λ)” është këndi i matur në rrafshin e ekuatorit midis rrafshit të meridianit që kalon në Greenwich (meridiani zero ose fillestar) dhe rrafshit të meridianit që kalon në pikën P (figura 4).
“Koordinatat” janë bashkësi 2 ose 3 numrash që përcaktojnë pozicionin e pikave në një sistem koordinativ të zgjedhur mbi sipërfaqen e sferës, elipsoidit ose rrafshit të një projeksioni.
“Meridianët” janë vijëprerje të fituara nga ndërprerja e sferës ose elipsoidit me rrafshe që përmbajnë boshtin e rrotullimit të sferës ose elipsoidit.
“Meridiani fillestar” është meridiani i zgjedhur me marrëveshje, në të cilin gjatësia gjeografike merret 0°. Ky meridian i quajtur ndryshe si meridiani zero kalon në Greenwich.
“Njësia” është madhësia e përcaktuar, në të cilën shprehen parametrat e matur.
“Nomenklatura” është një mënyrë e emërtimit dhe e ndarjes së fletëve të hartave, sipas disa kritereve të përcaktuara.
“Paralelet” janë vijëprerje të fituara nga ndërprerja e sferës ose elipsoidit me rrafshe pingule me boshtin e rrotullimit të sferës ose elipsoidit.
“Projeksion hartografik” është elementi bazë matematik për të gjitha llojet e hartave, nëpërmjet të cilit mundësohet paraqitja në rrafsh e sipërfaqes së lakuar, të elipsoidit tokësor.
“Projeksioni zonal tërthor i Mercator-it (TMzn)” është një projeksion cilindrik konform tërthor, në të cilin sipërfaqja e modelit të tokës (sferë ose elipsoid) projektohet në një sipërfaqe të cilindrit, i cili mund të jetë tangent me elipsoidin përgjatë meridianit qendror ose ndërprerës në dy meridianët kufizues të zonës që projektohet.
“Projeksioni Konik Konform i Lambertit (LCC)” është një projeksion konik konform polar, në të cilin sipërfaqja e modelit të tokës (sferë ose elipsoid) projektohet në një sipërfaqe të konit, i cili mund të jetë tangent me elipsoidin përgjatë një paraleli ose ndërprerës në dy paralele.
“Qeliza e rrjetit” quhet ndryshe një fletë harte, me përmasa të caktuara sipas shkallës.
“Rrjeti gjeografik” është një strukturë e ndërtuar nga meridianët dhe paralelet, që mundëson nxjerrjen e koordinatave gjeografike të pikave mbi sferë ose elipsoid.
“Sistemi rrjetit gjeografik” përbëhet nga tre komponentë: rrjeti, akset dhe njësitë.
“Sisteme kartezian i koordinatave” është një sistem koordinatativ në plan, i cili jep pozicionin e pikave në lidhje me 2 ose 3 akse reciprokisht pingule.
“Zonë” quhet hapësira e formuar nga kufizimi i dy meridianëve.
3.2 RRJETET GJEOGRAFIKE
Rrjeti gjeografik është një sistem referencë i pozicionimit të objekteve gjeohapësinore në sipërfaqen e tokës. Ai konsiston në një rrjet të ndërtuar nga meridianët dhe paralelet. Meridianët janë vija imagjinare që kalojnë në pika me gjatësi gjeografike të njëjtë (longtitude) dhe zhvendosen sipas drejtimit Lindje-Perëndim (East-West), ndërsa paralelet janë vija imagjinare që kalojnë në pika me gjerësi gjeografike të njëjtë (latitude) dhe zhvendosen sipas drejtimit Veri-Jug (North-South).
Figura 3. Meridianët dhe paralelet
Megjithëse i aplikuar në sipërfaqen sferike të tokës, rrjeti gjeografik është i ngjashëm me një sistem koordinativ plan. Origjina e rrjetit gjeografik është aty ku meridiani fillestar (prime meridian) takon ekuatorin. Vlerat e gjatësisë gjeografike janë të ngjashme në vlerat e X në një sistem koordinativ plan, ndërsa vlerat e gjerësisë gjeografike janë të ngjashme me vlerat Y. Vlerat e gjerësisë janë pozitive nëse janë në veri të ekuatorit dhe negative nëse janë në jug të tij. Vlerat e gjatësisë janë pozitive nëse janë në lindje të meridianit fillestar dhe negative nëse janë në perëndim të tij. Gjerësia dhe gjatësia mund të maten nësistemin grador “gradë-minuta-sekonda” (DMS - degree-minute-second, 1° = 60’, 1’=60”) ose nësistemin dhjetor-grador (DD - decimal i degrees).
Si të gjitha sistemet koordinative edhe një sistem gjeografik koordinatash përbëhet nga 3 komponentë:
a) rrjeti;
b) akset (boshtet koordinative);
c) njësitë.
Rrjeti gjeografik konsiston në një strukturë të ndërtuar nga meridianët dhe paralelet dhe ndërtohet si në figurë:
Figura 4. Ndërtimi i rrjetit gjeografik
Ndërtimi niset nga aksi i rrotullimit të elipsoidit. Pikat e ndërprerjes së këtij aksi me sipërfaqen e tokës quhen pole. Të gjitha pikat e sipërfaqes së tokës që ndodhen të baraslarguara nga polet krijojnë të ashtuquajturat paralele. Një paralel i veçantë quhet ekuator. Ai krijohet nga të gjitha pikat, të cilat kanë distancë të barabartë nga të dyja polet. Lidhja më e shkurtër midis dy poleve përgjatë sipërfaqes së tokës quhet meridian.
Sa më sipër del që nëpër çdo pikë P të sipërfaqes së tokës kalon një meridian dhe një paralel që janë normal me njëri-tjetrin. Tërësia e meridianëve dhe e paraleleve krijon një rrjet drejtkëndor. Kështu që pozicioni i një pike P, në sipërfaqen e tokës, përcaktohet qartë nëpërmjet paralelit dhe meridianit që kalojnë nëpër të. Rrjeti gjeografik grador është një sistem koordinatash gjeografike. Meridiani fillestar i këtij rrjeti kalon nëpër Greenvich ndërsa si njësi matëse përdoret grada (º).
Gjerësia gjeografike φ e një pike P është këndi që matet në planin e meridianit midis planit të ekuatorit dhe normales me sipërfaqen në pikën P. Referuar ekuatorit dallohen gjerësitë veriore (këndet nga ekuatori deri në polin e veriut) dhe gjerësitë jugore (këndet nga ekuatori deri në Polin e Jugut) me vlera 0° deri 90°.
Gjerësia gjeografike jepet e ilustruar më poshtë:
Figura 5. Gjerësia gjeografike
Gjatësia gjeografike λ është këndi që matet në planin e ekuatorit midis rrafshit të meridianit që kalon në Greenwich (meridiani zero ose fillestar) dhe planit të meridianit që kalon në pikën P. Nisur nga meridiani fillestar dallohen gjatësitë lindore dhe perëndimore me vlera nga 0° deri 180°.
Gjatësia gjeografike jepet e ilustruar më poshtë:
Figura 6. Gjatësia gjeografike
Për sistemet e rrjeteve gjeografike definohen këto koncepte:
- Për të dalluar polet përdoren emërtimet Pol i Veriut dhe Pol i Jugut.
- Në mënyrë analoge me polet edhe gjysmat e elipsoidit të ndara nga ekuatori emërtohen Gjysmësfera Veriore dhe Gjysmësfera Jugore ose Hemisfera Veriore dhe Jugore.
- Këndi λ quhet gjatësi gjeografike (longitude) e pikës P.
- Këndi φ quhet gjerësi gjeografike (latitude) e pikës P.
- Kur jepen koordinatat e pikës P e para jepet φ dhe pastaj λ.
3.2.1 PROJEKSIONET
Projeksioni hartografik është elementi i bazës matematike për të gjitha llojet e hartave, nëpërmjet të cilit mundësohet paraqitja në rrafsh e sipërfaqes së lakuar të elipsoidit tokësor.
Projektimi i hartës është procesi i transformimit të sipërfaqes sferike të tokës në një sipërfaqe plane. Rezultat i këtij transformimi është ndërtimi sistematik i vijave në një sipërfaqe plane për të paraqitur rrjetin gjeografik. Përveç asaj që lejon përdorimin e hartave në letër ose në format digjital, projektimi i hartave u mundëson përdoruesve të tyre të punojnë në një sistem koordinativ dypërmasor, më shumë se në një sistem sferik apo trepërmasor, i cili është shumë më kompleks si për të kryer matje ashtu edhe për të kryer llogaritje. Por, transformimi nga sipërfaqja sferike në sipërfaqe plane gjithmonë përmban shformime dhe asnjë tip projeksioni i hartës nuk është i përsosur.
Me anë të sistemeve të koordinatave gjeografike pozicioni i pikave (objekteve) mbi elipsoid identifikohet me anë të koordinatave këndore. Për të njehsuar gjatësitë dhe sipërfaqet në hartat e shkallëve të mëdha, p.sh., në hartat topografike zyrtare, rrjeti i koordinatave gjeografike është pak i përshtatshëm. Por, meqë në rajone të caktuara hartat janë pothuajse pa deformime, në harta, në vend të rrjeteve gjeografike mund të ndërtohen rrjete karteziane dhe në to të maten gjatësitë dhe sipërfaqet. Për këto rrjete duhen përcaktuar:
a) një pikë referimi për njehsimin e koordinatave;
b) vlerat y dhe x të pikës së referimit;
c) njësitë për dhënien e koordinatave (p.sh., metër ose kilometër).
Figura 7. Sistemi kartezian
Sistemet karteziane në planin e hartës quhen sisteme koordinative të projektuara. Këto janë sisteme koordinative, të cilat ndërtohen në projeksion pas projektimit të sipërfaqes së elipsoidit.
Një sistem koordinatash i projektuar përbëhet nga dy komponentë:
- Një projeksion i cili sërish përcaktohet nga forma dhe pozicioni që zë trupi i projektimit kundrejt elipsoidit ose sferës. Projeksioni shërben për atë që sipërfaqja tredimensionale e elipsoidit të projektohet në një sipërfaqe dydimensionale. Projeksione të caktuara ka kuptim të përdoren në varësi të rajonit elipsoidal që do të paraqitet.
- Një sistem kartezian koordinatash, i cili vendoset në planin e hartës. Ky përcaktohet nëpërmjet pozicionit të origjinës dhe njësisë matëse.
Në Shqipëri sistemi i koordinatave në plan mundësohet nga dy projeksione hartografike, të cilat janë:
1. TM zonal (Projeksioni Tërthor Zonal i Merkatorit);
2. LCC (Projeksioni Konik Konform i Lambertit).
3.2.1.1 PROJEKSIONI TM-ZONAL
“Projeksioni Tërthor i Merkatorit (TMzn)” është një projeksion cilindrik konform tërthor, në të cilin sipërfaqja e modelit të tokës (sferë ose elipsoid) projektohet në një sipërfaqe të cilindrit, i cili mund të jetë tangent me elipsoidin përgjatë meridianit qendror ose ndërprerës në dy meridianët kufizues të zonës që projektohet.
Cilindri tërthor është vetëm një sipërfaqe imagjinare.
Figura 8. Projeksioni Tërthor i Merkatorit
Në rastin e një cilindri tangent, të gjitha elementet (tiparet) përgjatë vijës së tangentes (përgjatë meridianit qendror), hartografohen pa shformime. Kjo do të thotë se faktori i shkallës përgjatë meridianit qendror është i barabartë me një (k0=1 ).
Figura 9. Faktori shkallë i shformimit në një sipërfaqe tangenciale me sferën
Shformimet rriten me largimin nga pika (vija) e tangentes. Në fakt, faktori i shkallës rritet në mënyrë simetrike teksa lëvizim nga meridiani qendror. Kjo është arsyeja pse ky projektim është më i përshtatshëm për zonat që janë të gjata në drejtimin Veri-Jug.
Në rastin e një cilindri sekant, të gjitha elementet (tiparet) përgjatë dy kurbave do të hartografohen pa shformime. Shkalla është reale (s’ka shformime) vetëm përgjatë kurbave dhe jo përgjatë meridianit qendror. Si në rastin e cilindrit tangencial, shformimi rritet kur largohemi nga kurbat.
Figura 10. Faktori shkallë i shformimit në një sipërfaqe prerëse me sferën
Midis linjave të sekantes, ku sipërfaqja është brenda zonës, elementet (tiparet), paraqiten më të vogla se në realitet dhe faktori i shkallës është më i vogël se 1 (deri në 0.9996). Në hartë ku sipërfaqja është jashtë sekanteve, elementet (tiparet) paraqiten më të mëdha se në realitet dhe faktori i shkallës është më i madh se 1.
Duke qenë se vendi ynë ka një shtrirje të gjatë përgjatë drejtimit Veri-Jug, atëherë është zgjedhur që cilindri të jetë tangent përgjatë meridianit qendror (λ = 20°) në Projeksionin Zonal Tërthor të Merkatorit (TMzn), ku zn - është numri identifikues i zonës. Çdo zonë shtrihet nga ekuatori në drejtim të veriut deri në gjerësinë veriore 84°. Ky projeksion do të përdoret për harta në shkallë më të madhe se 1:500 000.
- Parametrat e projeksionit (TMzn) për Shqipërinë janë:
- Sistemi referencë: ETRS89 (elipsoidi GRS80)
- Meridiani fillestar: Grinuiç (Greenwich - Londër)
- Meridiani qendror: 20°
- Origjina e gjerësisë: 0°
- Shkalla e shformimit
të meridianit qendror (k0): 1
- Vlera false e Lindjes: 500.000 m
- Vlera false e Veriut: 0 m
- Formulat e konvertimit të koordinatave gjeografike (φ, λ) në koordinatat në projeksionin TMzn (N, E):
Simbolet dhe përkufizimet:
a - gjysmëboshti i madh i eliposidit;
b - gjysmëboshti i vogël i eliposidit;
f - shtypja në pole e elipsoidit;
k0 - faktori shkallë për meridianin qendror;
φ0 - origjina e gjerësisë gjeodezike të paralelit;
λ0 - meridiani qendror (CM);
E0 - vlera false e Lindjes;
N0 - vlera false e Veriut;
φ - paraleli i gjerësisë gjeodezike (veriore pozitive);
λ - meridian i gjatësisë gjeodezike (lindore pozitive);
E - koordinata e Lindjes në projeksion;
N - koordinata e Veriut në projeksion;
γ - konvergjenca e meridianit;
ω - korrigjimi i harkut meridional;
S - distanca meridionale;
S0 - distanca meridionale nga ekuatori deri te φ0, shumëzuar me faktorin shkallë të meridianit qendror;
∆N - diferenca në Veri (∆N=N2 - N1);
∆E - diferenca në Lindje (∆E=E2 - E1);
E’ - diferenca në Lindje (E’=E - E0);
e2 - jashtqendërsia e parë në katror (e2 = 2f - f2);
e’2 - jashtqëndërsia e dytë në katror (e’2 = e2/(1-e2));
n - shtypja e dytë polare në elipsoid (n = f/(2 - f));
R - rrezja e lakorësisë të vertikalit të parë;
r0 - rrezja mesatare gjeometrike e lakores së shkallëzuar në rrjet;
r - rrezja e korrigjimit të sferës;
t - tan φ;
tf - azimuti i rrjetit;
η2 - koeficient (η2 = e’2 cos2 ϕ);
- koeficient (η2 = e’2 cos2 ϕf).
Llogaritja e konstantes së harkut të meridianit sipas formulave të mëposhtme:
- Llogaritja direkte:
Të dhënat (Input): Koordinatat gjeodezike të pikës P(φ, λ)
Produkti (Output): Koordinatat e pikës P (N, E)
- Llogaritja e anasjellë:
Të dhënat (Input): Koordinatat e pikës P (N, E)
Produkti (Output): Koordinatat gjeodezike të pikës P(φ, λ)
3.2.1.2 PROJEKSIONI LCC
“Projeksioni Konik Konform i Lambertit (LCC)” është një projeksion konik konform, në të cilin meridianët gjeografikë paraqiten vija të drejta, të dala nga një pikë, duke formuar kënde, që u përgjigjen ndryshimeve të gjatësive gjeografike përkatëse, kurse paralelet paraqiten harqe rrathësh bashkëqendrorë me qendër në pikën ku dalin meridianët. Ky projeksion përdoret për harta në shkallën 1:500 000 dhe më të vogla.
Figura 11. Projeksioni Konik Konform i Lambertit
- Parametrat e projeksionit (LCC) janë:
Meridiani Fillestar Grinuiçi
00
Gjerësia gjeografike e origjinës fallco ( Φ)
520 00’ 00” N
Gjatësia gjeografike e origjinës ( λ0)
100 00’ 00” E
Gjerësia gjeografike e paralelitit të parë standard
650 00’ 00” N
Gjerësia gjeografike e paralelitit të dytë standard
350 00’ 00” N
Spostimi Lindor i origjinës fallco
4 000 000 metra
Spostimi Verior i origjinës fallco
2 800 000 metra
- Formulat e konvertimit të koordinatave gjeografike (φ, λ) në koordinatat në projeksionin TMzn (N, E):
Simbolet dhe përkufizimet:
a - gjysmëboshti i madh i eliposidit;
b - gjysmëboshti i vogël i eliposidit;
f - shtypja në pole të elipsoidit;
k0 - faktori shkallë për paralelin qendror;
φ0 - origjina e gjerësisë gjeodezike të paralelit;
e2 - jashtëqendërsia e parë në katror (e2 = 2f - f2);
φu - paraleli i sipërm;
φl - paraleli i poshtëm;
φb - gjerësia (false) e origjinës së rrjetit në rastin e 2 paraleleve;
λ0 - gjatësia e origjinës së rrjetit, meridiani referues qendror (RM, λ0);
E0 - vlera false e Lindjes;
N0 - vlera false e Veriut;
R - rrezja e projeksionit sipas gjerësisë φ;
K - rrezja projeksionit në ekuator;
Q - gjerësia izometrike;
φ - paraleli i gjerësisë gjeodezike (veriore pozitive);
λ - meridian i gjatësisë gjeodezike (lindore pozitive);
E - koordinata e Lindjes në projeksion;
N - koordinata e Veriut në projeksion;
γ - këndi i konvergjencës;
k - faktori shkallë i rrjetit në një pikë të përgjithshme.
Llogaritja e konstanteve të elipsoidit dhe sipërfaqes së projektuar jepet sipas barazimeve të mëposhtme:
Në mënyrë të ngjashme për Qa, Qb, dhe Wu pas zëvendësimit të gjerësisë marrim.
Shënim. Exp (x) = ku: ε=2.71828 18284 59045 23536 02875 (bazuar në lagoritmin natyror)
- Llogaritja direkte:
Të dhënat (Input): Koordinatat gjeodezike të pikës P(φ, λ)
Produkti (Output): Koordinatat e pikës P (N, E), këndi i konvergjencës (γ), faktori shkallë (k)
- Llogaritja e anasjelltë
Të dhënat (Input): Koordinatat e pikës P (N, E), këndi i konvergjencës (γ).
Produkti (Output): Koordinatat gjeodezike të pikës P (φ, λ).
Më poshtë përdorim një përafrim për φ (duke llogaritur sinφ më shumë se një herë):
3.2.1.3 INDEKSIMI I FLETËS SË HARTËS
Shqipëria ndodhet midis gjerësive gjeografike veriore 39°38’ dhe 42°39’ dhe midis gjatësive gjeografike lindore 19°16’ dhe 21°04’. Vendit tonë i përgjigjet një sipërfaqe prej 28 748 km2, gjatësia maksimale e të cilit nga Veriu në Jug është 340 km, ndërsa gjerësia maksimale nga Perëndimi në Lindje është 148 km.
Megjithëse sipërfaqja e Shqipërisë është relativisht e vogël, ajo paraqitet me një sërë fletësh të hartave. Fletët e hartave paraqesin në vetvete trapezë të kufizuar nga vijat e meridianëve dhe paraleleve. Kufizimet sipas paraleleve quhen breza, ndërsa kufizimet sipas meridianëve quhen zona. Treguesi konvencional i fletëve të hartave topografike quhet emërtesë ose nomenklaturë. Si bazë për të gjitha emërtesat e hartave të vendit tonë është pranuar fleta e hartës së shkallës 1:1 000 000 me përmasat 6° gjatësi dhe 4° gjerësi gjeografike, e formuar nga ndërprerja e meridianëve dhe paraleleve.
Brezat emërtohen me germa të mëdha të alfabetit latin, duke filluar nga ekuatori në drejtim të dy poleve. Zonat emërtohen me numra arabë (1-60) duke filluar nga meridiani që ndodhet në largësinë 180° nga Grinuiçi. Renditja e numrave bëhet nga Perëndimi në Lindje (figura 12)
Figura 12. Indeksimi i fletëve të hartës
Fletët e hartave të shkallës 1:1 000 000, në të cilat shtrihet territori i Shqipërisë i kanë emërtesat K-34 dhe J-34 (figura 9). Nomenklatura J-34 është vetëm për një pjesë të vogël të Jugut të Shqipërisë.
Figura 13. Ndarja e fletëve të hartave në shkallë 1:1 000 000
Më poshtë jepet në mënyrë të detajuar mënyra e emërtimit të fletëve të hartës sipas shkallëve:
- Kalimi nga SH: 1:1 000 000 në 1:100 000.
Elementet
Përshkrimi
Shkalla e përfituar
100 000
Shkalla bazë
1 000 000
Ndarja
Trapezi i fletës së shkallës 1:1 000 000 ndahet në 12x12=144 ndarje
Emërtimi
Emërtimi bëhet me numra nga 1-144 (p.sh., K-34-124)
Përmasat e fletës
∆φ = 20’, ∆λ = 30’
- Kalimi nga SH. 1:1 000 000 në 1:500 000.
Elementet
Përshkrimi
Shkalla e përfituar
500 000
Shkalla bazë
1 000 000
Ndarja
Trapezi i fletës së shkallës 1:1 000 000 ndahet në 2 x 2 = 4 ndarje
Emërtimi
Emërtimi bëhet me germa të mëdha të alfabetit A-B-C-D (p.sh., K-34-B)
Përmasat e fletës
∆φ = 40, ∆λ = 60
- Kalimi nga SH: 1:1 000 000 në 1:200 000.
Elementet
Përshkrimi
Shkalla e përfituar
200 000
Shkalla bazë
1 000 000
Ndarja
Trapezi i fletës së shkallës 1:1 000 000 ndahet në 6 x 6 = 36 ndarje
Emërtimi
Emërtimi bëhet me numrat romakë I- XXXVI (p.sh., K-34- XXI)
Përmasat e fletës
∆φ = 40’, ∆λ = 60’
Në figurën e mëposhtme tregohet ndarja e fletëve të hartave për shkallët:
a) SH: 1: 500 000 me bazë SH: 1: 1000 000;
b) SH: 1: 200 000 me bazë SH: 1: 1000 000.
Figura 14. Ndarja e fletëve të hartës për shkallët 1:500 000 dhe 1:200 000
- Kalimi nga SH: 1:1 000 000 në 1:100 000.
Elementet
Përshkrimi
Shkalla e përfituar
100 000
Shkalla bazë
1 000 000
Ndarja
Trapezi i fletës së shkallës 1:1 000 000 ndahet në 12 x 12 = 144 ndarje
Emërtimi
Emërtimi bëhet me numra nga 1-144 (p.sh., K-34-39)
Përmasat e fletës
∆φ = 20’, ∆λ = 30’
Në figurën e mëposhtme tregohet ndarja e fletëve të hartës për shkallën SH: 1: 100 000 duke marrë si bazë hartën me shkallë SH: 1:1000 000.
Figura 15. Ndarja e fletëve të hartës në shkallën 1:100 000
- Kalimi nga SH: 1:100 000 në 1:50 000.
Elementet
Përshkrimi
Shkalla e përfituar
50 000
Shkalla bazë
100 000
Ndarja
Trapezi i fletës së shkallës 1:100 000 ndahet në 2x2=4 ndarje
Emërtimi
Emërtimi bëhet me germa të mëdha të alfabetit A-B-C-D (p.sh., K-34-39-D)
Përmasat e fletës
∆φ = 10’, ∆λ = 15’
- Kalimi nga SH: 1:50 000 në 1:25 000.
Elementet
Përshkrimi
Shkalla e përfituar
25 000
Shkalla bazë
50 000
Ndarja
Trapezi i fletës së shkallës 1:50 000 ndahet në 2 x 2 = 4 ndarje
Emërtimi
Emërtimi bëhet me germa të vogla të alfabetit a-b-c-d (p.sh., K-34-39-A-d)
Përmasat e fletës
∆φ = 5’, ∆λ = 7’30”
- Kalimi nga SH: 1:25 000 në 1:10 000.
Elementet
Përshkrimi
Shkalla e përfituar
10 000
Shkalla bazë
25 000
Ndarja
Trapezi i fletës së shkallës 1:25 000 ndahet në 2 x 2 = 4 ndarje
Emërtimi
Emërtimi bëhet me numrat nga 1-4 (p.sh., K-34-40- A-a -3)
Përmasat e fletës
∆φ = 2’30”, ∆λ = 3’45”
Në figurën e mëposhtme tregohet ndarja e fletëve të hartave për shkallët:
a) SH: 1: 50 000 me bazë SH: 1: 100 000;
b) SH: 1: 25 000 me bazë SH: 1: 50 000;
c) SH: 1: 10 000 me bazë SH: 1: 25 000.
Figura 16. Ndarja e fletëve të hartës në shkallët 1:50 000, 1:25 000 dhe 1:10 000
- Kalimi nga SH: 1:100 000 në 1:5 000.
Elementet
Përshkrimi
Shkalla e përfituar
5 000
Shkalla bazë
100 000
Ndarja
Trapezi i fletës së shkallës 1:100 000 ndahet në 16 x 16 = 256 ndarje
Emërtimi
Emërtimi bëhet me numrat nga 1-256 (p.sh., K-34-76-2)
Përmasat e fletës
∆φ = 1’ 15”, ∆λ = 1’ 52.5”
Në figurën e mëposhtme, tregohet ndarja e fletëve të hartës për shkallën SH: 1: 5 000, duke marrë si bazë hartën me shkallë SH: 1:100 000.
Figura 17. Ndarja e fletëve të hartës në shkallën 1:5 000
- Kalimi nga SH: 1:5000 në 1:2 500.
Elementet
Përshkrimi
Shkalla e përfituar
2 500
Shkalla bazë
5 000
Ndarja
Trapezi i fletës së shkallës 1:5 000 ndahet në 2 x 2 = 4 ndarje
Emërtimi
Emërtimi bëhet me germa e vogël a, b, c , d (p.sh., K-34-76-3-b)
Përmasat e fletës
∆φ = 37.5”, ∆λ = 56.25”
Në figurën e mëposhtme tregohet ndarja e fletëve të hartës për shkallën SH: 1: 2 500, duke marrë si bazë hartën me shkallë SH: 1: 5 000.
Figura 18. Ndarja e fletëve të hartës në shkallën 1:2 500
Ndarjet dhe emërtesat e fletëve paraqiten në tabelën e mëposhtme:
Tabela 1. Tabela përmbledhëse e emërtesave të hartave
Përmasat
Shkalla
Gjerësia (φ)
Gjatësia (λ)
Përcaktimi
Emërtesa
1:1 000 000
40
60
Sipas hartës ndërkombëtare SHK 1:1 000 000
K-34
1: 500 000
20
30
1/4 e fletës së hartës SHK 1:1 000 000
K-34-A, B, C, D
1: 200 000
40’
60’
1/36 e fletës së hartës SHK 1:1 000 000
K-34-I, II, III, ...XXXVI
1: 100 000
20’
30’
1/144 e fletës së hartës SHK 1:1 000 000
K-34-1, 2, 3, …144
1: 50 000
10’
15’
1/4 e fletës së hartës SHK 1: 100 000
K-34-…40… A, B, C, D
1: 25 000
5’
7’ 30”
1/4 e fletës së hartës SHK 1: 50 000
K-34-40-B-a, b, c, d
1:10 000
2’ 30”
3’ 45”
1/4 e fletës së hartës SHK 1: 25 000
K-34-40- A-a -1, 2, 3, 4
1:5 000
1’ 15”
1’ 52.5”
1/256 e fletës së hartës SHK 1: 100 000
K-34-40-1, 2, …256
1:2 500
37.5”
56.25”
1/4 e fletës së hartës SHK 1: 5 000
K-34-40-(256)-a, b, c, d
3.2.2 SKEMA KONCEPTUALE UML - SISTEMET E RRJETEVE GJEOGRAFIKE- DIAGRAMI
Figura 19: Diagrami UML: Sistemet e rrjeteve gjeografike
3.2.3 KATALOGU I TIPOLOGJISË
3.2.3.1 PROJEKSIONI TM-ZN
-- Emri --
Projeksioni Tërthor Zonal i Merkatorit (TMzn).
-- Përkufizimi --
“Projeksioni Tërthor Zonal i Merkatorit (TMzn)” është një projeksion cilindrik konform tërthor, në të cilin sipërfaqja e modelit të tokës (sferë ose elipsoid) projektohet në një sipërfaqe të cilindrit, i cili mund të jetë tangent me elipsoidin përgjatë meridianit qendror ose ndërprerës në dy meridianet kufizuese të zonës që projektohet.
- Tipi i elementit -
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizim nga FeatureType ProjeksioniTMz te FeatureType RrjetetGjeografike
ATRIBUTE
Shkalla: VleraEShkallës
Shumëllojshmëria: [1..*]
-- Emri --
Vlera e shkallës së emërtesës
-- Përkufizimi --
Shkalla në të cilën paraqitet emërtesa e hartës.
Për harta në shkallë më të mëdha se 1: 500 000 përdoret Projeksioni Tërthor Zonal i Merkatorit (TMzn).
[I detyrueshëm: PO]
3.2.3.2 PROJEKSIONI LCC
-- Emri--
Projeksioni Konform Konik i Lambertit (LCC)
-- Përkufizimi --
“Projeksioni Konik Konform i Lambertit (LCC)” është një projeksion konik konform, në të cilin meridianet gjeografike paraqiten vija të drejta, të dala nga një pikë, duke formuar kënde, që u përgjigjen ndryshimeve të gjatësive gjeografike përkatëse, kurse paralelet paraqiten harqe rrathësh bashkëqendrorë me qendër në pikën ku dalin meridianët.
- Tipi i elementit -
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Gjeneralizim nga FeatureType ProjeksioniLCC te FeatureType RrjetetGjeografike
ATRIBUTE
Shkalla: VleraEShkallës
Shumëllojshmëria: [1..*]
-- Emri -
Vlera e shkallës së emërtesës
-- Përkufizimi --
Shkalla në të cilën paraqitet emërtesa e hartës.
Për harta me shkallë më të vogla se 1: 500 000 përdoret Projeksioni Konik Konform i Lambertit (LCC)
[I detyrueshëm: PO]
3.2.3.3 PËRMASAT E FLETËS
-- Emri --
Përmasat e fletës
-- Përkufizimi --
Përmasat e fletëve të hartave paraqesin në vetvete trapezë të kufizuar nga vijat e meridianëve dhe paraleleve.
- Tipi i elementit -
DataType
ATRIBUTE
GjerësiGjeografike: DDMMSS.SS
Shumëllojshmëria: [1..*]
-- Emri --
Gjerësi gjeografike
-- Përkufizimi --
Dimensioni vertikal i trapezit të hartës. Diferenca e koordinatave të gjerësive gjeografike ndërmjet kulmet e trapezit.
-- Përshkrimi --
Shënim. Gjerësi gjeografike është këndi që formohet midis rrafshit të ekuatorit dhe rrezes, që kalon nëpër pikën së cilës i kërkohet pozicioni. Gjerësia matet nga rrafshi i ekuatorit në drejtimin e dy poleve dhe merr vlera nga 0° deri në 90°, prandaj gjerësia mund të jetë, veriore ose jugore, sipas pozicionit që ka pika në lidhje me rrafshin e ekuatorit.
[I detyrueshëm: PO]
GjatësiGjeografike: DDMMSS.SS
Shumëllojshmëria: [1..*]
-- Emri --
Gjatësi gjeografike
-- Përkufizimi --
Dimensioni horizontal i trapezit të hartës. Diferenca e koordinatave të gjatësisë gjeografike në kulmet e trapezit.
-- Përshkrimi --
Shënim
Gjatësia gjeografike është këndi që matet në rrafshin e ekuatorit dhe që formohet midis rrafshit të meridianit të Grinuiçit dhe rrafshit meridional nëpër pikën e kërkuar.
Gjatësitë e pikave mund të jenë lindore ose perëndimore, sipas pozicionit që kanë ato në lidhje me meridianin e Grinuiçit. Gjatësitë e pikave maten në Lindje dhe në Perëndim të këtij meridiani, prandaj këndi ka vlera 0° deri në 180°.
[I detyrueshëm: PO]
3.2.3.4 RRJETET GJEOGRAFIKE
-- Emri --
Rrjetet gjeografike
-- Përkufizimi --
Rrjeti gjeografik është një sistem referencë i vendndodhjes, për objektet gjeohapësinore, në sipërfaqen e tokës.
-- Përshkrimi --
Shënim. Rrjetet janë mjete të fuqishme për harmonizimin dhe reduktimin e kompleksitetit të grupeve të të dhënave. Rrjetet gjeografike janë, gjithashtu, mjete efektive komunikimi në raportimin e ndryshimeve gjeohapësinore të tipologjive.
- Tipi i elementit -
FeatureType
LIDHJE STRUKTURORE TË JASHTME
Generalization from FeatureType ProjeksioniTMz te FeatureType RrjetetGjeografike
Gjeneralizimi nga FeatureType ProjeksioniLCC te FeatureType RrjetetGjeografike
ATRIBUTE
PërmasatEFletësn: PërmasatEFletës
Shumëllojshmëria: [1..*]
-- Emri --
Përmasat e fletës
-- Përkufizimi --
Përmasat e fletëve të hartave paraqesin në vetvete trapezë të kufizuar nga vijat e meridianëve dhe paraleleve. Për secilën emërtesë vendosen përmasat e fletës Δ φ dhe Δ λ.
[I detyrueshëm: PO]
Emërtesa: TabelaENdarjesSëEmërtesave
Shumëllojshmëria: [1]
-- Emri --
Emërtesa
-- Përkufizimi --
Treguesi konvencional i fletëve të hartave topografike. Vlera e emërtesës merret nga tabela përmbledhëse e emërtesave të hartave (tabela 1).
[I detyrueshëm: PO]
InspireId: Identifikues
Shumëllojshmëria: [1]
-- Emri --
Inspire ID
-- Përkufizimi --
Identifikues i jashtëm i objektit gjeohapësionor.
-- Përshkrimi --
Shënim. Një identifikues i jashtëm është një identifikues unik i objektit i vendosur nga autoriteti përgjegjës, i cili mund të përdoret nga aplikimet e jashtme për t’iu referuar objektit gjeohapësinor. Identifikuesi është një identifikues lokal i objektit gjeohapësinor.
[I detyrueshëm: PO]
FillimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data në të cilën ky version i objektit gjeohapësinor është krijuar ose ndryshuar në të dhënat gjeohapësinore.
[I detyrueshëm: PO]
PërfundimiICiklitJetësor: Datë-Orë
Shumëllojshmëria: [0..1]
-- Emri --
Përfundimi i ciklit jetësor
-- Përkufizimi --
Data në të cilën ky version i objektit gjeohapësinor është përfunduar.
[I detyrueshëm: JO]
3.3 METADATA
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.4 KODI EPSG PËR KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare (KRGJSH), miratuar me vendimin nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si metadatë”, ndryshuar me vendimet nr. 322, datë 27.4.2016 dhe nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është EPSG - 6870.
3.5 CILËSIA E TË DHËNAVE
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur, për të vlerësuar dhe dokumentuar cilësinë për grupet e të dhënave gjeohapësinore të temës “Sistemet e rrjeteve gjeografike”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku pronat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit;
- vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve të metadatave të grupeve të të dhënave gjeohapësinore.
Specifikuar kërkesat ose rekomandimet, në lidhje me rezultatet e cilësisë së të dhënave të zbatueshme për grupet e të dhënave gjeohapësinore që lidhen me temën “Sistemet e rrjeteve gjeografike”.
Tabela e mëposhtme, paraqet të gjitha elementet dhe nënelementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, datasetit ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën “Sfera e vlerësimit”.
Masat që do të përdoren për secilin nga nënelementet e listuara të cilësisë së të dhënave janë përcaktuar në nënseksionet e mëposhtme.
Tabela - Elementet e cilësisë së të dhënave të përdorura në temën “Sistemet e rrjeteve gjeografike”.
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
3.6.1
Kompletimi
Komisioni
Të dhëna të tepërta të pranishme në grupin e të dhënave, siç përshkruhet nga fushëveprimi
Koleksion të dhënash, Grupet e të dhënave, Llojet e objektit gjeohapësinor
3.6.2
Kompletimi
Përjashtimi
Të dhënat që mungojnë nga grupi i të dhënave, siç përshkruhet nga fushëveprimi
Koleksion të dhënash, grupet e të dhënave, llojet e objektit gjeohapësinor, objekti gjeohapësinor
3.5.1 KOMPLETIMI - KOMISIONI (COMPLETENESS - COMMISSION)
Rekomandim
Komisioni duhet të vlerësohet dhe dokumentohet, duke përdorur normën e artikujve të tepërt siç specifikohet në tabelën e mëposhtme:
Emri
Norma e artikujve të tepërt
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletimi
Cilësia e të dhënave të nënelementeve
Komisioni
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i artikujve të tepërt në grupin e të dhënave, në lidhje me numrin e artikujve që duhet të ishin të pranishëm
Përshkrimi
Nuk ka përshkrim specifik për versionin 2.9
Fusha e vlerësimit
Llojet e objekteve gjeohapësinore: të gjitha llojet e objekteve gjeohapësinore; Grupi i të dhënave: seria e grupit të të dhënave.
Fusha e raportimit
Llojet e objekteve gjeohapësinore: të gjitha llojet e objekteve gjeohapësinore; Grupi i të dhënave: seria e grupit të të dhënave.
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Të vërteta: përqindje: raport
Cilësia e të dhënave të strukturës së vlerave
Vlera e vetme, çantë, vendos, rend, tabelë, matricë ose mbulim
Burimi referencë
SSH EN ISO 19157:2013 Informacion gjeografik - Cilësia e të dhënave
Shembulli
0.0189 ; 98.11% ; 11:582
Masa identifikuese
3 (SSH EN ISO 19157:2013)
3.5.2 KOMPLETIMI - PËRJASHTIMI (COMPLETENESS - OMISSION)
Rekomandim
Përjashtimi mund të vlerësohet dhe dokumentohet duke përdorur normën e artikujve të munguar, siç specifikohet në tabelën e mëposhtme:
Emri
Vlera e moskonformitetit të domeinit
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletimi
Cilësia e të dhënave të nënelementeve
Përjashtimi
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizimi
Numërimi i artikujve që mungojnë në grupin e të dhënave, në lidhje me numrin e artikujve që duhet të jenë të pranishëm
Përshkrimi
Nuk ka përshkrim specifik për versionin 2.9
Fusha e vlerësimit
Llojet e objekteve gjeohapësinore: të gjitha llojet e objekteve gjeohapësinore; Grupi i të dhënave: seria e grupit të të dhënave
Fusha e raportimit
Llojet e objekteve gjeohapësinore: të gjitha llojet e objekteve gjeohapësinore; Grupi i të dhënave: seria e grupit të të dhënave
Parametri
-
Cilësia e të dhënave të llojeve të vlerave
Të vërteta: përqindje: raport
Cilësia e të dhënave të strukturës së vlerave
Vlera e vetme, çantë, vendos, rend, tabelë, matricë ose mbulim
Burimi referencë
ISO/DIS 19157 Informacion gjeografik - Cilësia e të dhënave
Shembulli
0.0189 ; 98.11% ; 11:582
Masa identifikuese
7 (SSH EN ISO 19157:2013)
4. ANEKSE
1.1 Aneksi A - Katalogu i tipologjisë
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Nëntema
Tipi
Sistemet e rrjeteve gjeografike
3.3.1.1
TransverseMercatorProjection
ProjeksioniTM-Zonal
SistemetERrjeteveGjeografike
FeatureType
3.3.1.2
LambertConformalConicProjection
ProjeksioniLCC
SistemetERrjeteveGjeografike
FeatureType
3.3.1.3
CellSize
PërmasatEFletës
SistemetERrjeteveGjeografike
DataType
3.3.1.4
GeographicalGrid
RrjetetGjeografike
SistemetERrjeteveGjeografike
FeatureType
Referenca
- Data Specification on Geographical Grid Systems - Technical Guidelines
- Map Projections for Europe - Institute for Environment and Sustainability, European commission-joinr Research centre
- Universal Grids and Grid Reference Systems - National Geospatial Intelligence Agency (NGA) Standardization document
- United States National Grid - Federal Geographic Data Committee
- Spatial referencing by coordinates - Open Geospatial Consortium
- Hartografia Dixhitale - Gafur Muka, Thoma KoriniLiteratura
- Practical Geodesy - Maarten Hooijberg (formulat e transformimit)
