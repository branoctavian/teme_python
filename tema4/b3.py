masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
i = 0
while i < len(masini):
    if "Mercedes" == masini[i]:
        print(f"Am gasit masina dorita")
        break
    else:
        print(f"Am gasit masina {masini[i]}. Mai cautam")
    i += 1