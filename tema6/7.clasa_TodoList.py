

class TodoList:


    def todo(self):
        self.dict = {}
        print(self.dict)


    def adauga_task(self):
        nr_taskuri = int(input("Introduceti nr de task-uri pe care le aveti in minte: "))

        i = 0
        while i < nr_taskuri:
            self.nume = str(input("Introduceti numele unui task: "))
            self.descriere = str(input("Detaliati sarcinile task-ului: "))
            self.dict.update({self.nume: self.descriere})
            i += 1
            print(f"Lista de task-uri este urmatoarea: {self.dict}")


    def finalizeaza_task(self):
        while len(self.dict) > 0:
            self.task_rezolvat = str(input("Introduceti task-ul finalizat: "))
            if self.task_rezolvat in self.dict:
                del self.dict[self.task_rezolvat]
                self.alt_task = str(input("Ati mai finalizat si alt task? DA/NU: "))
                if self.alt_task == "NU":
                    break
            else:
                print(f"Taskul {self.task_rezolvat} nu exista!")


    def afiseaza_todo_list(self):
        print(f"Lista de activitati este: {self.dict.keys()}")


    def afiseaza_detalii_suplimentare(self):
        self.nume_task = str(input("Introduceti un task: "))
        if self.nume_task not in self.dict.keys():
            self.raspuns = str(input(f"{self.nume_task} nu este in lista de task-uri. Doriti sa adaugati? DA/NU: "))
            if self.raspuns == "NU":
                print("La revedere")
            elif self.raspuns == "DA":
                self.alt_task = str(input("Introduceti un alt task: "))
                self.detalii_task_nou = str(input("Detaliati task-ul: "))
                self.dict[self.alt_task] = self.detalii_task_nou
                print(f"Lista de taskuri actualizata este {self.dict}")
        else:
            print(f"Task-ul {self.nume_task} are urmatoarele detalii: {self.dict.get(self.nume_task)}")


dict1 = TodoList()

dict1.todo()
print("=================================")
dict1.adauga_task()
print("=================================")
dict1.finalizeaza_task()
print("=================================")
dict1.afiseaza_todo_list()
print("=================================")
dict1.afiseaza_detalii_suplimentare()
print("=================================")
