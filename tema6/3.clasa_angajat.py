
class Angajat:


    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu


    def descrie_angajat(self):
        print(f"Angajatul se numeste {self.nume} {self.prenume} si are salariul de {self.salariu} lei.")


    def nume_complet_angajat(self):
        print(f"Numele complet al angajatului este: {self.nume} {self.prenume}.")


    def salariu_lunar(self):
        print(f"Salariul lunar este de: {self.salariu} lei.")


    def salariu_anual(self):
        print(f"Salariul anual este de: {self.salariu * 12} lei, plus eventuale bonsuri de performanta.")


    def marire_salariu(self):
        self.procent = int(input(f"Salariul se mareste anual cu urmatoarele procente pentru angajatul {self.nume} {self.prenume}: "))
        print(f"Salariul se mareste anual cu {self.procent}%, astfel dupa primul an angajatul {self.nume} {self.prenume}"
              f" va avea un salariu lunar de {self.salariu + self.salariu * self.procent / 100} si un salariu anual de"
              f" {12 * (self.salariu + self.salariu * self.procent / 100)}.")


angajat1 = Angajat("Ion", "Ionescu", 3500)
angajat2 = Angajat("Pop", "Popescu", 3300)
angajat3 = Angajat("Bob", "Bobescu", 4000)
angajat1.descrie_angajat()
angajat2.descrie_angajat()
angajat3.descrie_angajat()
print("===================================")
angajat1.nume_complet_angajat()
angajat2.nume_complet_angajat()
angajat3.nume_complet_angajat()
print("===================================")
angajat1.salariu_lunar()
angajat2.salariu_lunar()
angajat3.salariu_lunar()
print("===================================")
angajat1.salariu_anual()
angajat2.salariu_anual()
angajat3.salariu_anual()
print("===================================")
angajat1.marire_salariu()
angajat2.marire_salariu()
angajat3.marire_salariu()
print("===================================")