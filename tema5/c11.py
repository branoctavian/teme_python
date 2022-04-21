def lunileanului(anbisect, lunadinan):
    lunile1_12 = {
        'Ianuarie': 31,
        'Februarie': 28,
        'Martie': 31,
        'Aprilie': 30,
        'Mai': 31,
        'Iunie': 30,
        'Iulie': 31,
        'August': 31,
        'Septembrie': 30,
        'Octombrie': 31,
        'Noiembrie': 30,
        'Decembrie': 31
    }
    if anbisect == 0:
        return lunile1_12.pop(lunadinan)
    else:
        lunile1_12["Februarie"] = 29
        return lunile1_12.pop(lunadinan)


tipan = int(input("Pentru an bisect introdu orice cifra, altfel introdu 0: "))
lunadinanaleasa = str(input("Introdu luna din an pentru care vrei sa afli nr de zile: "))
print(lunileanului(tipan, lunadinanaleasa))