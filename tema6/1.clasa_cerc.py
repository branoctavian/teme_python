from cmath import pi


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} si culoarea {self.culoare}")


    def aria(self):
        aria = pi * self.raza**2
        return aria


    def diametrul_cercului(self):
        print(f"Diametrul cercului este {self.raza * 2}")


    def circumferinta_cercului(self):
        print(f"Circumferinta cercului este: {self.raza ** 2 * pi}")


cerc1 = Cerc(4, "albastru")
cerc2 = Cerc(5, "verde")
cerc3 = Cerc(6, "rosu")

cerc1.descrie_cerc()
cerc2.descrie_cerc()
cerc3.descrie_cerc()
print("===========================================")
print(f"Aria cercului este: {cerc1.aria()}")
print(f"Aria cercului este: {cerc2.aria()}")
print(f"Aria cercului este: {cerc3.aria()}")
print("===========================================")
cerc1.diametrul_cercului()
cerc2.diametrul_cercului()
cerc3.diametrul_cercului()
print("===========================================")
cerc1.circumferinta_cercului()
cerc2.circumferinta_cercului()
cerc3.circumferinta_cercului()
print("==================Final====================")