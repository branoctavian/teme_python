masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_majuscule = []
masini_majuscule.append(masini[0])
for i in range(1, len(masini)-1):
    majuscule = masini[i].upper()
    masini_majuscule.append(majuscule)
masini_majuscule.append(masini[-1])
print(f"Noua lista este {masini_majuscule}")