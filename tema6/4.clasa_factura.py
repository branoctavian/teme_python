import datetime


class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self. cantitate = cantitate
        self. pret_buc = pret_buc


    def schimba_cantitatea(self):
        self.cantitate = int(input(f"Introduceti noua cantitatea a produsului {self.nume_produs}: "))
        print(f"Noua cantitate a produsului este de {self.cantitate} bucati.")


    def schimba_pretul(self):
        self.pret_buc = int(input(f"Introduceti noul pret al produsului {self.nume_produs}: "))
        print(f"Noul pret al produsului este de {self.pret_buc} lei/buc.")


    def schimba_nume_produs(self):
        self.nume_produs = str(input(f"Alegeti alt nume pentru produsul {self.nume_produs}: "))
        print(f"Noul nume al produsului este: {self.nume_produs}.")


    def genereaza_factura(self):
        print(f"Factura seria MZ numar {self.numar}")
        print(f"Data: {datetime.datetime.now()}")
        print("|Produs | Cantitate | Pret/Bucata | Total|")
        print(f"|{self.nume_produs}|     {self.cantitate}     |     {self.pret_buc}     | {self.cantitate * self.pret_buc} |")


produs1 = Factura(1, "Telefon", 7, 700)
produs2 = Factura(2, "Tableta", 5, 500)
produs3 = Factura(3, "S-watch", 4, 400)
produs1.genereaza_factura()
print("=======================================")
produs2.genereaza_factura()
print("=======================================")
produs3.genereaza_factura()
print("=======================================")
produs1.schimba_cantitatea()
produs2.schimba_cantitatea()
produs3.schimba_cantitatea()
print("=======================================")
produs1.schimba_pretul()
produs2.schimba_pretul()
produs3.schimba_pretul()
print("=======================================")
produs1.schimba_nume_produs()
produs2.schimba_nume_produs()
produs3.schimba_nume_produs()
print("=======================================")
produs1.genereaza_factura()
print("=======================================")
produs2.genereaza_factura()
print("=======================================")
produs3.genereaza_factura()
print("=======================================")
l = [produs1, produs2, produs3]
for i in range(len(l)):
    l[i].genereaza_factura()