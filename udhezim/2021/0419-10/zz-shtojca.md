# Shtojca
Anila Denaj
Aneksi I
Marrja e informacionit nga institucionet financiare
Për të realizuar marrjen e informacionit nga institucionet financiare është realizuar zhvillimi i një web servis-i SOAP, i cili mund të konsumohet nëpërmjet platformës ekzistuese të Ndërveprimit Qeveritar (Government Gateway).
Backend-et e institucioneve në fjalë mund të komunikojnë me Government Gateway duke postuar të dhënat nëpërmjet protokollit GovTalk.
Informacioni i sjellë nga institucionet financiare në Government Gateway ruhet në bazën e të dhënave dhe përgatitet për t’u shkëmbyer me autoritetet përkatëse.
Web servis-i implementon dy protokollet e komunikimit:
- Standardi RLLB;
- GovTalk.
Standardi WebService
Web servis-i është ngritur mbi skemat XSD të standardit RLLB, kjo do të thotë që të dhënat e dërguara nga institucionet financiare, në format xml, duhet të jenë të formatuara sipas standardit RLLB.
Implementimi i web servis-it me skemat xsd, të standardit RLLB, siguron marrjen e informacionit në formatin e duhur dhe eliminon mundësinë e dërgimit të të dhënave në formate të papërshtatshme.
Protokolli i komunikimit
Protokolli i komunikimit GovTalk ka formatin dhe strukturën si në figurën 3.
Është pikërisht DIS-i, mekanizmi që interpreton këtë format mesazhi, merr prej tij vetëm elementin <body> dhe e dërgon më tej në sistemin fundor, nëpërmjet “web service” që ky sistem fundor ekspozon.
[pic]
Fig. 3: Protokolli GovTalk
3.4.1 Raportimi nga institucioni financiar
Raportimi nga institucionet financiare kalon në tri hapa:
1. Kontrolli i skedarit të raportuar.
Mesazhi i ardhur nga institucionet financiare kalon në një seri verifikimesh:
- Formati i skedarit kontrollohet të jetë xml;
- Formati i mesazhit të dërguar kontrollohet sipas skemës xsd të standardit RLLB;
- Validohen referencat (MessageRefId dhe DocRefId). Këto duhet t’i përmbahen rregullave të përshkruara në dokumente dhe të jenë unike. DocRefId për ReportingFi mund të jetë përsëritëse (jounike) nëse DocSpecType është RLLB2. Pra kemi ritransmetim të informacionit;
- Validohen fushat TransmittingCountry dhe ReceivingCountry (duhet të jenë AL);
- Validohet ResidenceCountry për ReportingFi (duhet të jetë AL);
- Validohet MessageType;
- Validohet prezenca e një grupi raportimi (ReportingGroup). Në rast se lloji i mesazhit është RLLB701 duhet të ketë të paktën një raportim (AccountReport). Nëse mesazhi është RLLB703 (mungesë të dhënash) mesazhi nuk duhet të ketë asnjë raportim për ReportingGroup;
- Validohen kombinimet e ndryshme midis MessageTypeIndic dhe DoctypeIndic;
- Nëse MessageTypeIndic = RLLB701, asnjë nga elementet nuk duhet të ketë DocTypeIndic = RLLB2 apo RLLB3;
- Nëse MessageTypeIndic = RLLB702, asnjë nga elementet nuk duhet të ketë DocTypeIndic = RLLB 1;
- Nëse MessageTypeIndic = RLLB703, nuk duhet të kemi elementin ReportingGroup;
- Validim i deklarimit të ControllingPerson.
Nëse informacioni i dërguar nuk kalon kontrollet ai hidhet poshtë dhe sistemi dërgon si përgjigje mesazhin e gabimit për institucionin financiar.
2. Depozitimi i informacionit në bazën e të dhënave
Informacioni i mesazheve, të cilat kalojnë kontrollet e validimit, do të hidhet në bazën e të dhënave në tabelat përkatëse.
3. Shfaqja e mesazheve të dërguara në panel për përdoruesit e administratës tatimore
Punonjësit e autorizuar të administratës tatimore mund të shohin informacionin e dërguar nga institucionet financiare
[pic]
Fig. 4: Raportimi nga institucionet financiare
