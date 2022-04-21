#tema c15
print('Introdu valorile unghiurilor:')
X = int(input('X = '))
Y = int(input('Y = '))
Z = int(input('Z = '))
if X > 0 and Y > 0 and Z > 0 and (X + Y + Z) == 180:
    print('Triunghiul este valid')
elif X > 0 and Y > 0 and Z > 0 and (X + Y + Z) != 180:
    print('Triunghiul nu este valid')
else:
    print('Introdu valori pozitive mai mari decat 0 a caror suma sa fie egala cu 180')