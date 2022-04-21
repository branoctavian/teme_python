#Tema 1 - punctul b2
dispozitiv = 'telefon'
an_fabricatie = 2022
pret = 2499.9
waterproof = True
if waterproof == True:
    waterproof = 'rezistent la apa'
print(f'Vand {dispozitiv} fabricat in anul {an_fabricatie} la pretul de {pret} RON, acesta fiind {waterproof}')
#Tema 1 - punctul b3
print(type(dispozitiv))
print(type(an_fabricatie))
print(type(pret))
print(type(waterproof)) #daca anulez if-ul va aparea bool, daca nu anulez if-ul va aparea str
#Tema 1 - punctul b4
pret = round(pret)
print(pret)
print(type(pret))
#Tema 1 - punctul b5
print(f'Vand {dispozitiv} fabricat in anul {an_fabricatie} la pretul de {pret} RON, acesta fiind {waterproof}')
print('Vand ' + dispozitiv + ' fabricat in anul ' + str(an_fabricatie) + ' la pretul de ' + str(pret) + ' RON, acesta fiind '+ str(waterproof))
print(f'Donez {dispozitiv} fabricat in anul {an_fabricatie}, acesta fiind {waterproof}')
print('Donez ' + dispozitiv + ' fabricat in anul ' + str(an_fabricatie) + ', acesta fiind '+ str(waterproof))

