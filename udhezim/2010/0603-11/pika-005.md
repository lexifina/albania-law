5. Termat e përdorur
5.1 Termat dhe shkurtimet e përdorura në këtë udhëzim sqarohen në shtojcën A, bashkëlidhur këtij udhëzimi e cila është pjesë përbërëse e tij dhe do të konsiderohen të detyrueshme.
KAPITULLI II
Software-ët në sistemet e MTA
Me anë të këtij udhëzimi vendosen standardet dhe procedurat për zbatimin e programeve të sigurimit të sistemeve të sigurisë, të cilat garantojnë që rreziqet që lidhen me përdorimin e software-it, lidhur me sigurinë në sistemet tokësore të MTA, të reduktohen në një nivel të pranueshëm.
Ky udhëzim nuk përshkruan çdo lloj mjeti mbështetje të pajtueshmërisë për software-t.Ky është roli i standardeve të sigurimit të software-t. Prandaj është jashtë fushëveprimit të kësaj kërkese të përcaktojë standardet specifike kombëtare ose ndërkombëtare të sigurimit të standardeve të software-it.
Qëllimi i kësaj kërkese është të ofrojë për organet AKM dhe OSHTA një set kërkesash rregullatore të sigurisë të njësishme dhe të harmonizuara për përdorimin e software-ve në sistemet e MTA.
A. QËLLIMI
i) Qëllimi i këtij udhëzimi është që të ofrojë siguri për AKM dhe OSHTA nëpërmjet një grupi kërkesash rregullative të sigurisë të njëtrajtshme dhe të harmonizuar për përdorimin e software-ve në sistemet e MTA.
ii) Kjo kërkesë rregullatore ka lidhje me sigurinë në software-t që përdoren nga OSHTA për trafikun ajror civil, në sistemet tokësore të MTA-së, duke përfshirë të gjitha ndryshimet operative on-line të software-ve të tilla si cutover / hot swapping.
iii) Shtrirja e kësaj kërkese rregullatore është e përcaktuar për përbërësit tokësorë të MTA dhe të shërbimeve mbështetëse tokësore, duke përfshirë sistemet KNS, nën kontrollin e menaxhimit të OSHTA. Kjo kërkesë rregullatore nuk mund të zbatohet pa u ndryshuar dhe vlerësuar në mënyrë adekuate, për sistemet ajrore ose pjesë të hapësirës ajrore të sistemeve MTA.
iv) Dispozitat e kësaj kërkese rregullatore të sigurisë janë zhvilluar mbi bazën e një procesi a priori të vlerësimit efektiv të rrezikut dhe procesit të zbutjes të tij, që të zhvillohet në një nivel të duhur për të siguruar që i jepet vëmendje e duhur në të gjitha aspektet të MTA-je duke përfshirë edhe funksionet e MTA që do të kryhet nga software-t.
v) Kjo kërkesë rregullatore nuk përshkruan çdo lloj mjeti mbështetje të pajtueshmërisë së software-it. Ky është roli i standardeve të sigurimit të software-ve. Kjo, në përputhje me rrethanat, është jashtë fushëveprimit të kësaj kërkese, që të nxjerrë standarde specifike kombëtare apo ndërkombëtare të sigurimit të software-it.
B. ARSYETIMI
i) Vendimi 6/8/5 i SRC miraton përfshirjen e zhvillimit të një kërkese rregullatore sigurie të EUROCONTROL për sistemet e bazuara në software të MTA në programin e punës të SRC. Është vërejtur se nuk ka pasur një të tillë për këtë fushë brenda standardeve dhe praktikave të rekomanduara të ICAO-s.
ii) Udhëzimi i ministrit nr.20, datë 16.10.2008 “Përdorimi i sistemeve të menaxhimit të sigurisë nga ofruesit e shërbimit MTA”, kërkon që sistemet e menaxhimit të sigurisë të përfshijnë vlerësimin e rrezikut dhe të zbutjes së tij për të garantuar se funksionet në sistemin e MTA janë vlerësuar për rëndësinë e tyre dhe se të gjitha funksionet e sistemit të MTA janë të klasifikuara sipas rreptësisë së tyre. Kjo gjithashtu kërkon sigurimin e zbutjen e përshtatshme të vlerësimit të rreziqeve, përsa i përket rëndësisë së ndryshimit të kryer.
iii) Udhëzimi i ministrit nr.22, datë 16.10.2008 “Vlerësimi i rrezikut dhe zbutja e tij në MTA” zgjeron udhëzimin e ministrit nr.20, datë 16.10.2008 me kërkesat për vlerësimin dhe zbutjen e rrezikut, dhe siguron një proces gjithëpërfshirës në sistemin e MTA-së të kapaciteteve njerëzore, procedurave dhe pajisjeve (software dhe hardware) dhe ndërveprimet e tyre kur futet dhe/ose planifikohet një ndryshim në sistemin e MTA-së.
iv) Ky udhëzim është vazhdimi i një procesi rregullator të zhvillimit dhe perfeksionimit të sigurisë dhe zgjeron udhëzimin e Ministrit nr.22, datë 16/10/2008 lidhur me aspektet e software-ve dhe sistemeve të MTA. Kërkesat plotësuese rregullative për siguri në aspektet ”hardware” janë nën shqyrtim.
v) Siguria është një karakteristikë themelore e sistemeve të MTA. Ajo ka një ndikim dominues mbi efektivitetin operativ. Sistemet MTA, tani përfshijnë ndërveprime të rëndësishme në një mjedis më të madh dhe në integrim të vazhdueshëm, automatizimi të funksioneve operative të kryera më parë nëpërmjet procedurave manuale, rritje në tërësi, dhe përdorimi masiv dhe sistematik i programeve, kërkojnë një qasje më formale për arritjen e sigurisë.
C. OBJEKTIVI
Objektivi është ulja në nivele minimale të pranueshme të rreziqeve që lidhen me përdorimin e software-it në sistemet e MTA-së, nëpërmjet mbrojtjes dhe sigurisë për këto sisteme.
DISPOZITA TË ZBATUESHME
1. KËRKESAT E PËRGJITHSHME PËR SIGURINË
1.1 Brenda kuadrit të SMS së vet, dhe si pjesë e aktiviteteve të veta për vlerësimin e rrezikut dhe zbutjen e pasojave, OSHTA duhet të përcaktojnë dhe të zbatojnë një sistem sigurimi të sigurisë së software-ve që merret posaçërisht me aspekte që lidhen me software-t, duke përfshirë të gjitha ndryshimet operative on-line të software-ve (të tilla si cutover/hot swapping).
1.2 OSHTA duhet të garantojnë, si minimum, brenda sistemit të sigurimit të sigurisë së software-ve, se:
a) kërkesat ndaj software-it përcaktojnë saktë se çfarë kërkohet nga software-i, në mënyrë që të përmbushen objektivat dhe kërkesat e sigurisë, si identifikohen dhe në dhe nga vlerësimin e rrezikut dhe procesit të zbutjes së tij;
b) dallueshmëria është adresuar në lidhje me të gjitha kërkesat e software-ve;
c) zbatimi i programeve nuk përmban funksione të cilat ndikojnë negativisht mbi sigurinë;
d) Software-t e MTA përmbushin kërkesat për një nivel të besueshmërisë i cili është në përputhje me kriticitetin e software-it;
e) sigurinë që të gjitha kërkesat e mësipërme të përgjithshme të sigurisë, janë të kënaqur, dhe argumentet për të demonstruar sigurimin e kërkuar rrjedhin në çdo kohë nga:
i) një version software-i i njohur dhe i ekzekutueshëm;
ii) një gamë të njohur të të dhënave të konfigurimit, dhe
iii) një set i njohur i produkteve të këtij software-i dhe përshkrimet (duke përfshirë specifikimet) që janë përdorur në prodhimin e këtij versioni.
1.3 OSHTA duhet të garantojë sigurinë e nevojshme, te autoriteti i caktuar AKM, që kërkesat në nenin 1.2 më sipër janë përmbushur.
2. KËRKESA TË APLIKUESHME PËR SISTEMIN E SIGURIMIT TË SIGURISË SË SOFTWARE-ve
OSHTA duhet të sigurojë, si minimum, që sistemi i sigurimit të sigurisë së software-ve:
2.1 Është i dokumentuar, në veçanti, si pjesë e vlerësimit të rrezikut të përgjithshëm dhe zbutjes së tij.
2.2 Cakton nivelet e sigurimit të software-ve për të gjitha programet operative në MTA.
2.3 Përfshin sigurim për:
a) vlefshmërinë e kërkesave të software-ve;
b) verifikim software;
c) menaxhimin i konfigurimit të software-it dhe
d) kërkesat e software-it për gjurmëtimin.
2.4 Përcakton rreptësinë mbi të cilën sigurimet janë përcaktuar.
Rreptësia do të përcaktohet për secilin nivel sigurimi të software-it, dhe do të rritet kur rritet kriticiteti në përdorim i software-it . Për këtë qëllim:
a) Ndryshimit në rreptësinë të garancive për nivel sigurimi të software-it duhet të përfshijë kriteret e mëposhtme:
i) kërkohet të arrihet me pavarësi,
ii) kërkohet të arrihet,
iii) nuk kërkohet,
b) Sigurimet përkatëse për çdo nivel të sigurimit të software-ve do të japin besim të mjaftueshëm që software-t e MTA mund të veprojë në mënyrë të tolerueshme sigurie.
2.5 Përdor feed-back prej përvojës nga përdorimet e software MTA për të konfirmuar se sistemi i sigurimit të sigurisë së Software-ve dhe caktimi i niveleve të sigurimit, janë të përshtatshme. Për këtë qëllim, efektet që rezultojnë nga çdo mosfunksionim apo dështim i software-ve nga përvoja operative në MTA, do të raportohen sipas udhëzimit të ministrit nr.19 datë 16/10/2008, dhe do të vlerësohen sipas përcaktimeve në udhëzimin e ministrit nr.22 datë 16/10/2008.
2.6 Ofron të njëjtin nivel të besimit, përmes çfarëdo mjeti të zgjedhur dhe rënë dakord me AKM, për evolimin ose jo të software-ve të MTA (p.sh. COTS-software jashtë përdorimit komercial etj.) me të njëjtin nivel sigurimi të software-ve.
3. KËRKESAT E APLIKUESHME PËR NIVELIN E SIGURIMIT TË SOFTWARE
OSHTA duhet të garantojë, si minimum, brenda sistemit të sigurimit të sigurisë së software, që:
3.1 Nivel i sigurimi të software-ve lidh ashpërsinë në sigurimin e software-ve me kriticitetin e software-ve të MTA duke përdorur Skemën e Klasifikimit të Rreptësisë sipas udhëzimit nr.22, datë 16.10.2008, së bashku me gjasat e një efekti të caktuar negativ që mund të ndodhë.Katër nivele të sigurimit të software-ve do të identifikohen, ku me siguri software-i të nivelit 1 tregohet niveli më kritik.
3.2 Një nivel i caktuar sigurimi të software-it do të përllogaritet sipas efekteve më negative që një mosfunksionim ose dështim i software-it mund të shkaktojë, sipas udhëzimit nr.22, datë 16.10.2008. Kjo duhet të marr parasysh rrezikun bashkëngjitur me mosfunksionimin ose dështimin, dhe projektimin me/ose procedurat e mbrojtjes të identifikuara.
3.3 Të gjithë përbërësit e software-ve të MTA që nuk mund të jenë të pavarur nga njëri-tjetri do t’u përcaktohet niveli i sigurimit të software-ve sipas nivelit më kritik nga përbërësit e varur të këtij software-i.
4. KËRKESA E APLIKUESHME PËR VLEFSHMËRINË E SIGURIMIT TË SOFTWARE-it
OSHTA duhet të garantojnë, si minimum, brenda sistemi i sigurimit të sigurisë së software-it, se kërkesat për sigurinë:
4.1 Specifikojnë një sjellje funksionale (nominale dhe mënyra të reduktuara) të software-ve të MTA, sipas përmbushjes në kohë kërkesave, kapacitetin, saktësinë, burimeve të përdorimit të software-ve në hardware-t përkatës, fortësinë në kryerje të veprimeve në kushte anormale funksionimi dhe tolerance mbingarkimi.
4.2 Janë të plotë dhe të saktë, dhe janë gjithashtu në përputhje me kërkesat për sistemin e sigurisë.
5. KËRKESAT PËR VERIFIKIMIN E SIGURIMIT TË SOFTWARE-it
OSHTA duhet të sigurojë, si minimum, brenda sistemit të sigurimit për sigurinë e software-it që:
5.1 Mënyra e funksionimit të software-ve të MTA, përmbush në kohë kapacitetin, saktësinë, përdorimet e software-ve në hardware-t përkatës, fortësinë në kryerjen e veprimeve në kushte anormale funksionimi dhe tolerance mbingarkimi, si dhe i bindet kërkesave për software-t.
5.2 Software-t e MTA janë verifikuar në mënyrë përkatëse nga analiza dhe/ose testime dhe / ose mjete ekuivalent, siç është rënë dakord për ato me AKM.
5.3 Verifikimi i software-ve të MTA është i saktë dhe i plotë.
