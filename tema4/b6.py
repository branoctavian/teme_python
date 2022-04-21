pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
masini_buget = []
for i in pret_masini:
    if pret_masini[i] <= 15000:
        masini_buget.append(i)
print(f"Pentru un buget de 15000 de euro puteti achizitiona urmatoarele masini: {masini_buget}")