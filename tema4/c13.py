import random

numar_secret = random.randint(1, 30)
numar_ghicit = int(input("Introdu un numar cuprins intre 1 si 30: "))
print(numar_secret)
i = 0
while i != 30:
    if numar_ghicit > numar_secret:
        print("Nr secret e mai mic")
        break
    elif numar_ghicit < numar_secret:
        print("Nr secret e mai mare")
        break
    else:
        print("Felicitari! Ai ghicit!")
        break
    i += 1