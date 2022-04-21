#tema c12
#varianta operatori logici cu if else
# X = int(input('Introdu un numar: '))
# if (X >= 100000 and X <= 999999) or (X <= -100000 and X >=-999999):
#     print('Numarul introdus are exact 6 cifre')
# else:
#     print('Numarul introdus are numarul cifrelor diferite de 6')
#varianta cu if, else if, else
X = int(input('Introdu un numar: '))
if (X >= 100000 and X <= 999999):
    print('Numarul introdus are exact 6 cifre')
elif (X <= -100000 and X >=-999999):
    print('Numarul introdus are exact 6 cifre')
else:
    print('Numarul introdus are numarul cifrelor diferite de 6')