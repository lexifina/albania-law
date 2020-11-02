# Shtojca
REPUBLIKA E SHQIPËRISË
AGJENCIA E ADMINISTRIMIT TË PASURIVE TË SEKUESTRUARA DHE KONFISKUARA
Dokument për formatin e regjistrimit të të dhënave
Përmbajtja
1. Përmbledhje e sistemit dhe të dhënave
1.1 Regjistri i bazave të të dhënave
1.2 Kërkesat dhe rregullat për administrimin e të dhënave
1.3 Dhënësi/dhënësit e informacionit
1.4 Të dhënat parësore
1.5 Të dhënat dytësore
1.6 Bazat e të dhënave me të cilat ndërvepron sistemi
2. Arkitektura e sistemit dhe bazës së të dhënave
2.1 Objektet e aksesit të të dhënave
2.2 Ndërfaqet dhe modulet e sistemit
1. Përmbledhje e sistemit dhe të dhënave
Sistemi i administrimit të pronave të sekuestruara dhe konfiskuara i mundëson punonjësve të AAPSK të realizojnë procesin e menaxhimit dhe dhënies me qira të pasurive të sekuestruara dhe konfiskuara në mënyrë automatike. Objektivat e këtij sistemi janë:
- regjistrimi dhe monitorimi e të gjithë objekteve të sekuestruara dhe të konfiskuara të dhëna me qira;
- ndjekja e proceseve të punës në lidhje me pasuritë e menaxhuara nga AAPSK-ja;
- gjurmimi i kontratave për marrjen me qira të objekteve të sekuestruara dhe të konfiskuara;
- krijimin e një baze të dhënash me info të përgjithshëm për të gjitha pronat e sekuestruara dhe të konfiskuara.
1.1 Regjistri i bazave të të dhënave
Emërtimi bazës së të dhënave
SPSK (Sistemi i pronave të sekuestruara dhe të konfiskuara)
Emërtimi shkurt i bazës së të dhënave
SPSK
1.2 Kërkesat dhe rregullat për administrimin e të dhënave
Të dhënat që përdoren në sistemin e administrimit të pasurive të konfiskuara dhe sekuestruara janë të regjistruara në një bazë të dhënash, e cila aksesohet nëpërmjet sistemit nga përdorues me role të ndryshme. Rolet kryesore që aksesojnë sistemin dhe të drejtat e tyre janë:
- Administratori qendror
Realizon të gjitha konfigurimet e nevojshme për funksionimin e sistemit, si: konfigurimi i organigramës, përdoruesve, statuseve të pasurive, institucionet, njësitë matëse, llojet e llogarive.
- Kryeadministratori
Realizon shpërndarjen e pasurive në administratorët përkatës në bazë të urdhrit të ardhur ose vendimit të tij. Merret me koordinimin e punës dhe mbikëqyrjen e zbatimit të procedurave që lidhen me administrimin e pasurive nga administratorët.
- Administratori i pasurisë
Është personi që është caktuar me vendim gjykate për administrimin e pasurisë së sekuestruar/ konfiskuar ose me urdhër të brendshëm të Kryeadministratorit. Ndjek të gjitha procedurat e nevojshme për menaxhimin e pasurive që i janë caktuar.
- Koordinatori i terrenit
Ndjek dhe koordinon punën për marrjen në administrim të pasurive të sekuestruara dhe të konfiskuara. Kontrollon raportet mujore dhe tekniko-financiare të gjeneruara. Kontrollon dhe mbikëqyr statusin e pasurive në administrim të AAPSK-së.
- Koordinatori juridik
Ndjek dhe koordinon punën për marrjen në dorëzim të pasurisë nga administratori i pasurisë i caktuar. Monitoron kontratat e qirasë së regjistruara në sistem nga administratorët e pasurive dhe akseson raportet e gjeneruara në sistem në lidhje me pasuritë e dhëna me qira.
- Koordinatori financiar
Gjeneron raporte dhe statistika financiare që kanë të bëjnë me të ardhurat dhe shpenzimet e pasurive në administrim nga AAPSK-ja. Mbikëqyr raportimet e realizuara nga administratorët mbi të ardhurat dhe shpenzimet e kryera për pasuritë.
1.3 Dhënësi/dhënësit e informacionit
Më poshtë gjenden dhënësit e informacionit për këtë sistem:
Qytetarë
Biznese
Administratë
Administratorët e pasurive - regjistrimi i të dhënave
ZRPP, DPGJC, DPSHTRR, QKR - Komunikim nëpërmjet webservice
1.4 Të dhënat parësore
Të dhënat parësore janë informacione specifike, të mbledhura nga institucioni administrues, në përputhje me aktin e krijimit. Këto të dhëna listohen si më poshtë:
Numri
Të dhënat
1
Pasuria e sekuestruar/konfiskuar (emërtimi)
2
Vendimet gjyqësore
3
Lloji i pasurisë së sekuestruar/konfiskuar
4
Pronari/ pronarët e pasurisë
5
Vlera e tregut të pasurisë
6
Administratori i pasurisë dhe data e marrjes në dorëzim
7
Statusi i pasurisë
8
Sasia dhe njësia e pasurisë
9
Llojet e të ardhurave dhe shpenzimeve
10
Të ardhurat dhe shpenzimet e regjistruara për pasuritë
11
Kontratat e qirasë dhe qiramarrësit
12
Përdoruesit
13
Banka, lloji i llogarisë, interesi (për pasuritë e tipit: llogari)
1.5 Të dhënat dytësore
Të dhënat dytësore konsiderohen të dhënat që merren nga një bazë tjetër të dhënash, ku ato janë parësore. Këto të dhëna listohen si më poshtë:
Institucioni Drejtoria e Përgjithshme e Gjendjes civile
Databaza Regjistri Kombëtar i Gjendjes Civile
Numri
Të dhënat
1
NID
2
Emër
3
Atësi
4
Mbiemër
5
Datëlindje
6
Adresa
Institucioni Qendra Kombëtare e Biznesit
Databaza Regjistri Tregtar
Numri
Të dhënat
1
NIPT
2
Emri i subjektit
3
Tipi i subjektit
4
Statusi i subjektit
5
Data e regjistrimit
6
Përfaqësuesi
7
Adresa
8
Aktiviteti i subjektit
Institucioni Drejtoria e Përgjithshme e Shërbimeve të Transportit Rrugor
Databaza Regjistri Kombëtar i Mjeteve
Numri
Të dhënat
1
NID
2
Targa
3
Lloji i mjetit
4
Nr. Shasie
5
Marka
6
Modeli
7
Ngjyra
8
Viti
Institucioni Zyra e Regjistrimit të Pasurive të Paluajtshme
Databaza Regjistri Elektronik i Pasurive të Paluajtshme
Numri
Të dhënat
1
Zonë kadastrale
2
Volum
3
Faqe
4
Nr. i pasurisë
5
Lloji i pasurisë
6
Adresa e pasurisë
7
Pronarët
1.6 Bazat e të dhënave me të cilat ndërvepron sistemi
Këtu paraqiten lidhjet me bazat e tjera të të dhënave duke i ndarë ato si konsumues dhe eksportues informacioni drejt kësaj baze të dhënash.
Eksportues
Konsumues
Regjistri Kombëtar i Gjendjes Civile
SPSK
Regjistri Tregtar
SPSK
Regjistri Kombëtar i Mjeteve
SPSK
Regjistri Elektronik i Pasurive të Paluajtshme
SPSK
2. Arkitektura e sistemit dhe bazës së të dhënave
Më poshtë gjenden skemat për menaxhimin e pronave të sekuestruara dhe menaxhimin e aplikimeve të realizuara për pronat e sekuestruara.
Diagrami 1. Regjistrimi i pasurive
Diagrami 2. Kryeadministratori
Diagrami 3. Menaxhimi i pasurive të sekuestruara dhe të konfiskuara
2.1 Objektet e aksesit të të dhënave
Këtu përshkruhen të gjitha objektet që përdoren për të komunikuar me bazën e të dhënave. Çdo objekt, i cili përfshihet në këtë paragraf, përfaqësohet nga një tabelë ose tabela të cilat e përfaqëson atë në bazën e të dhënave.
Nr.
Emri i tabelës (klasa)
Përshkrimi i tabelës
1
PSK_Adresa
Kjo tabelë ruan adresat e sistemit
2
PSK_Aplikimi_per_qera
Kjo tabelë ruan aplikimet që do të bëhen nga subjektet në frontend për qira të pasurive të publikuara
3
PSK_Bashkia
Kjo tabelë ruan bashkitë për adresat
4
PSK_Dokumenta
Kjo tabelë ruan dokumentet e ngarkuara gjate procesimit të pasurive
5
PSK_Dokumenta_Aplikimi_per_qera
Kjo tabelë ruan dokumentet e ngarkuara gjate aplikimit për qira dhe kontratën e qiramarrjes në fund
6
PSK_Dokumenta_pasurie
Kjo tabelë ruan lidhjet e dokumenteve me pasuritë
7
PSK_Emaili
Në këtë tabelë ruhen emailet e përdoruesve et sistemit
8
PSK_Institucionet
Kjo tabelë ruan emrat e institucioneve nga vijnë dokumentet (si gjykata etj.)
9
PSK_Lidhje_kontrate_qera
Kjo tabelë do të ruajë të dhënat e kontratave për qira
10
PSK_Lloj_dokumenti
Kjo tabelë ruan llojet e dokumenteve
11
PSK_Lloj_dokumenti_Status_pasurie
Kjo tabelë ruan lidhjen e dokumenteve të ngarkuara me pasuritë përkatëse
12
PSK_Lloj_llogarie
Kjo tabelë ruan llojet e llogarive monetare
13
PSK_Lloj_pasurie
Kjo tabelë ruan llojet e pasurive
14
PSK_Lloj_shpenzimi_Te_ardhure
Kjo tabelë ruan llojet e shpenzimeve dhe të ardhurave
15
PSK_Njesi_Administrative
Kjo tabelë shërben për ruajtjen e njësive administrative
16
PSK_Njesi_matese
Kjo tabelë ruan njësitë matëse
17
PSK_Njesi_matese_Lloj_pasurie
Kjo tabelë ruan lidhjen e njësive me llojet e pasurive
18
PSK_Organigrama
Tabelë që shërben për ruajtjen organigramës
19
PSK_Organigrama_Role
Kjo është një tabele lidhëse e organigramës me rolet. Shërben për të bërë lidhjen e pozicionit të organigramës me rolet përkatëse.
20
PSK_Pasuri_Lloj_llogarie
Kjo tabelë ruan lidhjen e pasurisë me llojin e llogarisë. Do ruhet gjithë historiku. Duke pasur aktiv do kuptohet kush është lloji aktual i pasurisë (bëhet fjale për llogarite monetare)
21
PSK_Pasuri_Status_pasurie
Kjo tabelë ruan lidhjen e pasurisë me statusin e pasurisë
22
PSK_Pasuri_Status_qeraje
Kjo tabelë ruan lidhjen e pasurisë me statusin e qirasë
23
PSK_Pasurite
Kjo tabelë ruan të dhënat e pasurive
24
PSK_Përdorues
Në këtë tabelë ruhen përdoruesit e sistemit
25
PSK_Përdorues_Adresa
Kjo tabelë ruan lidhjen e personave ose pasurive me adresat
26
PSK_Përdorues_Organigrama
Kjo tabelë ruan lidhjen e përdoruesve me organigramën
27
PSK_Përdorues_Pyetje
Kjo tabelë shërben si lidhëse midis përdoruesve dhe pyetjeve të sigurisë.
28
PSK_Person
Kjo tabelë ruan të dhënat e personave dhe subjekteve
29
PSK_Person_Kontakti
Kjo tabelë ruan personat e kontaktit
30
PSK_Prefekture
Kjo tabelë ruan prefekturat
31
PSK_Pyetje
Kjo tabelë ruan pyetjet
32
PSK_Qarku
Kjo tabelë ruan qarqet
33
PSK_Role
Kjo tabelë ruan rolet
34
PSK_Rruga
Kjo tabelë ruan rrugët
35
PSK_Shpezime_Te_ardhura_Pasurie
Kjo tabelë ruan shpenzimet dhe të ardhurat e pasurive
36
PSK_Shteti
Kjo tabelë ruan shtetet
37
PSK_Status_pasurie
Kjo tabelë ruan statuset e pasurive
38
PSK_Status_qeraje
Kjo tabelë ruan statuset e qirasë
39
PSK_Telefoni
Kjo tabelë ruan telefonat e personave
40
PSK_User_logs
Kjo tabelë ruan loget e userave
2.2 Ndërfaqet dhe modulet e sistemit
Modulet kryesore që ndërveprojnë në sistem janë:
- Moduli i login, profilit dhe sigurisë
Faqet
Funksionalitetet
Logim në sistem
- Logim në sistem i përdoruesve me username dhe fjalëkalim
- Logim në sistem i përdoruesve sipas rolit të tyre
- Logim në sistem pasi është vendosur kodi i Google authentication nëse është aktivizuar opsioni
- Login në sistem pasi është vendosur kodi i ardhur me email nëse është aktivizuar opsioni
- Login në sistem nëse është vendosur kodi i ardhur me sms, nëse është aktivizuar opsioni
- Mundësia e rimarrjes së llogarisë në rast kur është harruar fjalëkalimi në varësi të opsioneve të sigurisë së aktivizuara (Google auth, mail, nr. Cel dhe pyetjet e sigurisë)
Profili i përdoruesit
- Modifikimi i të dhënave personale të përdoruesit
- Modifikimi i të dhënave të llogarisë së përdoruesit (username; fjalëkalim)
- Editimi i adresave të përdoruesit
- Editimi i adresave të emailit të përdoruesit
- Editimi i numrave të celularit të përdoruesit
- Editimi i numrave të kontaktit të përdoruesit
Aktivizimi i opsioneve të sigurisë
- Aktivizimi i login me Google authenticator
- Aktivizimi i login nëpërmjet adresës së email-it
- Aktivizimi i login nëpërmjet numrit të celularit
- Aktivizimi i pyetjeve të sigurisë për rimarrjen e llogarisë në rast kur janë harruar kredencialet
- Moduli i konfigurimeve të administratorit
Faqet
Funksionalitetet
Konfigurimi i përdoruesve
- Shfaqja e listës së përdoruesve të sistemit
- Shfaqja e listës së përdoruesve sipas filtrave
- Shfaqja e organigramës që me të cilën do të lidhen përdoruesit
- Shtimi i një përdoruesi të ri në sistem
- Modifikimi i të dhënave të një përdoruesi në sistem
- Fshirja e një përdoruesi nga sistemi
- Lidhja e një përdoruesi me pozicionin në organigramë
Konfigurimi i organigramës
- Shfaqja e organigramës në sistem
- Shfaqja e pozicioneve të organigramës sipas filtrave
- Shfaqja e roleve me të cilët do të lidhet organigrama
- Shtimi i një elementi të ri në organigramë
- Modifikimi i të dhënave të një elementi në organigramë
- Fshirja e një elementi të një organigrame nga sistemi
- Lidhja e një organigrame me rolet
Konfigurimi i llojeve të dokumenteve
- Shfaqja e listës së llojeve të dokumenteve
- Shfaqja e listës së dokumenteve sipas filtrimit
- Shtimi i një lloji të ri dokumenti
- Modifikimi i të dhënave të dokumenteve
- Fshirja e llojeve të dokumenteve
- Pastrimi i fushave kur do të shtohet një dokument i ri
Konfigurimi i statuseve të pasurive
- Shfaqja e listës së statuseve të pasurisë
- Shfaqja e listës së statuseve të pasurisë sipas filtrimit
- Shtimi i një statusi të ri
- Modifikimi i të dhënave të një statusi
- Fshirja e statuseve
- Pastrim i fushave kur do të shtohet një status i ri
Konfigurimi i lidhjes së statuseve me llojet e dokumenteve
- Shfaqja e listës së statuseve për të cilat do të caktohen dokumentet
- Shfaqja e listës së dokumenteve që do të lidhen me statuset e pasurive
- Caktimi i një ose me shume dokumentesh për status
- Caktimi nëse dokumentet janë të detyrueshëm apo opsionale për një status
- Heqja e llojeve të dokumenteve nga një status
Konfigurimi i llojeve të shpenzimeve dhe të ardhurave
- Shfaqja e listës së llojeve të shpenzimeve dhe të ardhurave
- Shfaqja e llojeve të shpenzimeve/ardhurave sipas filtrimit
- Shtimi i një lloji shpenzimi të ri
- Shtimi i një lloji të ardhure të re
- Modifikimi i të dhënave të një shpenzimi
- Modifikimi i të dhënave për llojet e të ardhurave
- Fshirja e një lloji shpenzimi
- Fshirja e një lloji të ardhure
- Pastrim i fushave për shtimin e një të ardhure/shpenzimi të ri
Konfigurimi i gjykatave
- Shfaqja e listës së gjykatave
- Filtrimi i gjykatave
- Shtimi i një gjykate të re
- Modifikimi i të dhënave të një gjykate
- Fshirja e një gjykate
- Pastrimi i fushave për shtimin e një gjykate të re
Konfigurimi i njësive matëse (në varësi të llojit të pasurisë)
- Shfaqja e listës së njësive matëse në varësi të llojit të pasurive
- Shtimi i një njësie matëse të re
- Modifikimi i të dhënave të njësisë matëse
- Fshirja e një njësie matëse
- Pastrimi i fushave për shtimin e një njësie matëse të re
Konfigurimi i llojit të llogarisë
- Shfaqja e listës së llojeve të llogarive
- Shtimi i një lloji llogarie të re
- Modifikimi i të dhënave të një lloji llogarie
- Fshirja e një lloji llogarie
- Pastrimi i fushave për llojin e llogarive
- Moduli i regjistrimit të pasurive të sekuestruara dhe të konfiskuara
Faqet
- Funksionalitetet
Login në sistem
- Login me kredencialet e përdoruesve në sistem
Regjistrimi i pasurive
- Regjistrimi i të dhënave të vendimit gjyqësor për pasuritë e sekuestruara
- Regjistrimi i të dhënave të pasurive të paluajtshme të sekuestruara dhe të konfiskuara
- Regjistrimi i të dhënave të pasurive të luajtshme të sekuestruara dhe të konfiskuara
- Regjistrimi i pasurive monetare të sekuestruara dhe të konfiskuara
- Regjistrimi i të dhënave për bizneset e konfiskuara ose të sekuestruara
- Regjistrimi i të dhënave të pronareve (subjekteve/individëve) për këto pasuri
- Moduli i procesimit dhe menaxhimit të pasurive të sekuestruara dhe konfiskuara
Faqet
Funksionalitetet
Kryefaqja
- Shfaqja e të gjitha pasurive të regjistruara sipas statusit (sekuestruara, konfiskuara, revokuara etj.)
- Shfaqja e të gjitha pasurive sipas rolit të përdoruesit (administratorit të pasurisë i shfaqen vetëm pasuritë e tij)
- Shfaqja e të gjitha pasurive për të cilat nuk është caktuar një administrator (i shfaqen kryeadministratorit)
- Shfaqja e të gjitha pasurive të regjistruara sipas llojit të pasurisë
- Filtrimi i pasurive të sekuestruara dhe konfiskuara sipas pronareve, numrit dhe datës së vendimit, datës së marrjes në dorëzim.
- Renditja e pasurive sipas të dhënave që shfaqen në kryefaqe
Hapja e detajeve të pasurisë në momentin kur zgjidhet një pasuri
- Mundësia e zgjedhjes së pasurive pa administrator dhe caktimi i një administratori për këto pasuri
- Shfaqja e pasurive të cilat janë publikuar për t’u dhënë me qira
Detajet e pasurisë
- Shfaqja e llojit të pasurisë
- Shfaqja e vendimeve të marra për atë pasuri, si dhe dokumentet e ngarkuara për vendim (nëse ka)
- Shfaqja e datës së marrjes në dorëzim, vlerës së pasurisë dhe administratorit të pasurisë
- Shfaqja e pronarit (subjektit ose personit) të pasurisë
- Shfaqja e të dhënave të regjistruara për pasurinë në varësi të llojit të pasurisë
- Shfaqja e shpenzimeve dhe të ardhurave të realizuara për pasurinë
- Mundësia e shtimit të shpenzimeve dhe të ardhurave për pasuri
- Mundësia e shtimit të urdhrave gjyqësore për pasurinë
- Shfaqja e kontratave të realizuara për një pasuri, si dhe pagesat e kryera të qirasë të lidhura me kontratat
- Caktimi i datës së marrjes në dorëzim të pasurisë nga administratori
- Ndryshim i statusit të pasurisë
Faqja e menaxhimit të pasurive/aplikimeve me qira
- Shfaqja e të gjitha aplikimeve të realizuara për pasuritë e sekuestruara/konfiskuara që jepen me qira
- Mundësia e filtrimit të aplikimeve sipas pasurive, aplikantit, administratorit, llojit të pasurisë.
Faqja e shpenzimeve dhe të ardhurave për pasuri (mund të shfaqen shpenzimet/ardhurat për pasuri dhe t’i shtojë ato)
- Shfaqja e shpenzimeve të realizuara për një pasuri
- Shfaqja e të ardhurave të realizuara për një pasuri
- Shtimi i një shpenzimi të ri për pasuri
- Shtim i një të ardhure të re për pasuri
- Modifikimi i të dhënave për shpenzimet e realizuara nga pasuria
- Modifikim i të dhënave për të ardhurat e pasurisë
- Fshirja e një shpenzimi/të ardhure për pasuri
- Filtrimi i shpenzimeve dhe të ardhurave
Faqja e menaxhimit të urdhrave të ekzekutimit për pasuri
- Shfaqja e urdhrave të ekzekutimit të lëshuar për një pasuri
- Shtimi i urdhrave të ekzekutimit në lidhje me një pasuri
- Modifikimi i urdhrave të ekzekutimit për një pasuri
- Fshirja e një urdhri ekzekutimi për pasuri
- Moduli i raporteve të gjeneruara nga sistemi
Raport mbi loget e përdoruesve
- Shfaq listën e logeve të përdoruesve që janë loguar me sukses
- Shfaq listën e logeve të përdoruesve që nuk janë loguar me sukses
- Shfaq listën e logeve të daljes së përdoruesve nga sistemi
- Mundësi filtrimi sipas intervalit të datave, llojit të logeve dhe përdoruesve
Raport në lidhje me të dhënat e pronave të sekuestruara dhe të konfiskuara
- Shfaqja e listës së pronave të sekuestruara dhe të konfiskuara ku të shfaqen informacionet bazë të pronës, si: vendndodhja, sipërfaqja, vlera
- Shfaqja e listës së pronave të sekuestruara dhe konfiskuara sipas llojit të pasurisë
- Filtrimi i listës së pronave të sekuestruara dhe të konfiskuara sipas kritereve të kërkimit
Raport në lidhje me statusin e pronave të sekuestruara dhe të konfiskuara
- Shfaqja e listës së pronave të sekuestruara dhe të konfiskuara sipas statusit dhe vlerës
- Filtrimi i listës së pronave sipas kritereve të kërkimit
Raport mbi monitorimin e pronave të dhëna me qira
- Shfaqja e statistikave mbi pronat e sekuestruara/konfiskuara të dhëna me qira
- Shfaqja e statistikave mbi pronat e konfiskuara dhe të sekuestruara sipas statusit të qirasë
- Filtrimi i listës së pronave sipas kritereve të kërkimit
Raportet e të ardhurave dhe shpenzimeve
- Shfaqja e listës së të ardhurave dhe shpenzimeve për pronat e kërkuara
- Shfaqja e pronave me të ardhurat dhe shpenzimet totale të realizuara për pronë
- Filtrimi i të ardhurave dhe shpenzimeve të pronave sipas kritereve të kërkimit
