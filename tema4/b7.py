numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
l = []
for i in range(len(numere)):
    if numere[i] == 3:
        l.append(i)
print(f"Numarul 3 in lista numere se repeta de {len(l)} ori.")