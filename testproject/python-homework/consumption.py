print("Hévízre utaztál üdülésre. Kérlek válaszolj, néhány ehhez kapcsolódó kérdésre.")
orszaguti_fogyasztas = int(input("Kérem az autód országúti fogyasztását (liter)?"))
varosi_fogyasztas = int(input("Kérem az autód városi fogyasztását (liter)?"))
orszaguton_megtett_út = int(input("Kérem az országúton megtett út hosszát (km)?"))
varosban_megtett_ut = int(input("Kérem a városban megtett út hosszát (km)?"))
költseg_1 = ((orszaguti_fogyasztas * (orszaguton_megtett_út/100)) + (varosi_fogyasztas * (varosban_megtett_ut/100)))*350
print("A hévizi út bekerülése, csak oda (350Ft/liter benzin árral számolva:)",költseg_1,"Ft volt")
print("A hévizi út bekerülése, oda-vissza (350Ft/liter benzin árral számolva:)",(2* költseg_1),"Ft volt")