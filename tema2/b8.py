#tema b8
X = int(input('X = '))
Y = int(input('Y = '))
Z = int(input('Z = '))
if X == Y == Z:
    print('Triunghiul este echilateral')
elif X == Y or Y == Z or X == Z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')