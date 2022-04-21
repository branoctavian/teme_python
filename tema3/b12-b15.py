#b12
zilele_saptamanii = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
zile_de_weekend = {'sambata', 'duminica'}
zilele_saptamanii.add('luni')
print(zilele_saptamanii)
#b13
verificare_zile_de_weekend = zile_de_weekend.issubset(zilele_saptamanii)
if verificare_zile_de_weekend == True:
    print('Zilele de weekend sunt un subset al zilelor saptamanii!')
else:
    print('Zilele de weekend nu sunt un subset al zilelor saptamanii!')
#b14
print(zilele_saptamanii.difference(zile_de_weekend))
#b15
print(zilele_saptamanii.intersection(zile_de_weekend))