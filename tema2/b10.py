#tema b10
nota = int(input('Nota in sistem romanesc introdusa este: '))
if nota > 9 and nota <= 10:
    print('Nota echivalenta in sistem american este A')
elif nota > 8 and nota <= 9:
    print('Nota echivalenta in sistem american este B')
elif nota > 7 and nota <= 8:
    print('Nota echivalenta in sistem american este C')
elif nota > 6 and nota <= 7:
    print('Nota echivalenta in sistem american este D')
elif nota > 4 and nota <= 6:
    print('Nota echivalenta in sistem american este E')
elif nota <= 4 and nota > 0:
    print('Nota echivalenta in sistem american este F')
else:
    print('Te rugam introdu o nota valida intre 1 si 10')