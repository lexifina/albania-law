3. APLIKACIONI ALTERNATIV
Aplikacioni alternativ për përpunimin e të dhënave të udhëtimit është një mjet rezervë (fallback system) i vënë në dispozicion nga SIU-ja, i destinuar të përdoret vetëm në rastet kur sistemi kryesor elektronik i transmetimit dhe përpunimit të të dhënave të udhëtimit nuk është operacional për shkak të një defekti, avarie teknike, mungese lidhjeje ose situate tjetër të papritur teknologjike.
Aplikacioni alternativ garanton vazhdimësinë e përpunimit të të dhënave dhe parandalon vonesat në analizën e rrezikut, duke siguruar që funksionet e sigurisë kombëtare dhe kontrollit kufitar të mos ndërpriten.
3.1 Qëllimi i aplikacionit alternativ
Aplikacioni alternativ, synon:
a) të mundësojë transmetimin e pandërprerë të të dhënave të udhëtimit dhe të dhënave të tjera të udhëtimit drejt SIU-së;
b) të sigurojë redundancë operative në rast dështimi të sistemit primar;
c) të garantojë që SIU-ja të ketë akses në kohë reale në të dhënat kritike për analizën e rrezikut;
d) të mbajë standardet e privatësisë dhe mbrojtjes së të dhënave në nivel të barabartë me sistemin kryesor.
3.2 Aktivizimi i aplikacionit alternativ
Aplikacioni alternativ përdoret vetëm në rastet, kur:
a) transportuesi nuk mund të transmetojë të dhëna në sistemin kryesor për shkak të defekteve teknike;
b) sistemi kryesor i SIU-së ka ndërprerje, ngadalësim serioz ose avari;
c) infrastruktura e komunikimit është e pamundur ose e pasigurt;
d) ka mangësi të përkohshme të serverëve të Policisë së Shtetit.
SIU-ja njofton transportuesit kur sistemi primar ka kaluar në gjendjen “jo operacionale”.
3.3 Procedurat e transmetimit në aplikacionin alternativ
Transportuesit janë të detyruar që:
a) të transmetojnë ndërmjet mjeteve rezervë të autorizuara nga SIU-ja (aplikacion web, API alternative, format të siguruar fallback);
b) të dërgojnë të dhënat në të njëjtin nivel cilësie dhe saktësie si në sistemin kryesor;
c) të përditësojnë të dhënat e udhëtimit sipas afateve ligjore edhe gjatë funksionimit të aplikacionit alternativ (48-24 orë, 180 minuta, 60 minuta, pas imbarkimit).
3.4 Administrimi i të dhënave në aplikacionin alternativ nga SIU-ja
SIU-ja kryen këto veprime:
a) regjistrimin e çdo transmetimi të kryer në aplikacionin alternativ;
b) verifikimin e saktësisë së të dhënave të dërguara;
c) krahasimin e tyre me strukturat e të dhënave të sistemit kryesor;
d) monitorimin e performancës teknike të aplikacionit rezervë;
e) garantimin e aksesit të kufizuar dhe të gjurmueshëm nga personeli i SIU-së.
f) verifikon automatikisht çdo të dhënë të marrë për integritet, plotësi dhe përputhshmëri.
3.5 Transferimi i të dhënave në sistemin kryesor
Sapo sistemi kryesor rikthehet në funksion:
a) të dhënat e regjistruara në aplikacionin alternativ transferohen automatikisht në sistemin primar;
b) SIU-ja verifikon përputhshmërinë dhe integritetin e të dhënave;
c) dokumentohet çdo hap i procesit të transferimit.
Ky proces garantohet nga strukturat e teknologjisë së informacionit të Drejtorisë së Përgjithshme të Policisë së Shtetit.
3.6 Fshirja e të dhënave nga aplikacioni alternativ
Pasi të dhënat janë transferuar me sukses:
a) ato fshihen menjëherë nga aplikacioni alternativ;
b) fshirja regjistrohet dhe dokumentohet në log-et e auditimit;
c) SIU-ja siguron që asnjë kopje e të dhënave të mos mbetet në sistemin rezervë.
Kjo procedurë është e detyrueshme për të përmbushur parimin e minimizimit, kufizimit të ruajtjes dhe integritetit, sipas GDPR-së dhe ligjit nr. 124/2024.
3.7 Masat e sigurisë në aplikacionin alternativ
Aplikacioni alternativ është i ndërtuar mbi të njëjtat standarde sigurie si sistemi kryesor:
a) enkriptim në transmetim dhe ruajtje (TLS 1.2+/AES-256);
b) kontroll aksesesh me autentikim shumëfaktorësh;
c) logim të detajuar të çdo veprimi;
d) auditim periodik të funksionalitetit dhe sigurisë;
e) izolim të mjedisit rezervë nga sistemet e tjera të PSH-së (network segmentation).
