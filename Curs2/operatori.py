x = int(input(''))
y = int(input(''))
z = int(input(''))
# media = (x+y)/2
# print(media)
# putere = x**y
# print(putere)
# modul = x%2
# print(modul) #impartirea cu rest, adica se afiseaza doar restul impartirii
nota_teza = int(input())
media_parcurs = (x+y+z)/3
medie_finala = (3*media_parcurs+nota_teza)/4
print(medie_finala)
nota_trecere = 5
if medie_finala >= nota_trecere:
    print(f'Felicitari, ai promovat cu nota {medie_finala}')
else:
    print('Nu ai promovat')