alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
alte_numere_crescator = []
l = len(alte_numere)
i = 0
while i < l:
    nr_min = min(alte_numere)
    alte_numere.remove(nr_min)
    alte_numere_crescator.append(nr_min)
    i += 1
print(f"Lista numerelor ordonate crescator este: {alte_numere_crescator}")