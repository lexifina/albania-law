# Shtojca
SHTOJCA I
FORMATI I ETIKETËS
(Në zbatim të neneve 12, 15 dhe 16)
1. Emri i markës/kompanisë:
Shembull: ALFA sh.p.k.
2. Logoja (nëse ka):
Vendoset sipër ose në cep në të majtë.
3. Numri serik unik (për çdo produkt):
Shembull: SN: 001294837B
4. QR code/Barcode
Lidhet me sistemin e verifikimit online ose informacion shtesë rreth produktit.
5. Vendi i prodhimit/data e prodhimit:
Shembull: Made in Albania - 06.2025
6. Simbol i sigurisë (opsional):
P.sh., hologramë, ngjyrë UV ose dizajn antikopjim.
7. Forma dhe madhësia e etiketës:
Rrethore (p.sh., 3 cm diametër);
Drejtkëndore (p.sh., 4 cm x 2 cm).
Shembull vizual i përshkrimit të një etikete/pulle (tekstualisht)
+--------------------------------+
| ALFA sh.p.k. |
| [Logoja këtu] |
| SN: 001294837B |
| QR code ▓▓▓▓▓▓▓ |
| Made in Albania - 06.2025 |
| Origjinalitet i garantuar |
SHTOJCA II
KODI UNIK ALFANUMERIK PËR ARMË
(Në zbatim të neneve 13 dhe 15)
AL25-AR15-003581
(AL = Shqipëri, 2025, AR15 = lloji i armës, numër unik serial)
1. Numër serial, që ndjek një format të strukturuar:
AL24-AR15-003581
- Ky format analizohet, si më poshtë:
i. AL - Shqipëria (kodi i vendit);
ii. 24 - Viti 2025;
iii. AR15 - Lloji i armës (AR-15, një armë gjysmautomatike);
iv. 003581 - Numri unik serial i armës (numër rendor).
2. Renditja e numri unik serial i armës:
Numri 003581 është një numër rendor serial dhe zakonisht renditet sipas një sistemi inkremental, domethënë që rritet një nga një me çdo njësi të re të regjistruar.
3. Formatimi:
Është një numër me 6 shifra.
Shifrat e para (zero) janë mbushëse për të ruajtur gjatësi fikse (në këtë rast: 6).
P.sh., Pas 003581 vjen 003582, pastaj 003583 e kështu me radhë.
4. Rritja inkrementale:
Numri rritet me +1 për çdo njësi të re të regjistruar të të njëjtit lloj (AR15 në këtë rast).
Nëse arma tjetër është e tipit AR15 dhe është regjistruar pas kësaj, ajo do të ketë numrin 003582.
5. Renditja në kontekst më të gjerë:
Numri është unik brenda kategorisë së armës dhe vitit.
Pra, AL24-AR15-003581 është arma e 3581-të e tipit AR15 e regjistruar në Shqipëri në vitin 2024.
Një armë e tipit tjetër, p.sh., AK47, do ketë një numër tjetër serial të ndarë, si p.sh., AL24-AK47-000142.
Shembuj të renditjes:
Numri serial i plotë
Renditja
AL24-AR15-000001
1
AL24-AR15-000002
2
...
...
AL24-AR15-003581
3,581
AL24-AR15-003582
3,582
6. Sistem automatik për gjenerimin e numrit serial në Excel.
Krijimi i një kodi serial të plotë me formatin:
AL (viti)-(lloji_armës) - (numri_serial_me_6_shifra)
A
B
C
D
Vendi
Viti
Lloji i armës
Numri serial i plotë
AL
2024
AR15
(formulë që gjenerohet)
Shto formulën në kolonën D (Numri serial i plotë): Në rreshtin e parë (rreshti 2), vendos këtë formulë në kolonën D:
=A2 & TEXT(B2, “00”) & “-” & C2 & “-” & TEXT (COUNTIFS (B$2: B2, B2, C$2:C2, C2), “000000”)
- Si funksionon kjo formulë?
A2 - Vendi (p.sh., AL)
TEXT(B2, “00”) - Shfaq vitin me dy shifra (p.sh., 2024 → 24)
C2 - Lloji i armës (p.sh., AR15)
COUNTIFS (B$2: B2, B2, C$2:C2, C2) - Numëron sa herë është përdorur ajo armë në atë vit deri në atë rresht (p.sh., 1 për të parën, 2 për të dytën etj.)
TEXT (..., “000000”) - E shfaq numrin rendor me 6 shifra (p.sh., 000001)
Shembull:
A
B
C
D
AL
2024
AR15
AL24-AR15-000001
AL
2024
AR15
AL24-AR15-000002
AL
2024
AK47
AL24-AK47-000001
AL
2025
AR15
AL25-AR15-000001
MK22-G19-000847
(MK = Maqedoni e Veriut, Glock 19, numër unik)
IT25-762NATO-00592
(Itali 2025, kalibër 7.62 NATO, numër serial)
Shembuj për municion:
AL24-9MM-1000BX-A58Z
(Shqipëri, 2024, municion 9 mm, pako me 1000 fishekë, kod unik A58Z)
US23-556-LOT2847-K3R2
(SHBA, 5.56 mm, lote prodhimi, kod unik)
SHTOJCA III
(Në zbatim të neneve 19 dhe 20)
Për kontejnerët, që transportohen me anije, përdoren disa lloje markimesh standarde për të treguar informacion të rëndësishëm rreth përmbajtjes, trajtimit dhe destinacionit të tyre. Këto markime janë të përcaktuara në standardet ndërkombëtare të publikuara nga organizata ndërkombëtare, si: ISO (International Organization for Standardization) dhe IMDG (International Maritime Dangerous Goods Code) dhe më të rëndësishmet për transportin detar janë:
1. Markimi ISO 6346 (Kodi i kontejnerit)
- Ky është një kod standard ndërkombëtar, që përfshin:
i. Kodi i pronarit (p.sh. MSCU për MSC);
ii. Kodi i llojit të kontejnerit;
iii. Numri serial i kontejnerit;
iv. Shifra kontrolli;
v. Ky markim përdoret për identifikimin dhe gjurmimin e kontejnerëve;
vi. Standardi ISO 6346 “Kontejnerët e mallrave - Kodimi, identifikimi dhe shënjimi/markimi” është një standard ndërkombëtar i përcaktuar nga International Organization for Standardization (ISO) i adoptuar dhe i publikuar si standard shqiptar (SSH ISO 6346) për identifikimin e kontejnerëve të ngarkesave të përdorura në transportin ndërkombëtar.
- Struktura e Kodit ISO 6346
- Kodi përbëhet nga 11 karaktere alfanumerike të ndara në pjesë, si më poshtë:
XXXX U 1234567
a) Kodi i pronarit (Owner code) - 3 shkronja
- Tregon kompaninë që zotëron kontejnerin.
- P.sh., “MSCU” për Mediterranean Shipping Company (MSC).
b) Shenja e pajisjes (Equipment category identifier) - 1 shkronjë
- “U” për kontejnerë të mallrave të përgjithshme;
- “J” për pajisje të bashkëngjitura;
- “Z” për rimorkio dhe trailera.
c) Numri serial (Serial number) - 6 shifra
- Numri serial (Serial number) është një numër 6-shifror që përdoret për identifikimin unik të një kontejneri brenda një kompanie pronare. Ky numër është i veçantë për çdo kontejner dhe shërben për qëllime gjurmimi, menaxhimi dhe dokumentimi të kontejnerëve në sistemin e brendshëm të kompanisë.
- Shembuj të numrave serialë:
i. 000123;
ii. 102478;
iii. 999999.
- Ky numër nuk duhet të përsëritet për më shumë se një kontejner brenda së njëjtës kompani pronare.
2. Kodi i madhësisë dhe llojit
Dy shkronja/numra specifikojnë gjatësinë, lartësinë dhe llojin e kontejnerit (p.sh. për qëllim të përgjithshëm).
Shembull: 22G1
22 = madhësia (lartësi standarde)
G1 = lloji
3. Shenjat operative
a) Tregues të peshës maksimale bruto, të ngarkesës së dobishme dhe peshës së vetë mjetit, të pajisjes ose të kontejnerit bosh.
b) Mund të përfshihen edhe udhëzime ose paralajmërime për trajtimin.
4. Kodi i vendit (opsional)
Bazuar në ISO 3166, ai tregon vendin ku kontejneri është i regjistruar ose operon.
5. Shifra e kontrollit (Check digit) - 1 shifër
- Përdoret për të verifikuar vlefshmërinë e kodit;
- Llogaritet nëpërmjet një formule matematikore të caktuar.
Shembull i plotë:
- MSCU 123456 5
- MSC - Kodi i pronarit (Mediterranean Shipping Company)
- U - Kontejner standard ngarkese
- 123456 - Numër unik serial
- 5 - Shifra e kontrollit
- Markime të tjera operative dhe të trajtimit:
a) “This Side Up” - për të treguar orientimin korrekt;
b) “Do Not Stack” - nuk duhet vendosur një kontejner tjetër sipër;
c) Pesha bruto e kontejnerit (VGM - Verified Gross Mass) - e detyrueshme sipas SOLAS-it.
- Markime të destinacionit
- Emërtimi i portit të destinacionit ose kodet e stacionit për sistemin logjistik.
- Etiketa për ngarkesë speciale
Kjo etiketë vendoset mbi kontejnerë, pajisje ose pako, që përmbajnë ngarkesa, që kërkojnë trajtim të veçantë, për shkak të rrezikut, të natyrës së brishtë, të kufizimeve të temperaturës ose të kushteve të transportit.
Etiketa për ngarkesë speciale tregon:
- llojin e rrezikut;
- kufizimet e trajtimit;
- kërkesa të posaçme të temperaturës;
- simbolet standarde ndërkombëtare për ngarkesa të rrezikshme sipas ADR/IMDG/ISO.
Mallrat ndahen në 9 klasa kryesore bazuar në llojin e rrezikut që paraqesin:
Klasa
Përshkrimi
1.
Eksplozivë (p.sh., fishekzjarrë, dinamit)
2.
Gaze (të ndezshme, të pandezshme, toksike)
3.
Lëngje të ndezshme (p.sh., benzina, alkooli)
4.
Substanca të ngurta të ndezshme dhe të vetëreaktive
5.
Substanca oksiduese dhe perokside organike
6.
Substanca toksike dhe infektuese
7.
Materiale radioaktive
8.
Substanca gërryese (acidë, baza të forta)
9.
Substanca të tjera të rrezikshme (p.sh., lëndë që rrezikojnë mjedisin detar)
SHTOJCA IV
(Në zbatim të neneve 21, 22 dhe 23)
1. Kodi unik i lotit
Kodi i lotit për uniformat paraqitet në format alfanumerik të strukturuar dhe përbëhet nga:
- kodi i prodhuesit;
- data e prodhimit;
- numri progresiv i lotit;
Shembull:
ALB01-160426-L02
2. Struktura e kodit të lotit
Kodi i lotit paraqitet sipas strukturës së mëposhtme:
ALB01-160426-L02
Ku:
- ALB01 - Kodi i prodhuesit;
- 160426 - Data e prodhimit (DDMMYY);
- L02 - Numri i lotit;
3. Shembull ilustrues i etiketës
+----------------------------+ | PRODHUESI: ALB01 |
| LOT: ALB01-160426-L02 |
| PROD: 16.04.2026 |
| MADE IN ALBANIA |
| ▓▓ QR CODE ▓▓ |
+----------------------------+
