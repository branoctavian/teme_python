def nr_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))
z = int(input("Introduceti al treilea numar: "))
print(nr_max(x, y, z))