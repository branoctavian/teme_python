def compararenr(a, b):
    if a > b:
        print(f"Primul numar introdus, {a}, este mai mare decat al doilea numar introdus, {b}.")
    elif b > a:
        print(f"Al doilea numar introdus, {b}, este mai mare decat primul numar introdus, {a}.")
    else:
        print(f"Numerele sunt egale")


x = int(input("Introduceti primul numar: "))
y = int(input("Introduceri al doilea numar: "))
compararenr(x, y)