4. Kontrolleri fiskal.
Sistemi fiskal, që do të zbatohet në pikat e tregtimit me pakicë, është sipas skemës:
- KDE dhe pajisje fiskale e instaluar në çdo dispenser të lidhur me kontrollerin fiskal;
- Sistemi për monitorimin dhe kontrollin e rezervuarëve të instaluar në çdo rezervuar të lidhur me kontrollerin fiskal;
- Kontrolleri fiskal, i lidhur në kohë reale me platformën e sistemeve fiskale në serverin qendror të DPT-së.
a) KDE-ja është pajisja që kontrollon e komandon qarkun elektronik të dispenserit dhe përpunon e transferon të dhënat e shitjes në pajisjen fiskale. Të gjithë dispenserat punojnë vetëm në regjimin automatik. Konstrukti i KDE-së është i ndërtuar sipas të njëjtave standarde si pajisja fiskale, me një pikë hapjeje, në të cilën do të vendoset vula fiskale, duke përfshirë edhe pikat e lidhjes të KDE-së.
KDE-ja ka një program logjik (firmware) fiskal me këto karakteristika:
- Në rast se dispenseri kalon në regjimin manual, KDE-ja memorizon kohën e kalimit në regjimin manual dhe të gjithë shumatorët e dispenserit dhe ajo, bashkë me pajisjen fiskale, kalojnë në regjimin e bllokimit. Këto informacione transmetohen menjëherë nga kontrolleri fiskal në serverin qendror të DPT-së. Rivendosja në punë e sistemit fiskal kryhet me procedurë të veçantë, duke përdorur një kod kontrolli të veçantë, i lëshuar nga platforma e sistemeve fiskale në serverin qendror, sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve. Në momentin e rivendosjes në punë, KDE-ja rilexon të gjithë shumatorët e dispenserit në momentin e kalimit automatik dhe këto të dhëna kontrolleri fiskal i transmeton në serverin qendror.
Nuk lejohet përdorimi i çfarëdolloj programi kompjuterik nga shoqëri të paautorizuara në transmetimin e të dhënave nga dispenseri në pajisjen fiskale.
- Në portën e komunikimit të dispenserit lidhet vetëm KDE-ja.
Furnizimi me karburant kryhet vetëm pas autorizimit nga pajisja fiskale dhe KDE-ja, sipas parimit “pa kupon, s’ka karburant”.
KDE-ja lidhet në mënyrë aktive vetëm me pajisjen fiskale dhe bllokon dispenserin, në rast shkëputjeje me pajisjen.
Në rast se një dispenser është pa pajisje fiskale të instaluar, ai stacion tregtimi bllokohet dhe nuk lejohet të tregtojë derisa të instalohet pajisja fiskale apo të procedohet me çinstalimin fizik të tij.
Është e ndaluar lidhja e KDE-së me programe të tjera të paautorizuara, nga shoqëri të paautorizuara.
b) Kontrolleri fiskal është pajisja master, që kontrollon, komandon e përpunon të dhënat nga pajisjet fiskale dhe nga sistemet e monitorimit e të kontrollit të instaluara në rezervuare, sipas pikës 6.1.2 të këtij vendimi. Kontrolleri fiskal memorizon në bazën e të dhënave të tij dhe dërgon në kohë reale të dhënat në paltformën e sistemeve fiskale në serverin qendror, pranë DPT-së.
Konstrukti i kontrollerit fiskal është i ndërtuar sipas të njëjtave standarde si pajisja fiskale, me një pikë hapjeje, në të cilën do të vendoset vula fiskale, duke përfshirë edhe pikat e lidhjes.
Hapja e kontrollerit kryhet vetëm me autorizim nga serveri qendror i pajisjeve dhe sistemeve fiskale, nëpërmjet shkëmbimit të çelësave të sigurisë. Në rast hapjeje të paautorizuar, kontrolleri bllokohet dhe nuk lejon funksionimin e të gjitha pajisjeve fiskale në atë pikë tregtimi. Zhbllokimi kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Kontrolleri fiskal ka të integruar apo të lidhur një sistem GPS të pozicionimit global të pikës së tregtimit me pakicë.
Kontrolleri fiskal mund të ofrojë si opsion një ndërfaqe grafike për menaxhimin administrativ të pikës dhe mundësinë e krijimit të një rrjeti me zyrën qendrore të kompanisë së tregtimit me pakicë të hidrokarbureve. Kjo ndërfaqe është pjesë e sistemit fiskal.
Është i ndaluar përdorimi i çfarëdo programi menaxhimi që nuk është pjesë e sistemit fiskal apo është i pacertifikuar nga shoqëria e autorizuar.
Protokollet e komunikimit dhe forma logjike e funksionimit të këtij sistemi përcaktohen me udhëzim të ministrit të Financave dhe Ekonomisë.
6.1.2 Sistemi për monitorimin dhe kontrollin e hyrjeve dhe të daljeve në rezervuarët e pikave të tregtimit me pakicë
Ky sistem është një sistem fizik (hardware), i përbërë nga këto elemente:
1. Sondat;
2. Njësia qendrore e sondave (konsole).
Sonda është një mekanizëm që shërben për të matur nivelin dhe temperaturën në rezervuar.
Njësia qendrore e sondave (konsole), shërben për përpunimin dhe auditimin e të dhënave nga sondat.
Sistemi i monitorimit dhe i kontrollit të hyrjeve dhe të daljeve në rezervuarë kryen këto funksione:
- Mat vazhdimisht nivelin e karburantit brenda çdo rezervuari dhe e kthen atë në vëllimin përkatës të karburantit;
- Gjen rrjedhjet e karburantit;
- Njësia qendrore e sondave dërgon informacion në kontrollerin fiskal për rrjedhjet, gabimet njerëzore, dështimet HW apo programimet e rreme;
- Njësia qendrore e sondave memorizon të gjitha veprimet hyrëse në rezervuar, duke matur vëllimin përkatës të karburantit dhe të gjitha detajet e furnizimit i dërgohen kontrollerit fiskal.
Këto të dhëna, kontrollerit fiskal i memorizon në bazën e të dhënave të tij dhe i dërgon në kohë reale në platformën e sistemeve fiskale pranë DPT-së.
Kontrolleri fiskal monitoron dhe krahason sasitë në dalje të dispenserave, të regjistruara nga pajisjet fiskale, me sasitë përkatëse në dalje të rezervuarëve gjatë operimit të pikës së tregtimit me pakicë të karburantit, në kohë reale.
Në rast se sistemi i monitorimit dhe i kontrollit të hyrjeve dhe të daljeve të rezervuarve shkëputet nga kontrolleri fiskal, sistemi fiskal bllokohet dhe kontrolleri fiskal dërgon menjëherë mesazhin e alarmit në serverin qendror të pajisjeve dhe sistemeve fiskale në DPT. Zhbllokimi i tij kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Në çdo rezervuar të pikës së tregtimit me pakicë instalohet sistemi i monitorimit dhe i kontrollit të hyrjeve dhe të daljeve.
Në rast se në një rezervuar nuk janë instaluar sondat, ajo pikë e tregtimit me pakicë të hidrokarbureve bllokohet derisa të instalohet sonda ose të procedohet mbyllja e tij.
Çdo rezervuar, para instalimit të sondave, kryen procedurën e kalibrimit elektronik.
Sistemi i monitorimit dhe i kontrollit të hyrjeve dhe të daljeve në rezervuar miratohet nga komisioni i caktuar për verifikimin e sistemit fiskal, i parashikuar në nenin 13.1, të kreut I, “Dispozita të përgjithshme”. Këto pajisje i nënshtrohen kontrollit periodik fiskal dhe të kalibrimit nga shoqëritë e autorizuara.
Protokollet e komunikimit dhe forma logjike e funksionimit të sistemit të monitorimit përcaktohen me udhëzim të ministrit të Financave dhe Ekonomisë.
6.2 Sistemet fiskale për zonat e lira doganore, shoqëritë e prodhimit dhe shoqëritë e tregtimit me shumicë të hidrokarbureve
Çdo zonë e lirë doganore apo shoqëri që ka licencën e tregtimit me shumicë të hidrokarbureve është e detyruar të instalojë në pikën e tregtimit sistemet fiskale të përcaktuar në pikat 6.2.1 dhe 6.2.2, të këtij vendimi. Subjekte të monitorimit fiskal janë të gjitha depozitat fikse apo lëvizëse të fluidit, të gjitha puset e prodhimit dhe ekstremitetet e rrugëve të kalimit të fluidit. Sistemet fiskale të instaluara në zonat e lira doganore, të prodhimit apo të tregtimit me shumicë, do të përshtaten me sistemet fiskale të përcaktuara në këtë vendim dhe do të ricertifikohen nga shoqëritë e autorizuara nga komisioni i caktuar për verifikimin e sistemeve fiskale, i parashikuar në nenin 13.1, të kreut I, “Dispozita të përgjithshme”.
6.2.1 Sistemi fiskal për kalimatësit e shitjeve me shumicë të hidrokarbureve
Sistemi fiskal që zbatohet nga shoqëritë e hidrokarbureve/shitësve me shumicë, zonat e lira doganore dhe shoqëritë prodhuese të hidrokarbureve e të derivateve të tyre, i cili regjistron llojin, sasinë dhe vlerën, është një sistem fizik (hardware), i përbërë nga këto elemente:
1. Pajisja fiskale me KDE;
2. Kalimatësi me kokë elektronike;
3. Sistemi i monitorimit dhe i kontrollit të depozitave, sipas pikës 6.2.2 të këtij vendimi;
4. Kontrolleri fiskal.
Skema e lidhjes së sistemit fiskal, që zbatohet nga shoqëritë e hidrokarbureve/shitësve me shumicë, zonat e lira doganore dhe shoqëritë prodhuese të hidrokarbureve e të derivateve të tyre, është si më poshtë vijon:
- Koka elektronike e kalimatësit lidhet me KDE-në e pajisjes fiskale, e cila lidhet me kontrollerin fiskal;
- Sistemi i monitorimit dhe i kontrollit të depozitave lidhet me kontrollerin fiskal;
- Kontrolleri fiskal lidhet në kohë reale me platformën e menaxhimit të pajisjeve dhe sistemeve fiskale në DPT.
Kontrolleri fiskal menaxhon informacionin nga pajisja fiskale, e cila është e lidhur me kokën elektronike të kalimatësit nëpërmjet KDE-së.
Këto të dhëna, pasi memorizohen në bazën e të dhënave të kontrollerit, krahasohen me të dhënat e sistemit të monitorimit e të kontrollit të depozitave. Ky informacion dërgohet në kohë reale nga kontrolleri fiskal në platformën e menaxhimit të pajisjeve e sistemeve fiskale në DPT.
Në rast se informacionet e marra nuk përputhen me njëra-tjetrën, sistemi bllokohet dhe dërgon informacionin në kohë reale në serverin qendror, në DPT. Zhbllokimi i tij kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Konstrukti i kontrollerit fiskal është i ndërtuar sipas të njëjtave standarde, si pajisja fiskale, me një pikë hapjeje, në të cilën do të vendoset vula fiskale, duke përfshirë edhe pikat e lidhjes.
Hapja e kontrollerit kryhet vetëm me autorizim nga serveri qendror i pajisjeve dhe sistemeve fiskale, nëpërmjet shkëmbimit të çelësave të sigurisë. Në rast të hapjes së paautorizuar, kontrolleri bllokohet dhe nuk lejon funksionimin e të gjitha pajisjeve fiskale në atë pikë tregtimi. Zhbllokimi kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Kontrolleri fiskal ka të integruar apo të lidhur një sistem GPS të pozicionimit global të pikës së tregtimit me shumicë.
Të gjitha pajisjet matëse, pjesë e sistemit fiskal, pasi të marrin miratimin nga Drejtoria e Përgjithshme e Metrologjisë, duhet të miratohen edhe në komisionin e certifikimit pranë Ministrisë së Financave dhe Ekonomisë, i caktuar për verifikimin e sistemeve fiskale, sipas nenit 13.1, të kreut I, “Dispozita të përgjithshme”, si pjesë e sistemit fiskal.
Këto pajisje i nënshtrohen kontrollit periodik fiskal dhe të kalibrimit nga shoqëritë e autorizuara.
Është i ndaluar përdorimi i çfarëdo programi që nuk është pjesë e sistemit fiskal apo i certifikuar nga shoqëria e autorizuar.
Protokollet e komunikimit dhe forma logjike e funksionimit të këtij sistemi përcaktohen me udhëzim të ministrit të Financave dhe Ekonomisë.
6.2.2 Sistemi i monitorimit dhe i kontrollit të hyrjeve e të daljeve në depozitat e pikave të shumicës.
Sistemi i monitorimit dhe i kontrollit të hyrjeve e të daljeve në depozitat e pikave të tregtimit me shumicë është një sistem fizik (hardware), i përbërë nga këto elemente:
1. Sondat;
2. Njësia qendrore e sondave (konsole);
3. Kontrolleri fiskal.
Sonda është një mekanizëm që shërben për të matur nivelin dhe temperaturën në depozita.
Njësia qendrore e sondave (konsole) shërben për përpunimin dhe për auditimin e të dhënave nga sondat.
Sistemi i monitorimit dhe i kontrollit të depozitave duhet të kryejë këto funksione:
- Të masë vazhdimisht nivelin e karburantit brenda çdo depozite dhe ta kthejë atë në vëllimin përkatës të karburantit;
- Njësia qendrore e sondave duhet të dërgojë informacion në kontrollerin fiskal për rrjedhjet, gabimet njerëzore, dështimet HW apo programimet e rreme.
- Njësia qendrore e sondave memorizon të gjitha veprimet hyrëse në rezervuar, duke matur vëllimin përkatës të karburantit dhe të gjitha detajet e furnizimit i dërgohen kontrollerit fiskal.
Këto të dhëna kontrollerit fiskal i memorizon në bazën e të dhënave të tij dhe i dërgon në kohë reale në serverin qendror të pajisjeve dhe sistemeve fiskale pranë DPT-së.
Kontrolleri fiskal monitoron dhe krahason sasitë në dalje të kalimatësve, të regjistruara nga pajisjet fiskale, me sasitë përkatëse në dalje nga depozitat, gjatë operimit të pikës së tregtimit me shumicë në kohë reale.
Në rast se sistemi i monitorimit dhe i kontrollit të hyrjeve e të daljeve të depozitave shkëputet nga kontrolleri fiskal, sistemi fiskal bllokohet dhe dërgon menjëherë mesazhin e alarmit në serverin qendror të pajisjeve e sistemeve fiskale në DPT. Zhbllokimi i tij kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Në çdo depozitë të pikës së tregtimit me shumicë do të instalohen sistemi i monitorimit dhe i kontrollit të hyrjeve e të daljeve. Në rast se në një depozitë nuk është instaluar ky sistem sonde, ajo pikë e tregtimit me shumicë të hidrokarbureve bllokohet derisa në atë depozitë të instalohet sistemi i monitorimit dhe i kontrollit të hyrjeve e daljeve ose të procedohet me bllokimin fizik të tij.
Sistemi i monitorimit dhe i kontrollit të hyrjeve e daljeve në depozita, pasi të marrë miratimin nga Drejtoria e Përgjithshme e Metrologjisë, miratohet nga komisioni i caktuar për verifikimin e sistemit fiskal, i parashikuar në nenin 13.1, të kreut I, “Dispozita të përgjithshme”. Këto pajisje i nënshtrohen kontrollit periodik fiskal dhe të kalibrimit nga shoqëritë e autorizuara.
Protokollet e komunikimit dhe forma logjike e funksionimit të këtij sistemi do të përgatitet sipas udhëzimit të ministrit të Financave dhe Ekonomisë.
6.3 Sistemi fiskal për pikat e tregtimit me pakicë të bombolave të GLN-së në njësitë e lëndëve djegëse
Sistemi fiskal që do të zbatohet nga shoqëritë e tregtimit me pakicë të bombolave të GLN-së në njësitë e lëndëve djegëse, duke regjistruar llojin, sasinë në kg dhe vlerën, është një sistem fizik (hardware), i përbërë nga këto elemente:
1. Pajisja fiskale me KDE;
2. Sonda për monitorimin dhe kontrollin e GNL-së, e instaluar në depozita;
3. Kontrolleri fiskal.
Skema e lidhjes së sistemit fiskal, që do të zbatohet nga shoqëritë e tregtimit me pakicë të bombolave të GLN-së në njësitë e lëndëve djegëse, është si më poshtë vijon:
- KDE-ja e pajisjes fiskale instalohet në dispenserin GNL ose në kokën elektronike të kalimatësit, që lidhet me kontrollerin fiskal;
- Sondat për monitorimin dhe për kontrollin e depozitës lidhen me kontrollerin fiskal;
- Kontrolleri fiskal është i lidhur në kohë reale me platformën e menaxhimit të pajisjeve dhe sistemeve fiskale në DPT.
Në çdo linjë të furnizimit të bombolave në njësinë e lëndëve djegëse do të instalohet dispenser GNL ose kalimatës me kokë elektronike.
Dispenseri do të punojë vetëm në regjimin automatik.
Kontrolleri fiskal menaxhon informacionin nga pajisja fiskale, e cila është e lidhur me dispenserin e GNL-së ose kokën elektronike të kalimatësit, nëpërmjet KDE-së. Këto të dhëna, pasi memorizohen në bazën e të dhënave të kontrollerit, krahasohen me të dhënat e sondave të monitorimit e të kontrollit të depozitave.
Ky informacion dërgohet në kohë reale nga kontrolleri fiskal në platformën e menaxhimit të pajisjeve dhe sistemeve fiskale në DPT.
Në rast se informacionet e marra nuk përputhen me njëra-tjetrën, sistemi bllokohet dhe dërgon informacionin në kohë reale në serverin qendror në DPT. Zhbllokimi i tij kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve. Konstrukti i kontrollerit fiskal është i ndërtuar sipas të njëjtave standarde si pajisja fiskale, me një pikë hapjeje, në të cilën do të vendoset vula fiskale, duke përfshirë edhe pikat e lidhjes.
Hapja e kontrollerit kryhet vetëm me autorizim nga serveri qendror i pajisjeve dhe i sistemeve fiskale, nëpërmjet shkëmbimit të çelësave të sigurisë. Në rast hapjeje të paautorizuar, kontrolleri bllokohet dhe nuk lejon funksionimin e gjitha pajisjeve fiskale në atë pikë tregtimi. Zhbllokimi kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Kontrolleri fiskal ka të integruar apo të lidhur një sistem GPS të pozicionimit global të pikës së tregtimit me pakicë të bombolave të GLN-së në njësitë e lëndëve djegëse.
Të gjitha pajisjet matëse, pjesë e sistemit fiskal, pasi të marrin miratimin nga Drejtoria e Përgjithshme e Metrologjisë, duhet të miratohen edhe në komisionin e certifikimit pranë Ministrisë së Financave dhe Ekonomisë, i caktuar për verifikimin e sistemeve fiskale sipas parashikimeve në nenin 13.1, të kreut I, “Dispozita të përgjithshme”, si pjesë e sistemit fiskal. Këto pajisje i nënshtrohen kontrollit periodik fiskal dhe të kalibrimit nga shoqëritë e autorizuara.
Protokollet e komunikimit dhe forma logjike e funksionimit të këtij sistemi përcaktohen me udhëzim të ministrit të Financave dhe Ekonomisë.
6.4 Sistemi fiskal për pikat e furnizimit me shumicë dhe zonat e lira doganore të gazit të lëngshëm
Sistemi fiskal që do të zbatohet nga shoqëritë e furnizimit me shumicë të gazit të lëngshëm dhe zonat e lira doganore, duke regjistruar llojin, sasinë në kg dhe vlerën, është një sistem fizik (hardware), i përbërë nga këto elemente:
1. Pajisja fiskale me KDE;
2. Sonda për monitorimin dhe kontrollin e GNL-së, e instaluar në depozita;
3. Kontrolleri fiskal.
Skema e lidhjes së sistemit fiskal, që do të zbatohet nga shoqëritë e tregtimit me shumicë të gazit të lëngshëm, është si më poshtë vijon:
- KDE-ja e pajisjes fiskale, e instaluar në kokën elektronike të kalimatësit, lidhet me kontrollerin fiskal;
- Sondat për monitorimin dhe kontrollin e depozitës lidhen me kontrollerin fiskal;
- Kontroller fiskal, i lidhur në kohë reale me platformën e menaxhimit të pajisjeve dhe sistemeve fiskale në DPT.
Në çdo linjë të tregtimit me shumicë të gazit të lëngshëm do të instalohet kalimatës me kokë elektronike.
Kontrolleri fiskal menaxhon informacionin nga pajisja fiskale, e cila është e lidhur me kokën elektronike të kalimatësit nëpërmjet KDE-së. Këto të dhëna, pasi memorizohen në bazën e të dhënave të kontrollerit, krahasohen me të dhënat e sondat e monitorimit e të kontrollit të depozitave. Ky informacion dërgohet në kohë reale nga kontrolleri fiskal në platformën e menaxhimit të pajisjeve dhe sistemeve fiskale në DPT.
- Në rast se informacionet e marra nuk përputhen me njëra-tjetrën, sistemi bllokohet dhe dërgon informacionin në kohë reale në serverin qendror në DPT. Zhbllokimi i tij kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve. Konstrukti i kontrollerit fiskal është i ndërtuar sipas të njëjtave standarde si pajisja fiskale, me një pikë hapjeje, në të cilën do të vendoset vula fiskale, duke përfshirë edhe pikat e lidhjes.
- Hapja e kontrollerit kryhet vetëm me autorizim nga serveri qendror i pajisjeve dhe i sistemeve fiskale, nëpërmjet shkëmbimit të çelësave të sigurisë. Në rast hapjeje të paautorizuar, kontrolleri bllokohet dhe nuk lejon funksionimin e të gjitha pajisjeve fiskale në atë pikë tregtimi. Zhbllokimi kryhet sipas procedurës së përcaktuar nga Drejtoria e Përgjithshme e Tatimeve.
Të gjitha pajisjet matëse, pjesë e sistemit fiskal, pasi të marrin miratimin nga Drejtoria e Përgjithshme e Metrologjisë, duhet të miratohen edhe në komisionin e certifikimit pranë Ministrisë së Financave dhe Ekonomisë, i caktuar për verifikimin e sistemeve fiskale, sipas parashikimeve në nenin 13.1, të kreut I, “Dispozita të përgjithshme”, si pjesë e sistemit fiskal. Këto pajisje i nënshtrohen kontrollit periodik fiskal dhe të kalibrimit nga shoqëritë e autorizuara.
Protokollet e komunikimit dhe forma logjike e funksionimit të këtij sistemi përcaktohen me udhëzim të ministrit të Financave dhe Ekonomisë.
Kontrolleri fiskal ka të integruar apo të lidhur një sistem GPS të pozicionimit global të pikës së tregtimit me shumicë të gazit lëngshëm.”.
Ky vendim hyn në fuqi pas botimit në Fletoren Zyrtare.
