# Shtojca
METODA E LLOGARITJES
SË PËRMASAVE TË ZONËS KRITIKE TË SHPËRHAPJES SË RREZATIMIT JOJONIZUES TË NJË ANTENE CELULARE
HYRJE
Për një ekspozim sa më të sigurt nga fushat e rrezatimeve jojonizuese janë hartuar në vazhdimësi dokumente të veçanta, të cilat përfaqësojnë mendimin e profesionistëve të nivelit më të lartë dhe të të gjithë organizatave ndërkombëtare në fushën e mbrojtjes nga rrezatimet elektromagnetike për publikun dhe për operatorët.
Nivelet e referencës për zbatim në vende të ndryshme mbështeten në rekomandimet e organizatave të specializuara ndërkombëtare si Komisioni Ndërkombëtar për Mbrojtjen nga Rrezatimi Jojonizues (International Commission on Non-Ionizing Radiation Protection (ICNIRP)) dhe Organizata Botërore e Shëndetësisë (World Health Organization (WHO)):
- ICNIRP “Guidelines for limiting exposure to time-varying electric, magnetic, and electromagnetic fields (up to 300 GHz)”. Health Phys. 74(4):494-522, 1998.
- ICNIRP Statement on the “Guidelines for limiting exposure to time-varying electric, magnetic, and electromagnetic fields (up to 300 GHz)”. Health Physics 97(3):257-258, 2009.
- ICNIRP “Guidelines for limiting exposure to electromagnetic fields (100 kHz to 300 GHz)”. Health Physics 118(5): 483-524, 2020.
- European Commission - Council Recommendation 1999/519/EC on the limitation of exposure of the general public to electromagnetic fields (0 Hz to 300 GHz). 30 July 1999, Official Journal of the European Communities; 42 (L199): 59-70, 1999,
të cilat gjejnë zbatim në VKM nr. 743, datë 16.10.2012 për miratimin e rregullores “Për mbrojtjen e publikut nga rrezatimet jojonizuese”.
Publikimi i Komitetit Evropian për Standardizimin Elektroteknik (CENELEC) EN 50401:2017 është referenca kryesore për rregullatorët evropianë, pasi ky standard bazohet në metodologjinë e IEC 62232:2017 dhe e përshtat atë për zbatimin në kuadrin ligjor të Bashkimit Evropian.
VËSHTRIM I PËRGJITHSHËM
Instalimi i një Stacioni Bazë (SB) dhe antenave të tij, në varësi të gjeometrisë së instalimit, topografisë rrethuese dhe parametrave teknike të gjenerimit të rrezatimit krijon kudo rrotull një fushë rrezatimi jojonizuese shtesë mbi atë natyral.
Në vijim do të shqyrtohen metodat e vlerësimit që duhen përdorur për të vlerësuar ose llogaritur intensitetin e fushës elektromagnetike, densitetin e fuqisë së saj dhe fuqinë e absorbimit specifik (Specific Absoption Rate - SAR). Nëpërmjet këtyre madhësive përcaktohen zonat rreth antenave të SB, ku nuk lejohet qëndrimi i publikut dhe i operatorëve.
Detyrë e projektimit të Stacionit Bazë dhe funksionimit të tij është mbulimi sa më i gjerë dhe cilësor i hapësirës përreth në zona rurale, urbane ose mjedise të mbyllura, por njëkohësisht është edhe kontrolli i vazhdueshëm i niveleve të rrezatimit për mbrojtjen e publikut nga rrezatimet jojonizuese të gjeneruara përreth SB, si dhe përcaktimi i dimensioneve të hapësirës së quajtur Zonë Kritike ose Zonë e Kontrolluar.
Zonë Kritike ose Zonë e Kontrolluar është hapësira rrotull antenës, jashtë së cilës nivelet e densitetit të fuqisë të fushës elektromagnetike, ose të intensitetit të fushës elektrike/magnetike të rrezatimit janë më të ulëta se Nivelet e Referencës, të përcaktuara në legjislacionin shqiptar, nën të cilat sigurohet mbrojtja e publikut.
Bazuar në rregullat ndërkombëtare të prodhimit dhe tregtimit, prodhuesve të sistemeve radio/antena iu kërkohet që t’i japin përdoruesit të produktit radio/antenë informacion për ekspozimin ndaj radiofrekuencave (RF), duke përfshirë kufijtë e pranueshëm të pajtueshmërisë. Kufiri i pajtueshmërisë përcaktohet duke iu referuar dimensioneve të hapësirës së lejuar për ekspozim ndaj RF, nëpërmjet metodave të vlerësimit të intensitetit të fushës RF, densitetit të fuqisë së fushës dhe fuqisë së absorbimit specifik (SAR).
Kufiri i pajtueshmërisë ose kufiri i Zonës Kritike është si një izosipërfaqe 3D që paraqet vendin gjeometrik të pikave rreth antenës, ku ekspozimi është i barabartë me vlerën kufi të zbatuar për ekspozimin në RF, si në figurën më poshtë.
Figura 1: Paraqitje e kufirit të pajtueshmërisë, i cili matematikisht jepet nga funksioni z=f (x,y)
Kufiri i pajtueshmërisë për izosipërfaqen mund të futet në volume me forma të thjeshta të karakterizuara nga një komplet distancash pajtueshmërie për të dhënë kufij më konservatorë, si në figurat më poshtë:
.
Figura 2: Kufiri i pajtueshmërisë - Zona Kritike në koordinata cilindrike
Kufiri i pajtueshmërisë ose hapësira e Zonës Kritike, që mbulon një sektor të antenës përshkruhet nga parametrat CDf, CDb, CDd,a, CDu,a, gjatësia dhe trashësia e antenës, siç tregohet në dyja rastet e treguar në figurën 2. Kudo në hapësirën jashtë izosipërfaqes ekspozimi në RF është nën kufirin e lejuar të ekspozimit, ndërsa brenda saj ekspozimi është mbi kufirin e lejuar.
Kufiri i pajtueshmërisë në formë të një paralelepipedi, treguar më poshtë, mund të përdoret për antenat e drejtuara, p.sh. për antenat panele që janë gjerësisht të përdorura në telekomunikacion.
Figura 3: Kufiri i pajtueshmërisë - Zona Kritike në formë paralelepipedi
VENDOSJA E KUFIRIT TË PËRPUTHSHMËRISË SË ANTENAVE MASSIVE MIMO (OSE BEAMFORMING)
Për produktet e Stacioneve Bazë që janë të pajisur me grup ose varg antenash të destinuara për zbatime me m-MIMO (massive Multiple-Input Multiple-Output), që përfaqëson një lloj të telekomunikacionit “wireless” ose beamforming (fromim të tufës), vlerësimi i kufirit të pajtueshmërisë duhet të marrë në konsideratë të gjithë modelet e përshtatshëm të amplifikimit (gain) të tufave G(φ,θ), që janë të konfiguruara në Stacion Bazë, përfshirë tufën kryesore, lobet dytësorë dhe lobet e tjera, për të gjitha përkuljet elektrike të antenave.
Një shembull i antenës MIMO dhe tufave korresponduese dhe modeleve të mbështjellësve jepen në figurën më poshtë.
a) Antena m-MIMO;
b) Pamje 3D e të gjithë tufave të antenës brenda mbështjellëses;
c) Pamje 3D e mbështjellëses që përfshin të gjithë tufat.
antena m-MIMO
b - Pamje 3D e të gjithë tufave të antenës brenda mbështjellëses
c- Pamje 3D e mbështjellëses që përfshin të gjithë tufat
Figura 4: Antena e tipit massive MIMO dhe tufave elementare korresponduese së bashku me mbështjellësen e tyre
Kufiri i pajtueshmërisë (përmasat e Zonës Kritike për produktin (Stacion Bazë + antenat)) do të përcaktohet duke përdorur çdo metodë të paraqitur në Annex B të IEC 62232:2022, siç është formula e thjeshtë sferike ose metoda të tjera llogaritëse më të avancuara.
Kufijtë e pajtueshmërisë përcaktohen normalisht me matje ose llogaritje për një ose disa konfigurime tipike, në kushtet e përdorimit të fuqisë maksimale dhe parametrave që përcaktojnë konfigurimin në kushtet e zonës ose fushës së largët. Disa nga parametrat kryesorë që përcaktojnë një konfigurim janë:
- fuqia e transmetimit;
- banda e frekuencës;
- gjerësia e bandës;
- teknologjia e përdorur;
- dupleximi sipas kohës dhe frekuencës;
- ushqyesi i antenës;
- humbjet në kabllo;
- informacion për tufat në shqyrtim (amplifikimi, gjerësia horizontale e tufës, gjerësia vertikale e tufës, EIRP etj.).
Për vetë specifikën e teknologjisë dhe instalimit konkret të një stacioni bazë të telefonisë celulare, llogaritjet për vlerësim shqyrtohen kryesisht në zonën e largët të rrezatimit, në të ashtuquajturën fushë e lirë, në gjithë pikat e hapësirës rrotull antenës ku plotësohet kushti r ≥ 2D2/λ, ku r është distanca nga qendra e antenës deri në pikën e vlerësimit të fushës, D është dimensioni më i madh i antenës dhe λ është gjatësia e valës në operim. Në këtë zonë antena konsiderohet si burim pikësor. Kjo është zona në të cilën ka mundësi ekspozimi për publikun.
Në kushtet kur λ ˂ r ≤ 2D2/λ, jemi në kushtet e zonës së afërt dhe aktualisht kjo është zonë ku ka mundësi për ekspozim profesional. Zona e hapësirës për r ˂ λ/4 emërtohet si fushë e afërt reaktive, konfiguracioni i së cilës është mjaft larg modelit të fushës së lirë; këtu edhe profesionistët - operatorët e mirëmbajtjes së stacionit nuk ka arsye të ekspozohen, veç nëse shkelin rregullat e sigurimit teknik.
Mbështetur në vlerësimet teorike, zbatimi i llogaritjeve për fushën e largët në kushtet e fushës së afërt r ≤ 2D2 /λ mbivlerëson ekspozimin, çka nga pikëpamja dozimetrike rrit sigurinë.
Për zonën e fushës së lirë llogaritja e fushës elektromagnetike nuk merr parasysh madhësinë e antenës, e cila supozohet të jetë një burim pikësor. Një antenë hipotetike izotropike përdoret si një referencë për të krahasuar paraqitjen e rrezatimit të antenës praktike: Fuqia P (watt) rrezatohet nga një pikë, uniformisht në sipërfaqen e sferës me rreze r.
Për parashikimet/vlerësimet numerike, nëse për zonën e fushës së afërt zbatohet modeli i fushës së largët (far field) zakonisht merret një rezultat i mbivlerësuar. Prandaj është e rëndësishme që para fillimit të një procedure vlerësimi të pajtueshmërisë të jenë të qartë kufijtë e çdo zone rreth burimit të rrezatimit (Field regions Rec. ITU T K.61(01.2019) f. 5).
Figura 5: Zonat e fushave rreth një burimi EM (dimensioni max. D i antenës të jetë më i madh se gjatësia e valës λ)
Tabela 1: Karakteristikat kryesore të FEM në zona të ndryshme
FEM
Zonë e afërt reaktive
Zonë e afërt reaktive - rrezatuese
Zonë e afërt
rrezatimi
Zonë e largët
rrezatimi
Kufiri i brendshëm
0
λ
3λ
Max. (3λ; 2D2/λ)
Kufiri i jashtëm
λ
3λ
Max. (3λ; 2D2/λ)
∞
Densiteti i fuqisë S [W/m2]
=
=
Jo
Jo
Lokale
Po
Z0
Z0
Z0
= Z0
METODAT E VLERËSIMIT PËR PËRCAKTIMIN E ZONËS KRITIKE
Në teori pika e referencës ose origjina “O” e sistemit koordinativ i korrespondon qendrës së antenës së Stacionit Bazë dhe përputhet me qendrën e një sfere të rrezatimit të antenës në fushën e largët. Për arsye praktike, kur antena e një SB është identifikuar qartë (një antenë e jashtme, ose elementet rrezatuese janë të dukshme), origjina “O” e sistemit koordinativ do të jetë qendra e sipërfaqes së pasme ose të përparme në rastin e antenave panel, qendra e antenës në rastin e antenave omnidireksionale ose çdo pikë karakteristike. Në rastin e SB-së, ku nuk ka tregues të jashtëm të pozicionit të antenës (antena të instaluara brenda një kutie), pika e referencës duhet të merret në mesin e sipërfaqes së mbulesës.
Figura 6: Sistemet e koordinatave karteziane, cilindrike dhe sferike për antenat e stacioneve bazëFigura 6: Sistemet e koordinatave karteziane, cilindrike dhe sferike për antenat e stacioneve bazëNë përputhje me metodën e vlerësimit, koordinatat për antenën dhe SB-në përshkruhen në sistemet kartezian, cilindrik dhe sferik.
Figura 6: Sistemet e koordinatave karteziane, cilindrike dhe sferike për antenat e stacioneve bazë
Figura 6: Sistemet e koordinatave karteziane, cilindrike dhe sferike për antenat e stacioneve bazë
Në mungesë të përkuljes së tufës, drejtimi (qendror) i tufës së antenës përputhet me drejtimin (Ox) dhe në koordinatat sferike me azimut = 00 dhe ngritje/përkulje = 00. Ky sistem koordinativ është harmonizuar në praktikën e përgjithshme të operatorëve, prodhuesve të SB dhe të antenave.
Tabelat e parametrave/variablat
Tabela I. Variablat/parametrat e dimensioneve
Variabli
Njësia matëse
Përshkrim
dxx
m
Distanca mes pikave që vlerësohen
rxx
m
Rrezja nga pika e origjinës
Lxx
m
Përmasat e antenës, zona e matjeve etj.
CD
m
Zona e sigurisë/distanca kritike ose e pajtueshmërisë
Tabela II. Variablat që lidhen me fuqinë e RF-së
Variabli
Njësia matëse
Përshkrim
Shënim
P ose Pmes
W
Fuqia mesatare e transmetuar në kohë
P mund të paraqitet dhe në dBm
EIRP (, θ)
W
Ekuivalente e fuqisë izotropike
EIRP (, θ) mund të paraqitet dhe në dBm
Tabela III. Parametrat e antenës që paraqiten nga dokumentacioni i prodhuesit
Variabli
Njësia
Përshkrim
D
Krahasuese Lineare
Drejtueshmëria max. e antenës për frekuencën përkatëse
Dφ,θ
Krahasuese Lineare
Drejtueshmëria e antenës në një pikë të caktuar sipas koordinatave sferike për frekuencën përkatëse
G
dBi
Amplifikimi max. i antenës për frekuencën përkatëse
G(φ,θ)
dBi
Amplifikimi i antenës për frekuencën përkatëse në një pikë të caktuar sipas koordinatave sferike
Gside lobe
dBi
Amplifikimi max. për lobin sekondar të antenës për frekuencën përkatëse
Δφ3dB
Radian
Këndi për hapjen horizontale të antenës për frekuencën përkatëse
Δθ3dB
Radian
Këndi për hapjen vertikale të antenës për frekuencën përkatëse
γ
Radian
Përkulja elektrike e rrezes kryesore të antenës në planin x-y për frekuencën përkatëse
Ne
Numër i plotë
Numri i elementeve të antenës që merret në shqyrtim
Tabela IV. Variablat e metrikës së ekspozimit
Variabli
Njësia
Përshkrim
Shënim
S
W m−2
Densiteti i fuqisë në varësi të E & H
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
E
V m−1
Vlera RMS për fushën elektrike në varësi të kohës
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
H
A m−1
Vlera RMS për intensitetin magnetik në varësi të kohës
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
SARwb
W kg−1
Përthithja dozimetrike për trupin e njeriut
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
SAR10g
W kg−1
SAR maksimal për 10 g
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
SAR1g
W kg−1
SAR maksimal për 1 g
Në varësi të kohës në bazë të modulimit ose vlerës konstante në varësi të fuqisë P ose Pavg
LLOGARITJE E THJESHTUAR E INTENSITETIT DHE E DENSITETIT TË FUQISË TË FUSHËS SË RF-së
Një rast tipik i vlerësimit të ekspozimit në RF nga një SB është ai i paraqitur në skicën më poshtë:
Figura 7: Rasti tipik për vlerësimin e ekspozimit RF
Për një vlerësim të parë, densitetet e fuqisë ekuivalente të mesatarizuar në hapësirë dhe densitetit maksimal (peak) në hapësirë mund të vlerësohen duke përdorur formulat e thjeshta të përafrimit sferik të përshkruara në ekuacionet (1) ose (2) në vijim. Në formula do të përdoren variablat e specifikuar nga tabelat e mësipërme:
Vlerat e mesatares kuadratike (RMS - Root Mean Square) të intensitetit të fushës elektrikë E dhe intensitetit të fushës magnetike H gjenden duke përdorur ekuacionet (3) dhe (4):
Distanca e pajtueshmërisë (CD ose Rm) në këtë drejtim mund të vlerësohet duke përdorur ekuacionet (5) ose (6).
Në rast se është e pranishme një sipërfaqe reflektuese e tokës/tarracës dhe ka të ngjarë të ndikojë ekspozimin në RF (si në figurën 8), mund të përdoret formula klasike sferike sipas ekuacionit (7):
|| - është koeficienti i reflektimit, p.sh. plani truallit/terrenit ose objekteve përreth.
Figura 8: Rasti tipik për vlerësimin e ekspozimit RF bashkë me reflektimin e truallit
Nëse koeficienti i reflektimit |u| = 1 + || njihet, mund të përdoret në ekuacionin (7).
VLERËSIMI I FUSHAVE EM TË GJENERUARA NGA n- ANTENA
Llogaritja e fushës elektromagnetike rezultante realizohet nëpërmjet formulave të fushës së largët në një sistem antenash: fusha elektromagnetike totale (rezultante) merret nëpërmjet superpozimit të densitetit të fuqisë së fushës (ose intensitetit të fushës elektrike/magnetike) të çdo antene. Kjo paraqitet gjeometrikisht në figurën më poshtë.
Figura 9: Fusha elektromagnetike rezultante e një sistemi antenash
Për antenën e n-të, intensiteti i fushës elektrike jepet nga:
dhe për fushën elektrike rezultante, të prodhuar nga të gjithë antenat kemi:
Për rastet kur grupet e antenave në vlerësim transmetojnë në breza të ndryshëm frekuencash, ose kur ka dhe grupe antenash të tjera të operatorëve fqinj dhe kur të gjithë transmetimet realizohen në frekuenca më të mëdha se 10 MHz, vlerësimi i Indeksit Total të Ekspozimit në frekuenca të ndryshme bëhet nëpërmjet inekuacionit të mëposhtëm:
ku Sf është densiteti i fuqisë ekuivalente në frekuencën rënëse f dhe Sf,max është niveli i referencës për frekuencën f.
LLOGARITJET E MADHËSIVE TË FUSHËS EM TË EMETUAR
Llogaritja e madhësisë së densitetit të fuqisë së një vale plane S, të emetuar nga një antenë e telefonisë së lëvizshme, e konsideruar si antenë pikësore, përgjithësisht realizohet nga formula më poshtë:
ku:
S - densiteti i fuqisë së valës plane ekuivalente, i shprehur në W/m2;
P - fuqia e antenës në hyrje në Watt (= numri i mbartësve x fuqia për çdo mbartës);
G - koeficienti i amplifikimit izotropik të antenës, ku si referencë është marrë antena izotropike, i shprehur në dBi;
r - distanca nga qendra e antenës deri në pikën ku llogaritet intensiteti i rrezatimit, i shprehur në m;
u = 1 + - faktori rregullues që merr në konsideratë reflektimin nga trualli ose nga objektet me të afërt me antenat. Faktori u i përket intervalit [1.0, 2.0], ku 1.0 i përket përhapjes në hapësirën e lirë, pa reflektim dhe 2.0 i përket sipërfaqeve plane përcjellëse.
Përgjithësisht rekomandohet që vlera e koeficientit të reflektimit të jetë jo më e madhe se 1,6 (shih bibliografinë [3], [4], [10]).
F - faktori i reduktimit të fuqisë për instalimet rurale dhe urbane në antenat që funksionojnë vetëm me teknologjitë m-MIMO dhe beamforming të gjeneratës LTE & 5G New Radio. Vetëm në rastin e teknologjisë m-MIMO që funksionon me teknologjinë TDD, në varësi edhe të “downlink duty cycle”, F rekomandohet 0.25.
Nga formula me sipër, llogaritet distanca minimale e sigurisë së Zonës Kritike për një frekuencë të caktuar të gjeneruar nga antena, me kushtin që densiteti i fuqisë të mos kalojë nivelin e referencës Smax për frekuencën në shqyrtim:
Relacionet e mësipërme mund të përdoren në përgjithësi për llogaritjen e rrezatimit elektro- magnetik në mjedisin rreth antenave të tjera të transmetimit në frekuencat radio, TV dhe telefonisë celulare, në rastet kur prania e tyre merret parasysh në studim.
PARAMETRAT KRYESORË PËR ZONËN KRITIKE
Modeli më i përdorshëm i vlerësimit për Zonën Kritike (përcaktimi i kufirit të pajtueshmërisë) mbështetet në modelin sferik, gjithmonë duke ndjekur supozimin e fushës së largët dhe duke e konsideruar burimin (antenën) si burim pikësor, nëpërmjet të cilit përcaktohen distanca e sigurisë në drejtimin e qendror të tufës së rrezatimit dhe distancën e sigurisë në drejtimin e lobit të poshtëm të difuzimit të tufës (dhe në të gjithë drejtimet ku mund të ketë prekje të zonave publike).
Në kushtet e mësipërme, llogaritja e vlerës së densitetit të fuqisë së rrezatimit të një vale plane S që emetohet nga antena bëhet sipas formulës të mësipërme (11).
Antenat e rrjeteve të telefonisë celulare nuk janë izotropike, përkundrazi janë antena me një rrezatim të përqendruar në një zonë të caktuar të hapësirës. Densiteti i fuqisë së rrezatimit dhe koeficienti i amplifikimit nuk mund të jetë uniform, por janë në funksion të këndeve θ dhe φ. Në këtë kuadër kemi:
a) amplifikim në drejtimin parësor të përhapjes së valës në bazë të diagramit të rrezatimit të antenës Gm [dBi] (për lobin kryesor);
b) amplifikim në drejtimin dytësor të antenës Gs [dBi] (për lobin dytësor);
c) këndin e hapjes vertikale θs në lobin kryesor.
Për të vlerësuar dimensionet e Zonës Kritike rreth antenës përdoren dy parametra Rm dhe Rs, që janë përkatësisht distanca e sigurisë, në varësi të lobit kryesor të diagramit së rrezatimit dhe të lobit dytësor të kësaj diagrame, të cilat llogariten si më poshtë:
Në vazhdim kontrollohet nëse distanca H e qendrës së antenës nga niveli i terrenit ku është montuar shtylla e antenës është më e madhe nga distanca Rm cos() + 2.0 m, ose nga distanca Rs + 2.0 m, e cila lidhet drejtpërdrejtë me lobin dytësor.
ku : ω = 90ο - ψ - α/2 dhe
ψ - këndi i përkuljes mekanike + përkuljes elektrike të drejtimit kryesor të përhapjes së rrezatimit në lidhje me horizontin (downtilt). Përkulja e përgjithshme jepet si shumë e përkuljes elektrike me përkuljen mekanike
Kushti siguron të gjithë zonën ku mund të kemi aktivitet njerëzor pranë antenës, si p.sh. lëvizjen e një personi 2 m të gjatë shumë pranë antenës.
Figura 10: Dimensionet e Zonës Kritike rreth antenës
Figura 11: Gjeometria e kushteve të sigurisë teknike pranë një antene
SHTOJCA 1
SUPOZIMET THEMELORE BAZUAR NË DIAGRAMET E RREZATIMIT
1. Antenat nuk rrezatojnë në mënyrë të njëtrajtshme në hapësirën përreth, por emetojnë rrezatim EM që është i përqendruar në drejtime të caktuara. Për këtë arsye, koeficienti i amplifikimit izotropik G(θ,φ) [dBi] është funksion i koordinatave polare këndore, pra këndit të ngritjes/përkuljes θ (0°<θ<180°) dhe këndit të azimutit φ (-180°<φ<180°).
Antenat klasifikohen si antena omnidireksionale, kur ato rrezatojnë në mënyrë të njëtrajtshme në të gjithë hapësirën dhe antena të drejtuara, kur energjia e rrezatimit drejtohet sipas një hapje të kufizuar.
Vlerat tipike për hapjen ndërmjet këndeve të gjysmëfuqisë në rrafshin horizontal janë përgjithësisht rreth 60° për antenat e drejtuara të telefonave celularë.
2. Modelet e rrezatimit të përdorura në llogaritjet merren nga modelet teorike të prodhuesve përmes supozimeve të përcaktuara. Me metodën e analizuar më poshtë, modelet e rrezatimit konsiderohen si mbështjellëse të modeleve teorike. Kjo mënyrë shmang pasaktësitë, për shkak të kushteve joideale të funksionimit të antenave në çdo rast, mbështjellësja e modelit të rrezatimit është shumë më konservative se modeli teorik i rrezatimit.
3. Për të thjeshtësuar metodën e llogaritjes, mund të supozohet se disa antena me rrezatim të drejtuar, të vendosura në të njëjtin mast/shtyllë ose në një mast shumë afër dhe afërsisht në të njëjtën lartësi, prodhojnë një model rrezatimi që i afrohet atij të një antene të drejtuar, nëse këndi relativ azimutal midis dy antenave të afërta është më i madh se gjysma e shumës së këndeve të gjysmëfuqive të këtyre antenave në planin horizontal. Prandaj, në këto raste, në vend të antenave reale mund të konsiderohet një antenë ekuivalente e drejtuar, me qendrën gjeometrike të dy antenave të drejtuara. Karakteristikat e emetimit të antenës ekuivalente njëdrejtimëshe merren duke kombinuar me karakteristikat më të forta të antenave reale. Rrjedhimisht, modeli i rrezatimit që konsiderohet nuk varet nga këndi azimutal dhe do të shqyrtohet vetëm plani vertikal (në lidhje me këndin θ, sipas shpjegimit në vijim). Nëse këndi azimutal relativ midis dy antenave të afërta është me i vogël se gjysmëshuma e këndeve të tyre të gjysmëfuqisë, atëherë në vend të dy grupeve të antenave, merret një antenë ekuivalente, me fuqi transmetimi shumën e të dyja grupeve të antenave dhe me karakteristika transmetimi që janë më pak të favorshmet nga të dyja grupet e antenave në shqyrtim.
4. Mbështjellësja e modelit të rrezatimit në planin vertikal. Në këtë rast, merret parasysh një tablo e rrezatimit të amplifikimit maksimal, e pavarur nga këndi i azimutit φ. Mbështjellësja e tablosë së rrezatimit në rrafshin vertikal është ndërtuar bazuar në modelet teorike të rrezatimit të vargjeve/grupeve të antenave për çdo varg/grup antene, si më poshtë:
4a) Përcakton koeficientin e amplifikimit maksimal Gm (dBi) në lobin kryesor;
4b) Përcakton koeficientin e amplifikimit maksimal Gs (dBi) në lobin anësor dytësor më të madh;
4c) Përcakton këndin e gjysmëfuqisë θ-3dB; për arsye sigurie, vlera e këndit rritet me 5o;
4d) Përcakton këndin θs ndërmjet dy drejtimeve, në lobin kryesor, në të cilin koeficienti i amplifikimit ka vlerën Gs. Për arsye sigurie, vlera e këndit rritet me 5o;
4e) Për rastit më të keq merren vlerat për Gm, Gs, θs, θ-3dB dhe ψ;
4f) Mbështjellësja e modelit të rrezatimit jepet nga funksioni i koeficientit të amplifikimit G(θ):
Figura 1.1: Mbështjellësja e diagrameve të rrezatimit në rrafshin vertikal
Termi max (Gs, Gm - 3dB) futet për të mbuluar rastin kur Gm - Gs < 3dB. Në këtë rast merret amplifikimi Gs në vend të Gm - 3dB në relacionin (1.1).
Në të njëjtën mënyrë analizohet dhe mbështjellësja e modelit të rrezatimit në rrafshin horizontal.
5. Mbështjellësja e tablosë së rrezatimit në planin horizontal
Në rastet e 1 ose 2 antenave me rrezatim të drejtuar në të njëjtin shtyllë/mast ose në shtylla shumë afër njëra-tjetrës, ku konsideratat e paragrafit 4 vlerësohen tepër të rrepta, do të ndërtohet një mbështjellëse shtesë i diagrameve të rrezatimit në planin horizontal (-180° < φ < 180°), si më poshtë:
5a) Këndi i gjysmë-fuqisë φ-3dB përcaktohet në diagramin horizontale të rrezatimit. Për arsye sigurie, vlera e këtij këndi rritet me 5°.
5b) Këndi φ-10dB përcaktohet ndërmjet dy drejtimeve, në lobin kryesor, në të cilin koeficienti i amplifikimit ka vlerën Gm - 10dB. Për arsye sigurie, vlera e këtij këndi rritet me 5°.
5c) Këndi φ-20dB përcaktohet ndërmjet dy drejtimeve, në lobin kryesor, në të cilin koeficienti i amplifikimit ka vlerën Gm - 20dB. Për arsye sigurie vlera e këtij këndi rritet me 5°.
5d) Përcaktohet vlera maksimale të pikut (maksimumi lokal që korrespondon me lobim anësor ose lobin e pasmë më vlerë më të madhe) të koeficientit të amplifikimit G në intervalet [-1800, ½ φ-3dB], [½ φ-3dB ,1800]. Lë të jetë Gr kjo vlerë.
5e) Duke supozuar se koeficienti i amplifikimit ka një pjerrësi konstante në secilin nga intervalet
[- ½ φ-20dB , 00], [00, ½ φ-20dB ], mbështjellja e diagramit të rrezatimit horizontal jepet nga funksioni i amplifikimit G(φ):
Termi max ( Gr, Gm - kdB) (për k = 3, 10 ose 20) është futur për të mbuluar ose detajuar rastin kur Gm - Gr < k dB. Në këtë rast merret në shqyrtim koeficienti i amplifikimit Gr në vend të madhësisë Gm - k dB në relacionin (1.2).
Prandaj, lobi i rrezatimit maksimal të koeficientit të amplifikimit Gm përshkruhet në një hapje këndore φ1 = φ-3dB + 5° në të dyja anët e orientimit të antenës. Për shkak të mënyrës së ndërtimit, mbështjellësja është simetrike në drejtimin φ = 0° .
Figura 1.2: Mbështjellësja e diagrameve të rrezatimit në rrafshin horizontal Figura 1.2: Mbështjellësja e diagrameve të rrezatimit në rrafshin horizontal
Figura 1.2: Mbështjellësja e diagrameve të rrezatimit në rrafshin horizontal
Figura 1.2: Mbështjellësja e diagrameve të rrezatimit në rrafshin horizontal
SHTOJCA 2
VLERËSIME TË PËRGJITHSHME PËR ANTENAT E GJENERATËS 5G
Antenat m-MIMO instalohen dhe operojnë në mënyre që të garantohet siguria e publikut, përfshirë stabilitetin e strukturave mbajtëse dhe vendosjen e distancave të nevojshme të sigurisë (distancat e pajtueshmërisë) nga pikat ku publiku ka akses.
Për vendinstalimet e antenave m-MIMO vendet (zonat) brenda të cilave mund të kapërcehen kufijtë e lejuar të ekspozimit për publikun, identifikohen para instalimit. Për të përcaktuar këto zona, të paktën për çdo antenë m-MIMO duhet të përcaktohet zona e investigimit. Për të llogaritur zonën e investigimit të antenës ndiqet modeli i prezantuar në vijim.
Zona e diskutuar e investigimit shtrihet:
a) Brenda tufës, jashtë së cilës fillon përgjysmimi i fuqisë (HPBW) të lobit kryesor të rrezatimit të antenës specifike m-MIMO, në një distancë sa 5-fishi i distancës së sigurisë (pajtueshmërisë) në drejtimin e lobit kryesor të antenës së veçantë m-MIMO.
b) Jashtë tufës ku fillon përgjysmimi i fuqisë (HPBW) të lobit kryesor të rrezatimit të antenës specifike m-MIMO, në një distancë të barabartë me distancën e sigurisë në drejtimin e tufës kryesore të antenës në studim.
Nëse brenda zonës së investigimit të antenës MIMO ka edhe antena të tjera fqinje (MIMO, ose të tjera), edhe nëse tufa e gjysmëfuqisë së lobit të tyre kryesor mbivendoset me tufën e gjysmëfuqisë së lobit kryesor të antenës MIMO në studim, mund të kërkohet një hartë e mbivendosjes së përmendur më sipër, duke i përfshirë në të njëjtën shkallë si dhe planimetria e vendinstalimit.
Studimi që paraqitet përcakton masat e përshtatshme për sigurinë e publikut, në përputhje me sa është vlerësuar në llogaritje (ose matje), shoqëruar nga projektet ose skicat arkitektonike, ku përshkruhen zonat ku publiku nuk lejohet në planin horizontal dhe vertikal.
Për një kuptim më të plotë, në shembujt e mëposhtëm paraqiten në përshkrim të shkallëzuar distancat nga pika instalimit të antenës, brenda të cilave nuk lejohet të ketë akses (në planin vertikal dhe horizotal). Këto paraqitje skematike e bëjnë shumë e dukshme që këto zona të ndaluara janë mjaft larg nga pikat dhe/ose nivelet e aksesit publik.
Në vijim jepet ilustrimi për Zonën e Kontrollit të një antene dhe zonës ku publikut nuk i lejohet të ketë akses.
Shembuj të skicimit të Zonës së Kontrollit dhe Zonës së Investigimit
Figura 2.1: Paraqitje e Zonës së Kontrollit në planin vertikal
Figura 2.2: Paraqitje e Zonës së Kontrollit në planin horizontalFigura 2.2: Paraqitje e Zonës së Kontrollit në planin horizontal
Figura 2.2: Paraqitje e Zonës së Kontrollit në planin horizontal
Figura 2.2: Paraqitje e Zonës së Kontrollit në planin horizontal
Shembuj të skicimit të zonave ku ndalohet aksesi pubik
Figura 2.3: Skicë e zonave ku aksesi publik është i ndaluar në planin vertikalFigura 2.3: Skicë e zonave ku aksesi publik është i ndaluar në planin vertikal
Figura 2.3: Skicë e zonave ku aksesi publik është i ndaluar në planin vertikal
Figura 2.3: Skicë e zonave ku aksesi publik është i ndaluar në planin vertikal
Figura 2.4: Skicë e zonave ku aksesi publik është i ndaluar në planin horizontal
SHTOJCA 3
VLERËSIMI I EKSPOZIMIT TË RF-së BAZUAR NË FUQINË MAKSIMALE TË TRANSMETUAR OSE NË EIRP
Niveli i fuqisë RF të transmetuar nga një SB në një rrjet të lëvizshëm ndryshon me kohën me qëllimin që të optimizojë shërbimin ndaj pajisjes së përdoruesit (User Equipment - UE), ndërkohë që minimizon interferencën në qelizat fqinje. Aftësia për të zvogëluar fuqinë mesatare të transmetuar, po ashtu zvogëlon konsumin e energjisë së rrjeteve të lëvizshme dhe shpenzimet operacionale të lidhura me to; kjo një kërkesë e rëndësishme për operatorët e rrjeteve të lëvizshëm. Kur projektohet një rrjet i lëvizshëm dhe përcaktohen parametrat e operimit të një SB, përgjithësisht operatorët konsiderojnë kufijtë e buxhetit të energjisë. P.sh. çdo SB operon nën nivelin e kapacitetit mesatar (p.sh. 50%) për të pasur mjaftueshëm hapësirë (rezervë) për të administruar maksimumet rastësore të trafikut, pa arritur ngjeshje të trafikut që mund të ndodhë në kapacitetin e plotë.
Në përgjithësi, sinjalet e transmetuara nga një SB përfshijnë kanalet e kontrollit, ose sinjalet e referencës, që janë të nevojshme për të identifikuar prezencën e UE-ve dhe iu garantojnë atyre (UE) aksesin në rrjet. Ky sinjalizim specifikon nivelin minimal të fuqisë që sistemi duhet të transmetojë për funksionimin e përshtatshëm të teknologjisë mobile. Në anën tjetër, çdo SB ka një nivel maksimal të fuqisë të transmetuar RF që ai mund ta shpërndajë drejt UE-te e lidhura brenda zonës së tij të mbulimit.
Sistemet e menaxhimit të rrjetit të lëvizshëm, duke përfshirë dhe menaxherin e rrjetit ofrojnë (kanë në strukturë) numërues që paraqesin performancën dhe operimin e sistemit. Mund të gjenerorohen statistika për një qelizë/site, ose për shumë site (stacione bazë) dhe qeliza të shpërndara në një rajon shumë të madh gjeografik. Ndërmjet shumë numëruesve në dispozicion, fuqia e transmetuar në Down Link (DL), d.m.th. fuqia totale e transmetuar nga SB drejt UE, është vlera më e rëndësishme për kërkimet mbi ekspozimin. Fuqia e transmetuar ndryshon në një mënyrë ciklike: sipas ditës dhe vakteve të saj, sipas javëve dhe fundjavave, sipas sezoneve (p.sh. SB montohet në një zonë turistike sezonale). Profilet e trafikut publikohen në literaturë teknike dhe merren në konsideratë në standardet ndërkombëtare. Impakti i ndryshimit të trafikut për teknologjinë mobile është raportuar në publikime të ndryshme në literaturë teknike.
Nëpërmjet statistikave të marra nga matjet në rrjet ndërtohen të ashtuquajturit Cummulative Distribution Function (CDF), të cilat paraqesin funksione empirike probabilitare për fuqinë e transmetuar të mesatarizuar në kohë. Nëpërmjet CDF-së merret informacion mbi shpërndarjen e vlerave të fuqisë së transmetuar gjatë intervaleve të ndryshëm të kohës në studim.
Shembuj të CDF-ve të fuqisë së transmetuar të mesatarizuar në kohë të marra nga matjet në një rrjet 3G në Indi jepen në figurën 3.1. Rezultate të ngjashme për matjet në një rrjet 2G/3G/4G në Suedi jepen në figurën 3.2.
Figura 3.1: CDF-të empirike të fuqisë të transmetuar (të normalizuar) për mjedise të ndryshme në rrjetin 3G në Indi ([4] IEC TR 62669:2019, faqe 40)Figura 3.1: CDF-të empirike të fuqisë të transmetuar (të normalizuar) për mjedise të ndryshme në rrjetin 3G në Indi ([4] IEC TR 62669:2019, faqe 40)
Figura 3.1: CDF-të empirike të fuqisë të transmetuar (të normalizuar) për mjedise të ndryshme në rrjetin 3G në Indi ([4] IEC TR 62669:2019, faqe 40)
Figura 3.1: CDF-të empirike të fuqisë të transmetuar (të normalizuar) për mjedise të ndryshme në rrjetin 3G në Indi ([4] IEC TR 62669:2019, faqe 40)
Figura 3.2: CDF-të empirike të fuqisë së transmetuar (të normalizuar) të kombinuar për një rrjet 2G/3G/4G në Suedi ([4], IEC TR 62669:2019, faqe 40)Figura 3.2: CDF-të empirike të fuqisë së transmetuar (të normalizuar) të kombinuar për një rrjet 2G/3G/4G në Suedi ([4], IEC TR 62669:2019, faqe 40)
Figura 3.2: CDF-të empirike të fuqisë së transmetuar (të normalizuar) të kombinuar për një rrjet 2G/3G/4G në Suedi ([4], IEC TR 62669:2019, faqe 40)
Figura 3.2: CDF-të empirike të fuqisë së transmetuar (të normalizuar) të kombinuar për një rrjet 2G/3G/4G në Suedi ([4], IEC TR 62669:2019, faqe 40)
Praktikisht nga figura ekstrapolohet faktori që vlerëson se çfarë përqindjeje kanë grupet e ndryshme të vlerave të fuqisë nën një kufi të caktuar, p.sh. sa për qind e vlerave të matura të fuqisë së transmetuar të normalizuar (e mesatarizuar në kohë, p.sh. 6 min. ose 30 min., sipas kërkesave përkatësisht të ICNIRP 1998, ose ICNIRP 2020) janë më të mëdha se një vlerë e caktuar.
Në figurën e mësipërme ilustruese 3.2, shihet se 95% e fuqive të matura nuk kanë vlerë më të madhe se 28.5% e vlerës mesatare të transmetuar.
Stacionet Bazë me antena m-MIMO prodhojnë një numër tufash të ngushta të njëkohshme individualisht të drejtuara drejt pajisjeve të targetuara, me qëllimin që të optimizojnë përdorimin e burimeve radio, duke fokusuar energjinë radio tek objektivat - përdoruesit dhe duke zvogëluar interferencën te pajisjet e tjera. Kjo sjellje prej “beam - centric” (tufë e qendërzuar) e sistemeve MIMO ndryshon nga teknologjitë konvencionale të aksesit në radio, për të cilat energjia transmetohet në mënyrë konstante në një sektor të gjerë këndor. Ky fokusim dinamik i energjisë në drejtime të ndryshme të veçanta (individuale) do të ndikojë, gjithashtu, ekspozimin aktual nga stacionet bazë me m-MIMO. SB me m-MIMO përdorin shumë elemente të antenave drejt pajisjeve të përdoruesve (User Equipment - UE) hapësinore multipleks, duke transmetuar energji RF në tufa të ngushta. Për qasjen e tufës mund të zbatohen lloje të ndryshme të beamforming (formimit të tufës) ngjashëm me një rrjetë (sitë) selektive (code book based), e cila lejon të krijohen tufa të ngushta me amplifikim të lartë drejt përdoruesve (users), dhe eigen beamforming (EBB) dhe zero forcing (reciprocity based), e cila merr në konsideratë vetitë shumërrugëshe të kanalit wireless. Me SB që përdorin m-MIMO, fuqia e transmetuar shpërndahet në drejtime të ndryshme për të dhënë shërbim UE-ve të ndryshëm në vendqëndrime të ndryshme gjeografike. Rrjedhimisht, beamforming (mënyra e krijimit të tufës), përfshin një ndryshueshmëri shtesë në përcaktimin e fuqisë që kontribuon në ekspozimin aktual maksimal. Reduktimi i fuqisë së një SB me m-MIMO mund të përshkruhet nga dy faktorë:
i. variacioni i trafikut;
ii. shpërndarja hapësinore e mesatarizuar në kohë e fuqisë së transmetuar ose EIRP.
Nga rezultatet e fushatave të matjeve të përshkruara më lart dhe të ilustruara nga grafiku i CDF-ve (dhe shumë e shumë të tjera nga grupe të ndryshme studiuesish paraqitur dhe në ICE 62669:2019) për 5G New Radio nxirret një faktor korrektimi, që në të gjithë përafrimet konservative nuk është më i lartë se 25%, gjë që koincidon dhe me rezultatet e studimeve me modele teorike statistikore si të cituar në [5].
Vlen të theksohet se për antenat m-MIMO, kur përdoret përafrimi i fushës së largët, kufiri i pajtueshmërisë së produktit SB/antenë mund të vlerësohet, duke u bazuar në modelin e mbështjellëses së rrezatimit (IEC 62232:2022, 6.1.5.7). Rikujtojmë që për 5G NR, kontributi i sinjalit të referencës në ekspozimin në RF neglizhohet meqë fraksioni i fuqisë së saj është shumë më i vogël se sa ai i sinjaleve të trafikut.
Formulat e thjeshta dhe klasike sferike mund të përdoren për vlerësimin e pajtueshmërisë së antenave MIMO-massive dhe antenave beamforming (që formojnë tufa). Në këtë rast, mund të përdoret mbështjellësja e modelit të rrezatimit G(ϕ,θ), në ekuacionet 1, 2 dhe 4 dhe nëpërmjet ekuacionit (7) paraqitur më parë gjatë shtjellimit të Metodës së llogaritjes së përmasave të Zonës Kritike të shpërhapjes së rrezatimit jojonizues nga një antene celulare.
Kufijtë e pajtueshmërisë për publikun e gjerë dhe për punonjësit përcaktohen duke filluar llogaritjet me një supozim për një nivel konservativ të fuqisë aktuale të transmetuar prej 25% të fuqisë maksimale të transmetimit për të gjithë stacionet bazë të instaluar në një vend. Justifikimi Teknik dhe Shkencor për këtë supozim mund të gjendet në bibliografinë e cituar [5], që është referuar si konkluzion praktik dhe normativ në IEC TR 62669:2019, f. 70. Gjithë të dhënat e matjeve të bëra të analizuara dhe pasqyruara në [5], por edhe më vonë, tregojnë se fuqia aktuale e transmetuar është mjaft më e ulët se pragu konservativ i faktorit të reduktimit të fuqisë prej 25%.
Siç shpjegohet në [5], fuqia maksimale aktuale e transmetuar varet nga mjedisi, ku SB-ja është instaluar dhe do të ketë një impakt në shpërndarjen e pritshme të përdoruesve, të lidhur dhe rrjedhimisht se si e sa fuqia e transmetuar e mesatarizuar në kohë shpërndahet brenda zonës (hapësirës) së skanimit nga grupi i antenave.
Rezultatet e marra nga të dhënat e matjeve të fuqisë reale të transmetuar (IEC 62669, 13.1.1 f. 39, 40 dhe 13.2.4 ... f. 48) mbështesin zgjedhjen e kësaj vlere, faktori të reduktimit të fuqisë (25%), si një shifër shumë konservative. Është me vlerë të theksohet se kjo fuqi konservative aktuale e transmetuar përfshin në llogari edhe faktin që fraksioni i kohës së dedikuar për transmetim DL në skemat TDD është më i vogël se koha totale e konsideruar për vlerësimin e ekspozimit. Përgjithësisht fraksioni i kohës së transmetimit downlink ndaj kohës totale është 75%.
Për të zbatuar metodologjinë e re për vlerësimin e pajtueshmërisë (vlerësimit të Zonës Kritike) për burimet e fushave elektromagnetike, fuqia maksimale aktuale caktohet nga rregullatorët vendës, që sipas konvergjimit të rezultateve të studimeve teknike dhe shkencore rekomandohen të bazohen në IEC 62232:2022 dhe IEC TR 62669:2019.
REFERENCA BIBLIOGRAFIKE
[1] ICNIRP-2020, International Commission on Non-Ionizing Radiation Protection (ICNIRP), Guidelines for limiting exposure to electromagnetic fields (100 kHz to 300 GHz), Health Physics, 118(5):483-524; 2020, https://www.icnirp.org/cms/upload/publications/ICNIRPrfgdl2020.pdf [viewed 2022-0714]
[2] ICNIRP-1998, International Commission on Non-Ionizing Radiation Protection (ICNIRP), Guidelines for limiting exposure to time-varying electric, magnetic, and electromagnetic fields (up to 300 GHz), Health Physics, 74: 494-522 1998,
www.icnirp.org/cms/upload/publications/ICNIRPemfgdl.pdf [viewed 2022-07-14]
[3] IEC 62232:2022. Determination of RF field strength, power density and SAR in the vicinity of base stations for the purposes of evaluating human exposure
[4] IEC TR 62669:2019, Case studies supporting IEC 62232 - Determination of RF field strength, power density and SAR in the vicinity of radiocommunication base stations for the purpose of evaluating human exposure
[5] B. Thors, A. Furuskär, D. Colombi, and C. Törnevik, Time-averaged Realistic Maximum Power Levels for the Assessment of Radio Frequency Exposure for 5G Radio Base Stations Using Massive MIMO, IEEE Access, vol. 5, pp. 19711-19719, September 18th, 2017
[6] Colombi, D.; Joshi, P.; Xu, B.; Ghasemifard, F.; Narasaraju, V.; Törnevik, C. “Analysis of the Actual Power and EMF Exposure from Base Stations in a Commercial 5G Network”. Applied Sciences 2020, 10, 5280.
[7] Rec. ITU T K.61 (01.2019)
[8] ITU-T K.100 (06/2021) Measurement of radio frequency electromagnetic fields to determine compliance with human exposure limits when a base station is put into service.
[9] Using Massive MIMO, IEEE Access, Vol. 5, pp. 19711-19719, September 2017, DOI:10.1109/ACCESS.2017.2753459.
[10] https://eeae.gr/files/templates/ypodeigma_meletis_radioekpompon.pdf
[11] KA-EEAE-KO-122022-01, Guidelines for the content of the study of the ECCC, according to the Cabinet Decision No. 32661 EX 2022 (B’4062/29.07.2022), December 2022 (https://eeae.gr/KA-EEAE-KO-122022-01.pdf
[12] CENELEC EN 50401/2017.
[13] Massive MIMO for 5G networks: https://www.ericsson.com/en/reports-and-papers/white-papers/advanced-antenna-systems-for-5g-networks
