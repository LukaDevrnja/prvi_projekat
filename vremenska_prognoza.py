temperatura = int(input("unesite temperaturau:"))
test_temperatura= -1
temperatura=test_temperatura
poruka=""
if temperatura < 0: 
    poruka = "oprez klizavo"

if temperatura > 0 :
    poruka = "temperatura iznad 0"
    if temperatura > 30:
        poruka ="ukljucite kilima uredjaje" 




ocekivana_poruka = "oprez klizavo"
if poruka== ocekivana_poruka :  

    print("case - ispod nule- test prosao")
