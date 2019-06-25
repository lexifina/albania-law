# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI
TEMA: ORTOIMAZHERIA
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1 Si lexohet dokumenti.
2.2 Detyrimet ligjore
2.3 Fusha e veprimit
3. TEMA
3.1 ORTOIMAZHERIA
Koncepti i mozaikimit (Mosaicking)
3.1.1 DIAGRAMA UML
3.1.1.1 Struktura e Paketës - diagrama
3.1.1.2 Përmbajtja-Ortoimazheria diagrama
3.1.2 KATALOGU I TIPOLOGJISË
3.1.2.1 Elementet E Mozaikimit (mosaic Element)
3.1.2.2 Elementët Shtesë Të Mozaikimit (Aggregated mosaic element)
3.1.2.3 Elementi Përbërës I Mozaikimit (single mosaic element)
3.1.2.4 Mbulesa Ortoimazherike (orthoimage coverage)
3.1.2.5 Shtesa Ortoimazherike (orthoimage aggregation)
3.1.2.6 Vlera E Metodës Së Interpolimit (interpolation method value)
3.1.3 METADATA
3.1.4 SISTEMI REFERENCË, NJËSITË E MATJES DHE RRJETAT GJEOGRAFIKE.
3.1.4.1 SISTEMET STANDARDE TË REFERIMIT, NJËSITË E MATJEVE DHE RRJETET
A. Korniza Referuese Gjeodezike e Shqipërisë
B. Sistemet koordinative referencë sipas INSPIRE
C. Sistemet e referencës kohore
D. Njësitë e matjeve
3.1.5 CILËSIA E TË DHËNAVE.
3.1.5.1 KoMpletuar - Përjashtimi. (Completeness - Omission)
3.1.5.2 Saktësia e pozicionimit - Saktësia absolute apo e jashtme. (absolute or external accuracy)
4. ANEKSE
4.1 KATALOGU I TIPOLOGJIVE
4.2 TË DHËNAT E IMPORTUARA
4.3 KODI EPSG PËR KRGJSH
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet e specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI, duke u mbështetur në Direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG). Koha e publikimit të versionit nr. 1 është qershor 2017. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2017_ OI _v.1 ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit
Standard - Lloji i dokumentit
NSDI - Qëllimi i dokumentit
2017 - Viti i krijimit
OI- Tema për të cilën është krijuar standardi: Ortoimazheria
v.1 - Numri i versionit të standardit
2. HYRJE
2.1 SI LEXOHET DOKUMENTI.
Ky material është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: - në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: - në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të kuptohet më lehtë.
3. Tema: - në këtë pjesë jepen specifikimet teknike për secilën temë.
4. Anekse: - në këtë pjesë jepen informacione shtesë shpjeguese në ndihmë të lexuesve.
Përmbajtja e kapitullit 3 është strukturuar në 6 pjesë kryesore:
1. Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës.
2. Diagramat UML - Këtu jepet përmbajtja e Katalogut të Tipologjive përkthyer sipas gjuhës UML.
3. Katalogu i tipologjive - Këtu shpjegohet struktura e temës me të gjitha elementet e saj përbërës.
4. Metadata - këtu jepen specifikimet teknike për metadata-t e temës përkatëse.
5. Sistemi Koordinativ Reference - këtu përcaktohet sistemi koordinativ referencë që është miratuar sipas vendimit nr. 669, datë 7.8.2013, i ndryshuar me vendim nr. 322, datë 27.4.2016.
6. Cilësia e të dhënave - këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet mes tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në ’Katalogun e tipologjive’ (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te Katalogu i tipologjive. Për përdoruesit, Katalogu i tipologjive mund të jetë veçanërisht i dobishëm për të kontrolluar nëse ai përmban të dhënat e nevojshme për aplikacionet që ata përdorin.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit në tabelat e të dhënave në Katalogun e tipologjive.
Tabelat nr. 1, 2, me anë të një shablloni, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shablloni, shpjegon mënyrën e organizimit të informacionit në tabelën e kod listës.
Tabela 1
Emri - Emërtimi i tipologjisë
Përkufizimi
Përkufizimi sipas direktivës INSPIRE për tipologjinë.
Përshkrimi
Shënime dhe përshkrime të tjera për tipologjinë.
Tipi i tipologjisë
Tipi i elementit që mund të jetë i këtyre llojeve:
«featureType» - një element që mund të jetë real në terren apo një dukuri abstrakte
«dataType» - një element tabelor që shërben vetëm si tabelë atributesh për t’u lidhur me një element tjetër
«enumeration» «codeList» - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration nënkupton “renditje vlerash”, ndërsa codeList nënkupton “listë vlerash ose ndryshe kod listë”. Në dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”.
«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të dhënat e importuara”
Gjeometria
Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë ose poligon.
Abstrakt - kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri.
Shumëllojshmëria
Lloji dhe numri i vlerave që mund të marrë atributi:
0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë 1..* - mund të marrë minimumi 1 vlerë ose shumë vlera
0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme.
1 - duhet të marrë detyrimisht 1 vlerë
I detyrueshëm
Po - nëse atributi është i detyrueshëm të plotësohet
Jo - nëse atributi nuk është i detyrueshëm të plotësohet
Rol shoqërimi
Në tabelën e lidhjeve “Rol shoqërimet” tregohen marrëdhëniet hierarkike ndërmjet
elementeve të ndryshme në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.
Tabela 2
ATRIBUTET
-- Emri --
Emërtimi i atributit
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve
-- Përshkrimi --
Shënime dhe përshkrime të tjera për elementin
[I detyrueshëm: Detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh: PO]
Tabela 3
ATRIBUTET
Vlera e parë e listës së gatshme, p.sh: Ligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve
Vlera e dytë (etj.) e listës së gatshme, p.sh: Joligjor
-- Emri --
Emërtimi i vlerës
-- Përkufizimi --
Përkufizimi sipas direktivës INSPIRE të elementeve
2.1 KARAKTERISTIKAT E <<VOIDABLE>> DHE SHUMËLLOJSHMËRIA
Stereotipi <<voidable>> përdoret për të përshkruar ato përkatësi të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha përkatësitë e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera ’void’. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore që mirëmbahen nga ofruesi i të dhënave ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kod listën Vlera E Arsyes Së Pavlefshmërisë (Void ReasonValue).
Stereotipi <<voidable>> nuk jep informacion nëse karakteristika ekziston apo jo në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh. nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh. nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.1.2 NUMËRTIMET DHE KOD LISTAT (ENUMERATION AND CODELIST).
Kod listat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kod listë, ’vlera të tjera’ përcakton llojin e përmbajtjes së kod listës, e përcaktuar specifikisht si më poshtë:
’jo’ përfaqëson kod lista që përmbajnë vetëm vlera të specifikuara në këtë dokument.
’të kufizuara’ përfaqëson kod lista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave.
’të hapura’ përfaqëson kod lista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave.
’po’ përfaqëson kod lista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kod lista me vlera jo të përmbajtura në dokument ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që dhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.1.3 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në botën reale.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “Fillimi I Ciklit Jetësor”.
Shënim i rëndësishëm
Disa terma në Katalogun e tipologjive, si p.sh. FeatureType, DataType etj, nuk janë përkthyer qëllimisht në gjuhën shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti të përdoret një gjuhë unike sipas termave të Direktivës INSPIRE.
2.2 DETYRIMET LIGJORE
Në bazë të ligjit nr. 72/2012, neni 16, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore për krijimin e NSDI në Shqipëri janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave.
Standardet (Rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata - në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilët do të implementojnë këtë direktivë.
- Specifikimi i të dhënave - standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brëndshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.3 FUSHA E VEPRIMIT
Të gjitha autoritetet publike, kompani private apo individë që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor si më poshtë:
Figura 1
Planifikimi - Është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
Vlerësimi - Është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë çertifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
Procesimi - Është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplot. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
Shpërndarja - Është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
Zbulimi - Është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
Analiza - Është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet më të dhënat që janë evidentuar.
Përditësimi - Është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
Arkivimi - Është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohet. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
Shkatërrimi - Është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacione në fuqi.
3. TEMA
3.1 ORTOIMAZHERIA
TË PËRGJITHSHME:
Fotografitë dhe imazhet e marra nga platformat ajrore apo satelitore luajnë një rol të rëndësishëm në paraqitjen e të dhënave të sipërfaqes së tokës si dhe gjendjen e mjedisit. Por këto imazhe satelitore pësojnë shtrembërime gjeometrike, të cilat shkaktohen nga optika dhe animet e kamerës apo sensorit si dhe ndryshimi i lartësive të sipërfaqes së tokës. Për të eliminuar këto shtrembërime bëhet rektifikimi i këtyre fotografive apo imazheve nga plani i pjerrët në atë horizontal dhe kalimi nga projeksioni qendror në atë ortogonal dhe pikërisht këto fotografi të rektifikuara quhen ortofoto.
Ortoimazheria është përfshirë në Aneksin II të INSPIRE si e dhënë që luan një rol të rëndësishëm në paraqitjen e të dhënave të informacionit tematik dhe monitorimin e mjedisit. Mbulimi ortoimazherik është koncepti kryesor i modelit të të dhënave që mund ti referohet një ortofotoje të vetme ose një mozaiku ortofotosh. Për më tepër, një mbulim ortoimazherik mund të përbëhet nga disa mbulime të tjera ortoimazherike. Tiparet që përshkruajnë bazën gjeometrike (d.m.th. rrjetin e rregullt) janë huazuar nga Modelit Konceptual Gjenerik dhe SSH EN ISO 19123:2007. Mbulesat ortoimazherike të shtuara (agreguara) duhet jenë të radhitura; p.sh. ti përshtaten një rrjeti të përbashkët. Përveç kësaj, radhitja është gjithashtu e nevojshme kur të realizohet mbulesa ortoimazherike në nivel evropian. Për të arritur këtë lind nevoja e një rrjeti pan-evropian.
PËRKUFIZIME:
Për temën e ortoimazherisë do të përcaktojmë termat e mëposhtme:
1. Band: është vargu i gjatësisë së valëve të rrezatimit elektromagnetik që prodhon një përgjigje të vetme nga një pajisje ndjesore.
2. Mozaik: është imazhi i përbërë nga fotografi ose imazhe të bashkuara se bashku (një mozaik mund të përbëhet nga imazhe të marra në data të ndryshme dhe nga sensor të ndryshëm)
3. Shtesa ortoimazherike: është formimi i një mbulimi ortoimazherik të ri nga kombinimi i disa nëngrupeve të mbulimeve ortoimazherike homogjene.
4. Raster: është një model drejtkëndor ku gjeometria hapësinore është e organizuar në formën e një rrjeti drejtkëndor, “të dhënat e rasterit” përdoren në fushën e informacionit gjeografik duke identifikuar të gjithë klasën e të dhënave.
5. Vija mozaikimi: janë vija që përdoren gjatë procesit të mozaikimit për të përcaktuar kufijtë e zonave të imazheve që hyjnë në proces. Këto vija zakonisht përshkojnë zonat ku dallimet radiometrike janë minimale ose ndjekin kufij natyror për të minimizuar dallimin e kufijve midis imazheve.
6. “Tiling” ose prerja me kuadrate: është procesi i prerjes së një imazhi në imazhe më të vogla në formë kuadratike. Prerja me kuadrate është ndarje matematikore e një imazhi origjinal.
Një grup kuadratesh mund të krijohet nga një imazh i vetëm ose nga një mozaik imazhesh. Skema më e zakonshme e prerjes me kuadrate që përdoret në lartësi për këtë qëllim është një rrjet i thjeshtë drejtkëndor ku kuadratet përputhen nga skajet pa mbivendosje të imazheve apo hapësirave. Megjithatë, ndonjëherë kërkohet që kuadratet individuale të mbivendosen me ato ngjitur për të garantuar një vazhdimësi të caktuar gjeohapësinore gjatë trajtimit të tyre. Skema e prerjes me kuadrate mund të ketë edhe një gjeometri më pak të rregullt me një densitet të ndryshueshëm të kuadrateve. Kjo strukturë të dhënash bazuar në skedar është artificiale dhe nuk ka kuptim të vërtetë logjik në vetvete edhe pse zakonisht bazohet në elementet e rrjetit të rregullt. Prandaj, kjo adresohet te pjesa e kodimit të specifikimit teknik të të dhënave.
7. Mbulimi: është një lloj tipari që përshkruan karakteristikat e fenomeneve të botës reale që ndryshojnë në hapësirë.
Ndryshe nga llojet e tjera të tipologjive, atributet e saj jo-gjeohapësinore shoqërohen ngushtësisht me atributet gjeohapësinore (d.m.th. gjeometrinë e tij). Ai vepron si një funksion për t’i kthyer vlerat e atributeve nga rangut të tij për çdo pozicion direkt brenda domenit të përkohshëm. Vlerat e atributeve të një rrjeti mbulimi të ortoimazheve janë organizuar duke përdorur gjeometrinë e një rrjeti të rregullt katërkëndëshash në dy dimensione. Një rrjet i rregullt tillë është i përbërë prej dy grupesh me vija paralele të ndara në mënyrë të barabartë që ndërpriten në kënde të drejta. Pikat e ndërprerjes quhen pika të rrjetit të rregullt ose pika model. Ato mbartin vlera të rangut të mbulimit, edhe nëse sasia fizike matet brenda një hapësire model që rrethojnë pikën e rrjetit. Zonat e kufizuara nga vijat e rrjetit të rregullt quhen qeliza të rrjetit dhe mbështesin vlerësimin e mbulimit përmes interpolimit. Ato nuk janë domosdoshmërisht katrore, por drejtkëndore. Mbani parasysh se qelizat e rrjetit të rregullt dhe pikat model janë dy nocione të veçanta. Një sistem rrjeti i rregullt koordinativ përkufizohet me anë të origjinës dhe boshteve të rrjetit. Koordinatat e rrjetit maten përgjatë boshteve nga origjina.
8. Rrjeti i mbulimit i korrigjuar (rektifikuar) - mbulimi, domeini i të cilit përbëhet nga një rrjet i korrigjuar,një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë. (shih figurën 2, djathtas, majtas)
Figura 2- Shembuj të një rrjeti të korrigjuar (majtas) dhe shembuj të një rrjeti referencë (djathtas)
9. Rrjetit i Mbulimit Referencë: Mbulimi, domenit i të cilit përbëhet nga një rrjet i referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 2, djathtas).
PARAQITJA E MBULIMIT TË ORTOIMAZHIT
Ortoimazheria e cila është një lloj e dhëne raster, është një formë e thjeshtë e informacionit gjeografik. Ajo konsiston në një grup vlerash që masin energjinë e rrezatimit, të organizuara në një rrjet të rregullt pikash së bashku me metadat përkatëse dhe të gjeoreferuara.
Vlerat e atributeve të një ortofotoje janë përshtatur duke përdorur gjeometrinë e një rrjeti kuadratik të rregullt në dy dimensione. Një rrjet i tillë është një rrjet i përbërë nga dy grupe me vija paralele që ndërpriten në kënde të drejta. Pikat e ndërprerjeve quhen pikat e rrjetit ose pika model. Ato mbartin vlerat e rangut të mbulimit, edhe nëse sasia fizike është matur aktualisht brenda një hapsire model (p.sh. pikseli i imazhit) që i rrethon ato. Zonat e kufizuara nga vijat e rrjetit quhen qeliza të rrjetit dhe mbështesin vlerësimin e mbulimit me anë të interpolimit. Këto qeliza nuk janë domosdoshmërisht katrore, por drejtkëndëshe. Vini re se qelizat e rrjetit dhe hapësirat model janë dy nocione të ndryshme. Hapsira model formojnë një rrjet të zhvendosur nga një prej qelizave të rrjetit, në mënyrë që cdo hapësirë model të ketë një pikë përkatëse në qendër të saj. Një sistem koordinativ i rrjetit përcaktohet me anë të origjinës dhe boshteve të rrjetit. Koordinatat e rrjetit maten përgjatë boshtit larg në distancë nga origjina.
Figura 4 - Shembull i rrjetit kuadratik të rektifikuar
Për më tepër, rrjeti i mbulimit të një ortoimazherie gjeo-rektifikohet sipas standradit SSH EN ISO 19123:2007. Ai lidhet me Tokën nëpërmjet një lidhje të afërt (afine), që krijon një transformim të thjeshtë mes rrjetit të rregullt të koordinatave dhe koordinatave në sistemin e shoqëruar të referimit bazuar në Tokë. Parametrat e transformimit përcaktohen nga vendndodhja e origjinës së rrjetit të rregullt, orientimi i boshteve dhe hapësirës së rrjetit në secilin drejtim brenda sistemit të jashtëm të referimit të koordinatave.
KONCEPTI I MOZAIKIMIT (MOSAICKING)
Në këtë specifikim, mozaikimi përcaktohet si procesi i prodhimit që lejon krijimin e një ortofotoje nga disa imazhe origjinale të rektifikuara. Mozaikimi zakonisht përfshin përpunimin e plotë radiometrik për të dhënë një ortofoto homogjene pa vija mozaikimi.
Figura 5-Mozaikimi i ortofotos me vija mozaikimi
Shtrirja kohore e një mozaiku nuk mund të jetë më e saktë se një interval kohor i një imazhi që është fituar në data dhe kohë të ndryshme. Skema e aplikimit të ortoimazhit ofron një qasje për të treguar në hapsirë kohën e përvetësimit ndërmjet lidhjes së pikselave të ortofotos dhe atributeve të përkohshme të burimit të imazhit. Pra ajo bazohet në përdorimin e vijave të mozaikimit që krijohen për të kryer procesin e mozaikimit.
KONCEPTI I PRERJES ME KUADRATE (TILING)
Motivimet e ndryshme mund t’i bindin prodhuesit e të dhënave t’i ndajnë të dhënat e ortoimazherisë në pjesë më të vogla. Zakonisht ky proces njihet si “prerje me kuadrate ose tiling”. Megjithatë, ky term mund të përfshijë kuptime të ndryshme në varësi të përshkrimit. Duhen dalluar tre nivele kryesore:
Së pari, prerja me kuadrate mund të implementohet nga brenda në formate skedarësh (p.sh. formati tiff kuadrator). Duke organizuar sërish përmbajtjen e lartësisë në kuadrate thuajse katrore në vend të shiritave horizontalisht të gjerë, kjo metodë përmirëson performancën për aksesimin dhe përpunimin e imazheve me rezolucion të lartë. Meqenëse kjo metodë reflekton strukturën e ruajtjes së të dhënave, nuk shfaqet në skemën e aplikimit që kushtëzohet nga niveli konceptual.
Së dyti, ortofotot me rezolucion të lartë që mbulojnë territore të gjera përfaqësojnë volume të mëdha të dhënash, që shpesh nuk mund të ruhen në mënyrë të arsyeshme në një skedar të vetëm imazhi. Zakonisht prodhuesit e të dhënave i ndajnë ato në skedarë të veçantë individualë për të lehtësuar ruajtjen e tyre, shpërndarjen dhe përdorimin. Skema më e zakonshme e prerjes me kuadrate që përdoret në ortoimazheri për këtë qëllim është një rrjet i thjeshtë drejtkëndor ku kuadratet përputhen nga skajet pa mbivendosje të imazheve apo hapësirave (Figura 6 a). Megjithatë, ndonjëherë kërkohet që kuadratet individuale të mbivendosen me ato ngjitur për të garantuar një vazhdimësi të caktuar gjeohapësinore gjatë trajtimit të tyre (Figura 6 b). Skema e prerjes me kuadrate mund të ketë edhe një gjeometri më pak të rregullt me një densitet të ndryshueshëm të kuadrateve (Figura 6 c).
a) Rrjet i thjeshtë me kuadrate
b) Prerje me kuadrate
c) Prerje me kuadrate
që përputhen në anët e tyre
të mbivendosur
me densitet të ndryshëm
Figura 6 - Konfigurimet e ndryshme të skemës së prerjes me kuadrate
Së treti, Ortofotot e mëdha mund të ndahen edhe në nëngrupe që kanë kuptim edhe në vetvete, sepse përshkruajnë struktura logjike (p.sh. fletët e hartave, njësisë administrative si qarqet ose rrethet etj.). Ndryshe nga rasti i mëparshëm, ky lloj i prerjes me kuadrate duke u bazuar në skedar është plotësisht brenda shtrirjes së modelit konceptual.
STRUKTURA E TË DHËNAVE (DATA STRUCTURE)
Përmes konceptit të mbulimit jepet niveli i parë i strukturës së të dhënave. Për më tepër skema e aplikimit ortoimazherisë ofron një nivel të dytë që përbëhet nga grupe mbulimesh në një strukturë tjetër logjike.Me fjalë të tjera, nëngrupet nga ortofoto homogjene mund të kombinohen që të ndërtojnë një mbulim ortofotoje. Shtimi i mbulimit nuk i mban direkt vlerat e veta të qelizave të pikselave. Kjo i referohet mbulimeve të dhëna, duke shmangur dublikimin e të dhënave.Rangu i caktuar i mbulimit llogaritet në lëvizje nga një shërbim ose aplikacion kur kërkohet nga përdoruesit.
Për zbatueshmëri, mbulimet e dhëna dhe të shtuara të ortofotove do të jenë pjesë e të njëjtit dataset të ortoimazherisë.
Figura 7 - Parimi i shtimit të ortofotos: mbivendosja e mbulesave të ortofotove A B dhe C përbëjnë mbulimin e ortoimazhit të shtuar D, pjesa e kufizuar me pika të ndërprera.
Ky mekanizëm është plotësisht i përsëritur në mënyrë që mbulimi i ortofotove mund të jetë një përbërje e mbulimeve tashmë të shtuara të ortofotove.
Vëmë re këtu se edhe pse konceptet e tyre janë të përafërta, shtimi i ortofotos dhe mozaikimi i saj ndyshojnë: i pari nuk është një proces i gjerë prodhimi, por një pamje dinamike për strukturën e grupeve të të dhënave.
3.1.1 DIAGRAMA UML
3.1.1.1 STRUKTURA E PAKETËS - DIAGRAMA
Figurë 1: Struktura e Paketës dhe lidhjet e jashtme
3.1.1.2 PËRMBAJTJA-ORTOIMAZHERIA DIAGRAMA
Figurë 2: PËRMBAJTJA-ORTOIMAZHERIA
3.1.2 KATALOGU I TIPOLOGJISË
3.1.2.1 ELEMENTET E MOZAIKIMIT (MOSAIC ELEMENT)
-- Emri --
Elementet e Mozaikimit
-- Përkufizimi --
Lloji abstrakt identifikon zonën dhe kohën e një ose disa imazheve të përdorura për të gjeneruar një mbulim ortoimazherik.
-- Përshkrimi --
Qëllimi kryesor i këtij lloji funksioni është sigurimi i një mekanizmi për të përshkruar shpërndarjen hapësinore të kohës së krijimit të një mozaikimi ortoimazherik. Koha e përvetësimit mund të shërbejë për çdo imazh të dhënë individual ose sete imazhesh të grupuara në bazë të kritereve të përkohshme.
Tipi i elementit - FeatureType
LIDHJET STRUKTURORE TË BRENDSHME
Gjeneralizim nga «featureType» ElementiPërbërësIMozaikimit te «featureType» ElementetEMozaikimit
[ Drejtimi është ’Burim -> Destinacion’. ]
Gjeneralizim nga «featureType» ElementetShtesëTëMozaikimit te «featureType» ElementetEMozaikimit
[Drejtimi është ’Burim -> Destinacion’. ]
ATRIBUTET
Gjeometria : GM_MultiSipërfaqe
Shumëllojshmëria: [1]
-- Emri --
Gjeometria
-- Përkufizimi --
Përfaqësimi gjeometrik në hapësirë perfshin datën dhe kohën e kalimit të disa të dhënave imazherike që kontribuojnë në mozaikimin përfundimtar.
-- Përshkimi --
SHËNIM Kufijtë e gjeometrisë janë zakonisht të bazuara në ndarje të përdorura për procesin e mozaikimit.
[I detyrueshëm: PO]
InspiredId : Identifikues
Shumëllojshmëria: [0..1]
-- Emri --
Inspire ID
-- Përkufizimi --
ATRIBUTET
Identifikues i jashtëm i objektit gjeohapësionor.
-- Pershkrimi --
SHËNIM 1 Një identifikues i jashtëm i objektit është një identifikues unik objekti i publikuar nga organi kompetent, i cili mund të përdoret nga aplikacionet e jashtme si referencë e objektit gjeohapësinor. Identifikuesi është një identifikues i objektit gjeohapësinor, jo një identifikues i fenomenit të botës reale.
SHËNIM 2 Kjo karakteristike duhet të përdoret për të referuar në mënyrë indirekte shembuj të elementeve të mozaikimit nga shembujt unike të ortoimazherisë.
[I detyrueshëm: PO]
KohaENgjarjes : TM_Periudha
Shumëllojshmëria: [1]
-- Emri --
Koha e ngjarjes
-- Përkufizimi --
Përshkrimi për kohën e marrjes së imazheve.
-- Përshkrimi --
SHËNIM 1: Kjo kohëzgjatje i referohet intervalit të kohës në të cilën imazhi përftohet nga sensori.
SHËNIM 2: Kur përftimi i imazhit konsiderohet si i menjëhershëm, pavarësisht nga koha e ekspozimit, data dhe koha e fundit mund të jenë identik me datën dhe kohën e fillimit.
SHEMBULL 1: fillimi: 2011-10-30 mbarimi: 2011/10/30
SHEMBULL 2: fillimi: 2011-06-07T14: 31: 02Z mbarimi: 2011-06-07T16: 10: 54Z.
[I detyrueshëm: JO]
LIDHJE
Lidhje (drejtimi: Burim -> Destinacion)
-- Emri --
Elementet e mozaikimit
-- Përkufizimi --
Përfaqësimi hapësinor i kohës së krijimit të një mbulimi të orto imazhit me mozaik
-- Përshkrimi --
Kjo lidhje do të përdoret vetëm kur mbulimi ortoimazh është një mozaik..
Burimi: (Class) MbulesaOrtoimazherike «featureType»
Objektivi: «voidable» Elementi i Mozaikimit (Class) Elementet e Mozaikimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
LIDHJE
Përfaqësimi hapësinor i kohës së krijimit të një mbulimi të orto imazhit me mozaik..
-- Përshkrimi --
SHËNIM Kjo lidhje do të përdoret vetëm kur mbulimi ortoimazh është një mozaik.
3.1.2.2 ELEMENTET SHTESË TË MOZAIKIMIT (AGGREGATED MOSAIC ELEMENT)
-- Emri --
Elementet shtesë të mozaikimit
-- Përkufizimi --
Elementet e mozaikimit lidhen me disa imazhe të dhëna që ndajnë të njëjtën kohë në një nivel të caktuar të përkufizimit (psh ditë, muaj).
-- Përshkrimi --
SHËNIM Gjeometria e një elementi të agreguar në mozaik korrespondon me bashkimin e zonave, nga disa imazhe të dhëna.
Tipi i elementit - FeatureType
LIDHJE STRUKTURORE TË JASHTME
Generalizim nga «featureType» ElementetShtesëTëMozaikimit te «featureType» ElementetEMozaikimit
[Drejtimi është is ’Burim -> Destinacion’
3.1.2.3 ELEMENTI PËRBËRËS I MOZAIKIMIT (SINGLE MOSAIC ELEMENT)
-- Emri --
Elementi përbërës i mozaikimit
-- Përkufizimi --
Elementet e mozaikimit në lidhje me një imazh të vetëm.
-- Përshkrimi --
SHËNIM Gjeometria e një elementi të vetëm mozaiku korrespondon saktësisht në zonën e kontribuar.
Tipi i elementit - FeatureType
LIDHJE STRUKTURORE TË JASHTME
Generalizim nga «featureType» ElementiPërbërësIMozaikimit te «featureType» ElementetEMozaikimit
[ Drejtimi është is ’Burim -> Destinacion’. ]
ATRIBUTET
BurimiReferencëIImazhit : Text (CharacterString)
Shumëllojshmëria: [0..1]
-- Emri --
Burimi referencë i imazhit
-- Përkufizimi --
Referenca të imazhit të dhënë.
-- Përshkrimi --
SHËNIM 1: Nuk ka asnjë kufizim për natyrën e imazhit. Për shembull mund të jetë i papërpunuar, para-përpunuar apo ortorektifikuar.
SHËNIM 2: Modelimi dhe shpërndarja e imazheve të dhëna qëndrojnë jashtë fushëveprimit të specifikimeve të pranishme.
SHËNIM 3: Identifikuesit e imazheve të të dhëna duhet të jenë URI . SHEMBULL: http://land.data.gov.uk/id/imagery/2011-5864726.
[I detyrueshëm: PO]
3.1.2.4. MBULESA ORTOIMAZHERIKE (ORTHOIMAGE COVERAGE)
-- Emri --
Mbulesa Ortoimazherike
-- Përkufizimi --
Imazhi Raster i sipërfaqes së Tokës që është korrigjuar gjeometrikisht (”ortorektifikuar”) për të hequr shtrembërimet e shkaktuara nga ndryshimet në lartësi, animet e sensoreve dhe fakultativisht nga sesorët optike.
-- Përshkrimi --
SHËNIM 1 Një mbulim ortoimazherik është një mbulim i vazhdueshëm i bazuar në një rrjet katërkëndësh që korrigjohet. Është i pajisur me një metodë interpolimi për të vlerësuar të dhënat e vlerës në çdo pozicion të drejtpërdrejtë brenda në domenin e saj.
SHËNIM 2 Një mbulimi ortoimazherik mund të rrjedh nga një imazh i vetëm i dhënë ose nga disa imazhe të ndryshme të dhëna të cilat janë mozaikuar dhe bashkuar së bashku.
SHËNIM 3 Një mbulimi ortoimazherik mund të jetë një grumbull i nëngrupeve nxjerrë nga mbulime të tjera ortoimazherike. Për shmangien e dyfishimit të të dhënave, ky lloj i ortofotos është ndërtuar në mënyrë dinamike në sajë të referencave të mbulesave që kontribuojnë në ortoimazhet.
Tipi i elementit - Feature Type
CONSTRAINTS
OCL. DimensioniIDomainitËshtë2
/* Dimensioni i rrjetit të përdorur duhet të jetë gjithmonë 2 */
OCL. OrigjinaDimensionale2
/*Origjina e rrjetit do të përshkruhet në dy dimensione*/
OCL. CRSeDomainit
/* Sistemi Koordinati ReferenCë i përdorur si bazë mbështetëse për rrjetin duhet të sigurohet.*/
OCL. ShtrirjaEDomainPermbanKordinataGjeografike
/*Atributi i ShtrirjaEDomainit duhet të popullohet me të pakten një nëntip të EX_ShtrirjaGjeografike*/
OCL. VarguIVleraveTeTipitInteger
/* Vlerat e gamës duhet e pëshkruhen me tipin e vlerës Integer*/
OCL. BashkimiIVektoreveIdentikeNeOrtoimazheri
/*Të gjithë instancat e MbulesaOrtoimazherike në të cilën referohet një ShtesëMbulimiOrtoimazherik, duhet të ndajë të njëjtin orientim të akseve të rrjetit dhe të njëjtën ndarje në secilin drejtim*/
OCL. KohaEPërshtatjes
/* Koha e pështatjes së një mbulese ortoimazherike duhet të sigurohet nga Koha e Ngjarjes apo nga Lidhja e Elementit të Mozaikimit.*/
LIDHJE STRUKTURORE TË JASHTME
Agregim nga «featureType» MbulesaOrtoimazherike te «featureType» MbulesaOrtoimazherike
-- Emri --
Mbulesa përbërëse ortoimazherike
-- Përkufizimi --
Referenca për mbulimin ortoimazherik që formon një mbulesë përbërëse ortoimazherike.
[ Drejtimi është ’Destinacion -> Burim’. ]
Generalizim nga «featureType» Mbulesa Ortoimazherike tek «featureType» RrjetiKoordinativIRektifikuar(Transformuar)
[ Drejtimi është ’Burim -> Destinacion’. ]
LIDHJET STRUKTURORE TË BREENDSHME
Agregim nga «featureType» MbulesaOrtoimazherike te «featureType» MbulesaOrtoimazherike
-- Emri --
Mbulesa përbërëse ortoimazherike
-- Përkufizimi --
Referenca për mbulimin ortoimazherik që formon një mbulesë përbërëse ortoimazherike.
[ Drejtimi është ’Destinacion -> Burim’. ]
ATRIBUTET
Emërtimi : Text (CharacterString)
Shumëllojshmëria: [0..1]
-- Emri-- Emërtimi
-- Përkufizimi --
Emërtimi i mbulesës ortoimazherike.
-- Përshkrimi --
SHËNIM Kjo fushë ka për qëllim të mbajë një emër që një ofrues i të dhënave mund të përdor edhe këtë fushë
përveç indetifikuesit të Inspire.
SHEMBULL 1 ”Orthofoto-së, middenschalig, , Provincie Limburg, Opname 2011 ”është emri i përdorur nga Agjencia Flamande e Informacionit Gjeografik (AGIV) për të treguar shembullin e mbulimit të ortoimazhit mbështetur në ortofotomozaikimin që mbulon njësinë administrative të provincës së Limburg me rezolucion 25 cm ’middenschalig’ fituar në vitin 2011 ’opname 2011’.
SHEMBULL 2 ”Ortofoto Urbane 2015” mund të jetë shembull i mirë i mbulimit me ortoimazheri.
[I detyrueshëm: PO]
FillimiICiklitJetësor : TM_Pozicionim
Shumëllojshmëria: [1]
-- Emri --
Fillimi i ciklit jetësor
-- Përkufizimi --
Data dhe koha në të cilën ky version i objektit gjeohapësinor ishte futur ose ndryshuar në grupin e të dhënave
gjeohapësinore.
-- Përshkrimi --
SHËNIM Meqenëse ky informacion nuk është gjithmonë i regjistruar automatikisht nga sistemi, por mund të kapet
manualisht, dhënia e kohës nuk është e nevojshme këtu. Kjo është arsyeja pse TM_Pozicionim ishte zgjedhur si lloj i vlerës në vend të Datë_Orë, që megjithatë, përdoret shpesh në specifikimet e tjera të të dhënave INSPIRE.
[I detyrueshëm: PO]
Gjurma : GM_MultiSipërfaqe
ATRIBUTET
Shumëllojshmëria: [1]
-- Emri -
Gjurma
-- Përkufizimi --
Zona gjeografike bashkëngjitur të dhënave të vlefshme të mbulimit ortoimazherik.
--Përshkrimi --
SHËNIM 1 Gjurmët duhet të vendosen në atë shtrirje gjeografike të domainit që përpunohet.
SHËNIM 2 Kjo karakteristikë është e detyrueshme nëse shembulli i mbulimit të ortoimazhit është një agregat i rasteve të tjera mbulimit me ortoimazh ose nëse elementet e mozaikimit janë dhënë.
[I detyrueshëm: PO]
InspireId : Identifikues
Shumëllojshmëria: [1]
-- Emri -- Inspire ID
-- Përkufizimi --
Indetifikues i jashtëm i objektit gjeohapësionor.
-- Përshkrimi --
SHËNIM Një identifikues i jashtëm është një identifikues unik i objektit i vendosur nga organi përgjegjës i cili mund të përdoret nga aplikimet e jashtme për t’ju referuar objektit gjeohapësinor. Identifikuesi është një identifikues lokal i objektit gjeohapësinor.
[I detyrueshëm: PO]
Koha e Ngjarjes : TM_Periudha
Shumëllojshmëria: [0..1]
-- Emri --
Koha e ngjarjes
-- Përkufizimi --
Përshkrimi i hapësirës së vëzhgimit dhe përfitimit në kohë.
-- Përshkrimi --
SHËNIM 1 Kjo masë e përkohshme i referohet vargut në kohë në të cilin imazhi kontribuon në mbulesën ortoimazherike.
SHËNIM 2 Kur përfitimi konsiderohet si i menjëhershëm, pavarësisht nga koha e ekspozimit, data e fundit dhe koha mund të jenë identike me datën dhe kohën e fillimit.
SHEMBULL 1 fillon: 2011-10-30 mbaron: 2011-10-30
SHEMBULL 2 fillon: 2011-06-07T14:31:02Z mbaron: 2011-06-07T16:10:54Z.
[I detyrueshëm: JO]
MbarimiICiklitJetësor : TM_Pozicionim
ATRIBUTET
Shumëllojshmëria: [0..1]
-- Emri--
Mbarimi i ciklit jetësor
-- Përkufizimi --
Data dhe koha në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u veçua në grupin e të dhënave
gjeohapësinore.
-- Përshkrimi --
SHËNIM Meqenësë ky informacion nuk është gjithmonë i regjistruar automatikisht nga sistemi, por mund të kapet manualisht, dhënia e kohës nuk është e nevojshme këtu. Kjo është arsyeja pse TM_Pozicionim ishte zgjedhur si lloj
i vlerës në vend të Datë_Orë, që megjithatë, përdoret shpesh në specifikimet INSPIRE të tjera të të dhënave.
[I detyrueshëm: JO]
ShtrirjaEDomainit : EX_Shtrirje
Shumëllojshmëria: [1..*]
-- Emri --
Shtrirja e Domainit
-- Përkufizimi --
Shtrirja e domain-it të dhënave gjeohapësinore të përkohshme të mbulimit.
-- Përshkrimi --
Burimi i të dhënave [SSH EN ISO 19123:2007]
SHËNIM 1 Lloji i të dhënave EX_Extent përcaktohet në SSH ISO 19103:2015. Shrirja e tyre mund të specifikohet në kohë dhe hapësirë.
SHËNIM 2 Shtrirja e domain duhet të specifikohet në hapësirë të paktën duke përdorur një nëntip të EX_GeographicExtent (EX_BoundingPolygon, EX_GeographicBoundingBox apo EX_GeographicPërshkrimi). Shtrirja gjeografike e tërë mbulimit ortoimazherik është e prekur, duke përfshirë edhe zonat ku pikat e rrjetës mbajnë vlerat zero.
[I detyrueshëm: JO]
Tipi I Interpolimit : VleraEMetodësSëInterpolimit
Shumëllojshmëria: [1]
-- Emri --
Tipi i interpolimit
-- Përkufizimi --
Metodat matematike të cilat do të përdoren për të vlerësuar një mbulim të vazhdueshëm, d.m.th. të përcaktojë vlerat e mbulimit në çdo pozicion të drejtpërdrejtë brenda domainit të mbulimit.
-- Përshkrimi --
SHËNIM 1: Fqinji më i afërt është vendosur si një vlerë e parazgjedhur në rastet kur ky informacion është lënë jashtë nga prodhuesit e të dhënave.
SHËNIM 2: Një mbulim i vazhdueshëm i rrjetit që përdor interpolimin fqinj më të afërt që vepron si një mbulim i dallueshëm i sipërfaqes.
[I detyrueshëm: PO]
[I detyrueshëm: PO]
ATRIBUTET
LIDHJE
Lidhje (drejtimi: Burim -> Destinacion)
-- Name --
Elementet e mozaikimit
-- Përkufizimi --
Përfaqësimi hapësinor i kohës së krijimit të një mbulimi të ortoimazhit me mozaik .
-- Përshkrimi --
Kjo lidhje do të përdoret vetëm kur mbulimi ortoimazh është një mozaik
Burimi: (Class) MbulesaOrtoimazherike «featureType»
Objektivi: «voidable» ElementiIMozaikimit (Class) ElementetEMozaikimit «featureType»
Shumëllojshmëria: [0..*]
-- Përkufizimi --
Përfaqësimi hapësinor i kohës së krijimit të një mbulimi të orto imazhit me mozaik.
-- Përshkrimi --
SHËNIM Kjo lidhje do të përdoret vetëm kur
mbulimi ortoimazh është një mozaik.
3.1.2.5 SHTESA ORTOIMAZHERIKE (ORTHOIMAGE AGGREGATION)
-- Emri --
Shtesa ortoimazherike
-- Përkufizimi --
Karakteristikat gjeometrike për shtesën ortoimazherike.
Tipi i elementit - DataType
ATRIBUTET
GjurmaPërbërëseEMbulimit : GM_MultiSipërfaqe
Shumëllojshmëria: [1]
-- Emri --
Gjurma përbërëse e mbulimit
-- Përkufizmi --
Përfaqësimi gjeometrik dhe përcaktimi i zonës gjeografike të një mbulim ortoimazherik që kontribon për mbulimin
shtesë ortoimazherik.
[I detyrueshëm: PO]
3.1.2.6. VLERA E METODËS SË INTERPOLIMIT (INTERPOLATION METHOD VALUE)
-- Emri --
Vlera e metodës së interpolimit
-- Përkufizimi --
Lista e kodeve që identifikojnë metodat e interpolimit të cilat mund të përdoren për vlerësimin e mbulesës ortoimazherike.
-- Përshkrimi --
SHËNIM 1 Kjo kodlistë rregullatore e INSPIRE rrjedh nga kodlista CV_Metoda e Interpolimit përcaktuar në SSH EN ISO 19123:2007. CV_Metoda e Interpolimit nuk përdoret si e tillë, sepse nuk zbatohet aktualisht.
SHËNIM 2 Shembull i vlerave: fqinji më i afërt, bilinear, bikuadratik, bikubik, etj ...
Tipi i elementit - Kod listë
ATRIBUTET
Bikuadratik:
-- Përkufizmi --
Interpolimi bikuadratik
Bikubik:
-- Përkufizmi --
Interpolimi bikubik
Bilinear:
-- Përkufizmi --
Interpolimi bilinear
Fqinji më i afërt:
-- Përkufizmi --
Interpolimi me elementin fqinjë më të afërt
3.1.3 METADATA
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015 “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.1.4 SISTEMI REFERENCË, NJËSITË E MATJES DHE RRJETAT GJEOGRAFIKE.
3.1.4.1 SISTEMET STANDARDE TË REFERIMIT, NJËSITË E MATJEVE DHE RRJETET
Sistemet e referencës, njësitë e matjeve dhe sistemet e rrjeteve gjeografike të përfshira në këtë nënseksion janë standardet që do të përdoren për të gjitha grupet e të dhënave INSPIRE, përveç kur ka përjashtime specifike të temës dhe/ose kërkesa të tjera të përcaktuara në seksionin 6.2.
A. Korniza Referuese Gjeodezike e Shqipërisë
Korniza Referuese Gjeodezike që do të përdoret në Republikën e Shqipërisë do të quhet:
“Korniza Referuese Gjeodezike Shqiptare” ose shkurt (KRGJSH - kodi EPSG: 68701). KRGJSH do të përcaktohet duke u mbështetur në Kornizën Referuese Gjeodezike Evropiane. KRGJSH do të përdoret në të gjitha aplikacionet që lidhen me përdorimin e koordinatave në territorin e vendit. Lidhja midis KRGJSH-së dhe sistemeve të tjera të përdorura në vendin tonë do të bëhet duke përdorur parametrat e transformimit të llogaritura për çdo rast.
KRGJSH përfshin:
a) Parametrat gjeodezikë bazë të përcaktuar në Sistemin Referues Gjeodezik 1980 (GRS-80) si më poshtë:
- Rrezja e ekuatorit të tokës: a = 6 378 137m;
- Konstantja gravitacionale gjeocentrike e tokës duke përfshirë edhe atmosferën: GM = 3 986 005 x 10-8 m3s-2;
- Faktori dinamik i figurës së tokës pa përfshirë baticën e qëndrueshme: J2 = 108 263 x 10-8;
- Këtij faktori i korrespondon shtypja në pole: 1/f = 298.257222100882711;
- Shpejtësia këndore e rrotullimit të tokës: ω = 7 292115.0 x 10-11rad.sek-1
b) Sistemin koordinativ gjeodezik ETRS 89;
c) Sistemin e lartësive që realizohet nëpërmjet reperave të rrjetit shtetëror të nivelimit të përfshirë në Rrjetin Unik Europian të Nivelacionit (UELN) dhe të përcaktuara në Sistemin Referues Vertikal Europian (EVRS) me ndihmën e të dhënave për forcën e rëndesës të unifikuara në sistemin International Gravity Standardization Network 1971 (IGSN 1971).
d) Sistemin e koordinatave në plan, i cili mundësohet nga dy projeksione hartografike:
- Projeksioni Tërthor Zonal i Merkatorit (TMzn) për harta në shkallë më të madhe se 1:500.000 me parametrat e mëposhtme:
Elipsoidi referencë: GRS80
--
Meridiani fillestar:
Grinuiç
-
Meridiani qendor (MQ):
200
-
-
-
Shkalla e shformimit në meridianin qendror (k0): Fallco e lindjes:
Fallco e veriut:
1
500 000 m
0 m
B. Sistemet koordinative referencë sipas INSPIRE
I. Datumi
Datumi për sistemet koordinative referencë dy-dimensionale dhe tre-dimensionale
Për sistemet koordinative referencë dy-dimensionale dhe tre-dimensionale dhe komponentja horizontale e sistemeve koordinative referencë të kombinuara të përdorura për të bërë të disponueshme grupin e të dhënave gjeohapësinore, si datum do të jetë datumi i Sistemit Referencë Tokësor Europian 1989 (ETRS89) në zona brenda kufijve gjeografik të tij ose datumi i Sistemit Referencë Tokësor Ndërkombëtar (ITRS) ose sisteme koordinative referencë gjeodezike të tjera të përputhura me ITRS, në zona që ndodhen jashtë kufijve gjeografik të ETRS89. Të përputhura me ITRS do të thotë që përkufizimi i sistemit bazohet në përkufizimin e ITRS dhe ka një marrëdhënie të mirë-dokumentuar mes dy sistemeve, sipas SSH EN ISO 19111:2007.
II. Sistemete koordinative referencë
Sistemet koordinative referencë
Grupet e të dhënave gjeohapësinore do të bëhen të disponueshme duke përdorur të paktën një prej
sistemeve koordinatave referencë të caktuara në seksionet 1.3.1, 1.3.2 dhe 1.3.3, përveç kur qëndron njëri prej kushteve të caktuara në seksionin 1.3.4.
Sistemet koordinative referencë tre-dimensionale
Koordinatat karteziane tre-dimensionale bazohen në një datum të caktuar në seksionin 1.2 dhe përdorin parametrat e elipsoidit GRS80 (Sistemi Gjeodezik Referencë 1980).
Koordinatat gjeodezike tre-dimensionale (gjerësia, gjatësia dhe lartësia elipsoidike) bazohen në një datum të caktuar në seksionin 1.2 dhe përdorin parametrat e elipsoidit GRS80.
Sistemet koordinative referencë dy-dimensionale
Koordinatat gjeodezike dy-dimensionale (gjerësia dhe gjatësia) bazohen në një datum të
caktuar në seksionin 1.2 dhe përdorin parametrat e elipsoidit GRS80.
Koordinatat në plan përdorin sistemin koordinativ referencë ETRS89 me projeksion LAEA (Lambert Azimuthal Equal Area) për analiza gjeohapësinore dhe raportime, ku duhet të
pasqyrohen sipërfaqet e vërteta.
Koordinatat në plan përdorin sistemin koordinativ referencë ETRS89 me projeksion LCC (Lambert Conformal Conic) për hartografime konforme në territorin e Europës në shkallë
të barabarta ose më të vogla se 1:500 000.
Koordinatat në plan përdorin sistemin koordinativ referencë ETRS89 me projeksion TM (Transverse Mercator) për hartografime konforme në territorin e Europës në shkallë të barabarta ose më të mëdha se 1:500 000.
Sistemet koordinative referencë të kombinuara
Për komponenten horizontale të sistemit koordinativ referencë të kombinuar, një prej sistemeve koordinative referencë të caktuara në seksionin 1.3.2 do të përdoret.
Për komponenten vertikale, do të përdoret një prej sistemeve koordinative referencë të
mëposhtme:
Për komponenten vertikale në sipërfaqen tokësore, do të përdoret Sistemi Referencë Vertikal Europian (EVRS) për të shprehur lartësitë e lidhura me gravitetin brenda kufijve
gjeografik të këtij sistemi. Në zona të cilat ndodhen jashtë kufijve gjeografik të EVRS, do të përdoren sisteme referencë vertikale të tjera të lidhura me fushën e gravitetit Tokësor për
të shprehur lartësitë e lidhura me gravitetin.
Për komponenten vertikale në atmosferen e lirë, presioni barometrik i konvertuar në lartësi duke përdour SSH ISO 2533:1975 Atmosferën Standarde Ndërkombëtare, ose do të përdoren sisteme referencë të tjera lineare ose parametrike. Aty ku janë përdorur sisteme referencë parametrike të tjera, ato do të përshkruhen në një referencë të kuptueshme duke
përdorur SSH EN ISO 19111-2:2012.
Për komponenten vertikale në zonat detare ku ka një rang të ndjeshëm batice (ujëra baticor), si sipërfaqe referencë do të përdoret Batica më e ulët Astronomike (LAT).
Për komponenten vertikale në zonat detare ku nuk ka një rang të ndjeshëm batice, në
oqeanet e hapura dhe efektivisht në ujëra më të thella se 200 metra, si sipërfaqe referencë do të përdoret niveli mesatar i detit (MSL) ose një nivel referencë i mirë-përcaktuar i afërt me MSL.
1.3.3 Sistemet koordinative referencë të tjera
Si përjashtime, ku mund të përdoren sisteme referencë të tjera nga ato të listuara në 1.3.1, 1.3.2 ose
, janë:
1. Sisteme koordinative referencë të tjera mund të caktohen për temat e të dhënave gjeohapësinore specifike në këtë Aneks.
2. Për zonat (regjionet) që ndodhen jashtë kontinentit të Europës, Shtetet Anëtare (MS) mund të përcaktojnë sisteme koordinative referencë të përshtatshme.
Kodet gjeodezike dhe parametrat e nevojshëm për përshkrimin e këtyre sistemeve koordinative
referencë dhe të cilat lejojnë veprimet e konvertimit dhe transformimit duhet të dokumentohen dhe duhet të krijohet një identifikues, sipas SSH EN ISO 19111:2007 dhe SSH ISO 19127:2019.
III. Paraqitja
Sistemet koordinative referencë të përdorura në shërbimin e shikimit të rrjetit
Për shfaqjen e grupeve të të dhënave gjeohapësinore nëpërmjet shërbimit të shikimit të rrjetit siç
specifikohet në rregulloren nr. 976/2009, së paku sistemet koordinative referencë për koordinatat gjeodezike dy-dimensionale (gjerësia, gjatësia) do të jenë të disponueshme.
IV. Identifikuesit për sistemet koordinative referencë
Identifikuesit e sistemeve koordinative referencë
1. Parametrat dhe identifikuesit e sistemit koordinativ referencë do të menaxhohen në një ose disa regjistra të përbashkët për sistemet koordinative referencë.
2. Vetëm identifikuesit që përmban një regjistër i përbashkët do të përdoren për referimin tek
sistemet koordinative referencë të listuara në këtë seksion.
3. Identifikuesit e listuar në tabelën 2 do të përdoren për referimin te sistemet koordinative referencë të përdorura në një grup të dhënash.
Këto udhëzuese teknike propozojnë përdorimin e http URl-të të ofruara nga Open Geospatial Consortium si identifikues të sistemit koordinativ referencë (shiko identifikuesit për CRS-të standard më poshtë). Këto janë të bazuara dhe të drejtojnë te përkufizimi në regjistrin e parametrave gjeodezik EPSG (http://www.epsg-registry.org/).
Shënim: Identifikuesit e CRS mund të përdoren p.sh. në:
- Kodimin e të dhënave,
- Metadatat e grupeve dhe shërbimeve të të dhënave, dhe
- Kërkesat për shërbimet e rrjetit të INSPIRE.
Tabela 2. http URl-të për sistemet koordinative referencë standard:
Sistemi koordinativ referencë
Shkurtimi
Identifikuesi http URl
Korniza Referuese Gjeodezike Shqiptare. ETRS89/ Abania
KRGJSH
http://www.epsg-
registry.org/export.htm?gml=urn:ogc:de f:crs:EPSG::6870
Kartezian 3D në ETRS89
ETRS89-XYZ
http://www.opengis.net/def/crs/EPSG/0/4
936
Gjeodezike 3D në ETRS89 mbi
GRS80
ETRS89-GRS80h
http://
www.opengis.net/def/crs/EPSG/0/4937
Gjeodezike 2D në ETRS89 mbi
GRS80
ETRS89-GRS80
http://
www.opengis.net/def/crs/EPSG/0/4258
Projeksion LAEA 2D në
ETRS89 mbi GRS80
ETRS89-LAEA
http://
www.opengis.net/def/crs/EPSG/0/3035
Projeksion LCC 2D në ETRS89
mbi GRS80
ETRS89-LCC
http://
www.opengis.net/def/crs/EPSG/0/3034
Projeksion TM 2D në ETRS89
mbi GRS80, zona 34N (18oË deri 24oË)
ETRS89-TM34N
http:// www.opengis.net/def/crs/EPSG/0/3046
Lartësi në EVRS
EVRS
http://
www.opengis.net/def/crs/EPSG/0/5730
3D të kombinuara: Gjeodezike
2D në ETRS89 mbi GRS80, dhe lartësitë EVRS
ETRS89-GRS80-EVRS
http:// www.opengis.net/def/crs/EPSG/0/7409
C. Sistemet e referencës kohore
Sistemet e referencës kohore
Sistemi standard i referencës kohore i cituar në pikën 5, Kreu II të VKM-së nr. 1077, datë 23.12.2015 “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”. do të përdoret, përveç rastit kur janë caktuar sisteme koordinative të
referencës kohore të tjera për tema të të dhënave gjeohapësinore specifike në ligjin 72/2012.
Shënim 1: Pika 5 e Kreut II të VKM-së nr. 1077, datë 23.12.2015 “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”thekson që sistemi standard referencë do të jetë kalendari Gregorian, me datat e shprehura në përputhje me SSH ISO 8601-1, 8601-2:2019.
Shënim 2: SSH ISO 8601-1, 8601-2:2019. Elementet e të dhënave dhe formatet e shkëmbimit - Shkëmbimi i informacionit - Pasqyrimi i datës dhe orës është një standard ndërkombëtar që mbulon shkëmbimin e të dhënave të lidhura datën dhe orën. Qëllimi i këtij standardi është që të sigurojë një metodë të qartë dhe të mirë-përcaktuar për pasqyrimin e datës dhe orës, në mënyrë që të shmangen keqinterpretimet e pasqyrimeve numerike të datë dhe orës, veçanërisht kur të dhënat transmetohen ndërmjet shteteve me konventa të ndryshme për shkrimin numerik të datës dhe orës. Standardi organizon të dhënat në mënyrë që afati më i madh kohor(viti) shfaqet fillimisht në të dhëna varg dhe vazhdon deri tek afati më i vogël kohor (sekondë). Ajo gjithashtu ofron një metodë të standardizuar për komunikimin informacionit të bazuar në kohë ndërmjet zonave kohore duke i dhënë një spostim të Kohës Universale të Koordinuar (UTC).
Shembull: 1997 (viti 1997); 1997-07-16 (16 Korrik 1997); 1997-07-16T 19:20:30+01:00 (16 Korrik 1997, 19ore 20min 30sek, zona kohore UTC+1).
D. Njësitë e matjeve
Kërkesa dhe rregulla të tjera
Të gjitha vlerat e matjeve duhet të shprehen nëpërmjet njësive SI ose jo-SI të pranuara për përdorim me Sistemin Ndërkombëtar të Njësive, përveç kur specifikohet ndryshe për tema apo tipa specifikë të të dhënave gjeohapësinore.
3.1.5 CILËSIA E TË DHËNAVE.
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nën elementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur për të vlerësuar dhe dokumentuar cilësinë e të dhënave për grupet e të dhënave që lidhen me të dhënat gjeohapësinore të temës Ortoimazheria.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- Specifikuar kërkesat apo rekomandimet lidhur me cilësinë e të dhënave të rezultateve të aplikueshme për grupet e të dhënave që lidhen me të dhënat gjeohapësinore për temën Emërtimet gjeografike.
- Vlerësuar dhe dokumentuar cilësinë e elementeve të metadatave të të dhënave të grupeve të të dhënave.
Tabela 3. Elementet e cilësisë të të dhënave të përdorura në temën e të dhënave gjeohapësinore
Pjesa
Elementi i cilësisë së të dhënave
Nënelementi i cilësisë së të dhënave
Përkufizimi
Sfera e vlerësimit
Sfera e vlerësimit
3.1.5.1
Kompletimi
Përjashtimi
Të dhënat e përjashtuara nga grupi i të dhënave, siç përshkruhen nga objekti i fushëveprimit.
Lloji i objektit gjeohapësinor
Vlerësim
3.1.5.2
Saktësia pozicionale
Saktësia pozicionale e të dhënave të rrjetit
Afrimi me vlerat e koordinatave të
raportuara të pranuara si të vërteta
ose të vërteta
Grup të dhënash; Lloji i objektit gjeohapësinor
Vlerësim
3.1.5.1 KOMPLETUAR - PËRJASHTIMI. (COMPLETENESS - OMISSION)
Rekomandim:
Përjashtimi duhet të vlerësohet dhe të dokumentohet duke përdorur normën e artikujve të munguar të përcaktuara në tabelat e mëposhtme.
Emri
Norma e artikujve të munguar
Emri alternativ
-
Cilësia e të dhënave të elementeve
Kompletuar
Cilësia e të dhënave të nënelementeve
Përjashtimi
Cilësia e të dhënave të matjeve themelore
Shkalla e gabimit
Përkufizim
Numri i artikujve të tepërta në setet e të dhënave në lidhje me numrin e artikujve që duhet të ishin të pranishëm.
Përshkrim
Kjo cilësi të dhënave të matura ofron një vlerësim të normës së pixels me të paktën një vlerë zero në një bandë të orthoimage. Ajo duhet të zbatohet vetëm në fushat e interesit të orthoimage, d.m.th. brenda kufirit të gjurmë të orthoimage. Ofruesi i të dhënave pritet të përshkruar arsyen nillvalue (p.sh. mbulimit të reve, kufizimin ushtarak.) brenda lloji varg atribut.
Fusha vlerësimit
Lloji i objektit hapësinor: OrthoimageCoverage
Fusha raportimit
Setet e të dhënave.
Parametër
-
Cilësia e të dhënave të llojeve të vlerave
Real, përqindje, raport
Cilësia e të dhënave të strukturës së vlerave
Vlerë e vetme
Burimi referencë
SSH EN ISO/DIS 19157:2013 Geographic information - Data
Shembull
-
Masa identifikuese
7 (SSH EN ISO/DIS 19157:2013)
3.1.5.2 SAKTËSIA E POZICIONIMIT - SAKTËSIA ABSOLUTE APO E JASHTME. (ABSOLUTE OR EXTERNAL ACCURACY)
Rekomandim:
Saktësia absolute ose e jashtme duhet të vlerësohet dhe dokumentohet duke përdorur saktësinë absolute pozicionale ose saktësinë e jashtme të nënelementeve dhe vlerën mesatare të pasigurive pozicionale siç është specifikuar në tabelën më poshtë.
4. ANEKSE
4.1 KATALOGU
Nr.
Emri i elementit anglisht
Emri i elementit shqip
Tema
Tipi
ORTOIMAZHERIA
3.1.2.1
Mosaic Element
Elementet e Mozaikimit
Ortoimazheria
«featureType»
3.1.2.2
Aggregated Mosaic
Element
Elementet Shtesë të
Mozaikimit
Ortoimazheria
«featureType»
3.1.2.3
Single Mosaic
Element
Elementi Përbërës i
Mozaikimit
Ortoimazheria
«featureType»
3.1.2.4
Orthoimage Coverage
Mbulesa Ortoimazherike
Ortoimazheria
«featureType»
3.1.2.5
Orthoimage
Aggregation
Shtesa Ortoimazherike
Ortoimazheria
«dataType»
3.1.2.6
Interpolation
Method Value
Vlera e Metodës së
Interpolimit
Ortoimazheria
«codeList»
ANEKSE
A
Identifier
Identifikues
Generic Conceptual Model
«dataType» imported
4.2 TË DHËNAT E IMPORTUARA
A. Identifikues-(Identifier) - Data Type
Identifikues
Përkufizim
Një objekt identifikues i jashtëm është një identifikues unik i objektit të publikuar
nga organi përgjegjës, i cili mund të përdoret nga aplikacionet e jashtme të referimit të objektit gjeohapësinor.
Paketa
Base Type
Referenca
INSPIRE Generic Conceptual Model, version 3.4 [DS-D2.5]
Përshkrim
-
4.3 KODI EPSG PËR KRGJSH
1 Shiko Aneks 4.3
