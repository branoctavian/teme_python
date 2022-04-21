def caracterinsir(sir, i):
    if i in sir:
        return True
    else:
        return False


sirdecaractere = str(input("Introduceti un sir de caractere: "))
caracter = str(input("Introduceti caracterul de verificat: "))
print(caracterinsir(sirdecaractere, caracter))