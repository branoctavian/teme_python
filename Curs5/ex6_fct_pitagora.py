def pitagora(c1, c2, ip):
    if ip**2 == c1**2 + c2**2:
        return True
    else:
        return False


cat1 = int(input("Introdu valoarea primei catete: "))
cat2 = int(input("Introdu valoarea celei de a doua catete: "))
ipo = int(input("Introdu valoarea ipotenuzei: "))
rez = pitagora(cat1, cat2, ipo)
if rez == True:
    print("Triunghi dreptunghic")
else:
    print("Triunghiul nu este dreptunghic")