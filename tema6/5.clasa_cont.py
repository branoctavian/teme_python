

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")


    def debitare_cont(self):
        self.suma = int(input(f"Buna ziua domnule/doamna, {self.titular_cont}! "
                         f"Ce suma doriti sa depuneti in contul {self.iban}? "))
        print(f"Cei {self.suma} lei v-au fost adaugati in contul {self.iban} cu succes!"
              f"Soldul actual este: {self.sold + self.suma}.")


    def creditare_cont(self):
        self.suma = int(input(f"Buna ziua domnule/doamna, {self.titular_cont}!"
                              f"Introduceti suma pe care doriti sa o retrageti din contul {self.iban}: "))
        print(f"Va rugam ridicati cei {self.suma} lei solicitati! "
              f"Soldul actual este: {self.sold - self.suma}.")


clientbanca1 = Cont("RO63AMGLH000011112222", "Ion Ionel", 5000)
clientbanca1.afisare_sold()
print("=======================================")
clientbanca1.debitare_cont()
print("=======================================")
clientbanca1.creditare_cont()
print("=======================================")