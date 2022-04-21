def verificaresetdenr(a, setdenr):
    if a in setdenr:
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return False
    else:
        setdenr.add(a)
        print(f"Am adaugat numarul nou in set, acesta fiind urmatorul: {setdenr}")
        return True

unsetdenroarecare = {5, -5, 0, 14, 13, 11, -16}
x = int(input("Introduceti un nr: "))
print(verificaresetdenr(x, unsetdenroarecare))
