#tema c14
X = int(input('X = '))
Y = int(input('Y = '))
Z = int(input('Z = '))
if X > Y and X > Z:
    print('X este cel mai mare numar din cele 3 introduse')
elif Y > X and Y > Z:
    print('Y este cel mai mare numar din cele 3 introduse')
elif Z > X and Z > Y:
    print('Z este cel mai mare numar din cele 3 introduse')
else:
    print('Cel putin doua numare sunt egale')
#tema c14_2(ordonarea crescatoare)
X = int(input('X = '))
Y = int(input('Y = '))
Z = int(input('Z = '))
if X <= Y and Y <= Z:
    print(f'{X}, {Y}, {Z}')
elif X >= Y and Y <= Z and Z >= X:
    print(f'{Y}, {X}, {Z}')
elif X >= Y and Y <= Z and Z <= X:
    print(f'{Y}, {Z}, {X}')
elif X <= Y and Y >= Z and X <= Z:
    print(f'{X}, {Z}, {Y}')
elif X <= Y and Y >= Z and X >= Z:
    print(f'{Z}, {X}, {Y}')
else:
    print(f'{Z}, {Y}, {X}')