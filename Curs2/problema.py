numar1 = int(input('Primul numar introdus este: '))
numar2 = int(input('Al doilea numar introus este: '))
operator = input('operator: ')
if operator == '+':
    print(numar1 + numar2)
elif operator == '-':
    print(numar1 - numar2)
elif operator == '*':
    print(numar1 * numar2)
elif operator == '/':
    if numar2 == 0:
        print('nu se poate realiza impartirea cu zero')
    else:
        print(numar1 / numar2)
elif operator == '%':
    print(numar1 % numar2)
elif operator == '**':
    print(numar1 ** numar2)
else:
    print('introdu te rog un operator aritmetic')