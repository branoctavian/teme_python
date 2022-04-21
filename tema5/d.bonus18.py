def reducere_10_procente(pret, reducere):
    if reducere in range(0, 101):
        return pret - pret*reducere/100
    else:
        return "reducere invalida, va rugam reintroduceti o reducere procentuala cuprinsa intre 0 si 100"


pret_introdus = int(input("Introduceti pretul unui produs: "))
procent_reducere = int (input("Introduceti reducerea procentuala aplicata produsului: "))

print(f" Pretul redus este: {reducere_10_procente(pret_introdus, procent_reducere)}")
