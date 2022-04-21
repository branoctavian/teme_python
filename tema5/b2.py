def parsauimpar(a):
    if a % 2 == 0:
        return True
    else:
        return False


numar = int(input("Introdu un numar: "))
print(parsauimpar(numar))