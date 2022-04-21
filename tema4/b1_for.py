masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina_preferata = input("""Alege marca de masina preferata din lista:,
Audi
Volvo
BMW
Mercedes
Aston Martin
Lastun
Fiat
Trabant
Opel
""")
for i in range(len(masini)):
    if masini[i] == masina_preferata:
        print(f"Masina mea preferata este {masini[i]}.")