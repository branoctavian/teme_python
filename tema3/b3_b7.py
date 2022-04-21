#b3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
#varianta 1
lista3 = lista1 + lista2
print(lista3)
#varianta 2
lista1.extend(lista2)
print(lista1)
#b4
lista3.sort()
print(lista3)
lista3.remove(0)
print(lista3)
#b5
lungimea_listei3 = len(lista3)
if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')
#b6
lista3.clear()
print(lista3)
#b7
if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')