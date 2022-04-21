def suma_lui_gauss(n):
    if n >= 0:
        return n * (n + 1) / 2
    else:
        print("Introduceti un numar pozitiv!")


a = int(input("Introduceti un numar: "))
print(f"Suma lui Gauss pentru {a} numere este: {suma_lui_gauss(a)}")