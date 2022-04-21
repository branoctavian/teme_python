

class Masina:
    culoare = "Gri"
    viteza_actuala = 0
    culori_disponibile = {"Albastru", "Verde", "Roz", "Rosu", "Portocaliu", "Alb", "Maro"}
    marca = "Skoda"
    inmatriculata = False


    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima


    def descriere(self):
        print(f"Specificatiile masinii sunt: \n"
              f"Marca: {self.marca} \n"
              f"Model: {self.model} \n"
              f"Viteza maxima: {self.viteza_maxima} \n"
              f"Viteza actuala: {self.viteza_actuala} \n"
              f"Culoare: {self.culoare} \n"
              f"Status inmatriculare: {self.inmatriculata} \n")


    def inmatriculare(self):
        self.inmatriculata = True
        print(f"Masina marca {self.marca}, modelul {self.model} a fost inmatriculata.")


    def vopseste(self):
        print(str(self.culori_disponibile))
        self.culoare = str(input("Alegeti una din culorile de mai sus: "))
        if self.culoare in self.culori_disponibile:
            print(f"Felicitari! Masina ta va avea culoarea: {self.culoare}!")
        else:
            print(f"Culoarea {self.culoare} nu este disponibila!")

    def accelereaza(self):
        self.viteza = int(input("Introdu viteza pana la care vrei sa accelereze masina: "))
        if self.viteza > 0 and self.viteza <= self.viteza_maxima:
            print(f"Masina a accelerat pana la viteza {self.viteza} km/h.")
        elif self.viteza > self.viteza_maxima:
            print(f"Masina a accelerat pana la viteza {self.viteza_maxima} km/h.")
        elif self.viteza < 0:
            print("Eroare: viteza nu poate fi negativa")


    def franeaza(self):
        self.viteza_actuala = 0
        print(f"Masina a franat pana a ajuns la {self.viteza_actuala} km/h.")

masina1 = Masina("Octavia RS", 250)
masina2 = Masina("Octavian Tour", 200)
masina3 = Masina("Fabia", 180)

masina1.descriere()
print("====================================")
masina1.inmatriculare()
print("====================================")
masina1.vopseste()
print("====================================")
masina1.accelereaza()
print("====================================")
masina1.franeaza()
print("====================================")
masina2.descriere()
print("====================================")
masina2.inmatriculare()
print("====================================")
masina2.vopseste()
print("====================================")
masina2.accelereaza()
print("====================================")
masina2.franeaza()
print("====================================")
masina3.descriere()
print("====================================")
masina3.inmatriculare()
print("====================================")
masina3.vopseste()
print("====================================")
masina3.accelereaza()
print("====================================")
masina3.franeaza()
print("====================================")