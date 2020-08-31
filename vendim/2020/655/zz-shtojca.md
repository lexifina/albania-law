# Shtojca
ANEKS 1
FORMA, PËRMBAJTJA DHE ELEMENTËT E SIGURISË SË VIZËS ELEKTRONIKE
Forma dhe përmbajtja e vizës elektronike është si më poshtë vijon:
I. Viza elektronike do të jetë e printueshme në printer bardhë e zi, dokument format A4, PDF
II. Modeli i vizës elektronike
- Viza elektronike do të përmbajë:
- Bandën e titullit, ku në krye në qendër vendoset Stema e Republikës së Shqipërisë, në rreshtin e dytë shkruhet teksti “ELECTRONIC VISA”/ “REPUBLIC OF ALBANIA”/ “AL0000000e”, ku vendoset nr. identifikues i vizës në sistem.
- Numri identifikues i vizës në sistem do te jetë me 8 karaktere dhe në fillim germat AL.
- Fushën ku është përcaktuar vendosja e fotos (G1).
- Fushën ku printohen të dhënat e që ruhen në MRZ (G2).
- Fushën ku do të printohet “Kodi i lexueshëm me makinë” (MRZ).
III. Tekstet dhe simbolet
Tekstet dhe simbolet që do të ketë të kompozuara viza elektronike, sipas modelimit të saj do të jenë:
- Stema e Republikës.
- Republika e Shqipërisë/Republic of Albania.
- AL.
- Harta e Shqipërisë.
IV. Teksti në vizën elektronike
1. Grupi i të dhënave G2, që përmban informacion mbi vizën, autoritetin lëshues, shtetasin e huaj posedues të vizës.
2. Dokumenti do të gjenerohet në format A4, PDF do të përmbajë dhe Kodin QR.
3. Kodi QR do të përdoret për të ruajtur të dhënat në format binar. Ky kod duhet të dëshifrohet nga lexuesi i pasaportave në PKK, nga telefoni celular etj.
4. Për konfigurimin e kodit QR, duhet të krijohet LDS (Logical Data Structure) duke përdorur MRZ (Zonën e lexueshme nga makina) të Vizës në DG1 (Grupi i të dhënave në vizë) dhe foton në DG2 (Fotografia në vizë).
5. LDS nënshkruhet dhe krijohet SOD (Document Sicurity Object).
6. Më tej SOD dhe LDS duhet të ruhen në Kodin QR, i cili do të printohet në vizën elektronike në format PDF dhe nëse skanohet, qoftë dhe nga telefoni, pasqyron të gjitha të dhënat e vizës.
7. Kodi QR, i cili do të printohet në vizën elektronike në format PDF, të përfshijë edhe të dhënat e pasaportës së aplikantit.
8. Dokumenti administrativ elektronik, përmban të dhënat e vulës elektronike të konvertuara vizualisht sipas formatit të mëposhtëm:
Paraqitja grafike e vulës institucionit (nëse është e aplikueshme)
/
Emri i institucionit lëshues
Data dhe ora e vulosjes-sipas vulës kohore- timestamp
Vlerën në hexadecimal/enkodim në string alfanumerik të hash të dokumentit apo vulës elektronike, të shfaqur në format të lexueshëm text apo në kod 1- apo dydimensional.
Shënim:
Ky dokument është gjeneruar dhe vulosur me anë të një procedure automatike nga një sistem elektronik (emri i institucionit përkatës).
9. Forma e vulës elektronike është drejtkëndore dhe përmasat e saj nuk duhet të kalojnë 40% të gjerësisë së dokumentit apo 30% të lartësisë së tij (shembull: për formatin A4-84mm horizontalisht dhe 89mm vertikalisht);
10. Vula elektronike vendoset në pjesën e fundit, të faqes së fundit të dokumentit.
11. Për qëllime të vërtetimit të vlefshmërisë së dokumentit me vulë elektronike të printuar në letër mjafton skanimi i QR code që gjeneron adresën elektronike në të cilën dokumenti administrativ elektronik aksesohet përgjatë kohëzgjatjes së ciklit jetësor të tij, URL sipas specifikimeve të RFC 3986.”
