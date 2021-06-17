eletkor = int(input("Hány éves vagy?"))
ital = int(input("Mit kérsz inni (sör=0, kóla=1, egyéb>1)?"))
if eletkor <18:
    if ital == 0:
        print("Sajnos, kiskorú nem kaphat sört!")
    elif ital ==1:
        print("Parancsoljon, a kólája!")
    else:
        print("Csak kólát tudunk adni!")
elif eletkor > 60:
    if ital == 0:
        print("Parancsoljon, a söre!")
    elif ital == 1:
        print("A koffein megemelheti a vérnyomását!")
    else:
        print("Sajnos,csak sört vagy kólát tudunk adni!")
else:
    if ital == 0:
        print("Parancsoljon, a söre!")
    elif ital == 1:
        print("Parancsoljon, a kólája!")
    else:
        print("Sajnos, csak sört vagy kólát tudunk adni!")