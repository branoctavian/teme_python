def sirdecaractere(sir):
    majuscule = 0
    minuscule = 0
    spatii = 0
    numere = 0
    altecaractere = 0
    for i in sir:
        if i.isupper():
            majuscule += 1
        elif i.islower():
            minuscule += 1
        elif i.isnumeric():
            numere += 1
        elif i.isspace():
            spatii += 1
        else:
            altecaractere += 1
    print(f"Numarul majusculelor este {majuscule}")
    print(f"Numarul minusculelor este {minuscule}")
    # print(f"Numarul caracterelor numere este {numere}")
    # print(f"Numarul de spatii este {spatii}")
    # print(f"Numarul altor tipuri de caractere este {altecaractere}")
sirstring = input("Introduceti un sir de caractere: ")
sirdecaractere(sirstring)