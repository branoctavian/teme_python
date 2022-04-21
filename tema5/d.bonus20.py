import datetime

def zile_ramase_pana_la_ziua_ta(urmatoarea_zi_de_nastere, data_curenta):
    return urmatoarea_zi_de_nastere - data_curenta


anul = int(input("Introdu anul urmator in care iti vei serba ziua: "))
luna = int(input("Introdu luna in care te-ai nascut: "))
ziua = int(input("Introdu ziua in care te-ai nascut: "))
urmatoareazidenastere = datetime.datetime(anul, luna, ziua)
now = datetime.datetime.now()
print(zile_ramase_pana_la_ziua_ta(urmatoareazidenastere, now))