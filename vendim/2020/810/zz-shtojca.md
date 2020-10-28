# Shtojca
STANDARDET SHTETËRORE PËR SPECIFIKIMET TEKNIKE TË INFORMACIONIT GJEOHAPËSINOR NË SHQIPËRI
TEMA: ZONAT ME RREZIQE NATYRORE
PËRMBAJTJA
1. Përshkrimi i standardeve
2. Hyrje
2.1 Qëllimi
2.2 Si lexohet dokumenti
2.3 Detyrimet ligjore
2.4 Fusha e veprimit
3. Tema
3.1 Zonat me rreziqe natyrore
3.1.1 Parathënie
3.1.2 Terma dhe përkufizime
3.1.3 Skemat e aplikimit dhe diagrami UML për temën “Zonat me rreziqe natyrore”
3.1.4 Katalogu i tipologjisë
3.1.4.1 Elementet abstrakte të ekspozuar a
3.1.4.2 Elementet e ekspozuara
3.1.4.3 Klasifikimi i rreziqeve natyrore
3.1.4.4 Klasifikimi i elementeve të ekspozuara
3.1.4.5 Mbulimi i rrezikut
3.1.4.6 Mbulimi i riskut
3.1.4.7 Mbulimi i elementeve të ekspozuara
3.1.4.8 Mbulimi i ngjarjeve të vëzhguara
3.1.4.9 Mundësia e ngjarjes
3.1.4.10 Ngjarja abstrakte e vëzhguar
3.1.4.11 Niveli ose intensiteti
3.1.4.12 Ngjarja e vëzhguar
3.1.4.13 Zona abstrakte e riskut
3.1.4.14 Zona abstrakte e rrezikut
3.1.4.15 Zona e rrezikut
3.1.4.16 Zonat e riskut
3.1.4.17 Vlerësimi sasior
3.1.4.18 Vlerësimi i vulnerabilitetit
3.1.4.19 Vlerat e metodës së përcaktimit
3.1.4.20 Vlerat e llojeve të elementeve specifike të ekspozuara
3.1.4.21 Vlerat e llojeve të rreziqeve specifike
3.1.4.22 Vlerat e kategorive të rreziqeve natyrore
3.1.4.23 Vlerat e kategorive të elementeve të ekspozuar a
3.2 Metadata
3.3 Kodi EPSG për KRGJSH-në
3.4 Cilësia e të dhënave
3.4.1 Përputhja logjike - Përputhja konceptuale (Logical consistency - Conceptual consistency)
3.4.2 Përputhja logjike - Përputhja me domain-in (Logical consistency - DOMAIN consistency)
3.4.3 Kërkesat minimale të cilësisë së të dhënave (Minimum data quality requirements)
4. Anekse
4.1 Aneks A - Katalogu i tipologjisë
4.2 Aneks B - Kodlistat
4.2.1 Kategoria e elementeve të ekspozuara
4.2.2 Vlerat e kategorive të rreziqeve natyrore
4.2.3 Kodlista për arsyet e pavlefshmërisë - Voidalbe
1. PËRSHKRIMI I STANDARDEVE
Ky dokument përmban standarde të specifikimeve teknike të të dhënave gjeohapësinore për ndërtimin e NSDI-së, duke u mbështetur në direktivën INSPIRE. Autori i këtij produkti është Autoriteti Shtetëror për Informacionin Gjeohapësinor (ASIG) në bashkëpunim me Drejtorinë e Përgjithshme të Emergjencave Civile, aktualisht Agjencia Kombëtare e Mbrojtjes Civile.
Data e publikimit të versionit nr. 1, është 10 mars 2018. Emërtimi i dokumentit është: ASIG_Standard_NSDI_2018_ ZRN_v.1, ku:
ASIG - Autoriteti përgjegjës për krijimin e standardit;
Standard - Lloji i dokumentit;
NSDI - Qëllimi i dokumentit;
2018 - Viti i krijimit;
ZRN - Tema për të cilën është krijuar standardi: “Zonat me rreziqe natyrore”, e cila i referohet temës “Natural risk zones” të direktivës INSPIRE;
v.1 - Numri i versionit të standardit.
2. HYRJE
2.1 QËLLIMI
Ky dokument përcakton specifikimet teknike, të harmonizuara konform direktivës INSPIRE, për të dhënat gjeohapësinore të temës “Zonat me rreziqe natyrore”, temë e cila është përcaktuar në nenin 11, pika 2/s, të ligjit nr. 72/2012, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”.
Ky dokument publikohet si standard që përcakton rregullat bazë të implementimit të NSDI-së[1] në Shqipëri, me qëllim përdorimin e tij nga autoritetet publike përgjegjëse për mbledhjen, përpunimin dhe përditësimin e informacionit gjeohapësinor, që të arrihet një kuptueshmëri unike dhe korrekte e të dhënave dhe shërbimeve gjeohapësinore, për të realizuar ndërveprueshmërinë e tyre.
2.2 SI LEXOHET DOKUMENTI
2.2.1 STRUKTURA E DOKUMENTIT
Ky material është i organizuar në katër kapituj kryesorë:
1. Përshkrimi i standardeve: Në këtë pjesë jepet emërtimi dhe autori i standardeve.
2. Hyrje: Në këtë pjesë jepen përshkrime dhe shpjegime për të kuptuar mënyrën si organizohet i gjithë informacioni dhe si mund të kuptohet më lehtë.
3. Tema: Në këtë pjesë jepen specifikimet teknike për secilën temë.
4. Anekse: Në këtë pjesë jepen informacione shtesë shpjeguese në ndihmë të lexuesve.
- Përmbajtja e kapitullit 3 është strukturuar në 4 pjesë kryesore:
3.1 Përshkrimi i temës - Këtu flitet në mënyrë të përgjithshme për përmbajtjen e temës, si dhe detajohen: Diagramet UML dhe katalogu i tipologjive.
3.2 Metadata - Këtu jepen specifikimet teknike për metadatat e temës përkatëse.
3.3 Sistemi koordinativ referencë - Këtu përcaktohet sistemi koordinativ referencë (KRGJSH).
3.4 Cilësia e të dhënave - Këtu jepet një përshkrim mbi cilësinë e të dhënave të elementeve dhe matjes së tyre.
2.2.2 DIAGRAMET UML DHE KATALOGU I TIPOLOGJISË
Diagramet UML ofrojnë një mënyrë të shpejtë për të parë elementet kryesore të specifikimeve dhe marrëdhëniet mes tyre. Përkufizimi mbi llojin e objektit gjeohapësinor, atributet dhe marrëdhëniet janë të përfshira në ’Katalogun e tipologjive’ (Feature Catalogue). Personat të cilët kanë ekspertizë tematike, por nuk janë të familjarizuar me UML-në, mund ta kuptojnë plotësisht përmbajtjen e modelit të të dhënave duke u fokusuar te ’Katalogu i tipologjive’. Për përdoruesit, katalogu i tipologjive mund të jetë veçanërisht i dobishëm për të kontrolluar nëse ai përmban të dhënat e nevojshme për aplikacionet që ata përdorin.
Në tabelat e mëposhtme shpjegohet përmbajtja dhe mënyra e organizimit të informacionit, në tabelat e të dhënave, në katalogun e tipologjive.
Tabelat nr. 1 dhe 2, me anë të një shablloni, shpjegojnë mënyrën e organizimit të informacionit në tabelën e tipologjive dhe të atributeve të tyre.
Tabela nr. 3, me anë të një shablloni, shpjegon mënyrën e organizimit të informacionit në tabelën e kodlistës.
Tabela 1
|Emri Emërtimi i tipologjisë |
|Përkufizimi |Përkufizimi sipas direktivës INSPIRE për tipologjinë |
|Përshkrimi |Shënime dhe përshkrime të tjera për tipologjinë |
|Lloji i tipologjisë |Tipi i elementit mund të jetë i llojit: |
| |«FeatureType» - një element që mund të jetë real në terren por dhe një dukuri abstrakte; |
| |«dataType» - një element tabelor që shërben vetëm si tabelë atributesh për t’u lidhur me një element |
| |tjetër; |
| |«Enumeration» «codelist» - listë e parapërgatitur vlerash ku elementi duhet të marrë vlerë. Enumeration|
| |nënkupton “renditje vlerash”, ndërsa codeList nënkupton listë vlerash ose ndryshe “kodlistë”. Në |
| |dokument gjenden të shqipëruara si “Numërtimet dhe kodlistat”; |
| |«Union» - një mbulesë topologjike e dy ose më shumë grupeve të të dhënave gjeohapësinore, që ruan |
| |tiparet që bien brenda shtrirjes gjeohapësinore të të dy grupeve të të dhënave hyrëse; |
| |«Imported» - të dhëna të specifikuara në tema të tjera të direktivës INSPIRE. Në dokument gjenden “Të |
| |dhënat e importuara”. |
|Gjeometria |Gjeometria e elementit sipas formatit vektor mund të gjendet në tri forma: pikë, linjë ose poligon. |
| |Abstrakt - kur elementi nuk është element real në terren, por konsiderohet vetëm si dukuri. |
|Shumëllojshmëria |Lloji dhe numri i vlerave që mund të marrë atributi: |
| |0..* - mund të marrë shumë lloje vlerash ose asnjë vlerë; |
| |1..* - mund të marrë minimumi 1 vlerë ose shumë vlera; |
| |0..1 - mund të mos marrë asnjë vlerë ose nëse merr vlerë, duhet të marrë vetëm 1 vlerë të vetme; |
| |1 - duhet të marrë detyrimisht 1 vlerë. |
|I detyrueshëm |Po - nëse atributi është i detyrueshëm të plotësohet; |
| |Jo - nëse atributi nuk është i detyrueshëm të plotësohet. |
|Rol shoqërimi |Në tabelën e lidhjeve “Rol shoqërimet” tregohen marrëdhëniet hierarkike ndërmjet elementeve të ndryshme|
| |në këtë temë, si dhe në temat e tjera. Këto marrëdhënie pasqyrojnë lidhjet që realizohen në skemat UML.|
|Atributet |«Atribut» - janë informacione të bashkëngjitura në format tabelor te tipologjitë gjeohapësinore. |
Tabela 2
|Atributet |
| |
|-- Emri -- |
|Emërtimi i atributit |
|-- Përkufizimi -- |
|Përkufizimi sipas direktivës INSPIRE të elementeve |
|-- Përshkrimi -- |
|Shënime dhe përshkrime të tjera për elementin |
|[i detyrueshëm: detyrueshmëria nëse atributi duhet të marrë vlerë, p.sh: Po] |
Tabela 3
|Atributet |
| |
|[pic] Vlera e parë e listës së gatshme, p.sh: Ligjor |
| |
|-- Emri -- |
|Emërtimi i vlerës |
|-- Përkufizimi -- |
|Përkufizimi i elementeve |
| |
|[pic] Vlera e dytë (etj.) e listës së gatshme, p.sh: joligjor |
|-- Emri -- |
|Emërtimi i vlerës |
|-- Përkufizimi -- |
|Përkufizimi i elementeve |
2.2.3 Karakteristikat e <<voidable>> dhe shumëllojshmëria
Stereotipi <<voidable>> përdoret për të përshkruar ato karakteristika të objekteve gjeohapësinore që mund të jenë ose mund të mos jenë të pranishme në grupet e të dhënave gjeohapësinore edhe pse mund të ekzistojnë në botën reale. Kjo nuk do të thotë që këtyre përkatësive duhet t’u jepet një vlerë.
Për të gjitha karakteristikat e përcaktuara për objektet gjeohapësinore duhet të paraqitet një vlerë - ose vlera përkatëse (nëse është e disponueshme në grupin e të dhënave që mirëmbahet nga ofruesi i të dhënave), ose vlera ’void’. Një vlerë void nënkupton që nuk ekziston një vlerë përkatëse në grupet e të dhënave gjeohapësinore që mirëmbahen nga ofruesi i të dhënave, ose që asnjë vlerë përkatëse nuk mund të nxirret nga vlerat ekzistuese.
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kodlistën ’Vlera e Arsyes së Pavlefshmërisë’ (Void Reason Value), e cila përmban:
- E pa njohur (Unknown)
-- Përkufizimi --
Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave.
-- Përshkrim --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” të një liqeni nuk është matur, atëherë arsyeja e pavlefshmërisë së kësaj karakteristike mund të jetë “E pa njohur”.
- E papopulluar (Unpopulated)
-- Përkufizimi --
Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të ekzistojë.
-- Përshkrim --
Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E pa populluar”.
- Konfidenciale (Withheld)
-- Përkufizimi --
Kjo karakteristikë mund të ekzistojë por është konfidenciale.
Stereotipi <<voidable>> nuk jep informacion nëse karakteristika ekziston apo jo në botën reale. Kjo shprehet duke përdorur shumëllojshmërinë:
Nëse një karakteristikë mund të ekzistojë apo mund të mos ekzistojë në botën reale, vlera minimale do të përcaktohet si 0. P.sh. nëse një adresë ka apo nuk ka një numër shtëpie, shumëllojshmëria e përkatësisë përkatëse do të jetë 0..1.
Nëse për një karakteristikë të caktuar ekziston të paktën një vlerë në botën reale, vlera minimale do të përcaktohet si 1. P.sh. nëse një njësi administrative ka gjithmonë të paktën një emër, shumëllojshmëria e përkatësisë përkatëse do të jetë 1..*.
2.2.4 MBULIMET - COVERAGES
Funksionet e mbulimit “coverages” përdoren për të përshkruar karakteristikat e një fenomeni në realitet që zhvillohet në kohë dhe/ose hapësirë. Shembuj tipik të tyre janë temperaturat, lartësitë, precipitimet, imazheria etj. Një mbulim përmban një grup vlerash, të cilat shoqërohen me një element gjeohapësinor, kohor, kohor-gjeohapësinor. Domein-et tipike gjeohapësinore janë grupe pikash (p.sh. vendndodhja e sensorëve), kurbat përcaktuese (p.sh. izolinjat), rrjetet (p.sh.: ortoimazheria, modelet e lartësisë) etj.
Në skemat e aplikimit të INSPIRE funksionet e mbulimit janë përcaktuar si vetitë e llojeve të objekteve gjeohapësinore ku lloji i vlerës së kësaj karakteristike është një realizim i një prej llojeve të specifikuara në SSH EN ISO 19123:2007.
Për të përmirësuar përputhjen me standardet e mbulimit në nivelin e zbatimit (p.sh.: ISO 19136 dhe OGC Shërbimi i Mbulimit në Internet) dhe për të përmirësuar harmonizimin ndërtematik për përdorimin e mbulimeve në INSPIRE, një skemë e aplikimit për llojet e mbulimit është përfshirë në Modelin Konceptues të Përgjithshëm “GenericConceptualModel”.
Kjo skemë aplikimi përmban llojet e mëposhtme të mbulimit:
- RrjetiIMbulimitIKorrigjuar (rektifikuar): Mbulimi, domein-i i të cilit përbëhet nga një rrjet i korrigjuar, një rrjet për të cilin ka një transformim përfundimtar midis koordinatave të rrjetit dhe koordinatave të sistemit koordinativ referencë (shih figurën 1, majtas).
- RrjetiIMbulimitReferencë: Mbulimi, domein-i i të cilit përbëhet nga një rrjet referimi - një rrjet i lidhur me një transformim që mund të përdoret për të kthyer vlerat e koordinatave të rrjetit në vlerat e koordinatave të referuara në një sistem referimi koordinativ (shih figurën 1, djathtas).
Aty ku është e mundur përdoren vetëm këto lloje të mbulimit (ose një nëntipi të tyre) në skemat e aplikimit në INSPIRE.
[pic][pic]
Figura 1: Shembuj të një rrjeti të korrigjuar (majtas) dhe të një rrjeti referues (djathtas)
2.2.5 NUMËRTIMET DHE KODLISTAT (ENUMERATION AND CODELIST)
Kodlistat modelohen si klasa në skemat e aplikimit, por vlerat e tyre menaxhohen jashtë skemave të aplikimit. Në kodlistë, ’vlera të tjera’ përcakton llojin e përmbajtjes së kodlistës, e përcaktuar specifikisht, si më poshtë:
- ’jo’ përfaqëson kodlista që përmbajnë vetëm vlera të specifikuara në këtë dokument;
- ’të kufizuara’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera të tjera të limituara të përcaktuara nga ofruesi i të dhënave;
- ’të hapura’ përfaqëson kodlista që përmbajnë vlera të specifikuara në këtë dokument dhe vlera shtesë në çdo nivel, të përcaktuara nga ofruesi i të dhënave;
- ’po’ përfaqëson kodlista që përmbajnë vlera të përcaktuara nga ofruesi i të dhënave.
Vlerat shtesë të përcaktuara nga ofruesit e të dhënave nuk duhet të zëvendësojnë apo të modifikojnë vlerat ekzistuese të përcaktuara në dokument.
Në rastin kur ofruesit e të dhënave do të përdorin kodlista me vlera jo të përmbajtura në dokument, ofruesit janë të detyruar t’i bëjnë këto vlera bashkë me përkufizimet e tyre, të disponueshme në një regjistër. Kjo do të mundësojë që edhe përdoruesit e tjerë t’i kuptojnë këto vlera dhe të kenë mundësi t’i përdorin.
2.2.6 PARAQITJA E DIMENSIONIT KOHOR
Skemat e aplikimit përdorin atributin “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor” për të regjistruar jetëgjatësinë e një objekti gjeohapësinor.
Atributi “FillimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është futur apo ndryshuar në grupin e të dhënave gjeohapësinore (në sistem). Atributi “PërfundimiICiklitJetësor” specifikon datën kur versioni i objektit gjeohapësinor është zëvendësuar apo tërhequr nga grupi i të dhënave gjeohapësinore (në sistem). Këto vlera kohore nuk kanë të bëjnë me karakteristikat kohore të objektit në realitet.
Ndryshimet që bëhen në atributin “PërfundimiICiklitJetësor” nuk shkaktojnë ndryshime në atributin “FillimiICiklitJetësor”.
|Shënim i rëndësishëm: |
|Disa terma në katalogun e tipologjive, si p.sh.: FeatureType, dataType, void, coverages etj., nuk janë përkthyer qëllimisht në gjuhën |
|shqipe. Qëllimi parësor është që të mos humbasin kuptimin gjatë përkthimit dhe së dyti që të përdoret një gjuhë unike sipas termave të |
|direktivës INSPIRE. |
2.3 Detyrimet ligjore
Në bazë të ligjit nr. 72/2012, neni 16, “Për organizimin dhe funksionimin e Infrastrukturës Kombëtare të Informacionit Gjeohapësinor në Republikën e Shqipërisë”, ASIG-u është përgjegjës për krijimin e standardeve për secilën nga temat e përcaktuara në ligj (neni 11), në përputhje me standardet evropiane (direktiva INSPIRE).
Standardet teknike të të dhënave gjeohapësinore për krijimin e NSDI-së në Shqipëri janë përshtatur nga specifikimet teknike të temave përkatëse në direktivën INSPIRE, si dhe praktikave më të mira ndërkombëtare që mbështesin dhe bazohen në këtë direktivë. Për implementimin e direktivës, kërkohet që të gjithë aktorët të zbatojnë disa standarde të përbashkëta, të cilat mundësojnë ndërveprimin e shërbimeve dhe harmonizimin e të dhënave gjeohapësinore.
Standardet (rregullat e implementimit - IR) duhet të krijohen për fushat e mëposhtme:
- Metadata: në këtë fushë direktiva përcakton standardet se si duhen të jenë metadatat. Ky standard është unik dhe i aplikueshëm për të gjitha institucionet ose palët e treta (siç është e përcaktuar në fushën e veprimit të kësaj direktive), të cilat do ta implementojnë atë (VKM-ja nr. 1077, datë 23.12.2015).
- Specifikimi i të dhënave: standardet e kësaj kategorie përfshijnë të gjitha atributet e objekteve të ndryshme që do të publikohen. INSPIRE ka përcaktuar disa atribute bazë të cilat do të shërbejnë për publikimin e të dhënave të ndryshme. Vendet e ndryshme, në varësi të ligjeve ose të nevojave të brendshme, mund të shtojnë atribute të tjera për t’i bërë sa më të përdorshme të dhënat. Të gjitha të dhënat që do të shtohen duhet të jenë të dokumentuara dhe të miratuara nga institucionet përgjegjëse lokale.
2.4 FUSHA E VEPRIMIT
Të gjithë autoritetet publike, kompanitë private apo individët, që mbajnë ose përpunojnë të dhëna gjeohapësinore për llogari të institucioneve publike, janë të detyruar t’i nënshtrohen këtij standardi.
Bazuar në modelet e proceseve të biznesit, sistemi i propozuar nga direktiva INSPIRE ka proceset dhe ciklin jetësor, si më poshtë:
[pic]
Figura 2: Proceset e ciklit jetësor
Planifikimi - Është procesi gjatë të cilit krijohen strukturat e të dhënave të nevojshme për të publikuar informacionin në portal. Rezultatet e këtij procesi janë modelet e ndryshme të të dhënave.
Vlerësimi - Është procesi gjatë të cilit të dhënat ekzistuese testohen kundrejt modelit. Rezultati i këtij procesi do të jetë certifikimi i të dhënave ose nevoja për të modifikuar të dhënat që të përshtaten me modelet e përcaktuara gjatë procesit të vlerësimit.
Procesimi - Është procesi gjatë të cilit mblidhen dhe modifikohen atributet e të dhënave për të prodhuar informacion kuptimplotë. Manipulimi i tyre bëhet kundrejt modeleve të përcaktuara gjatë planifikimit. Rezultatet e këtij procesi janë bashkësi të dhënash gati për t’u publikuar.
Shpërndarja - Është procesi gjatë të cilit të dhënat vihen në dispozicion për përdoruesit (qytetarët, autoritetet publike, organizatat ose palët e treta). Përdoruesi mund të shkarkojë, të përdorë, të analizojë ose të citojë të dhënat. Publikimi i të dhënave bazohet në modelet e ndryshme të përdorimit.
Zbulimi - Është proces i vazhdueshëm gjatë të cilit zbulohen të dhëna të reja ose të dhëna jocilësore në të dhënat e publikuara.
Analiza - Është procesi i analizimit të të dhënave të evidentuara në fazën e zbulimit. Gjatë këtij procesi merret vendimi çfarë do të bëhet me të dhënat që janë evidentuar.
Përditësimi - Është procesi kur propozohet shtimi, modifikimi ose fshirja e të dhënave. Ky proces regjistrohet nga procesi i analizimit të të dhënave ekzistuese dhe të publikuara.
Arkivimi - Është procesi gjatë të cilit bashkësitë e të dhënave që nuk nevojiten të aksesohen, arkivohen duke u bazuar në standarde lokale dhe në legjislacionin në fuqi të vendeve ku implementohen. Rezultat i këtij procesi janë të dhënat që bëhen të paaksesueshme për publikun, me akses vetëm nga autoritetet specifike. Këto të dhëna vazhdojnë të ruhen për arsye të përputhshmërisë me kuadrin ligjor në fuqi ose me standardet specifike.
Shkatërrimi - Është procesi gjatë të cilit të dhënat bëhen të parikuperueshme. Ky proces bazohet në standarde lokale ose në legjislacionin në fuqi.
3. TEMA
3.1 ZONAT ME RREZIQE NATYRORE
3.1.1 PARATHËNIE
Tema “Zonat me rreziqe natyrore” përfshin hapësirat e cenueshme në lidhje me rreziqet natyrore (atmosferike, hidrologjike, sizmike, vullkanike dhe zjarret e stimuluara nga era që, për shkak të pozicionit, agresivitetit dhe shpeshtësisë, kanë potencial të madh që të ndikojnë në shoqëri) si p.sh.: përmbytjet, rrëshqitjet, subsidencat, ortekët, zjarret në pyje, tërmetet, shpërthimet vullkanike.
Zonat e riskut natyror janë zona (territore) të cilat kërcënohen nga rreziqe natyrore, që mund të kenë numër të vogël ose të madh popullsie dhe/ose kanë vlerë të veçantë mjedisore, kulturore dhe ekonomike. Risku në këtë kontekst përkufizohet si:
Risk = Rrezik (Hazard) * Ekspozim * Vulnerabilitet
i shëndetit njerëzor, aseteve mjedisore, kulturore dhe ekonomike për zonën që studiohet
R=Rr (H)*E*V
Sipas këtij përkufizimi risku mund të shprehet në terma të tillë, si:
“Çdo vit ka një mundësi prej 1% për të pasur 100 shtëpi të shkatërruara për shkak të përmbytjeve të një madhësie të caktuar, në rastin e një rreziku nga përmbytje çdo 100 vjet, me elemente të ekspozuara prej 100 shtëpish që janë të cenuara nga përmbytja me 100%:”;
ose
“Një rrezik për shkak të zjarreve në pyje, të një madhësie të caktuar, për një periudhë prej 5 vjetësh, me 25 shtëpi të ekspozuara, çon në përfundimin se mesatarisht shkatërrohen 5 shtëpi çdo vit”.
Përkufizimi për secilin nga termat në funksion të riskut është një disiplinë më vete. Për qëllime të TWG-NZ (Thematic Working Group) është vendosur që përkufizimet specifike ekzistuese të përshtaten si më poshtë.
Risk (R)
Risku është kombinimi i pasojave të një ngjarjeje (harzard) dhe gjasave/probabilitetit që kjo ngjarje të ndodhë (ISO 31010).
Koment. Ky përkufizim i afrohet më shumë përkufizimit të “ISO/IEC Guide 73”. Fjala “risk” ka dy kuptime të dallueshme: në përdorimin popullor, zakonisht i vihet theksi në konceptin e shanseve ose mundësive, të tilla si “risku për një aksident”; ndërsa në kontekstin teknik, theksi është zakonisht i vendosur mbi pasojat, në termat e “humbjeve të mundshme” për ndonjë shkak, vend dhe periudhë të caktuar. Mund të vërehet se njerëzit jo domosdoshmërish ndajnë perceptime të njëjta në kuptimin dhe shkaqet themelore të risqeve të ndryshme (UNISDR 2009).
Rrezik (Hazard)
Një fenomen i rrezikshëm, substancë, aktivitet njerëzor ose gjendje që mund të shkaktojë humbje të jetës, dëmtim ose ndikime të tjera shëndetësore, dëmtim të pronës, humbje të mjeteve të jetesës dhe shërbimeve sociale dhe ekonomike, përkeqësim ose dëmtim mjedisor (UNISDR 2009).
Koment. Rreziqet që kanë të bëjnë me reduktimin e riskut të katastrofave, siç thuhet në shënimin 3, të “Hyogo Framework”, janë: “rreziqet me origjinë natyrore ose risqet e lidhura me elemente mjedisore dhe teknologjike”. Rreziqe të tilla lindin nga një seri të dhënash gjeologjike, meteorologjike, hidrologjike, oqeanike, biologjike dhe teknologjike, ndonjëherë duke vepruar në kombinim me njëra-tjetrën. Në mjediset teknike, rreziqet janë përshkruar në mënyrë sasiore nga frekuenca e mundshme e shfaqjes së intensiteteve të ndryshme, për zona të ndryshme, siç përcaktohet nga të dhënat historike ose analizat shkencore (UNISDR 2009).
Ekspozim (E)
Njerëz, prona, sisteme ose elemente të tjera, prezent në zonat e rreziqeve, që janë gjithashtu objekt i humbjeve të mundshme (UNISDR 2009).
Vulnerabilitet (V)
Karakteristikat dhe rrethanat e një komuniteti, sistemi ose aseti, që e bëjnë të ndjeshëm nga efektet dëmtuese një rrezik (UNISDR 2009).
Koment. Ka disa aspekte të vulnerabilitetit, që variojnë nga faktorë fizikë, social, ekonomik dhe të ambientit. Shembujt mund të përfshijnë: projektimin dhe ndërtimin e dobët të godinave; mbrojtjen e papërshtatshme të aseteve; informimin dhe ndërgjegjësimin e dobët të publikut; njohjen zyrtare të limituar të risqeve dhe marrjes së masave, si dhe nënvlerësimin për menaxhimin e mençur të ambientit. Vulnerabiliteti ndryshon ndjeshëm në raport me komunitetin përgjatë kohës. Ky përkufizim e identifikon vulnerabilitetin si karakteristikë të elementeve të interesit (komuniteti, sistemi apo asetet), të cilat janë të pavarura nga ekspozimi i tyre. Gjithsesi, në përdorimin e përditshëm fjala përdoret shpesh në një këndvështrim më të gjerë, për të përfshirë elementet e ekspozimit UNISDR (2009).
Një nga arsyet për vështirësinë në terminologji është se gjuha e riskut është zhvilluar në një gamë të gjerë disiplinash, duke përfshirë riskun financiar, menaxhimin e fatkeqësive etj. Vulnerabiliteti dhe ekspozimi janë dy nga termat që shkëmbehen më shpesh. Termat e përdorur në model ndjekin përkufizimet e UNISDR 2009 dhe së fundmi ata ndjekin modelin e dokumentit të Këshillit për “Asistencën ndaj risqeve dhe hartat udhëzuese për menaxhimin e katastrofave” të Bashkimit Evropian.
Në sektorin e sigurimeve risqet trajtohen duke përdorur termin “Perils”. Ky sektor bën përdorim të gjerë të informacioneve mbi rreziqet, vulnerabilitetin dhe risqet në sektorin publik, dhe përbën një pjesë të rëndësishme të kornizës ndërkombëtare për menaxhimin e risqeve. Gjithashtu, ky sektor do të përfitojë nga të dhëna të tilla duke pasur parasysh që direktiva INSPIRE aplikohet mbi të gjitha nga autoritetet publike, që mbajnë të dhëna ose veprojnë për llogari të tyre. Ky specifikim i të dhënave përshkruan informacionet gjeohapësinore që mund të jenë objekt i partneriteteve publik-privat, ndërmjet autoriteteve publike që mbajnë të dhënat dhe sektorin e sigurimeve.
[pic]
Figura 3: Konceptet kryesore në modelin e zonave të riskut natyror
Një tjetër shembull i përdorimit të gjerë të informacionit për zonat e risqeve natyrore, eurokodet e strukturuara të BE-së ose eurokodet, janë duke ndërtuar standardet për Evropën, të publikuara nga Komiteti Evropian për Standardizimin. Eurokod 1, për shembull, trajton veprimet e zjarrit në strukturat e ndërtesave, kurse Eurokod 8 i referohet ndërtesave rezistente ndaj tërmeteve. Kështu që gjithmonë është e rëndësishme të bashkëngjitet vlerësimi i “vulnerabilitetit” të strukturave të ndërtimit me aplikimin ose jo të eurokodeve. Për të bërë një vlerësim nëse struktura inxhinierike “e ekspozuar” (element i ekspozuar) është gjithashtu “vulnerabël” dhe “sa vulnerabël është ajo”(p.sh. një vlerësim specifik) ndaj një rreziku të caktuar (p.sh.: përmbytja, zjarri, rrëshqitja etj.), duhet të dimë karakteristikat e projektimit dhe të ndërtimit të kësaj strukture të veçantë, si dhe nëse dizajni është i bazuar në një standard ose kod të praktikës. Për shembull, nëse një ndërtesë apo një mur mbajtës është i përbërë nga materiale rezistente ndaj zjarrit, domethënë më pak vulnerabël nga zjarri, ose nëse një godinë është rezistente nga tërmetet nuk parashikohet që të pësojë dëme të mëdha për tërmete të një madhësie të caktuar, ndryshe nga një godinë që është ndërtuar pa marrë në konsideratë lidhje të veçanta me tërmetet.
[pic]
Figura 4: Diagrami alternativ që tregon konceptet kryesore në modelin e zonave të riskut natyror
Sipërfaqet tematike në zonat e riskut natyror
Ky specifikim i të dhënave duhet të jetë sa më i dobishëm dhe i përdorshëm që të sigurojë ndërveprim të të dhënave. Modeli i të dhënave është zhvilluar për të qenë i përshtatshëm për të dhënat publike dhe informacionin që është tashmë në dispozicion. Në shumë raste kjo është vetëm ndjeshmëri ose rrezik ose vulnerabilitet. Parashikohet që edhe në mungesë të një modeli të plotë risku, ende është e mundur të ndahen të dhënat dhe informacionet për një specifikim të përbashkët për rreziqet që kanë potencialin të prekin njerëzit, pronat dhe shërbimet, si dhe mjedisin në të gjithë Evropën.
Është e rëndësishme për të gjithë përdoruesit e mundshëm të informacionit të zonave të riskut natyror, të dinë se çfarë rreziku është duke shkaktuar një zonë e veçantë e riskut. Është e rëndësishme sidomos për zbutjen dhe menaxhimin e riskut. Prandaj, të dhënat dhe informacionet që përfshihen në këtë specifikim të të dhënave konceptuale e konsiderojnë ekzistencën e përcaktimit të një zone rreziku si objekti më i rëndësishëm që siguron thelbin e modelit të të dhënave. Elementet e ekspozuara, zonat e riskut dhe ngjarjet e kaluara të vëzhguara gjithashtu janë bashkuar konceptualisht nëpërmjet procesit të përcaktimit të rrezikut dhe riskut. Burimet e të dhënave për përcaktimin e secilit rrezik janë kryesisht brenda fushëveprimit të sipërfaqeve të tjera tematike të INSPIRE, p.sh. prerjet tektonike si një burim për tërmetet (Gjeologjia). Si pasojë, këto specifikime të të dhënave nuk i përfshin ato dhe as modelin e proceseve dhe metodave shkencore që janë përdorur në identifikimin e hapësirave të rrezikut.
Specifikimi i të dhënave përfshin modelimin e rrezikut natyror të shkaktuar pikësëpari nga fenomene natyrore. Është parashikuar që disa lloje të rreziqeve teknologjike mund të përshpejtojnë mundësinë për rreziqe natyrore (dhe në të kundërt), në një rast të tillë modeli do të qëndrojë me shumë mundësi i vlefshëm pasi faktorët shkakor nuk janë modeluar. Është gjithashtu e vërtetë që thelbi i modelit mund të jetë i vlefshëm dhe për modelimin e rreziqeve të tjera, përtej specifikimit të zonave të riskut natyror. Modeli nuk është projektuar duke menduar këto aspekte, por gjithsesi është i vlefshëm për të tilla raste.
Shumë rreziqe janë të papritura për nga natyra e tyre. Gjithsesi, disa prej kategorive të rreziqeve natyrore me një impakt të konsiderueshëm për kontingjentin civil dhe të mirat ambientale/kulturore dhe ekonomike nuk janë të natyrës së papritur. Mund të jenë fenomene permanente që nuk vihen re nga popullata (si p.sh.: emetimet e gazit të radonit, apo lëvizjet e lehta të themeleve). Këto procese të rrezikut konsiderohen brenda modelit. Të gjitha proceset e tjera natyrore, që nuk kanë një impakt potencial negativ në një aktivitet njerëzor, nuk merren në konsideratë.
Në realitet, ngjarjet e kaluara të rrezikut mund të shihen si procese natyrore të vetme, sekuenciale ose të kombinuara në lidhje me origjinën e tyre dhe efektet. Modelimi i këtyre rrethanave e komplikon komunikimin e praktikës së mirë shkencore, në modelimin e marrëdhënieve risk dhe rrezik. Modeli aktual i të dhënave nuk është projektuar për të operuar edhe në rrethanat e një risku të shumëfishtë ose rreziku të shumëfishtë.
Edhe pse modeli i të dhënave përfshin ngjarje të kaluara, të cilat janë të matshme dhe treguese për të kuptuar ngjarjet në të ardhmen, ai nuk merret me ngjarjet në kohë reale ashtu siç janë duke ndodhur, e cila është në fushën e monitorimit dhe reagimit emergjent, as nuk përfshin databazën e katastrofave.
Duke qenë se ka shume rrugë, modele dhe mënyra për të përcaktuar zonat me risk natyror dhe me kushtin që praktika e zakonshme të përdorë të dy llojet e të dhënave të tipit vektor dhe të mbulimit (raster), si të dhënat vektoriale dhe të mbulimit (raster) janë trajtuar në këtë specifikim të të dhënave.
Përderisa klasifikimi i propozuar i rrezikut nuk është i plotë, kjo mënyrë është përfaqësuese dhe duke marrë në konsideratë rreziqe të identifikuara në këtë fushë, një pjesë e madhe e rreziqeve për këtë hapësirë tematike do të merren në konsideratë. Gjithsesi, rekomandohet paraqitja e llojeve më të detajuara të rrezikut.
Për të bërë një përmbledhje, ky standard konsiderohet:
- një qasje e përgjithshme për të gjitha rreziqet natyrore;
- një qasje e përgjithshme për të gjitha zonat e riskut;
- pasqyron vetëm të dhënat më të rëndësishme;
- modelet e rreziqeve;
- ngjarjet e vrojtuara;
- të dhëna që mund të jenë vektoriale ose mbulesë (raster).
Standardi kryesisht nuk ka në konsideratë:
- të dhënat në kohë reale;
- rreziqet teknologjike;
- rreziqet dhe risqet e shumëfishta;
- modelimin e metodave të procesuara dhe shkencore, apo të dhënave të përdorura për përcaktimin e sipërfaqeve të rrezikut, elementeve të ekspozuara dhe zonave të riskut;
- menaxhimin e katastrofave.
Shembujt e përdorimit
Kjo pjesë përshkruan përdoruesit e identifikuar të informacionit gjeohapësinor për rreziqet dhe risqet natyrore, siç është e kërkuar nga grupet e interesit që janë përgjigjur nëpërmjet vrojtimit të kërkesave të përdoruesit. Modeli NZ Core-data mbulon një qasje të përgjithshme me mundësinë e përhapjes së modelit për rreziqe/risqe specifike.
Përdorime dhe përdorues të ndryshëm mund të grupohen në:
- analiza të riskut, për vlerësimin e risqeve natyrore dhe hartografimin e hapësirave që janë objekt i rreziqeve;
- planifikues të sigurisë publike, për rregullimin afatgjatë dhe menaxhimin e tokës dhe aktiviteteve;
- menaxhues të katastrofave, për përgjigjen ndaj katastrofave dhe operacioneve të emergjencave si rrezik paraprak ose input risku;
- përgjegjësi politike për zhvillimin e përgjithshëm të politikave, analizimin dhe sinjalizimin e tendencave, zakonisht në nivel kombëtar dhe ndërkombëtar;
- sigurimi dhe risigurimi për përgatitjen ndaj katastrofave;
- publikimi në përgjithësi për ndërgjegjësimin e qytetarëve.
3.1.2 TERMA DHE PËRKUFIZIME
- “Risk” është kombinimi i konsekuencave/pasojave të një ngjarje (rrezik) dhe gjasave /probabilitetit që kjo ngjarje të ndodhë (ISO 31010).
Shembull: 10000 njerëz do të humbasin furnizimin me ujë të pijshëm gjatë një tërmeti me magnitudë 6 ose më shumë, me një përqindje të caktuar.
- “Rrezik” (Hazard) është një fenomen i rrezikshëm, substancë, aktivitet njerëzor ose gjendje që mund të shkaktojë humbje të jetës, dëmtim ose ndikime të tjera shëndetësore, dëmtim të pronës, humbje të mjeteve të jetesës dhe shërbimeve sociale dhe ekonomike, përkeqësim ose dëmtim mjedisor (UNISDR 2009). Shembull: Rreziku (i) nga tërmeti.
- “Ekspozimi” në njerëz, prona, sisteme ose elemente të tjera prezente në zonat e rreziqeve, që janë gjithashtu objekt i humbjeve të mundshme (UNISDR 2009).
Shembull: Një spital në një zonë të infektuar.
- “Vulnerabilitet” karakteristikat dhe rrethanat e një komuniteti, sistemi ose aseti, që e bëjnë të ndjeshëm nga efektet dëmtuese të një rreziku (UNISDR 2009).
Shembull: Vendasit e moshuar.
3.1.3 SKEMAT E APLIKIMIT DHE DIAGRAMI UML PËR TEMËN “ZONAT ME RREZIQE NATYRORE”
Skema e aplikimit mbulon elemente që konsiderohen si të nevojshme për të përshkruar Zonat e Riskut Natyror. Kjo skemë aplikimi lejon përdoruesit të modelojnë konceptet kryesore siç janë: rreziku, vulnerabiliteti, ekspozimi, risku dhe ngjarja e vëzhguar.
Ne paraqesim në këto specifikime të të dhënave një model në të cilin konceptet janë abstrakte dhe mund të jenë të specializuara si në vektor (për të cilët bazohemi në standardin SSH EN ISO 19107:2005), dhe në mbulime-raster (për të cilët bazohemi në standardin SSH EN ISO 19123:2007).
Kjo është bërë për të krijuar një kornizë, e cila mundëson shkëmbimin e të dhënave që janë ose vektor ose mbulime (raster), duke pasur parasysh se cilido prej 4 objekteve gjeohapësinore mund të modelohet në njërën nga këto 2 mënyra.
Ka 4 lloje të objekteve gjeohapësinore që janë modeluar si vektor, ashtu edhe si mbulim (raster):
- ZonatERrezikut;
- ElementetEEkspozuara;
- ZonatERiskut;
- NgjarjaEVëzhguar.
Për secilën prej tyre, krijohen 3 lloje të objekteve gjeohapësinore:
- Një lloj objekti gjeohapësinor abstrakt që përmban pronat (atributet, apo kufizimet) të objektit gjeohapësinor, që janë të zakonshme si për përfaqësimin vektorial ashtu edhe për mbulimin (raster) të tij.
- Lloji i një objekti gjeohapësinor vektorial që gjenerohet nga objekti gjeohapësinor abstrakt. Ai ka veti që janë specifike për përfaqësimin e vektorit, të tilla si përkufizimi i gjeometrisë.
- Lloji i një objekti gjeohapësinor mbulimi (raster), i cili gjenerohet si nga objekti gjeohapësinor abstrakt, ashtu edhe nga lloji i objektit gjeohapësinor i mbulimit (raster-it) gjenerik. Ai ka pronat që janë specifike për përfaqësimin e mbulimit, siç është përcaktimi i domein-it dhe përkufizimi i vargut. Këto lloje të objekteve gjeohapësinore mbulimi (raster) kanë emrat e tyre të mbivendosur nga “mbulimi”.
Në vijim jepet një përshkrim i përgjithshëm për mënyrën e paraqitjes dhe ndërveprimit të bazës së të dhënave të kësaj teme.
- Zonat e rrezikut:
Më poshtë paraqiten llojet e objekteve gjeohapësinore të tipologjisë zonat e rrezikut (hazad areas):
- ZonaAbstrakteERrezikut;
- ZonatERrezikut (Vektor);
- MbulimiIRrezikut (Coverage).
Llojet e objekteve gjeohapësinore të mësipërme detajohen në atribute me dataType-et e mëposhtme:
- MetodaEPërcaktimit;
- KlasifikimiIRreziqeveNatyrore;
- MundësiaEShfaqjes;
- NiveliOseIntensiteti.
Karakteristikat e përbashkëta të “ZonësAbstrakteTëRrezikut”
Të dhënat gjeohapësinore të tipologjisë “ZonatERrezikut” kanë karakteristikat (atributet) e mëposhtme:
- Një identifikues - Inspire ID
- Një metodë përcaktimi: Ka disa mënyra për të përcaktuar perimetrin e rrezikut; duke e realizuar në përputhje me një model, ose duke e përkufizuar, duke interpretuar nëpërmjet të dhënave dhe/ose informacionit disponibël. Ky është modeluar duke përdorur tipet e të dhënave nga “MetodaPërcaktuese”. Ky tip i të dhënave (dataType) ka 2 vlera të mundshme:
- Modelimi;
- PërcaktiminIndirekt.
- Një lloj rreziku: kjo karakteristikë modelohet me llojet e përcaktuara nga dataType-i “KlasifikimiIRreziqeveNatyrore”.
KlasifikimiIRreziqeveNatyrore, sipas literaturës shkencore, fokusohet mbi natyrën e proceseve ose nga vet origjina e procesit, fizik, kimik ose biologjik (apo të gjitha bashkë), si shkaktarë të dëmeve me një vëmendje të vakët (nëse ka) të vetë dëmit. Ato merren me sisteme të fundme ose procese të fundme, me variabla të fundme dhe rezultate të pritshme të fundme.
Për shkak të faktit se në larminë e rreziqeve natyrore nuk ka një klasifikim gjerësisht të pranueshëm të tipeve të rreziqeve natyrore, është përcaktuar një listë me lloje të përgjithshme rreziqesh, e cila ka:
- Një dataType “KlasifikimiIRreziqeveNatyrore” që përmban:
-Një atribut “KategoriaERrezikut” që i referohet kodlistës: “VleratEKategorisëSëRreziqeveNatyrore”.
Kjo kodlistë hierarkike është përpunuar për të lehtësuar ndërveprueshmërinë në nivele të larta. Është populluar me shumë lloje të rreziqeve natyrore (shiko aneksin C). Gjithsesi kjo kodlistë mund të përhapet me furnizues të të dhënave të rrezikut në terma më të ngjeshur.
- Një atribut që i referohet një kodliste boshe: “VleratELlojeveTëRrezikutSpecifik”. Ky kod është një klasifikim i përcaktuar nga Autoritetet Përgjegjëse, i cili i lejon ato të realizojnë klasifikimin e tyre.
- Data kur objekti gjeohapësinor është futur në grupin e të dhënave dhe data kur objekti është hequr ose zëvendësuar nga një grup të dhënash, paraqiten me atributet “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor”.
- Periudha e vlefshmërisë
Periudha e vlefshmërisë (“PeriudhaEVlefshmërisë”) është korniza kohore fundore deri kur aplikohen rreziqet. I njëjti vlerësim i rrezikut mund të jetë i vlefshëm për një periudhë specifike ose për disa periudha specifike: vlerësimi i rrezikut të zjarreve në pyje efektivisht mund të vlerësohet vetëm në verë, ose ndoshta vetëm në verë ose vetëm në dimër (por jo për gjithë vitin). Ky atribut mund edhe të përdoret në analiza të rrezikut afatgjatë.
- Një lidhje bashkë-shoqërimi me “NgjarjetEVrojtuara”
Mund të përdoret pozicioni i një ngjarje ose eventi të vrojtuar si një input në modelimin e zonave të rrezikuara. Një zonë rreziku mund të ketë një ngjarje të vrojtuar si “burim”. Një lidhje shoqërimi ndërmjet objekteve gjeohapësinore të “ZonatERrezikut” dhe “NgjarjetEVrojtuara” vendoset për të shprehur pikërisht këtë raport. Një zonë rreziku mund të ketë 0 (nëse nuk është përdorur asnjë ngjarje e vrojtuar gjatë procesimit të modelimit të zonës së rrezikut) ose 1 ngjarje të vrojtuar. Kjo lidhje mund të zhvendoset vetëm nga sipërfaqet e ngjarjeve të vrojtuara.
Karakteristika specifike të llojit të objektit gjeohapësinor “ZonatERrezikut”
Përfaqësimi diskret (gjeometrik) i këtij objekti gjeohapësinor modelohet si “Sipërfaqe” ose ndryshe poligon dhe në përbërjen e tij ka dy atribute:
- Mundësia e ndodhjes
Mundësia e ndodhjes shpreh një koncept të përgjithshëm në lidhje me mundësinë (apo shansin) që një ngjarje të ndodhë. Ky atribut është i modeluar me llojin e të dhënave dataType-in “MundësiaENdodhjes”, i cili është një grup prej tri atributesh:
- “MetodaEVlerësimit”, që i referohet metodës së përdorur për të shprehur mundësinë e një ngjarje rreziku.
- “VlerësimiCilësor”, që lejon përshkrimin me gojë të lirë të vlerësimit që i bëhet një mundësie që të ndodhë një ngjarje rreziku.
- “ShpeshtësiaENdodhjes” e cila është njëkohësisht dhe një probabilitet që të ndodhë ose periudhë kthimi të ngjarjes. Kjo pasqyrohet në dy elemente “PeriudhaENdodhjes” dhe “ProbabilitetiINdodhjes”.
- Niveli ose intensiteti
Niveli (magnituda) ose intensiteti, mund të shprehet në mënyrë cilësore dhe në mënyrë sasiore. Për më tepër një vlerë me një shpjegim ka pak interes.
Tipi i të dhënave “NiveliOseIntensiteti” është një grupim prej 3 atributesh:
- VleraCilësore, që është një varg karakteresh (characterstring);
- VleraSasiore, që modelohet si një matje (që është një numër dhe një njësi);
- MetodaEVlerësimit në të cilën mund të shkruhen informacione të mëtejshme.
Karakteristika specifike të llojit të objektit gjeohapësinor “MbulimiIRrezikut”
Në paraqitjen e mbulimit, vlerat që variojnë në hapësirë (d.m.th të deklaruar si intervale të mbulimit) janë gjithashtu dhe NiveliOseIntensiteti i rrezikut ose MundësiaENdodhjes së një rreziku.
- Elementet e ekspozuara
Më poshtë paraqiten llojet e objekteve gjeohapësinore të tipologjisë “Elementeteekspozuara”:
- ElementetAbstrakteTëEkspozuara;
- ElementetEEkspozuara (vektor);
- MbulimiIElementeveTëEkspozuara (coverage).
Llojet e objekteve gjeohapësinore të mësipërme detajohen në atributet e mëposhtme:
- VlerësimiIVulnerabilitetit;
- KlasifikimiIElementëveTëEkspozuar;
- VleratEKategorisëSëRrezikut/Riskut.
Karakteristikat e përbashkëta të “ElementiAbstraktIEkspozuar”
Objekti gjeohapësinor i “ElementëtEEkspozuar” i referohet përfaqësimit gjeohapësinor të njerëzve, pronave, sistemeve ose të tjerë elemente prezente në zonat e rrezikut, që janë objekt i humbjeve të mundshme. Vlerësimi ose llogaritja e vulnerabilitetit mund të ndiqen për të tilla objekte gjeohapësinore.
Të dhënat gjeohapësinore të tipologjisë “ElementëtEEkspozuar” kanë karakteristikat (atributet) e mëposhtme:
- Një identifikues - Inspire ID;
- Data kur objekti gjeohapësinor është futur në grupin e të dhënave dhe data kur objekti është hequr ose zëvendësuar nga një grup të dhënash që paraqiten me atributet “FillimiICiklit Jetësor” dhe “PërfundimiICiklitJetësor”;
- Data kur objekti ka filluar të ekzistojë në realitet dhe data kur objekti nuk ekziston më në realitet (nëse është ashtu). Këto atribute janë “EVlefshmeNga” dhe “EVlefshmeDeri”.
Karakteristikat specifike të “ElementëtEEkspozuar”
Përfaqësimi diskret (gjeometrik) i këtij objekti gjeohapësinor modelohet si “Objekt” që përfshin të gjitha gjeometritë bazike (pikë, linjë ose poligon) dhe në përbërjen e tij llojin e të dhënave dataType-in “VlerësimiIVulnerabilitetit”, që ka karakteristikat e mëposhtme:
- “BurimiIVulnerabilitetit”,
Kjo i referohet tipit të rrezikut në të cilin vulnerabiliteti i elementit të ekspozuar është vlerësuar (ose llogaritur) duke përdorur “KlasifikimiIRreziqeveNatyrore”,
- “NiveliIVulnerabilitetit”,
Ky është rezultat i vlerësimit të vulnerabilitetit. Kjo karakteristikë modelohet me llojin e të dhënave dataType-in “NiveliOseIntesiteti”,
- “MadhësiaDheIntensitetiIVulnerabilitetit”,
Madhësia ose intensiteti i rrezikut në bazë të së cilës vlerësohet (ose llogaritet) vulerabiliteti i objektit të ekspozuar. Kjo karakteristikë modelohet me llojin e të dhënave dataType-in “NiveliOseIntesiteti”,
- “LlojetEElementeve”,
Duke qenë se për momentin nuk ka një listë ose klasifikim të përdorur gjerësisht të llojeve të elementeve të ekspozuara, është përcaktuar një lloj të dhënash i quajtur “KlasifikimiIElementëveTëEkspozuar” për të lehtësuar ndërveprueshmërinë e të dhënave dhe përmban:
- Një atribut të detyrueshëm që i referohet një kodliste ekzistuese: “VleratEKategoriveTëElementeveTëEkspozuara”. Kjo kodlistë hierarkike është përpunuar për të lehtësuar ndërveprueshmërinë në nivele të larta. Është tashmë e populluar me lloje të përgjithshme elementesh të ekspozuara (shiko aneksin C). Gjithsesi kjo kodlistë mund të përhapet nga furnizuesit e të dhënave me terma më të limituara.
- Një atribut që i referohet një kodliste boshe: “VleratETipitTëElementitSpecifikTëEkspozuar”. Ky kod është një tregues për t’i mundësuar autoriteteve përgjegjëse, të të dhënave të ekspozuara, për të përdorur një klasifikim specifik të këtyre elementeve.
Karakteristikat specifike të “MbulimiIElementëveTëEkspozuar”
Mbulimi i elementeve të ekspozuara ka atribut elementin “LlojetEElementeve”, i cili është i modeluar me llojin e të dhënave dataType-in “KlasifikimiIElementëveTëEkspozuar”.
Në paraqitjen e mbulimit, vlerat që variojnë në hapësirë (d.m.th të deklaruar si intervale të mbulimit) janë “MadhësiaDheIntensitetiIVulerabilitetit”.
- Zonat e riskut
Më poshtë paraqiten llojet e objekteve gjeohapësinore të tipologjisë “ZonatERiskut”:
- “ZonaAbstrakteERiskut”;
- “ZonaERiskut (Vektor)”;
- “MbulimiIZonësSëRiskut (Coverage)”.
Karakteristikat e përbashkëta të “ZonaAbstrakteERiskut”
Një zonë risku përkufizohet si shtrirja hapësinore e një kombinimi të pasojave të një ngjarje (rreziku) dhe probabilitetit të lidhur apo gjasat e ndodhjes së saj.
Të dhënat gjeohapësinore të kësaj tipologjie kanë karakteristikat (atributet) e mëposhtme:
- Një identifikues - Inspire ID;
- Një “BurimRisku”
Burimi i riskut i referohet llojit të rrezikut që krijon riskun. Në model, “BurimiRisku” i referohet llojeve të të dhënave të “KlasifikimitTëRreziqeveNatyrore”.
- Data kur objekti gjeohapësinor është futur në grupin e të dhënave dhe data kur objekti është hequr ose zëvendësuar nga një grup të dhënash paraqiten me atributet “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor”
- Një periudhë vlefshmërie (“PeriudhaEVlefshmërisë”) - shiko më sipër ZonaERrezikut
- Një lidhje me “ZonatERrezikut”
Përcaktimi i zonës së riskut rezulton nga bashkëndodhja në të njëjtin vend të rrezikut natyror me elemente që janë të ndjeshme ndaj këtij lloj rreziku. Si pasojë, një zonë risku është potencialisht e lidhur me një zonë rreziku (dhe anasjelltas, si krijimi i një objekti gjeohapësinor të zonës së rrezikut mund të ketë paraprirë krijimin e një objekti të zonës së riskut).
Një lidhje midis llojit të objektit gjeohapësinor të “ZonaERrezikut” dhe llojit të objektit gjeohapësinor të “ZonaveTëRiskut” është vendosur që të shprehë këtë. Çdo zonë risku duhet të ketë një zonë rreziku si burim. Kjo lidhje është e tipit “voidable” dhe mund të marrë vlera nga kodlista “VleratEPavlefshmërisë” nëse nuk popullohet.
- Një lidhje me “ElementëtEEkspozuar”
Në të njëjtën mënyrë siç ka një lidhje midis zonës së rrezikut dhe zonës së riskut, ekziston edhe një lidhje midis zonës së riskut dhe elementeve të ekspozuara. Një zonë risku është potencialisht e lidhur me elementet e ekspozuara, për aq sa një element i ekspozuar duhet të ishte identifikuar si i tillë brenda procesit të prodhimit të një zone risku.
Një lidhje midis llojeve të objekteve gjeohapësinore të “ElementëveTëEkspozuar” dhe llojit të objektit gjeohapësinor të “ZonaERiskut” është vendosur që të shprehë këtë. Ka të paktën një element të ekspozuar për secilën zonë risku. Kjo lidhje është e tipit “voidable” dhe mund të marrë vlera nga kodlista “VleratEPavlefshmërisë” nëse nuk popullohet.
Karakteristikat specifike të “ZonaERiskut”
Përfaqësimi diskret (gjeometrik) i këtij objekti gjeohapësinor modelohet si “Sipërfaqe”. Të gjithëa elementet gjeohapësinore modelohen si poligone dhe në përbërjen e tyre kanë atributet e mëposhtme:
- “NiveliIRiskut”
Është një vlerësim i kombinimit të pasojave të një ngjarjeje (rreziku) dhe probabilitetit të lidhur apo gjasave të ndodhjes së ngjarjes. Kjo karakteristikë është modeluar si një lloj i të dhënave dataType “NiveliOseIntensiteti”.
Karakteristikat specifike të “MbulimiIZonësSëRiskut”
Në paraqitjen e mbulimit, vlerat që variojnë në hapësirë (d.m.th të deklaruara si intervale të mbulimit) janë nivel i riskut. Meqenëse niveli i riskut është modeluar nga tipi i të dhënave “NiveliOseIntensiteti”, kufizimi në rangun e caktuar të mbulimit trajton tipin e të dhënave të “NiveliOseIntensiteti”.
- Ngjarja e vëzhguar
Më poshtë paraqiten llojet e objekteve gjeohapësinore të tipologjisë “NgjarjaEVëzhguar”:
- “NgjarjaAbstrakteEVëzhguar”;
- “NgjarjaEVëzhguar (Vektor)”;
- “MbulimiINgjarjesSëVëzhguar (Coverage)”.
Karakteristikat e përbashkëta të “NgjarjaAbstrakteEVëzhguar”
Një ngjarje e vëzhguar i referohet përfaqësimit gjeohapësinor të një fenomeni lidhur me studimin e rrezikut natyror të ndodhur/apo duke ndodhur dhe që është vëzhguar.
Të dhënat gjeohapësinore të kësaj tipologjie kanë karakteristikat (atributet) e mëposhtme:
- Një identifikues - Inspire ID
- Data kur objekti gjeohapësinor është futur në grupin e të dhënave dhe data kur objekti është hequr ose zëvendësuar nga një grup të dhënash paraqiten me atributet “FillimiICiklitJetësor” dhe “PërfundimiICiklitJetësor”
- Data kur objekti ka filluar të ekzistojë në realitet, dhe data kur objekti nuk ekziston më në realitet (nëse është ashtu). Këto atribute janë “EVlefshmeNga” dhe “EVlefshmeDeri”
- Një lloj rreziku: kjo karakteristikë modelohet me llojet e përcaktuara nga dataType “KlasifikimiIRreziqeveNatyrore”
- Një lidhje me “PrograminEMonitorimitTëMjedisit”
- Meqenëse është një objekt gjeohapësinor që ekziston në realitet atëherë kjo ngjarje e vëzhguar mund të monitorohet. Për të shprehur këtë realizohet një lidhje e tipit “voidable” ndërmjet dataType-it “NgjarjaAbstrakteEVëzhguar” dhe llojit “PrograminEMonitorimitTëMjedisit”.
Karakteristikat specifike të “NgjarjaEVëzhguar”
Përfaqësimi diskret (gjeometrik) i këtij objekti gjeohapësinor modelohet si “Objekt” që përfshin të gjitha gjeometritë bazike (pikë, linjë ose poligon). Ky element ka atribut elementin “MadhësiaOseIntensisteti”, i cili modelohet me llojin e të dhënave “NiveliOse”.
Karakteristikat specifike të “MbulimiINgjarjesSëVëzhguar”
Në paraqitjen e mbulimit, vlerat që variojnë në hapësirë (d.m.th të deklaruara si intervale të mbulimit) janë “MadhësiaOseIntensisteti” dhe “MundësiaENgjarjes”.
[pic]
Figura 5: Diagrami: Zonat e Riskut Natyror - E përgjithshme
[pic]
Figura 6: Zonat e Riskut Natyror - Lidhjet e jashtme
[pic]
Figura 7: DataType-t e grupit të të dhënave
[pic]
Figura 8: DataType dhe Kodlistat
3.1.4 KATALOGU I TIPOLOGJISË
3.1.4.1 ELEMENTET ABSTRAKTE TË EKSPOZUARA
-- Emri --
Elementet abstrakte të ekspozuara
-- Përkufizimi --
Njerëzit, pronat, sistemet ose elementet e tjera të pranishme në zonat e rrezikut, të cilat në këtë mënyrë i nënshtrohen humbjeve të mundshme.
Burimi: (UNISDR, 2009)
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «FeatureType» ElementetEEkspozuara, te «FeatureType» ElementetAbstrakteTëEkspozuara |
|Gjeneralizuar nga «FeatureType» MbulimiIElementëveTëEkspozuar, te «FeatureType» ElementetAbstrakteTëEkspozuara |
|ATRIBUTET |
| |
|[pic]EVlefshmeDeri: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|E vlefshme deri |
|-- Përkufizimi -- |
|Koha nga e cila elementi i ekspozuar nuk ekziston më në realitet. |
|[I detyrueshëm: JO] |
| |
|[pic]EVlefshmeNga: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|E vlefshme nga |
|-- Përkufizimi -- |
|Koha kur elementi i ekspozuar filloi të ekzistonte në realitet. |
|[I detyrueshëm: PO] |
| |
|[pic]FillimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Fillimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objekteve gjeohapësinore është futur ose ndryshuar në grupin e të dhënave gjeohapësinore. |
|[I detyrueshëm: PO] |
| |
|[pic]InspireId: Iidentifikues |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Inspire Id |
|-- Përkufizimi -- |
|Identifikuesi i objektit të jashtëm të elementeve të ekspozuara. |
|[I detyrueshëm: PO] |
| |
|[pic]PërfundimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [0..1] |
|-- Emri -- |
|Përfundimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objekteve gjeohapësinore është modifikuar për herë të fundit në grupin e të dhënave. |
|[I detyrueshëm: JO] |
|LIDHJE |
| |
|[pic]Lidhje (Drejtimi: Burim ->Destinacion) |
|Burimi: (Class) ZonaAbstrakteERiskut «featureType» |Target: «voidable» ElementetEEkspozuara (Class) |
| |ElementetAbstrakteTëEkspozuara «FeatureType» |
| |Shumëllojshmëria: [1..*] |
| | |
| |-- Përkufizimi -- |
| |Elementi që është brenda sipërfaqes së rrezikut. |
3.1.4.2 ELEMENTET E EKSPOZUARA
-- Emri --
Elementet e ekspozuara
-- Përkufizimi --
Objektet gjeohapësinore diskrete që përfaqësojnë elementin e ekspozuar.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic] Gjeneralizuar nga «FeatureType» ElementetEEkspozuara, te «FeatureType» ElementetAbstrakteTëEkspozuara |
|ATRIBUTET |
| |
|[pic] Gjeometri: GM_Object |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Gjeometria |
|-- Përkufizimi -- |
|Përfaqësimi gjeometrik i elementit të ekspozuar. |
|-- Përshkrimi -- |
|Nëse funksioni është i lidhur me një funksion Inspire të referuar gjeohapësinor, atëherë nuk ka gjeometri. Nëse jo, atëherë ka një gjeometri. |
|[I detyrueshëm: PO] |
| |
|[pic]VlerësimiIVulnerabilitetit: VlerësimiIVulnerabilitetit |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Vlerësimi i vulnerabilitetit |
|-- Përkufizimi -- |
|Vlersimi i vulnerabilitetit (censueshmërisë) për elementet e ekspozuara. |
|[I detyrueshëm: PO] |
3.1.4.3 KLASIFIKIMI I RREZIQEVE NATYRORE
-- Emri --
Klasifikimi i rreziqeve natyrore.
-- Përkufizimi--
Ky klasifikim siguron një pjesë të informacionit në lidhje me natyrën dhe llojin e rrezikut, i cili është dhe burimi i riskut.
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]KategoriaERrezikut: VleratEKategoriveTëRreziqeveNatyrore |
|Shumëllojshmëria: [1] |
| |
|-- Emri -- |
|Kategoria e rrezikut |
|-- Përkufizimi -- |
|Një klasifikim i përgjithshëm i llojeve të rrezikut natyror dhe rreziqeve. |
|[I detyrueshëm: PO] |
| |
|[pic]LlojiIRrezikutSpecifik: VleratELlojeveTëRreziqeveSpecifike |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Lloji i rrezikut specifik |
|-- Përkufizimi -- |
|Klasifikimi shtesë i rrezikut natyror që përcakton më tej llojin e rrezikut sipas një nomenklature që është specifike për këtë grup të dhënash. |
|[I detyrueshëm: JO] |
3.1.4.4 KLASIFIKIMI I ELEMENTEVE TË EKSPOZUARA
-- Emri --
Klasifikimi i elementeve të ekspozuara
-- Përkufizimi --
Kjo klasë siguron informacione rreth natyrës së elementeve të ekspozuara që merren në konsideratë gjatë analizës së riskut.
-- Emri--
Klasifikimi i elementeve të ekspozuara
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]KategoriaEElementëveTëEkspozuar: VleratEKategoriveTëElementeveTëEkspozuara |
|shumëllojshmëria: [1] |
|-- Emri-- |
|Kategoritë e elementeve të ekspozuara |
|-- Përkufizimi-- |
|Një klasifikim i përgjithshëm i llojeve të elementeve që janë të ekspozuara ndaj rrezikut. |
|[I detyrueshëm: PO] |
| |
|[pic]LlojetEElementëveSpecifikTëEkspozuar: VleratELlojeveTëElementëveSpecifikTëEkspozuar |
|shumëllojshmëria: [1] |
|-- Emri-- |
|Llojet e elementeve specifike të ekspozuara |
|-- Përkufizimi-- |
|Një emërtim shtesë i elementit të ekspozuar sipas një nomenklature që është specifike për këtë grup të dhënash. |
|[I detyrueshëm: PO] |
3.1.4.5 MBULIMI I RREZIKUT
-- Emri --
Mbulimi i rrezikut
-- Përkufizimi --
Një mbulim që përfaqëson informacion të vazhdueshëm në lidhje me një lloj rreziku natyror.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «FeatureType» MbulimIRrezikut, te «FeatureType» MbulimiSipasDomeinitDheGamës |
|[pic] Gjeneralizuar nga «FeatureType» MbulimIRrezikut, te «FeatureType» ZonaAbstrakteERrezikut |
3.1.4.6 MBULIMI I RISKUT
-- Emri --
Mbulimi i riskut
-- Përkufizimi --
Përfaqësimi i mbulimit të riskut natyror.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «FeatureType» MbulimiIRiskut, te «FeatureType» MbulimiSipasDomeinitDheGamës |
|[pic] Gjeneralizuar nga «FeatureType» MbulimiIRiskut, te «FeatureType» ZonaAbstrakteERiskut |
3.1.4.7 MBULIMI I ELEMENTEVE TË EKSPOZUARA
-- Emri --
Mbulimi i elementeve të ekspozuara
-- Përkufizimi --
Një mbulim që paraqet informacion të vazhdueshëm rreth elementeve të ekspozuara.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic] Gjeneralizuar nga « FeatureType» MbulimiIElementëveTëEkspozuar, te «FeatureType» MbulimiSipasDomeinitDheGamës |
|Gjeneralizuar nga «FeatureType» MbulimiIElementëveTëEkspozuar, te «FeatureType» ElementetAbstrakteTëEkspozuara |
|ATRIBUTET |
| |
|[pic]LlojiIElementëve: KlasifikimiIElementëveTëEkspozuar |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Llojet e elementeve |
|-- Përkufizimi -- |
|Një klasifikim i elementeve të ekspozuara. |
|[I detyrueshëm: PO] |
3.1.4.8 MBULIMI I NGJARJEVE TË VËZHGUARA
-- Emri--
Mbulimi i ngjarjeve të vëzhguara
-- Përkufizimi--
Një mbulim që përfaqëson informacion të vazhdueshëm rreth rasteve të vrojtuara.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic] Gjeneralizuar nga «FeatureType» MbulimiIRasteveTëVrojtuara, te «FeatureType» MbulimiSipasDomeinitDheGamës |
|[pic]Gjeneralizuar nga «FeatureType» MbulimiIRasteveTëVrojtuara, te «FeatureType» RastetAbstrakteTëVrojtuara |
3.1.4.9 MUNDËSIA E NGJARJES
-- Emri --
Mundësia e ngjarjes
-- Përkufizimi --
Mundësia e ngjarjes (Likelihood) është një koncept i përgjithshëm në lidhje me mundësinë që një ngjarje të ndodhë.
-- Përshkrimi --
Mundësia e ngjarjes (Likelihood) në përgjithësi shprehet si probabilitet ose frekuencë.
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]MetodaEVlerësimit: CitimiIDokumentit |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Metoda e vlerësimit |
|-- Përkufizimi -- |
|Një citim për metodën e përdorur për të shprehur mundësitë. |
|[I detyrueshëm: PO] |
| |
|[pic]VlerësimiCilësor: Tekst |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Vlerësimi cilësor |
|-- Përkufizimi -- |
|Një vlerësim cilësor i mundësive të shfaqjes së një rreziku |
|-- Përshkrimi -- |
|Ndonjëherë, kjo njihet si ndjeshmëri. |
|[I detyrueshëm: PO] |
| |
|[pic]VlerësimiSasior: VlerësimiSasior |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Vlerësimi sasior |
|-- Përkufizimi -- |
|Një vlerësim sasior i mundësive të shfaqjes së një rreziku. |
|-- Përshkrimi -- |
|Ndonjëherë, kjo njihet si ndjeshmëri. |
|[I detyrueshëm: PO] |
3.1.4.10 NGJARJA ABSTRAKTE E VËZHGUAR
-- Emri --
Rastet abstrakte të vëzhguara
-- Përkufizimi--
Një fenomen natyror i përshtatshëm për studimet e rreziqeve natyrore që kanë ndodhur dhe që janë vëzhguar.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic] Gjeneralizuar nga «FeatureType» RastiIVëzhguar, te «FeatureType» RastetAbstrakteTëVrojtuara |
|[pic] Gjeneralizuar nga «FeatureType» MbulimiIRasteveTëVrojtuara, te «FeatureType» RastetAbstrakteTëVrojtuara |
|ATRIBUTET |
| |
|[pic]EmriIRastit: Tekst |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Emri i rastit |
|-- Përkufizimi -- |
|Emri i zakonshëm i ngjarjes së vëzhguar. |
|[I detyrueshëm: PO] |
| |
|[pic]EVlefshmeDeri: datë-orë |
|Shumëllojshmëria: [0..1] |
|-- Emri -- |
|E vlefshme deri |
|-- Përkufizimi -- |
|Koha nga e cila rasti i vëzhguar nuk ekziston më në realitet. |
|[I detyrueshëm: PO] |
| |
|[pic]EVlefshmeNga: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|E vlefshme nga |
|-- Përkufizimi -- |
|Koha kur rasti i vëzhguar filloi të ekzistonte në realitet. |
|[I detyrueshëm: PO] |
| |
|[pic]FillimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Fillimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave gjeohapësinore. |
|[I detyrueshëm: PO] |
| |
|[pic]Inspireid: Identifikues |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|InspireId |
|-- Përkufizimi -- |
|Identifikuesi i objektit të jashtëm të objektit gjeohapësinor. |
|[I detyrueshëm: PO]] |
| |
|[pic]LlojetERreziqeve: KlasifikimiIRreziqeveNatyrore |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Llojet e rreziqeve |
|-- Përkufizimi -- |
|Një klasifikim i përgjithshëm dhe një klasifikim specifik i llojit të rrezikut. |
|[I detyrueshëm: PO]] |
| |
|[pic]PërfundimiICiklitJetësor: dDatë-orë |
|Shumëllojshmëria: [0..1] |
|-- Emri -- |
|Përfundimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objektit gjeohapësinor u zëvendësua ose u tërhoq në grupin e të dhënave gjeohapësinore. |
|[I detyrueshëm: JO] |
|LIDHJE |
| |
|[pic]Lidhje (Drejtimi:Burim ->Destinacion) |
|Burimi: (Class) RastetAbstrakteTëVrojtuara «FeatureType» |Target: «voidable» MonitorohetNga (Class) Programet E |
| |MonitorimitTëAmbientit «FeatureType» |
| |Shumëllojshmëria: [0..*] |
| | |
| |-- Përkufizimi -- |
| |Programi që monitoron ngjarjen e vrojtuar. |
| |
|[pic]Lidhje (Drejtimi: Burim ->Destinacion) |
|Burimi:(Class) ZonaAbstrakteERrezikut «feature Type» |Target: «voidable» Burimi (Class) RastetAbstrakteTëVrojtuara |
| |«featureType» |
| |Shumëllojshmëria: [0..*] |
| | |
| |-- Përkufizimi -- |
| |Ngjarja e vrojtuar që shkaktoi modelimin e një sipërfaqe të |
| |rrezikut. |
3.1.4.11 NIVELI OSE INTENSITETI
-- Emri --
Niveli ose intensiteti
-- Përkufizimi--
Vlerësimi në mënyrë sasiore ose cilësore i riskut, rrezikut ose vulnerabilitetit.
-- Përshkrimi--
Koncept i përbashkët për vlerësimin e nivelit të riskut, rrezikut, apo nivelit të vulnerabilitetit.
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]MetodaEVlerësimit: CitimIDokumentit |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Metoda e vlerësimit |
|-- Përkufizimi -- |
|Një shprehje për metodën e përdorur për të shprehur nivelin ose intensitetin. |
|[I detyrueshëm: PO] |
| |
|[pic]VleratCilësore: Tekst |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Vlera cilësore |
|-- Përkufizimi -- |
|Një vlerësim cilësor i nivelit ose intensitetit. |
|[I detyrueshëm: PO] |
| |
|[pic]VleratSasiore: Matje |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Vlerat sasiore |
|-- Përkufizimi -- |
|Një vlerësim në mënyrë sasiore i nivelit ose intensitetit. |
|[I detyrueshëm: PO] |
3.1.4.12 NGJARJA E VËZHGUAR
-- Emri --
Ngjarja e vëzhguar
-- Përkufizimi --
Objektet gjeohapësinore diskrete që përfaqësojnë fenomenin natyror, që lidhet me studimin e rreziqeve natyrore, që kanë ndodhur ose që ndodhin aktualisht dhe që janë vëzhguar.
-- Tipi i elementit --
Featuretype
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «featureType» RastiIVëzhguar, te «FeatureType» RastetAbstrakteTëVrojtuara |
|ATRIBUTET |
| |
|[pic] Gjeometria: GM_Objekt |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Gjeometria |
|-- Përkufizimi -- |
|Përfaqësimi gjeometrik i shtrirjes gjeohapësinore të mbuluar nga rasti i vëzhguar. |
|[I detyrueshëm: PO] |
| |
|[pic]OrigjinalitetiIMadhësisë: Niveli ose intensiteti |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Niveli ose intensiteti |
|-- Përkufizimi -- |
|Një shprehje e madhësisë ose intensitetit të një fenomeni. |
|[I detyrueshëm: PO] |
3.1.4.13 ZONA ABSTRAKTE E RISKUT
-- Emri --
Zona abstrakte e riskut
-- Përkufizimi --
Një zonë risku është një shtrirje hapësinore e kombinimit të pasojave të një rasti (rreziku) dhe probabilitetit/mundësisë lidhur me ndodhjen e tij.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË BRENDSHME |
|[pic]Gjeneralizuar nga «FeatureType» ZonatERiskut, te «FeatureType» ZonaAbstrakteERiskut |
|[pic]Gjeneralizuar nga «FeatureType» MbulimiIRiskut, te «FeatureType» ZonaAbstrakteERiskut |
|ATRIBUTET |
| |
|[pic]BurimiIRiskut: KlasifikimiIRreziqeveNatyrore |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Burimi i riskut |
|-- Përkufizimi -- |
|Një klasifikim i përgjithshëm dhe një klasifikim specifik të llojit të rrezikut që është burim i riskut. |
|[I detyrueshëm: PO] |
| |
|[pic]FillimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Fillimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora kur ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave. |
|[I detyrueshëm: PO] |
| |
|[pic]InspireId: Identifikues |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|InspireId |
|-- Përkufizimi -- |
|Identifikuesi i objektit të jashtëm të objektit gjeohapësinor. |
|[I detyrueshëm: PO] |
| |
|[pic]PërfundimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [0..1] |
|-- Emri -- |
|Përfundimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora kur ky version i objektit gjeohapësinor është modifikuar për herë të fundit në grupin e të dhënave. |
|[I detyrueshëm: JO] |
| |
|[pic]PeriudhëEVlefshme: TM_periudhë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Periudhë e vlefshme |
|-- Përkufizimi -- |
|Korniza kohore e afërt në të cilën vlen rreziku. |
|-- Përshkrimi -- |
|Është një interval i datave, ose shprehja e një kornize kohore për të cilën vlerësimet janë përcaktuar. |
|[I detyrueshëm: PO] |
|LIDHJE |
| |
|[pic]Lidhje (Drejtimi: Burimi ->Destinacioni) |
|Burimi: (Class) ZonaAbstrakteERiskut «FeatureType» |Target: «voidable» ElementetEEkspozuara (Class) |
| |ElementetAbstrakteTëEkspozuara «FeatureType» |
| |Shumëllojshmëria: [1..*] |
| | |
| |-- Përkufizimi -- |
| |Elementi që është brenda sipërfaqes së rrezikut. |
| |
|[pic]Lidhje (Drejtimi: Destinacion ->Burim) |
|Burim: «voidable» Burimi: (Class) ZonaAbstrakteERrezikut «FeatureType» |Target: (Class) ZonaAbstrakteeRiskut «FeatureType» |
|Shumëllojshmëria: [1] | |
|-- Përkufizimi -- | |
|Rreziku që konsiderohet në krijimin e objektit të zonës së riskut. | |
3.1.4.14 ZONA ABSTRAKTE E RREZIKUT
-- Emri --
Zona abstrakte e rrezikut
-- Përkufizimi --
Një zonë e prekur nga një rrezik natyror.
-- Përshkrimi --
Rreziku natyror është një proces apo fenomen natyror që mund të shkaktojë humbje të jetës, lëndime ose ndikime të tjera, dëmtimin e pronës, jetesës dhe shërbimet e humbura, stabilitetin social dhe ekonomik ose dëmtimin e mjedisit.
[Këshilli i Bashkimit Evropian - Dokumenti i punës i stafit të komisionit - Udhëzimet për vlerësimin dhe hartimin e rrezikut për menaxhimin e fatkeqësive]
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË BRENDSHME |
|[pic]Gjeneralizuar nga «FeatureType» ZonaERrezikut, te «FeatureType» ZonaAbstrakteERrezikut |
|[pic] Gjeneralizuar nga «FeatureType» MbulimIRrezikut, te «FeatureType» ZonaAbstrakteERrezikut |
|ATRIBUTET |
| |
|[pic]FillimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Fillimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave. |
|[I detyrueshëm: PO] |
| |
|[pic]InspireId: Identifikues |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|InspireId |
|-- Përkufizimi -- |
|Identifikuesi i objektit të jashtëm të zonës së rrezikut |
|[I detyrueshëm: PO] |
| |
|[pic]LlojiIRrezikut: KlasifikimiIRreziqeveNatyrore |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Lloji i rrezikut |
|-- Përkufizimi -- |
|Një klasifikim i përgjithshëm dhe një klasifikim specifik i llojit të rrezikut natyror. |
|[I detyrueshëm: PO] |
| |
|[pic]MetodaEPërcaktimit: VleratEMetodësSëPërcaktimit |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Metoda e përcaktimit |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objektit gjeohapësinor është futur ose ndryshuar në grupin e të dhënave. |
|[I detyrueshëm: PO] |
| |
|[pic]PërfundimiICiklitJetësor: datë-orë |
|Shumëllojshmëria: [0..1] |
|-- Emri -- |
|Përfundimi i ciklit jetësor |
|-- Përkufizimi -- |
|Data dhe ora në të cilën ky version i objektit gjeohapësinor është modifikuar për herë të fundit në grupin e të dhënave. |
|[I detyrueshëm: JO] |
| |
|[pic]PeriudhëEVlefshme: TM_Periudhë |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Periudhë e vlefshme |
|-- Përkufizimi -- |
|Korniza kohore e afërt ku vlen rreziku. |
|[I detyrueshëm: PO] |
|LIDHJE |
| |
|[pic]Lidhje (Drejtimi: Burim ->Destinacion) |
|Burimi: (Class) ZonaAbstrakteERrezikut «FeatureType» | Target: «voidable» |
| |Burimi (Class) RastetAbstrakteTëVrojtuara «FeatureType» |
| |Shumëllojshmëria: [0..*] |
| | |
| |-- Përkufizimi -- |
| |Ngjarja e vrojtuar që shkaktoi modelimin e një sipërfaqe të |
| |rrezikut. |
| |
|[pic]Lidhje (Drejtimi: Destinacion -> Burim) |
|Burimi: «voidable» Burimi: (Class) ZonaAbstrakteERrezikut «FeatureType» | target: (Class) ZonaAbstrakteERreziku «FeatureType» |
|Shumëllojshmëria: [1] | |
| | |
|-- Përkufizimi -- | |
|Rreziku që konsiderohet në krijimin e objektit të zonës së riskut. | |
3.1.4.15 ZONA E RREZIKUT
-- Emri --
Zona e rrezikut
-- Përkufizimi --
Objektet gjeohapësinore diskrete që përfaqësojnë një rrezik natyror.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «FeatureType» ZonaERrezikut, te «FeatureType» ZonaAbstrakteERrezikut |
|ATRIBUTET |
| |
|[pic] Gjeometria: GM_Sipërfaqe |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Gjeometria |
|-- Përkufizimi -- |
|Përfaqësimi gjeometrik i shtrirjes hapësinore të mbuluar nga zona e rrezikut. |
|[I detyrueshëm: PO] |
| |
|[pic]MadhësiaOseIntensiteti: NiveliOseIntensiteti |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Madhësia ose intensiteti |
|-- Përkufizimi -- |
|Shprehja e madhësisë ose intensitetit të një fenomeni. |
|-- Përshkrimi -- |
|Mund të adresojë një vlerë brenda shkallës rihter, ose një përshkrim të shkallës makro-sizmike evropiane ose një rrjedhje, përmbytje, etj. |
|[I detyrueshëm: PO] |
| |
|[pic]MundësiaENgjarjes: MundësiaENgjarjes |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Mundësia e ngjarjes |
|-- Përkufizimi -- |
|Ngjarja (likelihood) është një koncept i përgjithshëm në lidhje me mundësinë që një ngjarje të ndodhë. |
|[I detyrueshëm: PO] |
3.1.4.16 ZONAT E RISKUT
-- Emri --
Zonat e riskut
-- Përkufizimi --
Objektet gjeohapësinore diskrete që përfaqësojnë shtrirjen hapësinore të një kombinimi të pasojave të një rasti (rreziku) dhe probabilitetin/mundësinë e lidhur me ndodhjen e tij.
-- Tipi i elementit --
FeatureType
|LIDHJE STRUKTURORE TË JASHTME |
|[pic]Gjeneralizuar nga «FeatureType» ZonatERiskut, te «FeatureType» ZonaAbstrakteERiskut |
|ATRIBUTET |
| |
|[pic] Gjeometria: GM_Sipërfaqe |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Gjeometria |
|-- Përkufizimi -- |
|Përfaqësimi gjeometrik i shtrirjes hapësinore të mbuluar nga zona e riskut |
|[I detyrueshëm: PO] |
| |
|[pic]NiveliIRreziku: NiveliOseIntensiteti |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Niveli i rrezikut |
|-- Përkufizimi -- |
|Niveli i riskut është një vlerësim i kombinimit të pasojave të një rasti (rreziku) dhe probabiliteti/mundësia e lidhur me ndodhjen e tij. |
|[I detyrueshëm: PO] |
3.1.4.17 VLERËSIMI SASIOR
-- Emri --
Vlerësimi sasior
-- Përkufizimi--
Mundësia që të ndodhë apo të përsëritet periodikisht një fenomen rreziku.
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]PeriudhaEKthimit: VlerëNumerike |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Periudha e kthimit |
|-- Përkufizimi -- |
|Intervali afatgjatë i kohës ose numri i viteve brenda të cilave një ngjarje do të barazohet ose tejkalohet. |
|[I detyrueshëm: PO] |
| |
|[pic]ProbabilitetiINdodhjes: Probabilitet |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Probabiliteti i ndodhjes |
|-- Përkufizimi -- |
|Probabiliteti i ndodhjes së një rreziku, shprehur si një vlerë midis 0 dhe 1. |
|-- Përshkrimi -- |
|Kjo është vlera inverse e periudhës së kthimit. |
|[I detyrueshëm: PO] |
3.1.4.18 VLERËSIMI I VULNERABILITETIT
-- Emri --
Vlerësimi i vulnerabilitetit
-- Përkufizimi--
Vlerësimi i vulnerabilitetit
-- Përshkrimi--
Ai përmban pjesë të informacionit në lidhje me burimin e vulnerabilitetit, nivelin e tij, si dhe rreth madhësisë apo intensitetit të rrezikut, për të cilin vlerësohet vulnerabiliteti.
-- Tipi i elementit --
DataType
|ATRIBUTET |
| |
|[pic]BurimiIVulnerabilitetit: KlasifikimiIRreziqeveNatyrore |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Burimi i vulnerabilitetit |
|-- Përkufizimi -- |
|Lloji i rrezikut për të cilin vlerësohet vulnerabiliteti. |
|[I detyrueshëm: PO] |
| |
|[pic]LlojiIElementit: KlasifikimiIElementëveTëEkspozuar |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Lloji i elementit |
|-- Përkufizimi -- |
|Një klasifikim i elementeve të ekspozuara. |
|[I detyrueshëm: PO] |
| |
|[pic]MadhësiaDheIntensitetiIRrezikut: NiveliOseIntensiteti |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Madhësia ose intensiteti i rrezikut |
|-- Përkufizimi -- |
|Një shprehje e madhësisë ose intensitetit të një fenomeni. |
|-- Përshkrimi -- |
|Mund të adresojë një vlerë brenda shkallës rihter ose një përshkrim të shkallës makro-sizmike evropiane ose një rrjedhje përmbytje, etj. |
|[I detyrueshëm: PO] |
| |
|[pic]NiveliIVulnerabilitetit: NiveliOseIntensiteti |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Niveli i vulnerabilitetit |
|-- Përkufizimi -- |
|Niveli i vulnerabilitetit |
|-- Përshkrimi -- |
|Kur vlerësohet në mënyrë sasiore, është përqindje. |
|[I detyrueshëm: PO] |
3.1.4.19 VLERAT E METODËS SË PËRCAKTIMIT
-- Emri --
Vlerat e metodës së përcaktimit
-- Përkufizimi --
Një numërim për të përshkruar metodën e përdorur, për të përcaktuar zonën e riskut ose të rrezikut.
-- Përshkrimi--
Ekzistojnë disa mënyra për të përcaktuar perimetrin e një risku ose rreziku: ta modeloni atë, ose ta vlerësoni atë në mënyrë indirekte.
-- Tipi i elementit --
Enumeration-Numërtim
|ATRIBUTET |
| |
|[pic] Modelimi: |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Modelimi |
|-- Përkufizimi-- |
|Zona është llogaritur sipas një modeli. |
|[I detyrueshëm: PO] |
| |
|[pic]PërcaktimiIndirekt: |
|Shumëllojshmëria: [1] |
|-- Emri -- |
|Përcaktimi indirekt. |
|-- Përkufizimi-- |
|Zona është përcaktuar nga interpretimi i të dhënave dhe/ose informacionit në dispozicion. |
|[I detyrueshëm: PO] |
3.1.4.20 VLERAT E LLOJEVE TË ELEMENTEVE SPECIFIKE TË EKSPOZUARA
-- Emri --
Vlerat e llojeve të elementeve specifike të ekspozuara
-- Përkufizimi --
Një emërtim shtesë i elementeve të ekspozuara
-- Përshkrimi --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e përcaktuara nga ofruesit e të dhënave.
-- Tipi i elementit --
Kodlistë
3.1.4.21 VLERAT E LLOJEVE TË RREZIQEVE SPECIFIKE
-- Emri -
Vlerat e llojeve të rreziqeve specifike.
-- Përshkrimi -
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e përcaktuara nga ofruesit e të dhënave.
-- Tipi i elementit -
Kodlistë.
3.1.4.22 VLERAT E KATEGORIVE TË RREZIQEVE NATYRORE
-- Emri --
Vlerat e kategorive të rreziqeve natyrore.
-- Përkufizimi--
Një klasifikim i përgjithshëm i llojeve të rreziqeve natyrore.
-- Përshkrimi--
Vlerat e lejuara për këtë kodlistë specifikohen në aneksin C.
-- Tipi i elementit --
Kodlistë
3.1.4.23 VLERAT E KATEGORIVE TË ELEMENTEVE TË EKSPOZUARA
-- Emri --
Vlera e kategorisë së elementeve të ekspozuara.
-- Përkufizim --
Një klasifikim i elementeve të ekspozuara specifikuar në aneksin C
-- Tipi i elementit --
KodListë
3.2 METADATA
Përshtatja e elementeve të metadatës përcaktohet në rregulloren e miratuar me vendimin nr. 1077, datë 23.12.2015, të Këshillit të Ministrave “Për krijimin, ruajtjen dhe përditësimin e metadatave, strukturën e katalogimit dhe afatet e krijimit të metadatave specifike për çdo temë”.
3.3 KODI EPSG PËR KRGJSH-në
Referenca gjeodezike e të dhënave gjeohapësinore mbështetet në Kornizën Referuese Gjeodezike Shqiptare sipas vendimit nr. 669, datë 7.8.2013, të Këshillit të Ministrave, “Për miratimin e rregullave për përcaktimin, krijimin dhe realizimin e Kornizës Referuese Gjeodezike Shqiptare (KRGJSH), si metadatë” ndryshuar me vendimin nr. 322, datë 27.4.2016, dhe vendimin nr. 359, datë 29.5.2019.
Kodi EPSG për Kornizën Referuese Gjeodezike Shqiptare (KRGJSH) është: EPSG - 6870.
3.4 CILËSIA E TË DHËNAVE
Ky kapitull përfshin një përshkrim mbi cilësinë e të dhënave të elementeve dhe nënelementeve, si dhe cilësinë e matjes së të dhënave, që duhen përdorur për të vlerësuar dhe dokumentuar cilësinë e tyre për grupet e të dhënave që lidhen me të dhënat gjeohapësinore të temës “Zonat me rreziqe natyrore”.
Cilësia e të dhënave të elementeve, nënelementeve dhe matjeve duhet të përdoret për të:
- Vlerësuar dhe dokumentuar cilësinë e të dhënave dhe kufizimet e objekteve gjeohapësinore, ku karakteristikat ose kufizimet e tilla përcaktohen si pjesë e skemës së aplikimit.
- Vlerësuar dhe dokumentuar cilësinë e të dhënave të elementeve, të metadatave të grupeve të të dhënave gjeohapësinore.
- Për të specifikuar kërkesat ose rekomandimet në lidhje me rezultatet e cilësisë së të dhënave, të zbatueshme për grupet e të dhënave gjeohapësinore, që lidhen me temën “Zonat me rreziqe natyrore”.
Tabela e mëposhtme, paraqet të gjitha elementet dhe nënelementet e cilësisë së të dhënave që përdoren në këtë specifikim. Informacioni i cilësisë së të dhënave mund të vlerësohet në nivelin e objektit gjeohapësinor, llojit të objektit gjeohapësinor, datasetit ose grupit të të dhënave. Niveli në të cilin bëhet vlerësimi është dhënë në kolonën e “Sfera e vlerësimit”.
Masat që do të përdoren për secilën nga nënelementet e listuara të cilësisë së të dhënave janë përcaktuar në nënseksionet e mëposhtme.
Tabela - Elementet e cilësisë së të dhënave gjeohapësinore të përdorura në temën “Zonat me rreziqe natyrore”
| |Elementi i cilësisë së të |Nënelementi i cilësisë së | |Sfera e vlerësimit |
|Pjesa |dhënave |të dhënave |Përkufizimi | |
|7.1.1 |Përputhja logjike |Përputhja konceptuale |Zbatimin i rregullave të skemës konceptuale |Llojet e objekteve |
| | | | |gjeohapësinore, grupet e të |
| | | | |dhënave |
|7.1.2 |Përputhja logjike |Përputhja në domain-in |Zbatimin e vlerave, në vlerat e doman-it |Llojet e objektit |
| | | | |gjeohapësinor, objekti |
| | | | |gjeohapësinor |
3.4.1 PËRPUTHJA LOGJIKE - PËRPUTHJA KONCEPTUALE (LOGICAL CONSISTENCY - CONCEPTUAL CONSISTENCY)
Rekomandim
Për testet në përputhjet konceptuale, rekomandohet të përdoren nënelementet e cilësisë së të dhënave të përputhjes logjike - përputhjes konceptuale dhe masa e numrave të artikujve që nuk janë në përputhje me rregullat e skemës konceptuale të specifikuara në tabelën e mëposhtme:
|Emri |Skema konceptuale e përcaktuar |
|Emri alternativ |- |
|Cilësia e të dhënave të elementeve |Përputhja logjike |
|Cilësia e të dhënave të nënelementeve |Përputhja konceptuale |
|Cilësia e të dhënave të matjeve themelore |Numërimi i gabimit |
|Përkufizim |Numërimi i të gjithë artikujve në grupin e të dhënave që nuk janë në përputhje |
| |me rregullat e skemës konceptuale. |
|Përshkrimi |Nëse skema konceptuale përshkruan shprehimisht ose në mënyrë të saktë rregullat,|
| |këto rregulla duhet të ndiqen. Shkeljet ndaj rregullave të tilla mund të jenë, |
| |për shembull, vendosja e pavlefshme e karakteristikave brenda një tolerance të |
| |përcaktuar, dyfishimi i karakteristikave dhe mbivendosja e pavlefshme e |
| |karakteristikave. |
|Fusha e vlerësimit |Objekt gjeohapësinor: Llojet e objekteve gjeohapësinore. |
|Fusha e raportimit |Grupi i të dhënave |
|Parametër |- |
|Cilësia e të dhënave të llojeve të vlerave |Integer |
|Cilësia e të dhënave të strukturës së vlerave |- |
|Burimi reference |SSH EN ISO19157:2013 Informacion Gjeografik - Cilësia e të dhënave |
|Shembull |- |
|Masa identifikuese |10 |
3.4.2 PËRPUTHJA LOGJIKE - PËRPUTHJA ME DOMAIN-in (LOGICAL CONSISTENCY - DOMAIN CONSISTENCY)
Rekomandim
Për testet në përputhjet me domain-in, rekomandohet të përdoren nënelementet e cilësisë së të dhënave të përputhjes ligjore - përputhjes me domain-in dhe masa e numrit të artikujve që nuk janë në përputhje me vlerën e domain-it të tyre, të përcaktuar në tabelën e mëposhtme:
|Emri |Vlera e moskonformitetit të domein-it |
|Emri alternativ |- |
|Cilësia e të dhënave të elementeve |Përputhja ligjore |
|Cilësia e të dhënave të nënelementeve |Përputhja me domain-in |
|Cilësia e të dhënave të matjeve themelore |Numërimi i gabimit |
|Përkufizim |Numërimi i të gjithë artikujve në grupin e të dhënave që nuk janë në përputhje |
| |me vlerën e domein-it të tyre |
|Përshkrimi |- |
|Fusha e vlerësimit |Objekt gjeohapësinor: llojet e objekteve gjeohapësinore |
|Fusha e raportimit |Grupi i të dhënave |
|Parametër |- |
|Cilësia e të dhënave të llojeve të vlerave |Integer |
3.4.3 KËRKESAT MINIMALE TË CILËSISË SË TË DHËNAVE (MINIMUM DATA QUALITY REQUIREMENTS)
Nuk përcaktohen kërkesat minimale të cilësisë së të dhënave.
4. ANEKSE
4.1 ANEKS A - KATALOGU I TIPOLOGJISË
|Nr. |Emri i elementit, anglisht |Emri i elementit, shqip |Nëntema |Tipi |
|ZONAT ME RREZIQE NATYRORE |
| | | | | |
|3.1.4.1 |Coverage |MbulimiIRrezikut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.2 |ExposedElementCoverage |MbulimiIElementëveTëEkspozuar |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.3 |ObservedEventCoverage |MbulimiINgjarjeveTëVëzhguara |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.4 |RiskCoverage |MbulimiI Riskut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.5 |AbstractExposedElement |ElementëtAbstraktTëEkspozuar |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.6 |AbstractObservedEvent |NgjarjaAbstrakteEVëzhguar |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.7 |AbstractRiskZone |ZonaAbstrakteERiskut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.8 |AbstractArea |ZonaAbstrakteERrezikut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.9 |ObservedEvent |NgjarjaEVëzhguar |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.10 |Area |ZonaERrezikut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.11 |RiskZone |ZonaERiskut |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.12 |ExposedElement |ElementetEEkspozuara |Zonat me rreziqe natyrore |FeatureType |
|3.1.4.13 |LevelOrintensity |NiveliOseIntensiteti |Zonat me rreziqe natyrore |dataType |
|3.1.4.14 |LikeLihoodOfOccurrence |MundësiaENgjarjes |Zonat me rreziqe natyrore |dataType |
|3.1.4.15 |QuantitativeLikelihood |VlerësimiSasior |Zonat me rreziqe natyrore |dataType |
|3.1.4.16 |VulnerabilityAssessment |VlerësimiIVulnerabilitetit |Zonat me rreziqe natyrore |dataType |
|3.1.4.17 |NaturalClassification |KlasifikimiIRreziqeveNatyrore |Zonat me rreziqe natyrore |dataType |
|3.1.4.18 |ExposedElementClassification |KlasifikimiIElementeveTëEkspozuara |Zonat me rreziqe natyrore |dataType |
|3.1.4.19 |DeterminationMethodValue |VleratEMetodësSëPërcaktimit |Zonat me rreziqe natyrore |codeListe |
|3.1.4.20 |SpecificExposedElementTypeValue|VleratELlojeveTëElementeveSpecifikeTëEkspoz|Zonat me rreziqe natyrore |codeListe |
| | |uara | | |
|3.1.4.21 |SpecificTypeValue |VleratELlojeveTëRreziqeveSpecifike |Zonat me rreziqe natyrore |codeListe |
|3.1.4.22 |NaturalClassificatiValue |VleratEKategorisëSëRreziqeveNatyrore |Zonat me rreziqe natyrore |codeListe |
|3.1.4.23 |ExposedElementCategoryValue |VleratELlojeveTëElementeveTëEkspozuara |Zonat me rreziqe natyrore |codeListe |
4.2 ANEKS B - KODLISTAT
4.2.1 KATEGORIA E ELEMENTEVE TË EKSPOZUARA
-- Emri --
Vlera e kategorive të elementeve të ekspozuara
-- Përkufizimi --
Një klasifikim i elementit të ekspozuar
-- Identifikuesi --
http://inspire.ec.europa.eu/codelist/ExposedElementCategoryValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përbëhen nga vlerat e specifikuara në tabelën e mëposhtme dhe nga vlerat shtesë të çfarëdo niveli të përcaktuara nga ofruesit e të dhënave.
|Kodlistë |
|-- Emri -- |
|Sociale |
|-- Përkufizimi -- |
|Çdo gjë që lidhet me njerëz ose grupe njerëzish |
| |
|-- Emri -- |
|Njerëz |
|-- Përkufizimi -- |
|Prania e qenieve njerëzore. |
|--Varësia-- |
|Sociale |
| |
|-- Emri -- |
|Komuniteti |
|-- Përkufizimi -- |
|Një lidhje komplekse midis qenieve njerëzore që veprojnë si një tërësi ose si një njësi. |
|--Varësia-- |
|Sociale |
|-- Emri -- |
|Politike |
|-- Përkufizimi -- |
|Çdo objekt i rëndësishëm për politikën. |
|--Varësia-- |
|Sociale |
|-- Emri -- |
|Shërbim social |
|-- Përkufizimi -- |
|Çdo shërbim që u ofrohet njerëzve. |
|-- Varësia -- |
|Sociale |
|-- Emri -- |
|Ekonomike |
|-- Përkufizimi -- |
|Çdo objekt që lidhet me pronën, ekonominë dhe çështjet monetare. |
|-- Emri -- |
|Prona |
|-- Përkufizimi -- |
|Çdo objekt që lidhet me pronësinë/zotërimin, si një shtëpi. |
|--Varësia-- |
|Ekonomike |
|-- Emri -- |
|Infrastruktura |
|-- Përkufizimi -- |
|Çdo objekt që konsiderohet si një strukturë që ofron një shërbim, si një rrugë, një urë, një strukturë ushtarake, etj. |
|--Varësia-- |
|Ekonomik |
|-- Emri - |
|Aktiviteti ekonomik |
|-- Përkufizimi -- |
|Çdo objekt që paraqet një aktivitet ekonomik, si një industri. |
|--Varësia-- |
|Ekonomike |
|-- Emri -- |
|Përdorimi i tokës rurale |
|-- Përkufizimi -- |
|Çdo objekt jo-urban, që është i dedikuar për një përdorim të caktuar. |
|--Varësia-- |
|Ekonomike |
|-- Emri -- |
|Mjedisore |
|-- Përkufizimi -- |
|Çdo sipërfaqe/zonë që i nënshtrohet një niveli të caktuar mbrojtjeje, si parku natyror. |
|-- Emri -- |
|Trup ujor |
|-- Përkufizimi -- |
|Çdo akumulim i konsiderueshëm i ujit. |
|--Varësia-- |
|Mjedisore |
|-- Emri -- |
|Zonë e mbrojtur |
|-- Përkufizimi -- |
|Një zonë që është e mbrojtur sipas legjislacionit në fuqi. |
|--Varësia-- |
|Mjedisore |
|-- Emri -- |
|Burim ndotjeje |
|-- Përkufizimi -- |
|Një objekt që përmban ndotës |
|--Varësia-- |
|Mjedisore |
|-- Emri -- |
|Trashëgimi |
|-- Përkufizimi -- |
|Çdo gjë që lidhet me objektet përkatëse nga këndvështrimi i trashëgimisë kulturore. |
|-- Emri -- |
|Vlera kulturore |
|-- Përkufizimi -- |
|Çdo objekt që konsiderohet i rëndësishëm nga perspektiva kulturore, si stadiumi, teatri, muzeu, etj. |
|--Varësia-- |
|Trashëgimi |
|-- Emri -- |
|Vlera historike |
|-- Përkufizimi -- |
|Çdo objekt që konsiderohet historik. |
|--Varësia-- |
|Trashëgimi |
|-- Emri -- |
|Vend i trashëgimisë botërore. |
|-- Përkufizimi -- |
|Një vend (si pylli, mali, liqeni, shkretëtira, ndërtesa, kompleksi ose qyteti) që renditet nga UNESCO si një vend me rëndësi të veçantë |
|kulturore ose fizike. |
|--Varësia-- |
|Trashëgimi |
4.2.2 VLERAT E KATEGORIVE TË RREZIQEVE NATYRORE
-- Emri --
Vlerat e kategorive të rreziqeve natyrore.
-- Përkufizimi --
Një klasifikim i përgjithshëm i llojeve të rreziqeve natyrore.
-- Identifikuesi -
http://inspire.ec.europa.eu/codelist/RiskOrCategoryValue
-- Vlerat --
Vlerat e lejuara për këtë kodlistë përfshijnë vlerat e specifikuara në tabelën më poshtë
|Kodlistë |
| -- Emri -- |
|Gjeologjike/hidrologjike |
|-- Përkufizimi -- |
|Proceset që kanë një natyrë gjeologjike (gjeosferë) ose hidrologjike (hidrosferë) |
|-- Përshkrimi -- |
|Disa nga proceset e përfshira këtu janë trajtuar si gjeologjike në literaturën shkencore, siç janë rreziku vullkanik ose rrezik nga |
|tërmeti, ndërsa proceset e tjera nuk mund të kuptohen pa input gjeologjik dhe hidrologjik, siç janë llojet e caktuara të rrëshqitjeve të|
|dheut (që mund të nxiten dhe mobilizohen nga ujërat), ose përmbytjet (shumë të varura nga karakteristikat e infiltrimit të tokës, |
|topografia, luhatjet e prurjeve të ujit) etj. |
|-- Emri -- |
|Tsunami |
|-- Përkufizimi -- |
|Ndërprerja e valës së gjatë në një trup të madh ujor që arrin tokën e dalë. |
|-- Përshkrimi -- |
|Tsunami mund të shkaktohet nga tërmetet, rrëshqitja e dheut, shpërthimet vullkanike, meteorët, etj. Megjithëse është një lloj |
|përmbytjeje, zakonisht konsiderohet si një proces i ndarë |
|--Varësia-- |
|Gjeologjike/jidrologjike |
|-- Emri -- |
|Vullkanike |
|-- Përkufizimi -- |
|Një hapje, ose këputje, në koren e tokës që lejon magmën e nxehtë, hirin dhe gazrat të ngjiten lart |
|-- Përshkrimi -- |
|Proceset e lidhura drejtpërdrejtë me shpërthimet vullkanike përshihen në këtë kategori, si llava, rënia e hirit, shpërthimet vullkanike,|
|shpërthimet freatike, etj. |
|--Varësia-- |
|Gjeologjike/hidrologjike |
|-- Emri -- |
|Tërmete |
|-- Përkufizimi -- |
|(Rreziku) i tërmetit përfshin përhapjen e valëve elastike në ose afër sipërfaqes, pas realizimit të thyerjes tektonike ose burimeve të |
|tjera natyrore, siç janë shpërthimet vullkanike ose ndikimet e meteorit. |
|-- Përshkrimi -- |
|Në këtë kategori duhet të përfshihet edhe lëngëzimi, dridhja e tokës dhe efektet e tjera të shkaktuara direkt nga valët sizmike. |
|Proceset që mund të shkaktohen nga procese të tjera mund të përshtaten më mirë në klasa të tjera. |
|--Varësia-- |
|Gjeologjike/Hidrologjike |
|-- Emri -- |
|Fundosjet dhe kolapsi |
|-- Përkufizimi -- |
|Fundosjet dhe kolapsi përfshijnë kryesisht lëvizjen vertikale të sipërfaqes së tokës poshtë në tokë, për shkak të proceseve të ndryshme |
|të gërryerjes së shkëmbinjve ose tokës ose shkrirjes së shkëmbinjve deri në një pikë ku struktura e shkëmbinjve nuk mund të mbajë |
|ngarkesën e vet (kolaps) ose duke shkaktuar lëvizje relativisht të ngadalta poshtë. |
|-- Përshkrimi -- |
|Fundosjet dhe kolapsi mund të shoqërohen me shkëmbinj karbonatikë në zonat karstike, por mund të ndodhin edhe në rajone të tjera si toka|
|loese ose toka të ngjeshura. |
|--Varësia-- |
|Gjeologjike/Hidrologjike |
|-- Emri -- |
|Rrëshqitje |
|-- Përkufizimi -- |
|Proceset e lëvizjeve të pjerrësisë së dheut, të shkëmbinjve dhe të materialeve organike të lidhura me lloje të ndryshme të |
|ligështimit/dobësimit të tokës. |
|-- Përshkrimi -- |
|Disa terma të zakonshëm të përdorur për të përshkruar lloje të ndryshme të rrëshqitjeve të dheut, por nuk kufizohen vetëm në rrëshqitje,|
|rënie të shkëmbinjve, rrjedhje të mbeturinave. |
|--Varësia -- |
|Gjeologjike/hidrologjike |
|-- Emri -- |
|Ortek bore |
|-- Përkufizimi -- |
|Një masë dëbore me një vëllim tipik më të madh se 100 m3 dhe një minimum prej 50 metrash që rrëshqet me shpejtësi drejt tatëpjetës. |
|-- Përshkrimi -- |
|Ortekët e dëborës zakonisht përmbajnë materiale të mbledhura përgjatë rrugës, siç janë pemët, shkëmbinjtë etj. Formimi i ortekëve është |
|rezultat i një ndërveprimi kompleks midis terrenit, masës së dëborës dhe kushteve meteorologjike. |
|--Varësia-- |
|Gjeologjike/hidrologjike |
|-- Emri -- |
|Përmbytje |
|-- Përkufizimi -- |
|Proceset e përmbytjes së tokës zakonisht të thatë (të dalë), ose mbulimi i përkohshëm me ujë i tokës që zakonisht nuk mbulohet nga uji. |
|-- Përshkrimi -- |
|Përmbytjet mund të jenë shumë llojesh (përmbytje të papritura/shpejta, përmbytje të lumenjve, përmbytje të baticës) dhe mund të kenë |
|shumë shkaktarë (reshje, dëmtimi i digave të rezervuarit natyral të ujit, pengimi i kanalit të lumenjve, etj.). Tsunami dhe rritja e |
|stuhive zakonisht konsiderohen si një rrezik tjetër natyror. |
|--Varësia-- |
|Gjeologjike/Hidrologjike |
|-- Emri -- |
|Toksike ose radioaktive |
|-- Përkufizimi -- |
|Proceset që lidhen me natyrën e substancave që mund të përbëjnë një kërcënim për shëndetin e njeriut. |
|-- Përshkrimi -- |
|Azbesti, radioaktiviteti natyror ose emetimi i gazit janë disa shembuj të rreziqeve brenda kësaj kategorie. |
|--Varësia-- |
|Gjeologjike/hidrologjike |
| |
|-- Emri -- |
|Meteorologjike/klimatologjike |
|-- Përkufizimi -- |
|Proceset që kanë një natyrë (ose origjinë) meteorologjike (atmosferike) ose klimatike (ndryshime afatgjata të ndryshoreve mjedisore). |
|-- Emri -- |
|Thatësira |
|-- Përkufizimi -- |
|Dukuri e qëndrueshme dhe e gjerë e disponueshmërisë së ujit nën mesataren, të shkaktuar nga ndryshueshmëria e klimës. |
|-- Përshkrimi -- |
|Thatësira nuk duhet të ngatërrohet me “klimën e thatë”, e cila është një tipar mesatar afatgjatë i një klime të thatë. Po ashtu, |
|thatësira nuk duhet të ngatërrohet me mungesën e ujit, që pasqyron kushtet e mosbalancimeve afatgjata midis disponueshmërisë dhe |
|kërkesave të ujit. Thatësira mund të ndikojë në zonat e larta dhe të ulëta të reshjeve të Evropës dhe mund të zhvillohet gjatë |
|periudhave të shkurtra të javëve dhe muajve ose periudha shumë më të gjata të disa stinëve, viteve dhe madje dekadave. |
|--Varësia-- |
|Meteorologjike /Klimatologjike |
|-- Emri -- |
|Temperatura ekstreme |
|-- Përkufizimi -- |
|Një rritje ose rënie jonormale e temperaturës që zgjat më shumë se rritja ose rënia e zakonshme e saj. |
|-- Përshkrimi -- |
|Valët e nxehtësisë ose valët e të ftohtit. |
|--Varësia-- |
|Meteorologjike /klimatologjike |
| |
|-- Emri -- |
|Tornadot dhe uraganët |
|-- Përkufizimi -- |
|Erërat e forta (shpejtësi dhe intensitet i lartë). |
|--Varësia-- |
|Meteorologjike/klimatologjike |
| |
|-- Emri -- |
|Vetëtima |
|-- Përkufizimi -- |
|Shkarkimi i energjisë elektrike atmosferike. |
|--Varësia-- |
|Meteorologjike/klimatologjike |
| |
|-- Emri -- |
|Stuhi detare |
|-- Përkufizimi -- |
|Uji i shtyrë nga deti në tokë, për shkak të një uragani ose një ndryshimi të shpejtë në presionin atmosferik |
|-- Përshkrimi - |
|Edhe pse stuhia është një lloj përmbytjeje, zakonisht konsiderohet si një klasë e ndarë. |
|--Varësia-- |
|Meteorologjike/klimatologjike |
| |
|-- Emri -- |
|Zjarre |
|-- Përkufizimi -- |
|Kjo kategori përfshin të gjitha llojet e proceseve që përfshijnë ngjarjen dhe përhapjen e zjarrit. |
|-- Emri -- |
|Zjarr rënie në pyje dhe zona të tjera natyrore. |
|-- Përkufizimi -- |
|Zbulimi dhe përhapja e zjarrit në tokat e mbjella. |
|-- Përshkrimi -- |
|Zjarri i pyllit nënkupton zjarrin, i cili shpërthen dhe përhapet me shpejtësi në pyje dhe në toka të tjera apo që shpërthen në toka të |
|tjera dhe përhapet në toka të pyllëzuara. Përkufizimi i zjarrit në pyll përjashton djegien e parashikuar ose të kontrolluar, zakonisht |
|me qëllim reduktimin ose eliminimin e sasisë së lëndës së grumbulluar në terren (Rregullorja EC 2152/2003 - Forest Focus). |
|--Varësia-- |
|Zjarre |
|-- Emri -- |
|Zjarre nëntokësore |
|-- Përkufizimi -- |
|Zjarri që përhapet nën sipërfaqe, zakonisht ndodh në tokë të pasur me torfë. |
|--Varësia-- |
|Zjarre |
|-- Emri -- |
|Biologjike |
|-- Përkufizimi -- |
|Proceset që lidhen drejtpërdrejt me organizmat e gjallë ose produktet e prodhuara nga organizmat e gjallë. |
|-- Emri -- |
|Infeksione |
|-- Përkufizimi -- |
|Rritja jonormale e popullatës së organizmave të gjalla. |
|--Varësia-- |
|Biologjike |
|-- Emri -- |
|Epidemi |
|-- Përkufizimi -- |
|Një shpërthim i një sëmundjeje, që përhapet shpejt midis individëve në një zonë ose popullsi. |
|--Varësia-- |
|Biologjike |
|-- Emri -- |
|Alergjike |
|-- Përkufizimi -- |
|Produkte biologjike ose substanca, (të tilla si poleni) që mund të shkaktojnë alergji mbi një numër të madh njerëzish. |
|--Varësia-- |
|Biologjike |
|-- Emri -- |
|Kozmike |
|-- Përkufizimi -- |
|Proceset nga hapësira planetare. |
|-- Emri -- |
|Impakte meteorite. |
|-- Përkufizimi -- |
|Materiale të ngurta, që vijnë në tokë nga hapësira planetare. |
|--Varësia-- |
|Kozmike |
|-- Emri -- |
|Çrregullimet magnetike |
|-- Përkufizimi -- |
|Çrregullimet e fushës magnetike të Tokës. |
|--Varësia-- |
|Kozmike |
|-- Emri -- |
|Rrezatime diellore dhe kozmike |
|-- Përkufizimi -- |
|Rrezatimi nga hapësira planetare (rrezet UV, gama, etj). |
|--Varësia-- |
|Kozmike |
| |
|Tabela më poshtë përfshin vlera shtesë të rekomanduara, që mund të përdoren nga ofruesit e të dhënave |
|-- Emri -- |
|Gjeologjike/hidrologjike të tjera |
|-- Përkufizimi -- |
|Çdo proces që nuk është adresuar tashmë brenda kategorive të tjera gjeologjike ose hidrologjike. |
|-- Përshkrimi -- |
|Këtu midis proceseve të tjera, mund të përfshihen lëvizjet e dunave të rërës, erozionit të tokës, lëvizjet e ajsbergëve etj. |
|-- Emri -- |
|Meteorologjike/klimatologjike të tjera |
|-- Përkufizimi -- |
|Çdo proces që nuk është adresuar ende brenda kategorive të tjera meteorologjike / klimatologjike |
|-- Përshkrimi -- |
|Në këtë kategori mund të përfshihet dizertifikimi natyror. |
|-- Emri -- |
|Zjarre të tjera |
|-- Përkufizimi -- |
|Zjarre të tjera natyrore që nuk janë adresuar brenda kategorive të tjera të zjarrit. |
|-- Përshkrimi -- |
|Në këtë kategori mund të përfshihet dizertifikimi natyror me anë të zjarrit. |
|-- Emri -- |
|Biologjike të tjera |
|-- Përkufizimi -- |
|Rreziqe të tjera biologjike që nuk janë adresuar brenda kategorive të tjera biologjike. |
|-- Përshkrimi -- |
|Këtu mund të përfshihen prionet dhe substanca të tjera toksike të prodhuara nga (ose brenda) organizmave të gjallë. |
|-- Emri -- |
|Kozmike të tjera |
|-- Përkufizimi -- |
|Rreziqe të tjera kozmike që nuk janë adresuar tashmë brenda kategorive të tjera kozmike. |
4.2.3 KODLISTA PËR ARSYET E PAVLEFSHMËRISË - VOIDALBE
Arsyeja e përdorimit të vlerës void duhet të paraqitet kurdo që të jetë e mundur duke përdorur një nga vlerat e listuara në kodlistën VleraEArsyesSëPavlefshmërisë (VoidReasonValue), e cila përmban:
|Kodlistë |
| -- Emri -- |
|E pa njohur (Unknown) |
| |
|-- Përkufizimi -- |
|Vlera korrekte për këtë element gjeohapësinor nuk njihet ose është e pamatshme nga krijuesi i të dhënave. |
|-- Përshkrimi-- |
|Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” të një liqeni nuk është matur, atëherë arsyeja e pavlefshmërisë |
|së kësaj karakteristike mund të jetë “e pa njohur”. |
| |
|-- Emri -- |
|E pa populluar (Unpopulated) |
|-- Përkufizimi -- |
|Kjo karakteristikë nuk është pjesë e databazës së mirëmbajtur nga krijuesi i të dhënave. Pavarësisht kësaj kjo e dhënë mund të |
|ekzistojë. |
|--Përshkrimi-- |
|Shembull: Kur “kuota e sipërfaqes së një trupi ujor nga niveli i detit” nuk është e përfshirë në grupin e të dhënave që përmban objektin|
|gjeohapësinor të liqenit, atëherë vlera e kësaj karakteristike mund të jetë “E pa populluar”. |
| |
|-- Emri -- |
|Konfidenciale (Withheld). |
|-- Përkufizimi -- |
|Kjo karakteristikë mund të ekzistojë por është konfidenciale. |
[pic]
-----------------------
[1]NSDI - Infrastruktura Kombëtare e Informacionit Gjeohapësinor.
