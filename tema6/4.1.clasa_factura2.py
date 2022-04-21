import datetime


class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self. cantitate = cantitate
        self. pret_buc = pret_buc


    def cap_tabel(self):
        print(f"Factura seria MZ numar {self.numar}")
        print(f"Data: {datetime.datetime.now()}")
        print("|Produs | Cantitate | Pret/Bucata | Total|")


    def genereaza_factura(self):
        print(f"|{self.nume_produs}|     {self.cantitate}     |     {self.pret_buc}     | {self.cantitate * self.pret_buc} |")

produs1 = Factura(1, "Telefon", 7, 700)
produs2 = Factura(2, "Tableta", 5, 500)
produs3 = Factura(3, "S-watch", 4, 400)

produs1.cap_tabel()
l = [produs1, produs2, produs3]
for i in range(len(l)):
    l[i].genereaza_factura()