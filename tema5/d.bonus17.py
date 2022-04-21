def numere_comune(lista_nr_comune, l1, l2):
    list_nr_comune = [i for i in l1 if i in l2]
    return list_nr_comune


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
lista3 = []
print(numere_comune(lista3, list1, list2))