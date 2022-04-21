#Tema b8
propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = int(input(''))
print(propozitie[0:len(propozitie)-x])
#Tema b9
propozitie2 = str(propozitie[0:5] + propozitie[52:57])
print(propozitie)
#Tema b10
print(propozitie.count('the'))
#Tema b11
print(propozitie.replace('the','THE'))
#Tema b12
print(propozitie.find('rock'))
x = slice(53)
print(propozitie[x])