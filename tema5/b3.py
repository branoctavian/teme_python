def numarcaractere(a, b, c):
    len(a)
    len(b)
    len(c)
    return len(a) + len(b) + len(c)


nume = str(input("Introdu numele tau: "))
prenume = str(input("Introdu prenumele tau: "))
nume_mijlociu = str(input("Daca e cazul, introdu numele mijlociu: "))
print(numarcaractere(nume, prenume, nume_mijlociu))