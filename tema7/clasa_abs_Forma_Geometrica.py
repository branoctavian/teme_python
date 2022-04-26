from abc import (ABC, abstractmethod)


class FormaGeometrica(ABC):


    @public
    Pi = 3.14 # aici nu inteleg cum sa il folosesc pe Pi in clasa Cerc(FormaGeometrica)


    @abstractmethod
    def aria(self):
        print("Calculeaza suprafata unei forme geometrice exprimata in mp")
        pass

    def descrie(self):
        print("Cel mai probabil au colturi")


class Patrat(FormaGeometrica):


    def __init__(self, latura):
        self.__latura = latura


    def get_latura(self):
        return self.__latura


    def aria(self):
        return self.__latura ** 2


    def set_latura(self, alta_valoare):
        self.__latura = alta_valoare


    def del_latura(self):
        del self.__latura


class Cerc(FormaGeometrica):


    def __init__(self, raza):
        self.__raza = raza


    def get_raza(self):
        return self.__raza


    def aria(self):
        return Pi * self.__raza ** 2


    def set_raza(self, alta_valoare):
        self.__raza = alta_valoare

    def del_raza(self):
        del self.__raza


    def descrie(self):
        print("Eu nu am colturi!")


l1 = Patrat(5)
R1 = Cerc(2)

# print(l1.get_latura())
#
# l1.set_latura(4)
# print(l1.get_latura())
# l1.del_latura()
# try:
#     print(l1.get_latura())
# except Exception as e:
#     print(e)
#
# print(R1.get_raza())
# R1.set_raza(4)
# print(R1.get_raza())
#
# R1.del_raza()
#
# try:
#     print(R1.get_raza())
# except Exception as e:
#     print(e)
# print(R1.descrie())

print(l1.aria()) # aici cred ca nu trebuie sa introduc eu manual argumentul, nu am stiut cum sa
                         # il ia automat din declarerea variabile
print(R1.aria())   # aici cred ca nu trebuie sa introduc eu manual argumentul, nu am stiut cum sa
                         # il ia automat din declarerea variabile