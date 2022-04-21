def listanrpozitive(lista, listafiltrata):
    for i in range(len(lista)):
        if lista[i] >= 0:
            listafiltrata.append(lista[i])
    return listafiltrata


numere = [-5, 0, 5, 6, -7, 8, -10, 19, 21, -81]
nrpozitive = []
print(listanrpozitive(numere, nrpozitive))
