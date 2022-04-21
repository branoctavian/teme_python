tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for i in range(len(tastatura_telefon)):
    l = tastatura_telefon[i]
    for j in range(len(l)):
        print(f"Cifra curenta este {l[j]}")