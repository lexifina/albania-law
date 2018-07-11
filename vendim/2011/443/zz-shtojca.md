# Shtojca
ANEKS 1
KOMPONENTËT E ARKITEKTURËS SOFTWARE DHE HARDWARE TË ALBIS-it
Përshkrim teknik i ALBIS-it
Arkitektura teknike dhe funksionale e “Sistemit të menaxhimit elektronik të çështjeve të përmbarimit gjyqësor” është e orientuar 100% kundrejt shërbimeve (SOA-Service Oriented Architecture) dhe mundëson menaxhimin me sukses të çështjeve, dokumenteve dhe proceseve të punës së përmbarimit shtetëror dhe atij privat.
Arkitektura funksionale
Arkitektura funksionale e Sistemit është dizenjuar në mënyrë që të plotësojë maksimalisht të gjitha nevojat për menaxhimin e çështjeve të shërbimit të përmbarimit gjyqësor shtetëror dhe privat, si nga ana operative, gjithashtu, dhe nga ajo organizative. Për sa i përket anës operative, ajo u siguron përmbaruesve gjyqësorë, shtetërorë dhe privatë, një sistem fleksibël me një shkallë të lartë automatizimi, duke i dhënë mundësinë e rritjes së eficiencës së tyre në maksimum. Eficienca e lartë do të sigurojë si përfundim rritjen e cilësisë së shërbimit të përmbarimit gjyqësor ndaj qytetarëve shqiptarë. Për sa i përket anës organizative, arkitektura funksionale nëpërmjet raporteve, analizave, dhe statistikave u jep mundësinë organeve përkatëse të kenë në kohë reale dhe në mënyrë të saktë të gjithë informacionin e duhur për të kontrolluar dhe për të përmirësuar strukturën dhe funksionimin e këtij shërbimi.
Elementet themelore të arkitekturës funksionale janë: çështjet, dokumentet dhe palët. Këto elemente janë të ndërlidhura midis tyre dhe çdo element apo objekt tjetër në sistem është i lidhur me këto:
Sistemi i menaxhimit elektronik të çështjeve i ndërtuar në bazë të kërkesave të Ministrisë së Drejtësisë përbën një sistem të plotë dhe të avancuar duke plotësuar tërësisht kërkesat e shkallëzuara dhe të sofistikuara të shërbimit përmbarimor gjyqësor. Karakteristikat ose funksionet e tij kryesore mund të përmblidhen si më poshtë:
- Menaxhimi i çështjeve:
- regjistrimi i çështjeve;
- shpërndarja e çështjeve;
- monitorimi dhe ndjekja e çështjeve;
- alarme për çështjet.
- Menaxhimi i dokumenteve:
- regjistrimi i dokumenteve;
- integrimi me Microsoft Office;
- prodhimi i dokumenteve të çështjeve;
- kategorizimi i dokumenteve;
- integrimi me Windows Explorer.
- Menaxhimi i kontakteve:
- regjistri i kontakteve;
- struktura e dosjeve;
- historiku i komunikimi.
- Siguria:
- siguri në nivel objekti apo dokumenti;
- klasifikim i sigurisë.
- Rrjedha pune të strukturuara dhe të veçanta:
- automatizim i proceseve;
- rishikim i cikleve të çështjeve;
- menaxhim i rregullave.
- Instruktimi dhe ndihma:
- ndihmë dhe instruktim proaktiv i përdoruesit;
- ndihmë në përputhje me kontekstin.
- Ndërfaqe e bazuar në teknologjinë portal:
- vetëshërbim;
- ndërfaqe e bazuar sipas roleve.
- Navigim/kërkim
- Raportim:
- statistika dhe analiza në dimensione të ndryshme;
- statistika dhe analiza në kohë reale;
- fleksibilitet në krijimin e raporteve.
Arkitektura teknike
Arkitektura teknike e sistemit AlBIS është e bazuar në teknologjitë më të avancuara hardware dhe software, të cilat janë të testuara dhe sigurojnë një menaxhim dhe kontroll të plotë të proceseve dhe dokumenteve të sistemit të përmbarimit. Sistemi përmban opsionin përkatës që përmbaruesit gjyqësorë privatë të mund të logojnë vetëm përmes sistemit SIAIP, që përdoret prej tyre, në sistemin ALBIS. Ky opsion bën të mundur që përmbaruesit privatë të mos logohen dy herë, por mjafton të jenë të loguar 1 herë në SIAIP dhe me të njëjtat kredenciale, nëse duan, vijojnë punën në sistemin ALBIS.
Arkitektura software
Arkitektura software e AlBIS-it është e bazuar në platformën e IBM FileNet P8, e cila në bashkëpunim me komponentët e tjerë mundëson menaxhimin e çështjeve dhe të dokumenteve, në mënyrë të pajtueshme me të gjitha llojet e rregullave institucionale apo ligjore të shërbimit përmbarimor shtetëror apo privat. Gjithashtu, ajo bën të mundur kontrollin dhe menaxhimin nga Ministria e Drejtësisë, e të gjitha proceseve, informacionit dhe sigurisë.
Hierarkia e përdoruesve
Sistemi do të ketë këto role përdoruesish:
- Administratori do të ketë të drejtat e administrimit të sistemit.
- Specialistët me detyra monitoruese të Ministrisë së Drejtësisë ose të DPP-së do të kenë të drejta leximi në ato çështje që ata do të kontrollojnë.
- Drejtori i përgjithshëm i DPP-së dhe drejtori i Përgjithshëm i Çështjeve Rregullatore të Drejtësisë në Ministrinë e Drejtësisë do të ketë të drejta leximi te të gjitha çështjet e përmbarimit shtetëror.
- Drejtori i Përgjithshëm i Çështjeve Rregullatore të Drejtësisë në Ministrinë e Drejtësisë do të ketë të drejta leximi te të gjitha çështjet e përmbarimit privat.
- Kryetari i Zyrës Rajonale do të ketë të drejta të regjistrojë një çështje në sistem, të hedhë shortin, të zëvendësojë përmbaruesin (e zyrës përkatëse), të transferojë çështjen në një zyrë tjetër. Do të ketë të drejta leximi në të gjitha çështjet e zyrës së tij. Gjithashtu, do të ketë të njëjtat të drejta me një përmbarues kur ai/ajo është përgjegjës për çështjen.
- Përmbaruesi shtetëror do të ketë të gjitha të drejtat e nevojshme për përpunimin e çështjeve që i janë përcaktuar. Do të ketë mundësi të shikojë vetëm çështjet që i takojnë.
- Përmbaruesi privat do të ketë të gjitha të drejtat e nevojshme për regjistrimin dhe procesimin e çështjeve që ai ka marrë përsipër.
Arkitektura hardware (Data-Center në Ministrinë e Drejtësisë)
Arkitektura teknike hardware e AlBIS-it është një arkitekturë e dizenjuar duke përdorur pajisje të teknologjisë së fundit që bëjnë të mundur funksionimin me performacë maksimale të sistemit.
Pajisjet e njësisë qendrore (Data Center) përshijnë infrastrukturën e mëposhtme:
1. Fujitsu PY BX900 S1 System Unit me 8 server-a: PY BX920 S2 Dual Server Blade;
2. Firewall Cisco ASA5510-AIP10-K9;
3. UPS e instaluar në një Rack Fujitsu;
4. 46 HU Fujitsu Primergy Primecenter Rack.
ANEKS 2
MODELI I PARAQITJES SË TË DHËNAVE TË SISTEMIT ALBIS
1. Të dhëna parësore
ALBIS-i regjistron këto të dhëna parësore:
Fushat
Përshkrimi
Nr. i çështjes
Nr. i çështjes/i dosjes përmbarimore që regjistrohet. Vendoset nga ALBIS.
Nr. i vjetër i çështjeve
Numri i vjetër i çështjeve të regjistruara. Do të përdoret për çështjet aktive të cilat janë hapur përpara kalimit online të sistemit.
Zyra e përmbarimit/ përmbaruesi privat
Zyra e përmbarimit shtetëror ose përmbaruesi privat: vendoset nga ALBIS profili i përdoruesit.
Nr. i protokollit
Numri i protokollit me të cilin është regjistruar kërkesa për hapjen e çështjes përmbarimore në zyrën shtetërore.
Data/nr. i prot. të kërkesës
Data e regjistrimit të kërkesës për vënie në ekzekutim të kreditorit nga përmbaruesi gjyqësor privat ose shoqëria përmbarimore/nr. prot.
Nr./datë e urdhrit ekzekutiv/vendimit
Numër/datë e urdhrit të ekzekutimit ose numër/datë e vendimit të gjykatës kur nuk ka urdhër ekzekutimi të veçantë.
Gjykata
Gjykata që ka lëshuar urdhrin e ekzekutimit/vendimin.
Titulli ekzekutiv
Lloji i titullit ekzekutiv (numër, datë, të dhëna, origjinal apo i noterizuar)
Objekti
Përshkrimi i shkurtër i objektit të ekzekutimit.
Data e regjistrimit
Data e regjistrimit të çështjes (dd.mm.vvvv).
Statusi i çështjes:
Vendoset statusi i çështjes (aktiv, pezulluar, pushuar).
Transferimet e çështjeve përmbarimore
Vendoset nr. datë vendimi, autorizimi për transferimin e çështjes përmbarimore (emri i transferuesit dhe i marrësit).
Data e fillimit të ekzekutimit
Data në të cilën përmbaruesi fillon ekzekutimin e çështjes (dokumenti i parë procedural i përmbaruesit, nr. /datë).
Kreditori
Kreditori, bashkëkreditorët, përfaqësuesit ligjorë.
Debitori
Debitor, debitorët, dorëzanësit, hipotekuesit, palët e lidhura.
Lloji i detyrimit (monetar ose jomonetar)
Vendoset shuma e detyrimit të debitorit ose lloji i detyrimit jomonetar.
Lloji i taksës
Lloji i tarifës
Vendoset lloji i taksës përmbarimore: E vlerësueshme (%) ose e pavlerësueshme (3.800) dhe lloji i tarifës.
Komunikimi
Jepen të dhëna në lidhje me komunikimin ndërinstitucional shkresor të çdo çështjeje përmbarimore.
Informacion mbi procesin ekzekutues nga përmbaruesi gjyqësor
Jepet një informacion i kërkuar nga ministri i Drejtësisë apo struktura e autorizuar prej tij në lidhje me procesin ekzekutues të çështjes përmbarimore.
Komente
Mund të shkruhen komente nga më të ndryshmet.
Të dhëna dytësore
ALBIS-i regjistron këto të dhëna dytësore:
Person juridik (kompanitë/institucionet)
Regjistri Tregtar i QKB-së
Emri
Emërtimi i kompanisë apo i institucionit
E-mail
Adresa e postës elektronike
Numrat e telefonit
Vendosen numrat e telefonit. Mund të shtohen sipas nevojës
Adresa
Vendoset adresa e personit juridik
Kodi postar
Vendoset kodi postar
Qyteti
Qyteti (list)
Shteti
Shteti
NIPT
NIPT-i i kompanisë
Lloji i palës
Përzgjidhet nga lista lloji i kompanisë apo i institucionit
Person fizik (individ)
Regjistri Kombëtar i Gjendjes Civile
Emri
Vendoset emri i plotë i individit së bashku me atësinë
E-mail
Adresa e postës elektronike
Numrat e telefonit
Vendosen numrat e telefonit. Mund të shtohen sipas nevojës
Adresa
Vendoset adresa e personit
Kodi postar
Kodi postar
Qyteti
Qyteti
Shteti
Shteti
ID
Vendoset numri personal i kartës së identitetit
Të dhëna automjeti
Regjistri Kombëtar i Mjeteve
Targa e mjetit
Vendoset targa e mjetit të debitorit
Nr. i shasisë
Numri i shasisë së mjetit
Të dhëna të mjetit (lloji, marka, modeli, tipi, karroceria, ngjyra, nr. i dyerve, lënda djegëse, fuqia, cilindrata, viti i prodhimit, nr. i vendeve)
Të dhëna të skedës teknike të mjetit
Lloji i përdorimit
Lloji i përdorimit
Pronari i mjetit (ID, emër mbiemër, adresa)
Të dhëna të pronarit (debitorit)
Të dhëna të pasurive të paluajtshme
Regjistri Elektronik i Pasurive të Paluajtshme
Nr. i pasurisë
Vendoset nr. i pasurisë
Zona kadastrale
Vendoset nr. i zonës kadastrale
Volum, faqe
Të dhëna të volumit dhe të faqes të shënuara në kartelë
Lloji i pasurisë
Lloji i pasurisë
Të dhëna të pronarëve (ID, emër mbiemër, adresa)
Të dhëna të pronarit/pronarëve të pasurisë
Gjendja juridike e pasurisë
Vendoset gjendja juridike e pasurisë
