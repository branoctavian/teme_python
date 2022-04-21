from abc import abstractmethod


class FormaGeometrica:


    Pi = 3.14


    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil au colturi")


class Patrat(FormaGeometrica):


    def __init__(self, latura):
        self.__latura = latura


    def get_latura(self):
        return self.__latura


    def aria_patrat(self, latura):
        a = latura ** 2
        return a

    def set_latura(self, alta_valoare):
        self.__latura = alta_valoare


    def del_latura(self):
        del self.__latura


class Cerc(FormaGeometrica):


    def __init__(self, raza):
        self.__raza = raza


    def get_raza(self):
        return self.__raza


    def aria_cerc(self, raza):
        a = Pi * raza ** 2
        return a

    def set_raza(self, alta_valoare):
        self.__raza = alta_valoare

    def del_raza(self):
        del self.__raza


    def descrie(self):
        print("Eu nu am colturi!")


l1 = Patrat(5)
R1 = Cerc(2)

print(l1.get_latura())

l1.set_latura(4)
print(l1.get_latura())
l1.del_latura()
try:
    print(l1.get_latura())
except Exception as e:
    print(e)

print(R1.get_raza())
R1.set_raza(4)
print(R1.get_raza())

R1.del_raza()

try:
    print(R1.get_raza())
except Exception as e:
    print(e)
print(R1.descrie())

print(l1.aria_patrat(5))
print(R1.aria_cerc(2))