# Shtojca
PËRMBAJTJA
1. PËRSHKRIMI I STANDARDEVE
2. HYRJE
2.1. Qëllimi 2
2.2. Detyrimet ligjore
2.3. Fusha e veprimit
3. Të dhënat dhe sistemet që do të përfshihen në GIS-in Kombëtar
4. GIS-i KOMBËTAR
4.1. Moduli i hartës
4.2. Moduli i editimit
4.3. Moduli i metadatës
4.4. Moduli i shërbimeve të rrjetit
4.5. Moduli i arkivimit
4.6. Moduli i konformitetit
4.7. Aneks 1- Shërbimet e rrjetit
4.7.1. Shërbimi i zbulimit
4.7.2. Shërbimi i shikimit
4.7.3. Shërbimi i shkarkimit
4.7.4. Shërbimi i transformimit
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standardet që duhet të plotësojë informacioni gjeohapësinor për t’u bërë pjesë e GIS-it Kombëtar.
Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG).
Data e publikimit të versionit nr. 1 është Maj 2023. Emërtimi i dokumentit është ASIG_Standard_NSDI_2022_ GK_v.1, ku:
ASIG - autoriteti përgjegjës për krijimin e standardit
Standard - lloji i dokumentit
NSDI - qëllimi i dokumentit
2023 - viti i krijimit
GK - GIS-i Kombëtar
v.1 - numri i versionit të standardit
2. HYRJE
2.1. QËLLIMI
Qëllimi i këtij dokumenti është përcaktimi i specifikimeve teknike, të sistemit Kombëtar të Informacionit Gjeohapësinor (GIS-i Kombëtar), i cili përfshin të dhënat, sistemet tematike të informacionit gjeografik, dhe shërbimet e informacionit gjeografik, që ndërtohen në përputhje me standardet ndërkombëtare të fushës së gjeoinformacionit.
Krijimi i GIS-it Kombëtar është përcaktuar në nenin 16, pika 2, të ligjit nr. 72/2012, “Për Organizimin dhe Funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI-së në Shqipëri, për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe e shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë midis tyre.
2.2. DETYRIMET LIGJORE
Në bazë të nenit 16, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG është institucioni përgjegjës për krijimin e standardeve, duke përfshirë edhe standardin e GIS-it Kombëtar, në përputhje me standardet ndërkombëtare të fushës së gjeoinformacionit.
Standardet (Rregullat e Implementimit - IR) do të zbatohen për fushat e mëposhtme:
- Procedura - Përfshirja e të dhënave dhe shërbimeve gjeohapësinore në GIS-in Kombëtar, do të realizohet sipas rregullave të miratuara me vendimin e Këshillit të Ministrave nr. 451, datë 3.7.2019, “Për rregullat uniforme të Infrastrukturës së Informacionit Gjeohapësinor”.
- Metadata - Elementet e metadatës së të dhënave dhe shërbimeve gjeohapësinore, që do të përfshihen në GIS-in Kombëtar, përcaktohen në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
- Sistemi referues gjeodezik - Referenca gjeodezike e të dhënave gjeohapësinore, që do të përfshihen në GIS-in Kombëtar, mbështetet në Kornizën Referuese Gjeodezike Shqiptare (KRGJSH), e miratuar me vendimin e Këshillit të Ministrave nr. 669, datë 7.8.2013, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si Metadatë”, i ndryshuar.
- Ndërveprueshmëria e të dhënave - Të dhënat dhe shërbimet gjeohapësinore që do të përfshihen në GIS-in Kombëtar, do të jenë në përputhje me rregullat e ndërveprueshmërisë, të miratuara me vendimin e Këshillit të Ministrave, nr. 38, datë 18.1.2017, “Për miratimin e Rregullave të Ndërveprueshmërisës të Dhënave, Grupeve të të Dhënave dhe Shërbimeve Gjeohapësinore”.
- Shkëmbimi i të dhënave - Shkëmbimi i të dhënave, që do të përfshihen në GIS-in Kombëtar, do të realizohet nëpërmjet shërbimeve të rrjetit, sipas modulit të shtjelluar në këtë dokument, dhe rregullave të miratuara me vendimin e Këshillit të Ministrave nr. 399, datë 19.6.2019, “Rregullat për Shkëmbimin e Grupeve dhe të Shërbimeve të të Dhënave Gjeohapësinore mes Autoriteteve Publike”.
2.3. FUSHA E VEPRIMIT
Të gjitha autoritetet publike, kompanitë private apo individët që mbajnë, përpunojnë apo përditësojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE për informacionin gjeohapësinor kalon proceset dhe ciklin jetësor, si më poshtë:
Figura 1: Proceset e ciklit jetësor
“Ardhja e së dhënës” është depozitimi i të dhënave nga autoritetet publike përgjegjëse sipas Standardeve Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri. Përditësimi është procesi sipas të cilit autoriteti publik përgjegjës realizon shtimin, modifikimin ose fshirjen e të dhënave gjeohapësinore të cilat janë të publikuara.
“Kontrolli” është kontrolli teknik i s dhënës/shërbimeve të informacionit gjeohapësinor, të vëna në dispozicion nga autoritetet publike përgjegjëse, për miratimin/refuzimin e përfshirjes së tyre në GIS-in Kombëtar.
“Publikimi” është procesi me anë të cilit e dhëna e miratuar për përfshirje në GIS-in Kombëtar publikohet në Gjeoportalin Kombëtar.
“Arkivimi” është procesi gjatë të cilit grupet e të dhënave, të ardhura nga autoritetet publike përgjegjëse, të cilat kanë një kohëzgjatje të caktuar historike, ruhen për të qenë në dispozicion dhe të aksesueshme nga autoritetet publike.
3. TË DHËNAT DHE SISTEMET QË DO TË PËRFSHIHEN NË GIS-in KOMBËTAR
Të dhënat dhe sistemet e informacionit gjeohapësinor, që do të do të përfshihen në GIS-in Kombëtar, do të respektojnë kërkesat e këtij standardi, si dhe kërkesat specifike të standardeve tematike, për të gjitha temat e parashikuara sipas pikës 2, të nenit 11, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”.
Të dhënat do të mblidhen, përpunohen, përditësohen dhe vihen në dispozicion të publikut, në përputhje me standardet e miratuara për specifikimet teknike të informacionit gjeohapësinor në Shqipëri, për temat e mëposhtme.
1. Përcaktimi i kornizës referuese gjeodezike dhe kontrolli gjeodezik;
2. Sistemet e rrjeteve gjeografike;
3. Emërtimet gjeografike;
4. Imazhi i hartës bazë;
5. Kufijtë e njësive administrative;
6. Sistemi i adresave;
7. Parcelat kadastrale;
8. Rrjetet e transportit;
9. Hidrografia;
10. Zonat e mbrojtura;
11. Modeli digjital i terrenit;
12. Mbulesa e tokës;
13. Ortoimazheria;
14. Gjeologjia;
15. Njësitë statistikore;
16. Ndërtesat;
17. Pedologjia;
18. Përdorimi i tokës;
19. Shëndeti i njerëzve dhe siguria e tij;
20. Infrastruktura urbane dhe shërbimet qeveritare;
21. Infrastruktura për monitorimin e mjedisit;
22. Infrastruktura industriale;
23. Infrastruktura bujqësore dhe akuakultura;
24. Demografia;
25. Zonat me përdorim të kufizuar;
26. Zonat me rreziqe natyrore;
27. Kushtet atmosferike
28. Meteorologjia;
29. Hidrologjia;
30. Detet;
31. Zonat ekologjike;
32. Habitatet;
33. Shpërndarja e specieve;
34. Burimet energjetike;
35. Burimet minerale.
Specifikimet teknike të të dhënave të standardeve të kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. Standardet Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri kanë përcaktuar disa atribute bazë, duke u bazuar në direktivën INSPIRE të BE-së, të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Autoritetet publike përgjegjëse, në zbatim të legjislacionit sektorial ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga autoriteti publik përgjegjës.
Figura 2. Skema e përgjithshme për përfshirjen e të dhënave dhe sistemeve në GIS-in Kombëtar
4. GIS-i KOMBËTAR
“GIS-i Kombëtar” është Sistemi Kombëtar i Informacionit Gjeohapësinor, i cili përfshin të gjitha të dhënat dhe sistemet e informacionit gjeografik që ndërtohen për tema të veçanta, në përputhje me standardet e miratuara, që ndërveprojnë me njëri-tjetrin dhe që integrohen nga ASIG-u.
Sistemi i informacionit gjeografik (GIS) është sistemi që mbledh, ruan, analizon, përpunon dhe paraqet të dhëna që lidhen me një fenomen natyror apo shoqëror, gjeoreferencimi i të cilit mundësohet nga një sistem referues koordinativ i përbashkët. Këto sisteme janë një mënyrë teknologjike e të kuptuarit të gjeoinformacionit dhe të marrjes së vendimeve inteligjente. Përdorimi i sistemeve të informacionit gjeografik (GIS) në dekadat e fundit ka marrë një rëndësi gjithnjë e më të madhe. GIS-i gjen përdorim të gjithanshëm në shumë fusha, veçanërisht në krijimin e bazës së të dhënave gjeohapësinore, ku bëhet i mundur menaxhimi i të dhënave gjeohapësinore ndërmjet tematikave të ndryshme.
Autoritet publike përdorin sistemet e informacionit gjeografik (GIS) për të pasur një menaxhim më të mirë të bazave të të dhënave, por edhe për të vlerësuar rezultatet e politikave që ndërmarrin. Në GIS, autoritetet publike integrojnë lloje të ndryshme të dhënash për të kuptuar, për të funksionalizuar zgjidhjet, për të komunikuar njohuri dhe për të angazhuar palët e interesuara duke përfshirë edhe publikun. Përdorimi i GIS-it përfshin inteligjencën e vendndodhjes në vendimmarrje të nivelit të lartë, ofron njohuri të fuqishme mbi çështjet kritike me të cilat përballet kombi dhe mbështet politikëbërjen e bazuar në shkencë dhe në analizë.
Sistemi i Informacionit Gjeografik (GIS) integron pesë komponentë kyç:
- Harduer - përfshin pajisjet fizike mbi të cilat funksionon një Sistem i Informacionit Gjeografik, i cili është i pajisur me një gamë të gjerë të llojeve të infrastrukturës harduareike.
- Softuer - ofron funksione dhe mjete të nevojshme për të ruajtur, analizuar dhe për të shfaqur informacionin gjeohapësinor.
- Informacion gjeohapësinor - janë metadatat, të dhënat dhe grupet e të dhënave gjeohapësinore, që lidhen me një fenomen çfarëdo të realitetit, gjeoreferencimi i të cilit mundësohet nga një sistem hapësinor koordinativ i përbashkët.
- Ekspertët GIS - janë specialistët, teknikët që projektojnë dhe mirëmbajnë sistemin deri tek ata që e përdorin për të kryer punën e tyre në përditshmëri, të cilët merren me menaxhimin dhe zbatimin e planeve për zgjidhjen e problemeve në botën reale.
- Metodologjia - është funksionimi sipas një plani të mirëprojektuar dhe rregullave të cilat janë modele dhe praktika operative unike për çdo autoritet.
Sistemi i GIS-it Kombëtar mundëson ndërveprueshmërinë midis të dhënave dhe shërbimeve gjeohapësinore (specifikimet teknike për ndërveprueshmërinë, harmonizimin e grupeve të të dhënave gjeohapësinore dhe shërbimet e të dhënave gjeohapësinore etj.), bazuar në Standardet Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri, të miratuara me VKM-të përkatëse.
Krijimi i GIS-it Kombëtar nuk synon vetëm një sistem GIS/TIK që siguron shkëmbimin e gjeoinformacionit ndërmjet institucioneve, por një sistem të nivelit të lartë që përfshin një seri rregullash dhe procedurash administrative, standardesh dhe specifikimesh teknike të detyrueshme për autoritetet publike përgjegjëse. Kjo do të sigurojë që nivelet e ndryshme të përdoruesve (autoritete publike qendrore dhe lokale, sektori privat dhe qytetarët) të kenë informacion të disponueshëm, lehtësisht të aksesueshëm, efektiv, dhe të përditësuar.
Modulet përbërëse të GIS-it Kombëtar janë:
1. Moduli i hartës;
2. Moduli i editimit;
3. Moduli i metadatave;
4. Moduli i shërbimeve të rrjetit;
5. Moduli i arkivimit;
6. Moduli i konformitetit.
4.1. MODULI I HARTËS
Moduli i hartës konsiston në ofrimin e shërbimeve të shikimit për të dhënat gjeohapësinore dhe bën të mundur aksesimin e funksionaliteteve të ndryshme në funksion të të dhënave, për analizimin, përditësimin, dizenjimin, menaxhimin dhe shfaqjen interaktive të informacionit gjeohapësinor.
Funksionalitet bazë që duhet të ofrojë moduli i hartës janë:
1. Identifikimi - ky funksionalitet mundëson identifikimin e objekteve nga të gjitha shtresat e dukshme në hartë.
2. Selektimi i thjeshtë dhe hapësinor i të dhënave gjeohapësinore - ky funksionalitet mundëson të selektoni një objekt në hartë.
3. Marrja e koordinatave në hartë - ky funksionalitet jep mundësinë të marrësh koordinatat e një pike, duke klikuar në hartë dhe zmadhimin me koordinata në një pikë të caktuar në hartë.
4. Matja e gjatësisë dhe sipërfaqes - funksionaliteti i matjes së gjatësive dhe i sipërfaqes në hartë.
5. Vizatimi i një pike, poligoni, pikë me koordinata, vendosja e një shënimi - me këtë funksionalitet mund të vizatoni lloje të ndryshme të objekteve të gjeometrisë në hartë.
6. Lidhja me hartën “Permalink” - ky funksionalitet përdoret për të krijuar lidhjen me pamjen aktuale të hartës, ku mund të kopjohet dhe të ndahet lidhja me kodin QR me përdoruesit e tjerë.
7. Hedhja e një shërbimi të jashtëm - ky funksionalitet mundëson shtimin e shtresave të jashtme WMS/WFS/WMTS në hartë.
8. Kërkimi i avancuar dhe i thjeshtë - ky funksionalitet lejon të specifikoni parametrat e kërkimit të thjeshtë dhe të avancuar.
9. Ngarkimi i një layer-i të ri në Map Viewer me drag & drop - ky funksionalitet mundëson krijimin ose ndryshimin e një shtrese të përkohshme në ambientin e punës së përdoruesve.
10. Zoom sipas koordinatave - ky funksionalitet mundëson zmadhimin me koordinata ose të tregoni koordinatat e një pike të caktuar, të zgjedhur.
11. Pamja 3-dimensionale - ky funksionalitet mundëson paraqitjen 3-dimensionale të hartës, e ngjashme me shikimin e hartës në realitet.
12. Mjetet e navigimit - harta përmbledhëse, pamje e plotë, zmadho, zmadho me drejtkëndësh, zvogëlo, pamje e mëparshme, pamja pasardhëse, rrjeti koordinativ etj.
13. Shkarkimi - shkarkimi i të dhënave gjeohapësinore në zonën e kërkuar.
14. Printimi - ky funksionalitet mundëson ruajtjen e një zone të zgjedhur të hartës në formën e një formati PDF, PNG ose JPEG.
15. Gjeoreferimi - funksionaliteti që mundëson ngarkimin dhe gjeoreferencimin e imazheve në hartë.
4.2. MODULI I EDITIMIT
Qëllimi i këtij moduli është të mundësojë një mjedis më shumë përdorues dhe të sigurojë mbështetje për krijimin, editimin dhe shkarkimin e shtresave. Çdo përdorues nga autoritetet publike do të ketë mundësi të editojë dhe të modifikojë shtresa të përcaktuara. Këto shtresa të përcaktuara do të krijohen dhe do të strukturohen sipas Standardeve Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri. Kjo strukturë do t’i mundësojë editorit të GIS-it Kombëtar të menaxhojë vërtetësinë e të dhënave hyrëse në kohë reale. Për çdo institucion do të ketë një set shtresash të përcaktuara të cilat janë pjesë e Standardeve Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri dhe çdo autoritet publik përgjegjës do të ketë akses të editojë vetëm shtresat që ka në përgjegjësi.
Moduli i editimit do të mbështetet në funksionalitet e modulit të hartës dhe aksesi i tij do të kryhet nëpërmjet regjistrimit të përdoruesve GOV.
Moduli i editimit do të përmbushë nevojat e përdoruesve, autoritete publike përgjegjës për mbledhjen, përpunimin dhe përditësimin e të dhënave gjeohapësinore. Ky modul do të lehtësojë detyrat dhe proceset e mirëmbajtjes dhe të menaxhimit të informacionit gjeohapësinor, në mënyrë që të sigurojë ndërveprueshmërinë e grupeve të të dhënave sipas Standardeve Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri.
Funksionalitet bazë që duhet të ofrojë moduli i editimit:
1. Modifikimin e veçorive të gjeometrisë (pikë, vijë, poligon);
2. Funksionalitetin e veçorive të lidhjes së vertekseve gjeometrike ndërmjet tipologjive (pikë, vijë, poligon), snapping;
3. Krijimin e atributeve të kërkuara për veçoritë e shtuara dhe modifikimin e veçorive ekzistuese me të dhëna të editueshme të shtresave.
4. Krijimin e kodlistave të përcaktuara më parë për fushat e atributeve në mënyrë që të lehtësohet shpejtësia e futjes së të dhënave, si dhe krijimin e shtresave me modelin e të dhënave të paracaktuara sipas Standardeve Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri.
5. Zbatimin e rregullave topologjike në krijimin e shtresave.
4.3. MODULI I METADATËS
Moduli i metadatës është një katalog, i cili mundëson informacion të detajuar për të dhënat, grupet e të dhënave dhe shërbimet gjeohapësinore, që do të përfshihen në GIS-in Kombëtar. Ky modul do të mundësojë zbulimin, inventarizimin dhe përdorimin e të dhënave, grupeve të të dhënave gjeohapësinore, apo shërbimeve që lidhen me to. Metadatat që do të përfshihen në katalog, do të kenë një profil unik dhe do të sigurojnë informacion të detajuar mbi të dhënat, burimet e të dhënave, prejardhjen e tyre etj., për një përdorim sa më efektiv të të dhënave.
Përmbajtja, mënyra e plotësimit, përditësimi dhe mirëmbajtja e metadatës realizohen në përputhje me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”, dhe “Udhëzuesin teknik të detajuar mbi profilin e metadatave për krijuesit dhe përdoruesit”, të hartuar nga ASIG.
4.4. MODULI I SHËRBIMEVE TË RRJETIT
Qëllimi i modulit të shërbimeve të rrjetit është të specifikojë karakteristikat dhe standardet e shërbimeve të rrjetit, që do të aplikohen nga GIS-i Kombëtar dhe sistemet tematike të informacionit gjeografik, në përputhje me kërkesat e përcaktuara në nenin 23 të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, dhe Standardet Shtetërore për Specifikimet Teknike të Informacionit Gjeohapësinor në Shqipëri, që ka përafruar ky ligj.
Shërbimet e rrjetit që do të ofrojë GIS-i Kombëtar janë:
1. Shërbimi i zbulimit,
2. Shërbimi i shikimit,
3. Shërbimi i shkarkimit,
4. Shërbimi i transformimit.
Shpjegimi i detajuar mbi shërbimet e rrjetit jepet në aneksin 1.
4.5. MODULI I ARKIVIMIT
Qëllimi i këtij moduli ka në fokus arkivimin e të dhënave gjeohapësinore, të ardhura nga autoritetet publike përgjegjëse, që kanë një kohëzgjatje të caktuar historike, të cilat duhen ruajtur për të qenë në dispozicion dhe të aksesueshme nga autoritetet publike.
Krijimi i një mjedisi të përshtatshëm për arkivimin e të dhënave gjeohapësinore ndihmon në shmangien e rrezikut të humbjes së të dhënave dhe ruajtjen e arkivit me nivele që mbështeten në kopje të shumta, të ruajtura në mënyrë diskrete në sistem. Gjithashtu, sistemi duhet të ofrojë një arkivim automatik të të dhënave gjeohapësinore.
Etapat e krijimit të një mjedisi për ruajtjen e të dhënave janë:
1. Krijimi i një zone arkivimi të fshehtë ku kopjet e të dhënave mund të ruhen dhe të menaxhohen pa u ndryshuar;
2. Krijimi i një hapësire ku të vendoset një kopje e të dhënave, e cila mund të jetë e aksesueshme nga autoritetet publike.
Të dyja (2) mjediset duhet të jenë në sisteme të izoluara ruajtje dhe të dhënat duhet të bëhen back up.
Qëllimi kryesor i arkivimit të të dhënave është të sigurojë akses të përshtatshëm dhe afatgjatë të të dhënave. Aksesimi i të dhënat për përdoruesit fundorë mundësohet nëpërmjet internetit dhe funksioneve të kërkimit, në mënyrë që përdoruesit të mund të gjejnë grupet e të dhënave gjeohapësinore që plotësojnë nevojat e tyre. Metadatat e të dhënave dhe grupeve të të dhënave gjeohapësinore, të arkivuara në sistemin e inventarit gjeohapësinor, mundësojnë informacion për përdoruesit mbi grupet e të dhënave gjeohapësinore të arkivuara dhe të zëvendësuara. Sistemi i arkivit duhet të ofrojë mjete ndihmëse për gjetjen e kontekstit të plotë dhe/ose metadatave të arkivuara, për të gjurmuar futjen dhe për të mbështetur ruajtjen e të dhënave. Mjetet ndihmëse dhe metadatat e arkivuara, duhet të ofrojnë një lidhje të drejtpërdrejtë me kontekstin e të dhënave, pavarësisht se ku ruhen, si ruhen apo si emërtohen.
4.6. MODULI I KONFORMITETIT
Autoritet publike përgjegjëse ngarkojnë të dhënat gjeohapësinore në modulin e konformitetit, fizikisht ose nëpërmjet shërbimeve të rrjetit.
Moduli i konformitetit realizon kontrollin teknik, të të dhënave/sistemeve të informacionit gjeohapësinor, të vëna në dispozicion nga autoritetet publike përgjegjëse për miratimin/refuzimin e përfshirjes së tyre në GIS-in Kombëtar.
Konformiteti do të realizohet për kontrollin e të dhënave dhe shërbimet e rrjetit, të informacionit gjeohapësinor, si më poshtë:
Kontrolli i konformitetit të të dhënës
Kontrolli
Përshkrimi
1
Kontrolli i sistemit koordinativ referencë
Ky proces realizohet duke kontrolluar çdo tipologji (featureType) të të dhënave që vijnë nëse e kanë të deklaruar sistemin koordinativ sipas sistemit KRGJSH - ETRS_1989_Albania_2010
2
Kontrolli i katalogut të tipologjive
Kjo fazë konsiston në kontrollin e strukturës së të dhënave gjeohapësinore dhe konformitetit të tyre kundrejt modelit të të dhënave të standardit. Ky kontroll ndahet në dy faza:
- Kontrolli i strukturës, emërtimeve dhe numrit të tipologjive (feature-ve).
- Kontrolli i strukturës, emërtimeve dhe numrit të atributeve të tipologjive.
3
Kontrolli i metadatës
Plotësimi i elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin e Këshillit të Ministrave nr. 1077, datë 23.12.2015, “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
4
Kontrolli i cilësisë së të dhënave
Cilësia e të dhënave realizohet dhe deklarohet nga ana e institucionit përkatës që depoziton informacionin gjeohapësinor. Ky kontroll konsiston në cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur për të vlerësuar dhe për të dokumentuar cilësinë e të dhënave për grupet që lidhen me të dhënat gjeohapësinore të secilës temë. Cilësia dhe saktësia e të dhënave deklarohet në metadatën e secilës shtresë.
Kontrolli i së dhënës konsiston në kontrollin e konformitetit të së dhënës siç është shpjeguar në hapat e mësipërm i cili realizohet nga ASIG (konkretisht pika 1, 2 dhe 3), si dhe në kontrollin e cilësisë dhe saktësisë së të dhënës e cila deklarohet në katalogun e metadatës nga autoriteti publik përgjegjës që krijon të dhënën, sipas udhëzuesit teknik të përgatitur nga ASIG-u.
ASIG-u harton dhe miraton udhëzuesin teknik për kontrollin e konformitetit brenda 3 muajve nga miratimi i standardit të GIS-it Kombëtar.
Kontrolli i konformitetit të shërbimeve të rrjetit
Bazuar në aneksin 1 të këtij dokumenti (Shërbimet e rrjetit), bëhet kontrolli i të dhënave gjeohapësinore të marra me anë të shërbimeve të rrjetit nga autoriteti publik përgjegjës burim.
Funksionet e Shërbimit të Shikimit janë:
Nr.
Shërbimet e shikimit
Përshkrimi
1
GetMap
Marrja dhe publikimi i të dhënave gjeohapësinore në hartë.
2
GetInfo
Marrja e informacionit mbi shërbimin WMS të publikuar në hartë.
3
GetCapabilities
Marrja e një përshkrimi të detajuar së të dhënës së krijuar me shërbim WMS.
4
Sistemi koordinativ
Sistemi koordinativ dhe gjeometria
4.7. ANEKS 1 - SHËRBIMET E RRJETIT
4.7.1. SHËRBIMI I ZBULIMIT
Në mënyrë që të jetë në përputhje me kriteret e kërkimit të përcaktuara në nenin 23, pika 2, të ligjit nr. 72/2012, Shërbimi i Zbulimit do të suportohet tek elementet e metadatave të listuara në tabelën 2 të këtij kreu.
Tabela 2
Kriteret minimale të kërkimit
Elementet e metadatave sipas INSPIRE
Fjalët kyçe (Keywords)
Fjalët kyçe (Keywords)
Klasifikimi i të dhënave dhe shërbimeve gjeohapësinore (për të dhënat gjeohapësinore dhe grupet e të dhënave gjeohapësinore)
Temat specifike
Klasifikimi i të dhënave dhe shërbimet gjeohapësinore (për shërbimet e të dhënave gjeohapësinore)
Tipi i shërbimeve dhe të dhënave gjeohapësinore
Cilësia dhe vlefshmëria e grupit të të dhënave gjeohapësinore
Rrjedhimet (derivatet)
Cilësia dhe vlefshmëria e grupit të të dhënave gjeohapësinore
Rezultatet gjeohapësinore
Shkalla e përputhshmërisë me rregullat e ndërveprueshmërisë, sipas përcaktimeve të nenit 18 të ligjit nr. 72/2012
Specifikimet
Shkalla e përputhshmërisë me rregullat e ndërveprueshmërisë sipas përcaktimeve të nenit 18 të ligjit nr. 72/2012.
Shkalla e përputhshmërisë
Pozicionimet gjeografike.
Kufijtë gjeografik
Kushtet e aplikimit për aksesin dhe përdorimin e të dhënave dhe shërbimeve gjeohapësinore
Aplikimi i kushteve për aksesin dhe përdorimin
Kushtet e aplikimit për aksesin dhe përdorimin e të dhënave dhe shërbimeve gjeohapësinore
Akses i limituar për përdoruesit publik
Autoriteti publik përgjegjës për krijimin, menaxhimin, mirëmbajtjen dhe shpërndarjen e të dhënave dhe shërbimeve gjeohapësinore
Palët përgjegjëse
Autoriteti publik përgjegjës për krijimin, menaxhimin, mirëmbajtjen dhe shpërndarjen e të dhënave dhe shërbimeve gjeohapësinore
Rolet e palëve përgjegjëse
Elementet ose grupet e elementeve të mëposhtme të metadatave duhet të jenë, gjithashtu, në dispozicion si kriter kërkimi:
1. Titulli i burimit;
2. Abstrakti i burimit;
3. Lloji i burimit;
4. Identifikuesi unik i burimit;
5. Referenca kohore.
Lejon zbulimin e burimit përmes kombinimit të kritereve të kërkimit dhe suportimit të funksioneve logjike dhe të kombinueshme.
Lejon zbulimin e burimeve bazuar në vendndodhjen gjeografike të burimit dhe suportimit të funksioneve gjeohapësinore të listuara në tabelën 3.
Tabela 3
Emri i operatorit
Karakteristikat
Kryqëzimet
Kërkon elementet e metadatave të kufijve gjeografikë të cilët ndërpriten në një zonë të caktuar të interesit.
1. LISTA E FUNKSIONEVE
Në mënyrë që të jetë në përputhje me kërkesat e nenit 23, pika 1/a dhe 2, të ligjit nr. 72/2012, Shërbimi i Zbulimit do të sigurojë funksionet e renditura në tabelën 4 të këtij kreu.
Tabela 4
Funksionet
Rolet
Metadata për Shërbimin e Zbulimit
Siguron të gjithë informacionin e nevojshëm në lidhje me shërbimin dhe përshkruan aftësitë e shërbimit.
Zbulimi i metadatave
Funksioni i zbulimit të metadatave lejon kërkesën e elementeve të metadatave burim, në bazë të një deklarate që të shikohet nga Shërbimi i Zbulimit.
Publikimi i metadatave
Funksioni i publikimit të metadatave lejon editimin e elementeve burim të metadatave, në Shërbimin e Zbulimit (push ose pull mekanizmat e metadatave). Editimi nënkupton vendosje, përditësim dhe fshirje.
Linkimi i Shërbimit të Zbulimit
Funksioni i linkimit për Shërbimin e Zbulimit tregon disponueshmërinë e këtij shërbimi për zbulimin e burimeve duke ruajtur burimet e metadatave.
Parametrat kërkesë-përgjigje të çdo funksioni plotësojnë përshkrimin e çdo operacioni dhe formojnë një pjesë integrale të specifikimit teknik të Shërbimit të Zbulimit.
2. FUNKSIONET E METADATAVE PËR MARRJEN E SHËRBIMIT TË ZBULIMIT
2.1. Marrja e kërkesës së metadatës për Shërbimin e Zbulimit
2.1.1. Parametrat e kërkesës së metadatave për Shërbimin e Zbulimit. Parametrat e kërkesës së metadatave për Shërbimin e Zbulimi tregojnë gjuhën e zakonshme për përmbajtjen e përgjigjes së Shërbimit të Zbulimit.
2.2. Përgjigjja e Metadatave për Shërbimin e Zbulimit
Përgjigjja e metadatave për Shërbimin e Zbulimit përmban grupet e mëposhtme të parametrave:
- Metadatat e Shërbimit të Zbulimit;
- Funksionet e metadatave;.
- Gjuha e metadatës (në cilën gjuhë zyrtare është e shkruar).
2.2.1. Parametrat e metadatave të Shërbimeve të Zbulimit.
Këta parametra duhet të përmbajnë të paktën elementet e metadatave të Shërbimit të Zbulimit.
2.2.2. Parametrat e funksioneve të metadatave. Parametrat e funksioneve të metadatave japin metadata rreth funksioneve të zbatuara nga Shërbimi i Zbulimit. Këta parametra metadatash do të përshkruajnë secilin funksion si vijon:
1. Të tregojnë për publikimin e metadatave nëse mekanizmi pull, push ose të dyja janë në dispozicion.
2. Të përshkruajnë çdo funksion, duke përfshirë si minimum një përshkrim të shkëmbimit të të dhënave, si dhe adresën e rrjetit.
2.2.3. Parametrat e gjuhës. Dy parametrat e gjuhës që duhet të sigurohen:
- Parametri i gjuhës së përgjigjes, i cili tregon përdorimin e gjuhës së zakonshme në parametrat e përgjigjes së metadatave për Shërbimin e Zbulimit
- Parametri i suportimit të gjuhës përmban listën e gjuhëve të zakonshme të suportuara nga Shërbimi i Zbulimit
3. FUNKSIONI I METADATËS PËR SHËRBIMIN E ZBULIMIT
3.1. Kërkesa e zbulimit të metadatave.
Kjo kërkesë përmban parametrat e mëposhtëm:
- Gjuha;
- Pyetjet;
3.1.1. Parametri gjuhë
Parametri gjuhë tregon gjuhën e zakonshme të kërkuar për përmbajtjen e përgjigjes së zbulimit të metadatave.
3.1.2. Parametri pyetje
Parametri pyetje përmban kombinimet e çdo kriteri të specifikuar në paragrafin “Kriteret e kërkimit”. Përgjigjja e Zbulimit të Metadatave.
3.2 Përgjigjja e Zbulimit të Metadatave
3.2.1. Parametrat e përgjigjes së Zbulimit të Metadatave
Parametrat e përgjigjes së Zbulimit të Metadatave duhet të përmbajnë të paktën elementet e metadatave të çdo burimi, që përputhen me kërkesën.
4. FUNKSIONI I PUBLIKIMIT TË METADATAVE
Funksioni i publikimit të metadatave mundëson publikimin e burimeve të elementeve të metadatave në Shërbimin e Zbulimit. Dy janë alternativat:
- Mekanizmi push, lejon editimin e burimeve të elementeve të metadatave të arritshme nga Shërbimi i Zbulimit.
- Mekanizmi pull, lejon Shërbimin e Zbulimit të tërheqë burimet e elementeve të metadatave nga një lokacion në distancë. Së paku një nga alternativat e mësipërme duhet të plotësohet.
4.1. Mekanizmi push.
4.1.1. Kërkesa për editimin e metadatave.
4.1.1.1. Parametrat e kërkesës së editimit të metadatave.
Parametri i kërkesës së editimit të metadatave ofron të gjithë informacionet e kërkuara, burimet e elementeve të metadatave të krijuara, përditësuara ose fshirë në Shërbimin e Zbulimit.
4.2. Mekanizmi pull
4.2.1. Kërkesë për mbledhjen e metadatave
4.2.1.1. Parametrat e kërkesës për mbledhjen e metadatave.
Parametrat e kërkesës për mbledhjen e metadatave japin të gjitha informatat në lidhje me lokacionet në distancë, të nevojshme për të gjetur burimet e metadatave të vlefshme. Ajo do të përfshihet si një minimum elementesh të metadatave të shërbimeve të të dhënave gjeohapësinore të dedikuara.
5. FUNKSIONI I LINKIMIT PËR SHËRBIMIN E ZBULIMIT
Funksioni i Linkimit për Shërbimin e Zbulimit lejon deklarimin e disponueshmërinë e një Shërbimi Zbulimi në përputhje me këto rregulla, për zbulimin e burimeve nëpërmjet Shërbimit të Zbulimit të një vendi tjetër duke ruajtur burimet e metadatave të vendit kryesor.
5.1. Kërkesa për Linkimin e Shërbimit të Zbulimit
5.1.1. Parametrat e Linkimit të Shërbimit të Zbulimit
Kërkesa për Linkimin e Shërbimit të Zbulimit do të japë të gjithë informacionin në lidhje me Shërbimin e Zbulimit të autoritetit publik ose palës së tretë, në përputhje me këto rregulla, duke bërë të mundur që Shërbimi i Zbulimit të marrë burimet e metadatave, duke u bazuar në një kombinim të kritereve të kërkimit nga Shërbimet e Zbulimit të autoritetit publik dhe palës së tretë, dhe t’i mbledhë ato me të tjera burime metadatash.
4.7.2. SHËRBIMI I SHIKIMIT
1. LISTA E FUNKSIONEVE
Në mënyrë që të jetë në përputhje me kërkesat e nenit 23, pika 1/b dhe pika 2, të ligjit nr. 72/2012, Shërbimi i Shikimit do të sigurojë funksionet e renditura në tabelën 5 të këtij kreu.
Tabela 5
Funksionet
Roli
Marrja e Shërbimit të Shikimit të metadatave
Prodhon të gjithë informacionet e nevojshme rreth shërbimeve dhe përshkrimit të aftësive të shërbimit konkret.
Marrja e hartës (Get Maps)
Rikthen përmbajtjen e hartës gjeografike dhe informacionin tematik të ardhur nga vlefshmëria e të dhënave gjeohapësinore. Kjo hartë është një imazh referuar gjeohapësirës.
Linku i Shërbimi të Shikimit
Lejon një autoritet publik ose një palë të tretë për të deklaruar një Shërbim Shikimi për shikimin e burimeve të tij, duke ruajtur aftësitë e Shërbimit të Shikimit të lokacionit të autoritetit publik apo palës së tretë.
Parametrat kërkesë-përgjigje të çdo operacioni plotësojnë përshkrimin e çdo operacioni dhe formojnë një pjesë integrale të specifikimit teknik për Shërbimin e Shikimit.
2. FUNKSIONI I METADATËS SË MARRJES SË SHËRBIMIT TË SHIKIMIT
2.1. Marrja e kërkesës së metadatave për Shërbimin e Shikimit
2.1.1. Parametrat e marrjes së kërkesave të metadatave për Shërbimin e Shikimit. Parametrat e marrjes së kërkesave së metadatave për Shërbimin e Shikimit tregojnë gjuhën e zakonshme për përmbajtjen e përgjigjes së marrjes së metadatave për Shërbimin e Shikimit.
2.2. Parametrat e përgjigjes së metadatave për marrjen e Shërbimit të Shikimit.
Parametrat e përgjigjes së metadatave për marrjen e Shërbimit të Shikimit do të përmbajnë grupin e mëposhtëm:
- Metadatat e Shërbimit të Shikimit;
- Funksionet e metadatave;
- Gjuha;
- Shtresat e metadatave.
2.2.1. Parametrat e metadatave për Shërbimin e Shikimit
Parametrat e metadatave për Shërbimin e Shikimit duhet të përmbajnë të paktën elementet e metadatave të Shërbimit të Shikimit.
2.2.2. Parametrat e funksioneve të metadatave
Parametrat e funksioneve të metadatave përshkruajnë funksionet e Shërbimit të Shikimit dhe do të përmbajnë si një minimum përshkrimin e të dhënave të shkëmbimit dhe adresën e rrjetit për çdo funksion.
2.2.3. Parametrat e gjuhës
Dy parametrat e gjuhës duhet të sigurojnë:
- Parametri i Gjuhës së Përgjigjes tregon gjuhën e zakonshme të përdorur në parametrat e përgjigjes së metadatave për marrjen e shërbimit.
- Parametri i Gjuhës së Suportimit përmban listën e gjuhëve të zakonshme të suportuar nga Shërbimi i Shikimit.
2.2.4. Parametrat e shtresave të metadatave
Elementet e metadatave të renditura në tabelën 6, do të sigurohen për çdo Layer.
Tabela 6
Elementet e metadatave
Përshkrimi
Titulli i burimit
Titulli i Layer-it, përdoret për komunikim njerëzor, për prezantimin e Layer-it, p.sh. në një menu.
Burim abstrakt
Layer abstrakt.
Fjalët kyçe
Shtimi i fjalëve kyçe.
Geographic Bounding Box
Minimumi i kufijve drejtkëndësh mbështetur në Sistemin Koordinativ Referues të zonave të mbulimit nga layer-i.
Identifikuesi unik i burimit
Identifikimi unik i burimit përdoret për të krijuar layer-in.
Parametrat specifikë të layer-ave të listuara në tabelën 7, do të sigurohet për çdo layer.
Tabela 7
Parametrat
Përshkrimi
Emri
Harmonizimi i emrit të layer-it
Sistemi Referues Koordinativ
Lista e Sistemeve Referuese Koordinative në të cilin layer-i është i vlefshëm.
Llojet
Lista e llojeve të pasqyruara të vlefshme për layer-at.
Një lloj përbëhet nga një titull dhe një identifikues unik.
Legjenda URL
Lokacioni i legjendës për çdo lloj, gjuha dhe dimensioni.
Çift dimensionesh
Tregon suportimin e dy akseve dimensionale për grupe shumëdimensionale të të dhënave apo grupeve të të dhënave gjeohapësinore.
3. FUNKSIONI I MARRJES SË HARTËS (GET MAP)
3.1. Kërkesa për marrjen e hartës
3.1.1. Parametrat e kërkesës për marrjen e hartës
Parametrat e kërkesës për marrjen e hartës listohen në tabelën 8.
Tabela 8
Parametrat
Përshkrimi
Layer-at
Lista e emërtimeve të shtresave të përfshira në hartë.
Llojet
Lista e llojeve e përdorur për çdo layer.
Sistemi Referues Koordinativ
Sistemi Koordinativ Referues i Hartës.
Bounding box
Katër këndet e hartës dydimensionale për çiftin e dimensioneve dhe selektimin e Sistemit Referues Koordinativ.
Gjerësi e figurës
Gjerësia e hartës në piksel.
Lartësia e figurës
Lartësia e hartës në piksel.
Formati i figurës
Formati output i figurës.
Gjuha
Gjuha e përdorur për përgjigje.
Çifti dimensional
Akset dydimensionale të përdorura për hartën. Për shembull një dimension gjeografik dhe koha.
4. FUNKSIONET E LIDHJES SË SHËRBIMIT TË SHIKIMIT
4.1. Kërkesa lidhje e Shërbimit të Shikimit.
4.1.1. Parametrat e kërkesës së lidhjes në Shërbimin e Shikimit.
Parametrat e kërkesës së lidhjes së Shërbimit të Shikimit do të tregojnë të gjithë informacionin në lidhje me Shërbimin e Shikimit të autoritetit publik ose palës së tretë në përputhje me kërkesat e nenit 23, pika 2, e ligjit nr. 72/2012, duke bërë të mundur që Shërbimi i Shikimit të marrë një hartë me Shërbimin e Shikimit të autoriteti publik dhe ta bashkojnë atë me harta të tjera.
5. KARAKTERISTIKAT TË TJERA
Shërbimi i Shikimit duhet të ketë karakteristikat e mëposhtme.
- Sistemi Koordinativ Referues
Parametrat e linkimit të Shërbimit të Shikimit do të stimulohen në të njëjtën kohë, duke përdorur një sistem të vetëm koordinativ referues dhe Shërbimi i Shikimit duhet të suportojë të paktën Sistemin Referues Koordinativ zyrtar.
- Formati i figurës
Shërbimi i Shikimit duhet të suportojë të paktën një nga formatet e mëposhtëm:
- Formati PNG (Portable Network Graphics).
- Formati GIF (the Graphics Interchange Format), pa kompresim.
4.7.3. SHËRBIMI I SHKARKIMIT
1. LISTA E VEPRIMEVE
Në mënyrë që të jetë në përputhje me kërkesat e nenit 23, pika 1/c, të ligjit nr. 72/2012, Shërbimi i Shkarkimit duhet të sigurojë funksionet e renditura në Tabelën 9 të këtij kreu.
Tabela 9
Funksionet
Roli
Metadata e shërbimit të shkarkimit (Get Download Service Metadata).
Siguron informacionin e nevojshëm në lidhje me shërbimin, grupet e të dhënave gjeohapësinore të vëna në dispozicion, dhe përshkruan aftësitë e shërbimit.
Marrja e të dhënave gjeohapësinore (Get Spatial Data Set).
Lejon tërheqjen e grupit të të dhënave gjeohapësinore.
Përshkrimi i të dhënave gjeohapësinore (Describe Spatial Data Set).
Ky operacion kthen si përgjigje përshkrimin e të gjitha llojeve të objekteve gjeohapësinore të përfshira në grupin e të dhënave gjeohapësinore.
Linkimi i shërbimit të shkarkimit.
I jep të drejtën, një autoriteti publik ose një pale të tretë, mbi Shërbimin e Shkarkimit për të shkarkuar të dhënat ose grupet e të dhënave gjeohapësinore, aty ku është e praktikueshme. Shkarkon shërbimin, duke ruajtur aftësinë e shkarkimit në vendndodhjen e autoritetit publik apo palës së tretë përgjegjëse.
Parametrat kërkesë-përgjigje të çdo operacioni plotësojnë përshkrimin e çdo funksioni dhe formojnë një pjesë integrale të specifikimeve teknike të Shërbimit të Shkarkimit.
2. FUNKSIONI I METADATAVE TË SHËRBIMIT TË SHKARKIMIT (GET DOWNLOAD SERVICE METADATA)
2.1. Kërkesa për marrjen e të dhënave gjeohapësinore (Get Spatial Data Set)
2.1.1 Përshkrimi i të dhënave gjeohapësinore (Describe Spatial Data Set)
Parametrat e kërkesës së Shërbimit të Shkarkimit për metadatat tregojnë gjuhën e zakonshme që do të përdoret për përmbajtjen e përgjigjes për Shërbimin e Shkarkimit të metadatave.
2.2. Funksioni i marrjes së përgjigjes për metadatat e shërbimit të shkarkimit.
Funksioni përgjigje për metadatat e Shërbimit të Shkarkimit përmban grupet e mëposhtme të parametrave:
- Metadatat e shkarkimit;
- Funksionet e metadatave;
- Gjuha;
- Metadatat e të dhënave gjeohapësinore.
2.2.1 Parametrat e metadatave për Shërbimin e Shkarkimit.
Parametrat e Shërbimit të Shkarkimit të metadatave duhet të përmbajnë elementet e metadatave të shërbimeve, sipas VKM-së nr. 1077, datë 23.12.2015.
2.2.2 Parametrat e funksioneve të metadatave.
Parametrat e funksioneve të metadatave japin metadata rreth zbatimit të funksioneve të Shërbimit të Shkarkimit. Ato duhet të japin të paktën një përshkrim të çdo funksioni, duke përfshirë shkëmbimin e të dhënave dhe adresën e rrjetit.
2.2.3 Parametrat e gjuhës
Sigurohen dy parametra gjuhe:
- Parametrat e gjuhës së përgjigjes tregojnë gjuhën e zakonshme që përdoret në parametrat e përgjigjes së metadatave të Shërbimit të Shkarkimit.
- Parametrat e gjuhës së suportimit përmbajnë listën e gjuhëve të zakonshme, mbështetur nga Shërbimi i Shkarkimit.
2.2.4 Parametrat e metadatave për grupin e të dhënave
Elementet e metadatave të grupit të të dhënave gjeohapësinore, të vëna në dispozicion, duhet të parashikohen. Përveç kësaj, për çdo grup të dhënash gjeohapësinore, duhet të parashikohen lista e Sistemeve Koordinative të Referimit, të vlefshme sipas rregullave të ndërveprueshmërisë.
3. VEPRIMET E MARRJES SË GRUPIT TË TË DHËNAVE GJEOHAPËSINORE
3.1 Kërkesa për marrjen e një grupi të dhënash gjeohapësinore
Kërkesa për marrjen e një grup të dhënash gjeohapësinore përmban parametrat e mëposhtëm:
- Gjuhën;
- Identifikimin e të dhënave gjeohapësinore;
- Sistemin Koordinativ Referues.
3.1.1. Parametrat e gjuhës
Në parametrin gjuhë shënohet gjuha natyrore e të dhënave gjeohapësinore.
3.1.2. Parametrat Identifikues të të Dhënave Gjeohapësinore.
Identifikimi i parametrave të të dhënave gjeohapësinore duhet të përmbajë identifikues unik të këtyre burimeve gjeohapësinore.
3.1.3. Parametrat e Sistemit Referues Koordinativ
Parametrat e Sistemit Koordinativ duhet të përmbajnë një nga Sistemet Koordinativ Referues të përfshira në listën e disponueshme të këtyre sistemeve të parashikuara në pikën 2.2.4.
3.2. Përgjigjja e të dhënave gjeohapësinore
3.2.1. Parametrat e përgjigjes së të dhënave gjeohapësinore
Parametrat e të dhënave gjeohapësinore duhet të jenë të paraqitura në gjuhën dhe në Sistemin Koordinativ Referues të kërkuar.
4. PËRSHKRIMI I VEPRIMEVE TË TË DHËNAVE GJEOHAPËSINORE
4.1 Përshkrimi kërkesës së të dhënave gjeohapësinore
Përshkrimi kërkesës së të dhënave gjeohapësinore përmban parametrat e mëposhtëm:
- Gjuhën;
- Identifikimin e grupit të të dhënave gjeohapësinore;
4.1.1. Parametrat e gjuhës.
Parametrat gjuhësorë tregojnë gjuhën e zakonshme të kërkesës për përshkrimin e tipit të objekteve gjeohapësinore.
4.1.2. Parametrat e identifikimit të të dhënave gjeohapësinore
Parametrat identifikues të të dhënave gjeohapësinore do të përmbajnë burim identifikues unik të të dhënave gjeohapësinore.
4.2. Përshkrimi i përgjigjes së të dhënave gjeohapësinore
4.2.1. Parametrat e përshkrimit të përgjigjes së të dhënave gjeohapësinore
Parametrat e përshkrimit të përgjigjes së të dhënave gjeohapësinore duhet të jenë përshkrimi i kërkesës së objekteve dhe të dhënave gjeohapësinore në gjuhën e kërkuar.
5. FUNKSIONI I LINKIMIT TË SHËRBIMIT TË SHKARKIMIT
Funksioni i linkimit të Shërbimit të Shkarkimit nënkupton disponueshmërinë e Shërbimit të Shkarkimit, në përputhje me këto rregulla, për shkarkimin nga burime të ndryshme nga ai i vendit të burimit kryesor.
5.1. Kërkesa për Linkimin e Shërbimit të Shkarkimit
5.1.1. Parametrat e kërkesës për Linkimin e Shërbimit të Shkarkimit
Parametrat e kërkesës për linkimin e Shërbimit të Shkarkimit duhet të përmbajnë të gjithë informacionin rreth Shërbimit të Shkarkimit të autoritetit publik ose palës së tretë përgjegjëse, në përputhje me këto rregulla.
Aksesimi direkt i funksioneve të shkarkimit.
6. LISTA E FUNKSIONEVE.
Kur Shërbimi i Shkarkimit jep akses të drejtpërdrejtë të grupeve të të dhënave gjeohapësinore, ai do të ofrojë, përveç funksioneve të renditura në tabelën 11, dhe funksionet e renditura në tabelën 10 të këtij kreu.
Tabela 10
Funksionet
Rolet
Marrja e objekteve gjeohapësinore (Get Spatial Object).
Ky funksion lejon rikthimin e objekteve gjeohapësinore bazuar mbi një kërkesë.
Tipi i përshkrimit të objekteve gjeohapësinore (Describe Spatial Object Type)
Ky funksion rikthen përshkrimin e tipit specifik të objektit gjeohapësinor.
7. FUNKSIONI I MARRJES SË OBJEKTEVE GJEOHAPËSINORE
7.1. Kërkesa për marrje të objekteve gjeohapësinore
Kërkesa për marrje të objekteve gjeohapësinore ka parametrat e mëposhtëm:
- Gjuha;
- Identifikimi i të Dhënave Gjeohapësinore;
- Sistemi Referues Koordinativ;
- Kërkesa.
7.1.1 Parametrat gjuhësorë
Parametrat gjuhësorë tregojnë gjuhën e zakonshme të kërkuar për objektet gjeohapësinore.
7.1.2. Identifikimi i parametrave të grupit të të dhënave gjeohapësinore.
Identifikimi i parametrave të grupit të të dhënave gjeohapësinore duhet të përmbajë identifikues unikë të burimeve të të dhënave gjeohapësinore. Kur parametrat nuk janë dhënë, do të supozohet se janë përzgjedhur të gjitha të dhënat gjeohapësinore të vëna në dispozicion.
7.1.3. Parametrat e Sistemit Koordinativ Referues
Sistemi Koordinativ Referues duhet të përmbajë një nga Sistemet Koordinative Referues të përfshirë në listën e Sistemeve Koordinativ Referues të përcaktuara në rregullat e ndërveprueshmërisë.
7.1.4. Parametrat e pyetjes
Parametrat e pyetjes do të përbëhen nga kriteret e kërkimit të renditura në pikën 9.
7.2. Përgjigjja e një grupi të dhënash gjeohapësinore.
Përgjigjja e një grupi të dhënash gjeohapësinore do të përmbajë parametrat e mëposhtme:
- Vendosja e objekteve gjeohapësinore;
- Metadatat e objekteve gjeohapësinore.
7.2.1. Parametrat e një grupi objektesh gjeohapësinore
Parametrat e një grupi objektesh gjeohapësinore - Së pari duhet të jetë grup i objekteve gjeohapësinore që është në përputhje me rregullat e ndërveprueshmërisë dhe plotëson kriteret e kërkimit sipas kërkesës, në gjuhën e kërkuar dhe në Sistemin Koordinativ Referues.
7.2.2. Parametrat e Metadatave të Objektet Gjeohapësinore
Parametrat e metadatave të objekteve gjeohapësinore duhet të përmbajnë të paktën elementet e metadatave të objekteve gjeohapësinore.
8. FUNKSIONET E PËRSHKRIMIT TË TIPIT TË OBJEKTIT GJEOHAPËSINOR
8.1. Përshkimi i tipit të kërkesës së objekteve gjeohapësinore. Përshkrimi i tipit të kërkesës së objekteve gjeohapësinore përmban parametrat e mëposhtëm:
- Gjuha;
- Tipi i objektit gjeohapësinor.
8.1.1. Parametri gjuhë
Parametri gjuhë, duhet të tregojë gjuhën e zakonshme të kërkuar për përshkrimin e tipit të objektit gjeohapësinor.
8.1.2. Parametrat e tipit të objektit gjeohapësinor
Parametrat e tipit të objektit gjeohapësinor duhet të përmbajnë emrin e gjuhës së zakonshme të tipit të objektit gjeohapësinor, siç është specifikuar në rregullat e ndërveprueshmërisë. Kur parametri nuk është dhënë, do të supozohet që të gjitha llojet e objekteve gjeohapësinore janë përzgjedhur.
8.2. Përshkrimi i përgjigjes së tipit të objektit gjeohapësinor
8.2.1. Përshkrimi i parametrave të përgjigjes së objektit gjeohapësinor
Parametrat e përgjigjes së objektit gjeohapësinor është përshkrimi i llojit të objektit gjeohapësinor në përputhje me rregullat e ndërveprueshmërisë.
9. KRITERET E KËRKIMIT PËR MARRJEN E FUNKSIONEVE TË OBJEKTEVE GJEOHAPËSINORE
Për shkak të veprimeve të grupit të të dhënave gjeohapësinore për Shërbimin e Shkarkimit, do të implementohen kriteret e mëposhtme të kërkimit:
- Identifikimi unik i burimeve të të dhënave gjeohapësinore;
- Të gjitha atributet identifikuese të përshtatshme dhe marrëdhëniet midis objekteve gjeohapësinore të përcaktuara në bazë të rregullave të ndërveprueshmërisë, në veçanti Identifikuesi Unik i Objektit Gjeohapësinor dhe karakteristikat e dimensioneve kohore, duke përfshirë datën e përditësimit.
- Bounding box e shprehur në ndonjë nga Sistemet Koordinative Referuese të njohura, sipas rregullave të ndërveprueshmërisë.
- Tema e të dhënave gjeohapësinore. Për zbulimin e objekteve gjeohapësinore përmes një kombinimi të kritereve e kërkimit, do të suportohet nga operatorët logjikë dhe krahasues.
4.7.4. SHËRBIMI I TRANSFORMIMIT
1. LISTA E FUNKSIONEVE
Në mënyrë që të jetë në përputhje me kërkesat e nenit 23, pika 1/ç, të ligjit nr. 72/2012, Shërbimi i Transformimit do të ofrojë funksionet e renditura në tabelën 11 të këtij kreu.
Tabela 11
Funksionet
Roli
Metadata për marrjen e Shërbimit të Transformimit
Siguron të gjithë informacionin e nevojshëm mbi shërbimin dhe përshkruan veçoritë e shërbimit, duke përfshirë edhe kategorinë e transformimit, suportet e transformimit, tipat e të dhënave input të pranuara, definimin e modelit të suportuar dhe gjuhën e hartës.
Transformimi
Kryen procesin aktual të transformimit.
Linkimi i Shërbimit të Transformimit
Lejon disponueshmërinë e Shërbimit të Transformimit për transformimin e grupit të të dhënave gjeohapësinore nëpërmjet Shërbimit të Transformimit të një autoriteti tjetër, duke ruajtur aftësinë e transformimit nga vendndodhja e autoritetit publik apo palës së tretë.
Parametrat kërkesë-përgjigje të çdo funksioni plotësojnë përshkrimin e çdo funksioni dhe formojnë një pjesë integrale të specifikimeve teknike të Shërbimit të Transformimit.
2. FUNKSIONI I METADATAVE PËR MARRJEN E SHËRBIMIT TË TRANSFORMIMIT
2.1. Kërkesa e metadatave për marrjen e Shërbimit të Transformimit
2.1.1. Parametrat e kërkesës së metadatave për marrjen e Shërbimit të Transformimit
Parametrat e kërkesës së metadatave për marrjen e Shërbimit të Transformimit tregojnë gjuhën e zakonshme për përmbajtjen e kërkesës së metadatave për marrjen e Shërbimit të Transformimit.
2.2. Përgjigjja e metadatave për marrjen e Shërbimit të Transformimit
Përgjigjja e metadatave për marrjen e Shërbimit të Transformimit përmbajnë grupet e mëposhtme të parametrave:
- Metadatat e Shërbimit të Transformimit;
- Funksionet e metadatave;
- Gjuhën.
2.2.1. Parametrat e metadatave për Shërbimin e Transformimit
Parametrat e metadatave për Shërbimin e Transformimit duhet të përmbajnë të paktën elementet e metadatës të Shërbimit të Transformimit.
2.2.2. Parametrat e funksioneve të metadatave
Parametrat e funksioneve të metadatave japin metadata rreth funksioneve të zbatuara nga Shërbimi i Transformimit.
Ato do të përshkruajnë çdo funksion, duke përfshirë si një minimum, përshkrimin e shkëmbimit të të dhënave dhe adresën e rrjetit, të listuara si më poshtë:
- Kategoritë e transformimit të miratuara nga funksioni i transformimit;
- Dekodimin për vendosjen e inputeve të të dhënave gjeohapësinore të miratuara nga funksioni i transformimit;
- Modeli i gjuhës së të dhënave miratuara nga funksioni i transformimit;
- Modeli i gjuhës së hartës miratuar nga funksioni i transformimit;
2.2.3. Parametrat e gjuhës
Dy parametra duhet të sigurohen:
- Parametri i gjuhës së përgjigjes tregon gjuhën e zakonshme të përdorur në përgjigjen e metadatës për marrjen e Shërbimit të Transformimit;
- Parametrat e gjuhës të suportuar përmban listën e gjuhëve të zakonshme mbështetur nga Shërbimi i Transformimit.
3. FUNKSIONI I TRANSFORMIMIT
3.1. Kërkesa për transformim
Kërkesa për transformim përmban parametrat e mëposhtëm:
- Input i të dhënave gjeohapësinore;
- Modeli i burimit;
- Model i targetit;
- Model i hartëzimit.
3.1.1. Parametrat input të të dhënave gjeohapësinore
Parametrat input të të dhënave gjeohapësinore duhet të tregojnë të dhënat gjeohapësinore për t’u transformuar.
3.1.2. Parametri i modelit të burimit
Parametri i modelit të burimit do të specifikojë modelin input të të dhënave gjeohapësinore.
3.1.3. Parametri i modelit të targetit
Parametri i modelit të targetit duhet të specifikojë modelin në të cilin inputi i të dhënave gjeohapësinore do të transformohet.
3.1.4. Parametri i modelit të hartëzimit
Parametër i modelit të hartëzimit duhet të specifikojë hartën nga modeli burim në modelin target.
3.2. Përgjigje e transformimit
3.2.1. Parametrat e përgjigjes së transformimit.
Parametrat e përgjigjes së transformimit duhet të përmbajnë të dhënat gjeohapësinore të transformuara në përputhje me rregullat e ndërveprueshmërisë.
4. FUNKSIONI I LINKIMIT TË SHËRBIMIT TË TRANSFORMIMIT
4.1. Linkimi i kërkesës së Shërbimit të Transformimit
4.1.1. Parametrat e linkimit të kërkesës së Shërbimit të Transformimit
Parametrat e linkimit të kërkesës së Shërbimit të Transformimit duhet t’u sigurojnë të gjitha informacionet në lidhje me Shërbimin e Transformimit autoriteteve publik apo palëve të treta në përputhje me këto rregulla, duke bërë të mundur përdorimin e Shërbimit të Transformimit prej tyre.
