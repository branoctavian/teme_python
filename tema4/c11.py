alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] > 0:
        numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append(alte_numere[i])
print(f"Numerele pare din lista sunt: {numere_pare}")
print(f"Numerele impare din lista sunt: {numere_impare}")
print(f"Numerele pozitive din lista sunt: {numere_pozitive}")
print(f"Numerele negative din lista sunt: {numere_negative}")