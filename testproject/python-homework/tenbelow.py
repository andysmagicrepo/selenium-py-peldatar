osszeg = 0
darab = 0
szam = 0
print("10 alatti számok összeadása, ha a bevitt szám nagyobb, mint 10 akkor kilép! ")
while True:
    szam = int(input("Kérek egy 10 alatti számot vagy befejezem és kiírom az eddigiek összegét?"))
    if szam < 10:
        osszeg += szam
        darab += 1
    else:
        break
print("A bevitt 10 alatti számok összege:",osszeg,"," "Darabszáma:",darab)