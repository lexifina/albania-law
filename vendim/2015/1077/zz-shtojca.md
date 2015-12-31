# Shtojca
RREGULLORE
PËR KRIJIMIN, RUAJTJEN DHE PËRDITËSIMIN E METADATAVE, STRUKTURËN E KATALOGIMIT DHE AFATET E KRIJIMIT TË METADATAVE SPECIFIKE PËR ÇDO TEMË
KREU I
TË PËRGJITHSHME
1. Fusha e veprimit
Kjo rregullore përcakton rregulla të hollësishme për krijimin, ruajtjen, përditësimin, dhe katalogimin e metadatave për të dhënat gjeohapësinore, grupet e të dhënave gjeohapësinore si dhe shërbimet e të dhënave gjeohapësinore për temat e listuara në nenin 11 të ligjit nr. 72/2012, datë 28.6.2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”, si dhe për çdo temë tjetër të miratuar me VKM.
2. Përkufizime
- “ASIG” - Autoriteti Shtetëror për Informacionin Gjeohapësinor
“Autoritet përgjegjës “ - Autoritete publike sipas neneve 2, 12, të ligjit nr. 72/2012, datë 28.6.2012, “Për organizimin dhe funksionimin e infrastrukturës kombëtare të informacionit gjeohapësinor në Republikën e Shqipërisë”.
- “Metadata” është informacioni që përshkruan të dhënat, grupet e të dhënave gjeohapësinore dhe shërbimet që lidhen me to, të cilat mundësojnë zbulimin, inventarizimin dhe përdorimin e të dhënave e të grupeve të të dhënave gjeohapësinore.
-”Vlera domain” nënkupton përshkrimin e vlerave të lejuara të një atributi.
- “Varg karakteresh” nënkupton vlerën domain e elementeve të metadatës e shprehur si një grup karakteresh të cilat trajtohen si një njësi e vetme.
- “Text i lirë” nënkupton vlerën domain të një elementi të metadatës të shprehur në një ose më shumë gjuhë natyrore.
- “Cikli i jetës” nënkupton historinë e një grupi të dhënash, ciklin e jetës së tyre nga mbledhja përdorimi dhe përditësimi i tyre deri në formën aktuale, në përputhje me EN ISO 19101.
- “Element i metadatës” nënkupton një njësi diskrete të metadatës, në përputhje me EN ISO 19115.
- “Listë emrash” nënkupton një koleksion emrash, të identifikuara nga një Burim Identifikues Uniform (URI) i referencës, të cilat janë përdorur në gjuhën (XML) të dokumenteve si emrat e elementeve dhe atributet e tyre.
- “Cilësi” është tërësia e karakteristikave të një produkti që lidhet me aftësinë e saj për të kënaqur nevojat e deklaruara dhe të nënkuptuara, në përputhje me EN ISO 19101,
- “Të dhëna gjeohapësinore” është çdo e dhënë që i referohet në mënyrë të drejtpërdrejtë apo të tërthortë një vendi ose zone gjeografike të veçantë
- “Grup të dhënash gjeohapësinore” nënkupton një koleksion të identifikueshëm të dhënash gjeohapësinore.
- “Shërbime për informacionin gjeohapësinor” janë operacionet që mund të realizohen, përmes aplikacioneve kompjuterike, për informacionin gjeohapësinor, të dhënat dhe grupet e të dhënave gjeohapësinore ose për metadatat që lidhen me to
3. Referencat për vlefshmërinë e të dhënave dhe grupeve të të dhënave gjeohapësinore do të adresohet në elementet e mëposhtme:
- Gama e hapësirës dhe kohës që i përkasin të dhënat,
- Nëse performanca e të dhënave është kontrolluar bazuar në një standard të caktuar.
- Shkalla në të cilën të dhënat janë të përshtatshme për qëllimin e kërkuar.
- Vlefshmëria ligjore e të dhënave gjeo-hapësinore.
KREU II
ELEMENTET E METADATAVE
1. Identifikimi
Elementet e mëposhtëm të metadatave janë të domosdoshëm:
Titulli i burimit:
Kjo karakteristikë është unike, shpreh emrin me të cilin burimi është i njohur.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
1.2. Abstrakti i burimit:
Kjo është një përmbledhje e shkurtër që tregon përmbajtjen e burimit.
Vlera domain e këtij elementi të metadatave është teksti i lirë.
1.3. Tipi i burimit:
Ky është lloji i burimit të përshkruar nga metadata.
Vlera domain e këtij elementi të metadatave është përcaktuar në kreun IV.
1.4. Lokalizuesi i burimit:
Lokalizuesi i burimit/ve përcakton lidhjen për burimet ose informacion shtesë në lidhje me burimet.
Vlera domain e këtij elementi të metadatës është një varg karakteresh (URL)
1.5. Identifikuesi unik i burimit:
Një vlerë unike për identifikimin e burimit.
Vlera domain e këtij elementi të metadatës është një kod i detyrueshëm, varg karakteresh, i caktuar nga administratori (poseduesi i të dhënave) dhe një “namespace” varg karakteresh unike për identifikimin dhe kontekstin e kodit identifikues (për shembull, poseduesi i të dhënave).
1.6. Burimi i çiftëzuar:
Nëse burimi është një shërbim të dhënash gjeohapësinore kjo metadatë identifikon elemente, aty ku është e nevojshme, me objekt shërbimin e të dhënave gjeohapësinore, përmes identifikuesit unik të burimit.
Vlera domain e këtij elementi të metadatës është një kod i detyrueshëm, varg karakteresh, i caktuar nga administratori (poseduesi i të dhënave) dhe një “namespace” varg karakteresh unike për identifikimin dhe kontekstin e kodit identifikues (për shembull, poseduesi i të dhënave).
1.7. Gjuha e burimit:
Gjuha/ët e përdorura në burim.
Vlera domain e këtij elementi të metadatës është e kufizuar në gjuhët e përcaktuara në ISO 639-2.
2. Klasifikimi i të dhënave dhe shërbimeve gjeohapësinore
2.1. Kategoria tema:
Kategoria tema është një skemë klasifikimi e nivelit të lartë për të ndihmuar në kërkimin dhe grupimin e të dhënave gjeohapësinore mbi një bazë të disponueshme të burimit/eve të të dhënave.
Vlera domain e këtij elementi të metadatës është përcaktuar në kreun IV, pika 2
2.2. Lloji i të dhënave dhe shërbimeve gjeohapësinore:
Ky është një klasifikim për të ndihmuar në kërkimin e të dhënave dhe shërbimeve të të dhënave të disponueshme gjeohapësinore. Një shërbim i veçantë do të kategorizohet vetëm në një kategori.
Vlera domain e këtij elementi të metadatës është përcaktuar në kreun IV, pika 3.
3. Fjalët kyçe
Nëse burimi është një shërbim i të dhënave gjeohapësinore, do të ofrohet të paktën një emërtim i kreut IV, pika 4.
Në qoftë se burimi është një e dhënë gjeohapësinore apo një grup të dhënash gjeohapësinore do të përdoret të paktën një fjalë kyçe, e cila përshkruan temën përkatëse për të dhënat gjeohapësinore të përcaktuar në nenin 11, të ligjit nr. 72/2012.
Për çdo fjalë kyçe, do të ofrohen elementet e mëposhtëm të metadatës:
3.1. Vlera e fjalës kyç:
Vlera e fjalës kyçe është zakonisht një fjalë apo një frazë gjuhësore e formalizuar për të përshkruar temën. Kategoria tema është shumë e përgjithshme për pyetje të detajuara ndaj fjala kyçe do të ndihmojë për një kërkim të plotë të tekstit e do të na lejojë për një kërkim më të strukturuar.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
3.2. Origjina e fjalorit të kontrolluar:
Nëse vlera e fjalës kyçe e ka origjinën nga një fjalor i kontrolluar (enciklopedi, ontologji), citimi i origjinës së fjalorit të kontrolluar është detyrueshëm. Ky citim duhet të përfshijë të paktën titullin dhe një datë reference (data e publikimit, data e rishikimit të fundit ose e krijimit) të origjinës.
4. Vendndodhja gjeografike
Kërkesa për vendndodhjen gjeografike, të përmendur në nenin 3, pika 9, të ligjit nr. 72/2012, do të shprehet me elementin “Kutiza e kornizës gjeografike” të metadatës.
4.1 Kjo është shkalla e saktësisë në hapësirën gjeografike, të dhënë si një kuti kornizë e cila duhet të shprehet me koordinata, në gradë dhjetore, me një saktësi prej të paktën dy decimale. (Bazuar në kornizën referuese gjeodezike shqiptare “KRGJSH 2010”).
5. Referenca kohore
Ky element i metadatës adreson kërkesën që të ketë informacion mbi dimensionin kohor të të dhënave siç referohet në nenin 18, të ligjit nr. 72/2012. Së paku një nga elementet e metadatës të përmendura në pikat 5.1 deri 5.4 do të ofrohen në këtë rast.
Vlera domain e elementeve të metadatës të përmendura në pikat 5.1 deri 5.4 është një grup i afateve kohore. Çdo datë do t’i referohet një sistemi referimi kohor dhe do të shprehet në një formë të përputhshme me atë sistem. Sistemi i referencës së parazgjedhur do të jetë kalendari gregorian, me datat e shprehura në përputhje me ISO 8601.
5.1. Dimensioni Kohor:
Shtrirja kohore e cila përcakton periudhën kohore të mbuluar nga përmbajtja e burimit. Ky afat mund të shprehet në një nga format që vijojnë:
- një datë e përcaktuar;
- një interval kohor me datën e fillimit dhe mbarimit të intervalit;
- një përzierje e datave të veçanta dhe intervaleve kohore.
5.2. Data e publikimit:
Kjo është data e publikimit të burimit kur ekziston ose nga data e hyrjes në fuqi. Nuk mund të jetë më shumë se një data publikimi.
5.3. Data e rishikimit të fundit:
Kjo është data e rishikimit të fundit të burimit, nëse burimi është rishikuar. Nuk do të ketë më shumë se një datë të rishikimit të fundit.
5.4. Data e krijimit:
Kjo është data e krijimit të burimit. Nuk do të ketë më shumë se një datë të krijimit të burimit të metadatës
6. Cilësia dhe vlefshmëria
Kërkesat e përmendura në nenin 23, të ligjit nr. 72/2012, në lidhje me cilësinë dhe vlefshmërinë e të dhënave gjeohapësinore duhet të adresohen nga elementet në vijim të metadatës:
6.1. Cikli i Jetës:
Kjo është një deklaratë në historinë e procesit dhe/ose cilësinë e përgjithshme të të dhënave gjeohapësinore. Kur është e përshtatshme kjo mund të përfshijë një deklaratë nëse cilësia dhe siguria e të dhënave janë vërtetuar, nëse version i disponueshëm është versioni zyrtar (nëse ekzistojnë versione të shumta), dhe nëse ai ka vlefshmëri ligjore.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
6.2. Rezolucioni gjeohapësinor:
Rezolucioni gjeohapësinor i referohet nivelit të detajeve të të dhënave gjeohapësinore. Ajo duhet të shprehet si një vlerë zero për rezolucionin e distancës (tipike për të produktet që rrjedhin nga imazhet) ose në shkallë ekuivalente (tipike për hartat apo produktet hartografike).
Një shkallë ekuivalente shprehet në përgjithësi si një vlerë numerike të plotë duke e shprehur shkallën në emërues.
Një distance rezolucioni shprehet si një vlerë numerike lidhur me një njësi të gjatësisë.
7. Konformiteti
Kërkesat e përmendura në nenin 3, pika 15, të ligjit nr. 72/2012, në lidhje me ndër-veprueshmërinë, dhe shkallën e përputhshmërisë, me zbatimin e rregullave të ndërveprueshmërisë do të adresohen nga elementet në vijim të metadatave.
7.1. Specifikimi:
Ky është një citim i rregullave zbatuese të miratuara në bazë të nenit 18, të ligjit nr. 72/2012 dhe udhëzimet teknike të dala në zbatim të tyre. Ky citim do të përfshijë të paktën titullin dhe një datë reference (data e publikimit, data e rishikimit të fundit ose e krijimit) të VKM-së “Mbi rregullat e ndërveprueshmërisë”, dhe VKM-së për miratimin e standardit përkatës.
7.2. Shkalla e konformitetit:
Kjo është shkalla e konformitetit të të dhënave apo grupeve të të dhënave gjeo-hapësinore.
Vlera domain e këtij elementi të metadatës është përcaktuar në kreun IV, pika 5.
8. Kufizime në lidhje me aksesin dhe përdorimin
Metadata duhet të përshkruajë kufizimet në lidhje me aksesin dhe përdorimin të cilat mund të jenë secila ose të dyja së bashku:
- një sërë kushtesh që aplikohen për të hyrë dhe përdorur (8.1);
- një sërë kufizimesh për akses publik (8.2).
8.1. Kushtet që zbatohen për aksesin dhe përdorimin:
Ky element i metadatës përcakton kushtet për akses dhe shfrytëzim të të dhënave gjeo-hapësinore, grupeve të të dhënave gjeo-hapësinore dhe shërbimeve të të dhënave gjeohapësinore, dhe ku janë të aplikueshme, si dhe tarifat përkatëse siç përcaktohet në nenin 26, të ligjit nr. 72/2012.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
Elementi është i detyrueshëm të ketë vlerë. Nëse nuk ka kushte që zbatohen për aksesin dhe përdorimin e burimeve, duhet të citohet “nuk ka kushte për akses”. Nëse kushtet janë të panjohura, duhet të citohet “kushte të panjohura”.
Ky element gjithashtu duhet të japë informacion për tarifat e nevojshme për të hyrë dhe për të përdorur burimin, nëse ka tarifa, ose i referohet një lokalizuesi uniform të burimit (URL) ku informacioni mbi tarifat është në dispozicion.
8.2. Kufizimet në aksesin publik:
Kur autoriteti përgjegjës do të kufizojë aksesin e publikut në të dhënat gjeohapësinore, grupet e të dhënave gjeohapësinore dhe shërbimet e të dhënave gjeohapësinore. Sipas përcaktimeve të nenit 25, të ligjit nr. 72/2012, ky element i metadatës do të japë informacion mbi kufizimet dhe arsyet për to. Nëse nuk ka kufizime për aksesin publik, ky element i metadatës do të tregojë këtë fakt.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
9. Autoritetet përgjegjëse për krijimin, ruajtjen, përditësimin dhe shpërndarjen e të dhënave dhe shërbimeve gjeohapësinore
Për qëllimet e neneve 2 dhe 12, të ligjit nr. 72/2012, do të ofrohen dy elementet në vijim për metadatat:
9.1 Pala përgjegjëse:
Ky është përshkrimi i autoritetit përgjegjës për krijimin, ruajtjen dhe përditësimin e të dhënave dhe shërbimeve gjeohapësinore i cili duhet të përfshijë:
- emrin e autoritetit përgjegjës si tekst i lirë;
- një adresë e-maili të kontaktit si një varg karakteresh.
9.2 Roli i palës përgjegjëse:
Ky është roli i autoritetit përgjegjës për krijimin, ruajtjen dhe përditësimin e të dhënave dhe shërbimeve gjeohapësinore.
Vlera domain e këtij elementi të metadatës është përcaktuar në kreun IV, pika 6.
10. Metadata për metadatat
Për qëllimet e neneve 11 dhe 12, të ligjit nr. 72/2012, do të ofrohen elementet e mëposhtme të metadatave:
10.1 Pika e kontaktit të metadatës:
Ky është përshkrimi i autoritetit përgjegjës për krijimin mirëmbajtjen dhe administrimin e metadatës i cili duhet të përfshijë.
- emrin e autoritetit përgjegjës, si tekst i lirë;
- një adresë e-maili të kontaktit, si një varg karakteresh.
10.2 Data e metadatës:
Data e cila specifikon kur metadata është krijuar ose përditësuar. Kjo datë duhet të shprehet në përputhje me ISO 8601.
10.3 Gjuha e metadatës:
Kjo është gjuha në të cilën janë shprehur elementet e metadatës.
Vlera domain e këtij elementi të metadatës është e kufizuar në gjuhët e përcaktuara në ISO 639-2.
11. Sistemi koordinativ
Përcakton Sistemin Koordinativ Referencë në të cilën janë të dhënat gjeohapësinore, grupet e të dhënave gjeohapësinore si dhe shërbimet e të dhënave gjeohapësinore.
Vlera domain e këtij elementi të metadatës është teksti i lirë.
KREU III
INSTRUKSIONE MBI SHUMËLLOJSHMËRINË DHE KUSHTET E ELEMENTEVE TË METADATËS
Metadata që përshkruan një burim që do ti përmbahet një të dhëne gjeohapësinore ose një grupi të dhënash gjeohapësinore, përbëhet nga elementet e metadatës ose një grup elementesh të metadatës të listuar në tabelën 1 ndërsa metadata që përshkruan një shërbim të dhënash gjeoha-pësinore përbëhet nga elementet e metadatës ose një grup elementesh të metadatës të listuar në tabelën 2.
Këto elemente ose grupe elementesh të metadatës duhet të jenë në përputhje me shumë-llojshmërinë e parashikuar dhe kushtet përkatëse të paraqitura në tabelat 1 dhe 2.
Kur nuk është shprehur asnjë kusht në lidhje me një element specifik të metadatës, atëherë ai element është i detyrueshëm.
Tabelat paraqesin informacionin e mëposhtëm:
- Kolona e parë paraqet referencën në kreun II, duke përcaktuar elementin ose grupin e elementeve të metadatës.
- Kolona e dytë paraqet emrin e elementit ose grupit të elementeve të metadatës.
- Kolona e tretë specifikon shumëllojshmërinë e elementeve të metadatës. Shprehja e shumë-llojshmërisë ndjek logjikën e shumëllojshmërisë së gjuhës së unifikuar të modelimit (UML) në të cilën:
- 1 do të thotë se duhet të ketë vetëm një instancë të këtij elementi të metadatës në rezultat.
- 1.. * do të thotë se duhet të ketë të paktën një instancë të këtij elementi në rezultat.
- 0..1 tregon se prezenca e këtij elementi të metadatës në rezultat është e kushtëzuar por mund të ndodhë vetëm një herë.
- 0.. * tregon se prezenca e këtij elementi të metadatës është e kushtëzuar por mund të ndodhë një herë ose më shumë.
- Kur shumëllojshmëria është 0..1 ose 0.. * kushtet përcaktojnë kur elementet e metadatës janë të mandatuar.
- Kolona e katërt përmban shprehje të kushteve kur shumëllojshmëria e elementit nuk i përkon të gjithë tipave të burimeve. Gjithë elementet janë të detyrueshme në kushte të ndryshme.
Tabela 1. Metadata për të dhëna dhe grupe të dhënash gjeohapësinore
Referenca
Elementet e metadatës
Shumëllojshmëria
Kushtet
1.1
Titulli i burimit
1
1.2
Abstrakti i burimit
1
1.3
Tipi i burimit
1
1.4
Lokalizuesi i burimit
0..*
E detyrueshme n.q.s. një URL është e vlefshme për të marrë më shumë informacion mbi burimin dhe/ose shërbimet lidhur me aksesimin.
1.5
Idenfitifukuesi unik i burimit
1..*
1.7
Gjuha e burimit
0..*
E detyrueshme n.q.s. burimi përmban informacion të tipit tekst.
2.1
Kategoria e temës
1..*
3
Fjalë kyçe
1..*
4.1
Kuti e kornizës gjeografike
1..*
5
Referenca kohore
1..*
6.1
Cikli i jetës
1
6.2
Rezolucioni gjeohapësinor
0..*
E detyrueshme për të dhëna ose grupe të dhënash n.q.s. një shkallë ekuivalence ose rezolucioni mund të specifikohet.
7
Përputhshmëria
1..*
8.1
Kushtet e aksesimit dhe përdorimit
1..*
8.2
Kufizimi për aksesin publik
1..*
9
Autoriteti përgjegjës
1..*
10.1
Pika e kontaktit të metadatës
1..*
10.2
Data e metadatës
1
10.3
Gjuha e metadatës
1
11
Sistemi Koordinativ
1..*
Tabela 2. Metadata për shërbimet gjeohapësinore
Referenca
Elementet e metadatës
Shumëllojshmëria
Kushtet
1.1
Titulli i burimit
1
1.2
Abstrakti i burimit
1
1.3
Tipi i burimit
1
1.4
Lokalizuesi i burimit
0..*
E detyrueshme n.q.s. lidhja me shërbimin është e mundur
1.6
Burim i çiftëzuar
0..*
E detyrueshme n.q.s. lidhja me të dhënat mbi të cilat shërbimi operon është e mundur
2.2
Tipi i shërbimit të të dhënave gjeohapësinore
1
3
Fjalë kyçe
1..*
4.1
Kutia e kornizës gjeografike
0…*
E detyrueshme për shërbime me përmbajtje të përcaktuar gjeografike
5
Referenca kohore
1..*
6.2
Rezolucioni
gjeohapësinor
0..*
E detyrueshme kur ka një kufizim në rezolucionin hapësinor për këtë shërbim.
7
Përputhshmëria
1..*
8.1
Kushtet për aksesim dhe përdorim
1..*
8.2
Kufizimet për aksesin publik
1..*
9
Autoriteti përgjegjës
1..*
10.1
Pika e kontaktit të metadatës
1..*
10.2
Data e metadatës
1
10.3
Gjuha e metadatës
1
11
Sistemi Koordinativ
1..*
KREU IV
VLERAT “DOMAIN” DHE KATALOGIMI I METADATAVE
Për vlerat ku specifikohen elementet e metadatës të përcaktuara në kreun II, vlerat domain të përshkruara në këtë kre nga pika 1 deri në pikën 6, duhet të përdoren sipas kombinimeve të shprehura në tabelat 1 dhe 2 të kreut III.
Në lidhje me një temë të caktuar, secila vlerë përcaktohet nga:
- një identifikues numerik;
- një emër tekstual;
- një emër neutral gjuhësor për kompjuterë (vlera e shprehur në kllapa);
- një përshkrim opsional apo përkufizim.
1. Llojet e burimeve
1.1 Të dhënat gjeohapësinore (të dhënat)
1.2 Grupet e të dhënave gjeohapësinore (grupet e të dhënave)
1.3 Shërbimet e të dhënave apo grupe gjeohapësinore (shërbimet)
2. Përputhshmëria e EN ISO 19115 me temat e nenit 11 të ligjit nr. 72/2012
2.1. Fermat bujqësore - Rritja e kafshëve dhe/ose kultivimi i bimëve. Kjo kategori vlen për temën q) “Infrastruktura bujqësore dhe akuakultura” të nenit 11 të ligjit nr. 72/2012.
2.2. Biota - Flora dhe / ose fauna në mjedisin natyror. Kjo kategori vlen për temën xh) “Shpërndarja e specieve” të nenit 11 të ligjit nr. 72/2012.
2.3. Kufijtë- Juridiksioni territorial. Kjo kategori vlen për temën d) “Kufijtë e njësive administrative” dhe temën k) “Njësitë statistikore” të nenit 11 të ligjit nr. 72/2012.
2.4. Klimatologjia/ meteorologjia/ atmosfera. Proceset dhe fenomenet e atmosferës. Kjo kategori vlen për temën sh) “Kushtet atmosferike” dhe temën t) “Meteorologjia” të nenit 11 të ligjit nr. 72/2012.
2.5. Ekonomia - Aktivitetet ekonomike në fushën e energjisë dhe minierave. Kjo kategori vlen për temën y) “Burimet energjitike” dhe temën z) “Burimet minerare” të nenit 11 të ligjit nr. 72/2012.
2.6. Lartësia- Lartësia mbi ose nën nivelin e detit. Kjo kategori vlen për temën gj) “Modeli dixhital i terrenit” të nenit 11 të ligjit nr. 72/2012.
2.7. Mjedisi - Burimet e mjedisit, mbrojtja dhe ruajtja e tij. Kjo kategori vlen për temën g) “Zonat e mbrojtura” të nenit 11 të ligjit nr. 72/2012.
2.8. Informacioni gjeoshkencor- Informacioni në lidhje me shkencat e tokës. Kjo kategori vlen për temën j) “Gjeologjia” dhe temën s) “Zonat me rreziqe natyrore” të nenit 11 të ligjit nr. 72/2012.
2.9. Shëndeti- Shëndeti, shërbimet shëndetësore dhe siguria shëndetësore. Kjo kategori vlen për temën n) “Shëndeti injerëzve dhe siguria e tij” të nenit 11 të ligjit nr. 72/2012.
2.10. Imazhi i hartës bazë / Mbulesa e tokës- Kjo kategori vlen për temën i) “Ortoimazheria” dhe temën h) “Mbulesa e tokës” të nenit 11 të ligjit nr. 72/2012.
2.11. Inteligjenca Ushtarake - Bazat ushtarake, strukturat dhe aktiviteteti i tyre. Kjo kategori nuk zbatohet në mënyrë specifike për ndonjë nga temat nenit 11 të ligjit nr. 72/2012.
2.12. Ujërat - Karakteristika të burimeve ujore, sistemet e kullimit dhe karakteristikat e tyre. Kjo kategori vlen për temën f) “Hidrografia” të nenit 11 të ligjit nr. 72/2012
2.13. Emërtimet gjeografike dhe vendndodhja. Kjo kategori vlen për temën c) “Emërtimet gjeografike” dhe temën dh) “Sistemi i adresave” të nenit 11 të ligjit nr. 72/2012.
2.14. Oqeanet. Karakteristikat dhe kushtet fizike të oqeaneve. Kjo kategori vlen për temën u) “Detet” të nenit 11 të ligjit nr. 72/2012.
2.15 Kadastra dhe planifikimi - Informacion i cili përdoret për veprime të që kanë të bëjnë me përdorimin dhe statusin juridiktë tokës. Kjo kategori vlen për temën e) “Parcelat kadastrale”, temën m) “Përdorimi i tokës” dhe temën rr) “Zonat me përdorim të kufizuar” të nenit 11 të ligjit nr. 72/2012.
2.16. Shoqëria - Karakteristikat e shoqërisë dhe kulturave shoqërore. Kjo kategori vlen për temën r) “Demografia” të nenit 11 të ligjit nr. 72/2012.
2.17. Strukturat ndërtimore - Objekt të ndërtuara nga njeriu për qëllime të ndryshme. Kjo kategori vlen për temën l) “Ndërtesat”, temën o) “Infrastruktura për monitorimin e mjedisit” dhe temën p) “Infrastruktura industriale” të nenit 11 të ligjit nr. 72/2012.
2.18. Transporti - Infrastruktura dhe rrjetet për transportin e njerëzve dhe mallrave. Kjo kategori vlen për temën ë) “Rrjetet e transportit” të nenit 11 të ligjit nr. 72/2012.
2.19. Shërbimet/komunikimi - Shërbimet qeveritare që kanë të bëjnë me energjinë, ujin, pastrimin/infrastruktura e shërbimeve. Kjo kategori vlen për temën nj) “Infrastruktura urbane dhe shërbimet qeveritare” të nenit 11 të ligjit nr. 72/2012.
3. Llojet e shërbimeve të të dhënave gjeohapësinore
3.1. Shërbimi i Kërkimit (zbulimit)- Shërbim që bën të mundur kërkimin e të dhënave gjeohapësinore, grupet e të dhënave gjeohapësinore dhe shërbimet për të dhënat gjeohapësinore në bazë të përmbajtjes së metadatës korresponduese dhe për të shfaqur përmbajtjen e metadatave
3.2. Shërbimi i konsultimit (pamjes) - Shërbime me anë të të cilave bëhet e mundur minimalisht shfaqja, lundrimi, zmadhimi apo zvogëlimi, shtresëzimi i grupeve të të dhënave gjeohapësinore që shfaqen dhe shfaqja e legjendës së informacionit dhe të çdo përmbajtjeje relevante të metadatatës;
3.3. Shërbimi i shkarkimit (daunlodimi) - Shërbim që mundëson shkarkimin e kopjeve ose pjesëve të grupeve të të dhënave gjeohapësinore dhe, kur është rasti, aksesi i drejtpërdrejtë në to.
3.4.Shërbimi për transformimin (transformimi) - Shërbim që mundëson cilave transformimin i grupeve të të dhënave gjeo-hapë-sinore, me qëllim realizimin e ndërveprueshmërisë.
3.5. Shërbimi i evokimit (thirrjes) - Shërbim që mundëson evokimin e shërbimeve për të dhënat, grupet e të dhënave dhe shërbimet gjeoha-pësinore.
3.6. Shërbime të tjera
4. Klasifikimi i shërbimeve të të dhënave gjeohapësinore
Fjalët kyçe janë të bazuara në taksonominë e shërbimeve gjeografike të EN ISO 19119. Kjo taksonomi është e organizuar në kategori dhe nënkategori ku nënkategoritë përcaktojnë vlerën domain të shërbimeve të klasifikimit të të dhënave gjeohapësinore
4.1 Shërbime gjeografike të ndërveprimit njerëzor (humanInteractionService)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.1.1 Observuesi i katalogut (human Catalogue Viewer) - Shërbim klienti që lejon një përdorues të ndërveprojë me një katalog të lokalizuar, të kërkojë dhe të administrojë metadatat rreth të dhënave gjeografike dhe shërbimeve gjeografike
4.1.2 Observuesi gjeografik (human Geographic Viewer)- Shërbim klienti që lejon një përdorues të shikoj një ose më shumë mbledhje karakteristikash ose mbulime.
4.1.3 Observuesi gjeografik i faqes elektronike (human Geographic Spreadsheet Viewer) - Shërbim klienti që lejon një përdorues të ndërveprojë me disa objekte të dhënash dhe të kërkojë llogaritje të ngjashme me një faqe elektronike aritmetike por të shtrirë në të dhëna gjeografike.
4.1.4 Shërbim shtimi (human Service Editor) - Shërbim klienti që lejon një përdorues të kontrolloj shërbimet e përpunimeve gjeografik.
4.1.5 Zinxhiri (human Chain Definition Editor) - Siguron ndërveprim përdoruesi me një shërbim zinxhiri përcaktimi.
4.1.6 Administratori i aprovimit të fluksit (HumanWorkflowEnactmentManager) - Siguron ndërveprim të përdoruesit me një shërbim për aprovimin të fluksit të punës.
4.1.7 Editori i karakteristikave gjeografike (humanGeographicFeatureEditor) - Observuesi gjeografik që lejon një përdorues të ndërveprojë me karakteristikat e të dhënave.
4.1.8 Editori i simboleve gjeografike (human Geographic Symbol Editor) - Shërbim klienti që lejon një përdorues të zgjedhë dhe administrojë simbole librarie.
4.1.9 Editori i karakteristikave përgjithësuese (humanFeatureGeneralizationEditor) - Shërbim klienti që lejon një përdorues të ndryshojë (modifikojë) karakteristikat hartografike të një karakteristike ose grupi karakteristikash duke thjeshtëzuar pamjen e tij, duke ruajtur elementet e tij të spikatur - ekuivalenti hapësinor i thjeshtë-zimit.
4.1.10 Observuesi i strukturës së të dhënave gjeografike (human Geographic Data Structure Viewer). Shërbim klienti që lejon një përdorues të aksesojë një pjesë të të dhënës për të parë strukturën e saj të brendshme.
4.2 Shërbim i administrimit të modeleve/ informacionit gjeografik (info Management Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.2.1 Shërbim i aksesimit të karakteristikave (infoFeatureAccessService) - Shërbim që i lejon një klienti të ketë akses për të administruar një grupi karakteristikash.
4.2.2 Shërbim i aksesimit të hartës (infoMapAccessService) - Shërbim që i mundëson një klienti aksesimin e një grafike gjeografike, p.sh., imazhe të të dhënave gjeografike.
4.2.3 Shërbim i aksesimit (hapjes) së mbulimit (info Coverage Access Service) - Shërbim që i mundëson një klienti aksesimin për dhe administrimin e një grupi mbulimi.
4.2.4 Shërbim i përshkrimit të sensorëve (info Sensor Description Service) - Shërbim që ofron përshkrimin e një sensori mbulimi, duke përfshirë sensor vendndodhjeje dhe orientimi, si dhe karakteristikat gjeometrike, dinamike dhe radiometrike të sensorit për qëllime gjeo-procesimi.
4.2.5 Shërbim i aksesimit të produktit (info Product Access Service) - Shërbim që ofron akses dhe administrim të një depozite produktesh gjeografike.
4.2.6 Shërbim për llojet e karakteristikave (info Feature Type Service) - Shërbim që i ofron klientit aksesim dhe administrim të një mbledhjeje e llojeve të përcaktimit
4.2.7 Shërbimi i katalogut (info Catalogue Service) - Shërbim që ofron shërbime zbulimi dhe administrimi në një grup metadatash rreth shembujve (fakteve).
4.2.8 Shërbim i regjistrimit (info Registry Service) - Shërbim që ofron akses te një grup metadatash rreth tipave.
4.2.9 Shërbim informues (info Gazetteer Service) - Shërbim që ofron akses në një direktori të nënklasave të një klase apo klasave të fenomeneve të botës reale të cilat përmbajnë disa informacione në lidhje me pozicionin.
4.2.10 Shërbim i menaxhimit të porosive (info Order Handling Service) - Shërbim që i ofron klientit mundësinë të porositë produkte nga një furnitor.
4.2.11 Shërbim i kontrollit të statusit (info Standing Order Service) - Shërbim për menaxhimin e porosive që lejon një përdorues të kërkojë që një produkt që ndodhet në një zonë të caktuar gjeografike të shpërndahet pasi të jetë në dispozicion.
4.3 Shërbimet e menaxhimit të detyrës (task Management Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.3.1 Shërbimi zinxhir i përcaktimit (chain Definition Service) - Shërbim për të përcaktuar një zinxhir dhe për ta mundësuar atë të ekzekutohet nga shërbimi i miratimit të fluksit të punës.
4.3.2 Shërbim i miratimit të fluksit të punës (workflow Enactment Service) - Shërbimi i miratimit të fluksit të punës interpreton një zinxhir dhe kontrollon instalimin e shërbimeve dhe renditjes së aktiviteteve
4.3.3 Shërbimi i regjistrimit (subscription Service)- Shërbim që lejon klientët të regjistrohen për njoftime rreth ngjarjeve.
4.4 Shërbimet e përpunimit gjeohapësinor (spatial Processing Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.4.1 Shërbim i konvertimit të koordinatave (spatial Coordinate Conversion Service) - Shërbim për të ndryshuar koordinatat nga një sistem Koordinativ në një tjetër që është i lidhur me të njëjtën projeksion.
4.4.2 Shërbim i transformimit të kordinatave (spatial Coordinate Transformation Service) - Shërbim për të ndryshuar koordinatat nga një sistem referimi koordinatash bazuar në një projeksion te një sistem referimi koordinatash në një projeksion të dytë.
4.4.3 Shërbim i konvertimit të mbulimit / vector(spatial Coverage Vector Conversion Service) - Shërbim për të ndryshuar përfaqë-simin hapësinor nga një skemë mbulimi në një skemë vektori, ose anasjelltas
4.4.4 Shërbim i konvertimit të koordinatave të imazhit (spatial Image Coordinate Conversion Service) - Shërbim konvertimi të koordinatave ose transformimi të koordinatave për të ndryshuar sistemin e referimit për një imazh.
4.4.5 Shërbim korrigjimi (spatial Rectification Service) - Shërbim për transfor-mimin e një imazhi në projeksion paralel ortogonal dhe rrjedhimisht në një shkallë konstante.
4.4.6 Shërbim i korrigjimit të ortofotos (spatial Orthorectification Service) - Një shërbim korrigjimi që eliminon animimin e imazhit dhe zhvendosjen për shkak të relievit të terrenit.
4.4.7 Shërbim i korrigjimit të gjeometrisë së elementeve gjeohapësinore (spatialSensor GeometryModelAdjustmentService) - Shërbimi që korrekton modelet e sensorëve gjeometrik në mënyrë që të përmirësojë lidhjen e imazheve me imazhe të tjera dhe/ose me pikat e njohura të terrenit.
4.4.8 Shërbim i konvertimit të gjeometrisë së imazhit gjeohapësinor (spatialImage Geometry Model Conversion Service) - Shërbim që konverton modelet e sensorëve gjeometrik në një tjetër por në të njëjtin model të sensorëve gjeometrik.
4.4.9 Shërbim i nën vendosjes (spatial Subsetting Service) - Shërbim që nxjerr të dhëna të vazhdueshme, nga një burim në një rajon gjeohapësinor, qoftë nga vendndodhja gjeografike ose nga rrjeti koordinativ.
4.4.10 Shërbim i shembullit (spatial Sampling Service) - Shërbim që nxjerr të dhëna nga një burim, duke përdorur një skemë konstante shembujsh qoftë nga vendndodhja gjeografike ose nga rrjeti Koordinativ.
4.4.11 Shërbim i ndryshimit të mbulesës (spatial Tiling Change Service) - Shërbim që ndryshon mbulesën e të dhënave gjeografike
4.4.12 Shërbim i matjes së dimensioneve (spatial Dimension Measurement Service) - Shërbim për të llogaritur dimensione të objekteve të dukshëm në një imazh ose në të dhëna të tjera gjeografike.
4.4.13 Shërbime të manipulimit të karakteristikave (spatial Feature Manipulation Service) - Regjistron një karakteristikë te tjetra, një imazh, ose një tjetër grup të dhënash ose koordinatash, duke korrektuar ndryshime relative ndërrimi, diferenca alternative, diferenca në shkalle dhe diferenca perspektive. Verifikon që të gjitha karakteristikat në koleksion janë topologjikisht konstante sipas rregullave të topologjisë së koleksionit të tipareve, dhe identifikon dhe/ose korrekton mospërputhjet që zbulohen
4.4.14 Shërbim i lidhjes së karakteristikave(spatial Feature Matching Service) - Shërbim që përcakton se cila karakteristikë dhe pjesë e karakteristikave përfaqëson të njëjtën entitet nga bota e vërtetë nga disa burime të dhënash, si p.sh., lidhje e skajeve dhe....
4.4.15 Shërbim i përgjithësimit të karakteristikës (spatial Feature Generalization Service) - Shërbim që zvogëlon variacionin hapësinor në një grup karakteristikash për të rritur efektivitetin e komunikimit duke iu kundërvënë efekteve të padëshiruara të reduktimit të të dhënave.
4.4.16 Shërbim i përcaktimit të itinerarit (spatial Route Determination Service) - Shërbim për të përcaktuar rrugën më të mirë midis dy pikave të specifikuara bazuar mbi parametrat e të dhënave dhe vetitë që janë në koleksionin e tipareve.
4.4.17 Shërbimi i pozicionimit (spatial Positioning Service) - Shërbim i siguruar nga një pajisje pozicionimi për përdorim, e cila shumë qartësisht interpreton informacionin e pozicionit, dhe përcakton në qoftë se rezultatet arrijnë kërkesat për përdorim
4.4.18 Shërbim i analizës së përafërt (spatial Proximity Analysis Service) - Duke na u dhënë një pozicion ose karakteristike gjeografike, gjejmë të gjithë objektet me një grup atributesh të dhëna që janë të lokalizuar brenda pozicionit apo karakteristikës të specifikuar nga përdoruesi.
4.5 Shërbimi i përpunimit tematik (thematic Processing Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.5.1 Shërbim për llogaritjen e parametrit (thematic Goparameter Calculation Service) - Shërbim me anë të të cilit mund të nxjerrim rezultatet sasiore të aplikimit të kërkuar, që nuk janë në dispozicion nga vetë të dhënat e papërpunuara. Shërbim që gjeneron rezultate kuantitative të drejtuara drejtë aplikacionit, të cilat nuk janë të mundura të merren nga të dhënat e papërpunuara.
4.5.2 Shërbimi i klasifikimit të temave (thematic Classification Service) - Shërbim për të klasifikuar të dhëna rajonale gjeografike bazuar në atribute tematike.Shërbim për klasifikimin e rajoneve të të dhënave gjeografike duke u bazuar në atributet e temave
4.5.3 Shërbim i përgjithësimit të tiparit tematik (i grumbullimit të vetive) (thematic Feature Generalization Service) - Shërbim që përgjithëson lloje funksionesh në një koleksion funksionesh për të rritur efektivitetin e komunikimit dhe ulur efektet negative të reduktimit të të dhënave. Shërbim që grumbullon tipat e vetive në një koleksion vetish për të rritur efektivitetin e komunikimit duke luftuar efektet e padëshirueshme të reduktimit të të dhënave
4.5.4 Shërbimi i filtrimit (thematic Subsetting Service) - Shërbim që nxjerr të dhëna nga një burim duke u bazuar në vlerat e disa parametrave.
4.5.5 Shërbimi i numërimit gjeohapësinor (thematic Spatial Counting Service)- Shërbim që numëron vetitë gjeografike.
4.5.6 Shërbim i zbulimit(dedektimit) të ndryshimeve (thematic Change Detection Service) - Shërbim për të gjetur dallimet mes dy grupeve të të dhënave që përfaqësojnë të njëjtën zonë gjeografike në kohë të ndryshme Shërbim për të gjetur ndryshimet midis dy data seteve që paraqesin të njëjtën zonë gjeografike në kohë të ndryshme.
4.5.7 Shërbimi i marrjes së informacionit gjeografik (thematic Geographic Information Extraction Service) - Shërbime që ndihmojnë në marrjen e informacionit mbi terrenin dhe vetitë e tij nga imazhe të largëta dhe të skanuara.
4.5.8 Shërbimi i përpunimit të imazhit (thematicImageProcessingService) - Shërbim për të ndryshuar vlerat e atributeve tematike të një imazhi duke përdorur një funksion matematikor. Shërbim për të ndryshuar vlerat e atributeve të temave të një imazhi duke përdorur funksione matematike.
4.5.9 Shërbimi i gjenerimit me rezolucion të ulët (thematic Reduced Resolution Generation Service)- Shërbim që redukton rezolucionin e një imazhi.
4.5.10 Shërbim i manipulimit të imazhit (thematic Image Manipulation Service) - Shërbime për manipulimin e vlerave të të dhënave në një imazh: ndryshim i ngjyrave dhe kontrastit, vendosja e filtrave të ndryshëm, manipulimi i rezolucionit të imazhit, heqja e deformimeve të imazhit, korrigjime sistematike-radiometrike, ndryshime në ndriçim etj.
4.5.11 Shërbime për kuptimin e imazhit (thematic Image Understanding Service) - Shërbime që ofrojnë dedektim automatik të ndryshimit të imazhit, regjistrim të diferencës së imazhit, shfaqja dhe analizë të rëndësisë së diferencës, diferencim bazuar mbi zonë dhe model.
4.5.12 Shërbime të sintezës së imazhit (thematic Image Synthesis Service) - Shërbim për krijimin ose transformimin e imazhit duke përdorur modele gjeohapësinore kompjuterike, transformime në perspektivë, dhe manipulime të karakteristikave për të përmirësuar shikueshmërinë, mprehtësi e rezolucionit, dhe /ose reduktimi i mbulimit të faktorëve atmosferikë (reve dhe mjegullës)
4.5.13 Manipulimi i imazhit multiband (thematicMultiband Image Manipulation Service)- Shërbim që modifikon një imazh duke përdorur bandat e imazhit
4.5.14 Shërbimi i zbulimit të objektit (për dedektimin e imazhit) (thematic Object Detection Service)- Shërbim për të zbuluar objekte të botës reale në një imazh. Shërbim për detektimin e objekteve reale në një imazh
4.5.15 Shërbimi i analizës gramatikore të gjeoinformacionit (thematic Geoparsing Service) - Shërbim që skanon dokumente tekst për referenca bazuar mbi pozicionin, të tilla si emra vendesh, adresa, kode postare etj. duke i përgatitur për kalim te shërbimi i gjeokodimit.
4.5.16 Shërbimi i gjeokodimit (thematic Geocoding Service)- Shërbim që përmbush referencat tekst të bazuara mbi pozicionin me koordinata gjeografike (ose referenca të tjera gjeohapësinore)
4.6 Shërbimet e përpunimit gjeografik kohor (temporal Processing Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.6.1 Shërbim për transformimin e sistemit të referencës kohore (temporal Reference System Transformation Service) - Shërbim për të ndryshuar vlerat e instancave kohore nga një sistem referimi kohor në një sistem tjetër referimi kohor.
4.6.2 Shërbim filtrues (temporal Subsetting Service) - Shërbim që filtron të dhënat nga një burim në intervale të vazhdueshme bazuar në vlerat e pozicionimit kohor.
4.6.3 Shërbimi i marrjes së mostrave (temporal Sampling Service) - Shërbim që merr të dhënat nga një burim duke përdorur skema të qëndrueshme mostrash bazuar në vlerat e pozicionimit kohor
4.6.4 Shërbim i analizës së përafrimit kohor (temporal Proximity Analysis Service) - Duke u dhënë një interval kohor ose ngjarje, të gjenden të gjithë objektet me një atribut të caktuar që janë të lokalizuara brenda një intervali të specifikuar nga përdoruesi.
4.7 Shërbimet e përpunimit gjeografik të metadatave (metadata Processing Service)
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.7.1 Shërbim për llogaritjen statistikore (metadata Statistical Calculation Service) - Shërbim për të llogaritur statistikat e një grupi të dhënash.
4.7.2 Shërbim për shënimet gjeografike (metadata Geographic Annotation Service) - Shërbim që shton informacion ndihmëse për një imazh apo një veti në një koleksion vetish.
4.8 Shërbimet e komunikimit gjeografik (Comservice).
Kjo kategori përfshin nënkategoritë e mëposhtme:
4.8.1 Shërbime Kodimi (com Encoding Service) - Shërbim që ofron implementimin e rregullave të kodimit dhe ofron një ndërfaqe për funksionalitetet e kodimit dhe dekodimit
4.8.2 Shërbim i transferimit (com Transfer Service) - Shërbim që ofron implementimin e një ose më shumë protokolleve të transportit, që lejojnë të dhënat të transferohen midis sistemeve të shpërndara të informacionit mbi linja komunikimi online ose offline.
4.8.3 Shërbimi i kompresimit gjeografik (com Geographic Compression Service) - Shërbim që konverton pozicione gjeografike të një grupi vetish në formë të kompresuar dhe anasjelltas.
4.8.4 Shërbimi për konvertimin e formatit (comGeographicFormatConversionService) - Shërbim që konverton nga një format në një tjetër të dhënat gjeografike.
4.8.5 Shërbimi i mesazheve (com Messaging Service)- Shërbimi që i lejon disa përdorues të shikojnë, komentojnë dhe modifikojnë një grup vetish njëkohësisht.
4.8.6 Menaxhimi i informacionit në largësi (com Remote File And Executable Management) - Shërbim që mundëson aksesin e klientit në një memorie sekondare për vetitë gjeografike në mënyrë virtuale (sikur të ndodhej aty)
5. Shkalla e konformitetit
5.1 Konformant - Burimi është plotësisht konformant me specifikimet e miratuara.
5.2 Jokonformant - Burimi nuk përputhet me specifikimet e miratuara.
5.3 Nuk vlerësohet - Shkalla e konformitetit nuk është vlerësuar.
6. Rolet dhe përgjegjësitë
6.1 Ofruesi i të dhënave - Pala që mbledh (ofron) informacionin.
6.2 Kujdestari - Pala që pranon llogaridhënien dhe përgjegjësinë për të dhënat dhe siguron kujdesin dhe mirëmbajtjen e burimeve të përshtatshme.
6.3 Pronari - Pala që zotëron ose porosit informacionin gjeohapësinor sipas legjislacionit në fuqi (autoriteti përgjegjës për temën përkatëse).
6.4 Përdoruesi - Pala që përdor informacionin gjeohapësinor të publikuar.
6.5 Shpërndarësi - Pala që shpërndan informacionin.
6.6 Krijues - Pala që ka krijuar informacionin.
6.7 Pika e kontaktit (point Of Contact) - Pala që mund të kontaktohet për marrjen e informacionit në lidhje me burimin e të dhënave e shërbimeve apo përditësimin e tyre (personi i kontaktit të autoritetit përgjegjës për temën përkatëse).
6.8 Investigues kryesor - Pala përgjegjëse për hulumtimin e metodologjisë së mbledhjes së informacionit.
6.9 Përpunuesi - Pala që ka përpunuar të dhënat nëse burimi është modifikuar.
6.10 Botuesi -Pala që ka publikuar informacionin.
6.11 Autori -Autoriteti Përgjegjës për temën sipas nenit 11 të ligjit nr. 72/2012.
KREU V
METADATAT SPECIFIKE PËR ÇDO TEMË
Autoritetet publike përgjegjëse për krijimin dhe mirëmbajtjen e të dhënave gjeohapësinore, të parashikuara në nenin 12 të ligjit nr. 72/2012, në bashkëpunim me ASIG-un, krijojnë, mbledhin dhe përditësojnë metadatat për të dhënat gjeohapësinore, grupet e të dhënave gjeohapësinore dhe shërbimet e të dhënave gjeohapësinore, sipas kësaj rregulloreje, për temat e mëposhtme:
1. Sistemet e rrjeteve gjeografike;
2. Emërtimet gjeografike;
3. Imazhi i hartës bazë;
3. Kufijtë e njësive administrative;
5. Sistemin e adresave;
6. Parcelat kadastrale;
7. Rrjetet e transportit;
8. Hidrografinë;
9. Zonat e mbrojtura(mjedisore dhe trashëgimisë kulturore);
10. Modelin dixhital të terrenit;
11. Mbulesën e tokës;
12. Ortoimazherinë;
13. Gjeologjinë;
14. Njësitë statistikore;
15. Nndërtesat;
16. Pedologjinë;
17. Përdorimin e tokës;
18. Shëndetin e njerëzve dhe sigurinë e tij;
19. Infrastrukturën urbane dhe shërbimet qeveritare;
20. Infrastrukturën për monitorimin e mjedisit;
21. Infrastrukturën industriale;
22. Infrastrukturën bujqësore dhe akua-kulturën;
23. Demografinë;
24. Zonat me përdorim të kufizuar;
25. Zonat me rreziqe natyrore;
26. Kushtet atmosferike;
27. Meteorologjinë;
28. Hidrologjinë;
29. Detet;
30. Zonat ekologjike;
31. Habitatet;
32. Shpërndarjen e specieve;
33. Burimet energjetike;
34. Burimet minerare.
