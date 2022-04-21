def suma(x, y):
    return x + y


def diferenta(x, y):
    return x - y


def inmultirea(x, y):
    return x * y


def impartirea(x, y):
    return x / y


print("Selecteaza operatiunea pe care doresti sa o aplici!")
print("1.Suma")
print("2.Diferenta")
print("3.Inmultirea")
print("4.Impartirea")

while True:
    alege = input("Alege una din operatii(1/2/3/4): ")
    if alege in ('1', '2', '3', '4'):
        nr1 = float(input("Introdu primul numar: "))
        nr2 = float(input("introdu cel de-al doilea numar: "))
        if alege == '1':
            print(nr1, "+", nr2, "=", suma(nr1, nr2))
        elif alege == '2':
            print(nr1, "-", nr2, "=", diferenta(nr1, nr2))
        elif alege == '3':
            print(nr1, "*", nr2, "=", inmultirea(nr1, nr2))
        elif alege == '4':
            print(nr1, "/", nr2, "=", impartirea(nr1, nr2))
        alta_operatie = input("Mai vrei sa faci o operatie? (da/nu): ")
        if alta_operatie == "nu":
            break
    else:
        print("Operatiune invalida")