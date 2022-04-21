masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(masini)):
    if "Trabant" == masini[i] or "Lastun" == masini[i]:
        continue
    print(f"S-ar putea sa va placa masina {masini[i]}")