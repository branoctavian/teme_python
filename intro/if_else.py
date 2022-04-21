piesa_faina = True
print ('pornim radio')
if piesa_faina : True
print('dau mai tare')
print('si fredonam')
print ('oprim radio')

numar = 2
if numar % 2 == 0:
    print ('numar par')
else:
    print ('numar impar')

ora = int(input('Introdu ora: '))
if ora < 0:
    print('te rugam introdu o ora intre 0 - 24')
elif ora <= 11:
    print('Buna dimineata!')
elif ora <=18:
    print('Buna ziua!')
elif ora <= 21:
    print('Buna seara!')
elif ora <= 24:
    print('Noapte buna!')
else:
    print('ora invalida')
