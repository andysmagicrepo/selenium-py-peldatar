ev = int(input("Kérek egy évszámot és megmondom szökőév volt-e?"))
szokoev1 = not(bool(ev % 4))
szokoev2 = not(bool(ev % 400))
nem_szokoev = bool(ev % 100)
print(szokoev1)
print(szokoev2)
print(nem_szokoev)
if (szokoev2 and nem_szokoev) or (szokoev1 and nem_szokoev) or (szokoev1 and szokoev2 and (not(nem_szokoev))):
    print("A megadott év:", ev, "szökőév!")
else:
    print("A megadott év:", ev, "Nem szökőév!")