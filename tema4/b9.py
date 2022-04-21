numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar_max = 0
for i in range(len(numere)):
    if numere[i] > numar_max:
        numar_max = numere[i]
print(f"Numarul cel mai mare din lista este {numar_max}")