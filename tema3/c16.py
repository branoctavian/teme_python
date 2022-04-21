titulari = ['Messi', 'Ronaldo', 'Maradona', 'Pele', 'Figo']
rezerve = ['Puyol', 'Hagi', 'Popescu']
schimbari_efectuate = 2
schimbari_max = 3
schimbari_ramase = schimbari_max - schimbari_efectuate
jucator_iesit = input('Introdu numele jucatorului pe care vrei sa il schimbi: ')
jucator_intrat = input('Introdu numele jucatorului pe care vrei sa il introduci: ')
if jucator_iesit in titulari and schimbari_ramase > 0:
    titulari.remove(jucator_iesit)
    titulari.append(jucator_intrat)
    print(f"A iesit {jucator_iesit} si a intrat {jucator_intrat}, schimbari ramase: {schimbari_ramase-1}")
elif jucator_iesit not in titulari:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_iesit} nu este in teren")
    print(f"Schimbari ramase: {schimbari_ramase}")
elif schimbari_ramase == 0:
    print('Ati efectuat numarul maxim de schimbari')
    print(f"Jucatorii din teren sunt acestia: {titulari}")