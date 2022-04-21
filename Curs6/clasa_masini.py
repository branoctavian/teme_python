
class Car:
    def __init__(self, marca, an_fabricatie, model, culoare, pret):
        self.marca = marca
        self.an_fabricatie = an_fabricatie
        self.model = model
        self.culoare = culoare
        self.pret = pret
    def prezentare_masina(self):
        print(
            f"Masina are urmatoarele caracteristici: {self.marca, self.an_fabricatie, self.model, self.culoare, self.pret}")


car1 = Car("Dacia", 1970, "model 1100", "galben", 500)
# car1.prezentare_masina()
car2 = Car("Volvo", 2000, "XC 600", "alb", 1000)
# car2.prezentare_masina()
car3 = Car("VW", 2010, "Golf", "albastru", 2000)

lista = [car1, car2, car3]
for i in range(len(lista)):
    # lista[i].prezentare_masina()
    if lista[i].pret < 1000:
        lista[i].prezentare_masina()

if car1.pret > car2.pret:
    print(f"Car1 este mai scump decat car2 si are urm caracteristici {car1.pret}")
else:
    print(f"Car2 este mai scump decat car1 si are urm caracteristici {car2.pret}")