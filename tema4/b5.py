masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if "Lastun" == masini[i]:
        masini_vechi.append(masini[i])
        masini.remove(masini[i])
        masini.append("Tesla")
    if "Trabant" == masini[i]:
        masini_vechi.append(masini[i])
        masini.remove(masini[i])
        masini.append('Tesla')
print(f"Masini noi: {masini}.")
print(f"Masini vechi: {masini_vechi}")