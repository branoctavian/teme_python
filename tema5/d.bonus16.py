def numeromanesc(prenume):
    for i in range(len(prenume)):
        if prenume[-1] == "a":
            return "Prenumele introdus este de fata"
        elif prenume == "Carmen":
            return "Prenumele introdus este de fata"
        elif prenume[-1] != "a":
            return "Prenumele introdus este de baiat"
        elif prenume == "Alexandru" or prenume == "Radu":
            return "Prenumele introdus este de baiat"


prenumeales = str(input("Alege un nume romanesc: "))
print(numeromanesc(prenumeales))