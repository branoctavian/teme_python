
class Dreptunghi:
    def __init__(self, latime, lungime, culoare):
        self.latime = latime
        self.lungime = lungime
        self.culoare = culoare


    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are latimea de {self.latime} cm, lungimea de {self.lungime} cm si culoarea {self.culoare}.")


    def arie_dreptunghi(self):
        print(f"Dreptunghiul are aria {self.latime * self.lungime}.")


    def perimetrul_dreptunghiului(self):
        print(f"Diametrul dreptunghiului este {self.latime * 2 + self.lungime * 2}.")

    def schimba_culoarea(self):
        self.culoare = str(input("Alege o alta culoare a dreptunghiului: "))
        print(f"Culoarea dreptunghiului s-a schimbat in {self.culoare}")


dreptunghi1 = Dreptunghi(4, 5,  "albastru")
dreptunghi2 = Dreptunghi(5, 6, "verde")
dreptunghi3 = Dreptunghi(6, 7, "rosu")


dreptunghi1.descrie_dreptunghi()
dreptunghi2.descrie_dreptunghi()
dreptunghi3.descrie_dreptunghi()
print("===================================")
dreptunghi1.arie_dreptunghi()
dreptunghi2.arie_dreptunghi()
dreptunghi3.arie_dreptunghi()
print("===================================")
dreptunghi1.perimetrul_dreptunghiului()
dreptunghi2.perimetrul_dreptunghiului()
dreptunghi3.perimetrul_dreptunghiului()
print(f"==================================")
dreptunghi1.schimba_culoarea()
dreptunghi1.descrie_dreptunghi()
print(f"==================================")
dreptunghi2.schimba_culoarea()
dreptunghi2.descrie_dreptunghi()
print(f"==================================")
dreptunghi3.schimba_culoarea()
dreptunghi3.descrie_dreptunghi()
print(f"==================================")