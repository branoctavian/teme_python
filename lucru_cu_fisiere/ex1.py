# vom citi date din fisierul date_ex1.txt

# vom deschide f in modul de citire
f = open("date_ex1.txt", "r")

# pasul 2: citim continutul fisierului si afisam la consola

# continut = f.read()
continut = f.readlines()
print(continut)

# pasul 3

f.close()