


#avem 3 scaune
"""
1. material piele
culoare negru
format spatar
2. material: piele
culoare: maro
format: spatar
3. material: burete
culoare: multicolor
format: simplu
"""

"""
solutia 1 - un dictionar pentru fiecare scaun
"""
#
# d1 = {
#     "material": piele,
#     "culoare": negru,
#     "format": spatar
# }
# d2 = {
#     "material": piele,
#     "culoare": maro,
#     "format": spatar
# }
# d3 = {
#     "material": burete,
#     "culoare": multicolor,
#     "format": simplu
# }
# lista_scaune = [d1, d2, d3]

"""
solutia 2 - cate o lista pentru fiecare caracteristica
"""
# l_material = [piele, piele, burete]
# l_culoare = [negru, maro, multicolor]
# l_format = [spatar, spatar, simplu]

"""
solutia 3 - definim o clasa Scaun
"""

class Scaun:

    def __init__(self, mat, cul, form):
        self.material = mat
        self.culoare = cul
        self.format = form

s1 = Scaun("piele", "negru", "spatar") #creez un nou scaun
print(s1)           #s1 va fi un obiect de tip scaun
print(type(s1))     #afisam efectiv tipul / clasa obiectului
print(f"Scaunul s1 este din material: {s1.material}, are culoarea {s1.culoare} si are {s1.format}")

s2 = Scaun("piele", "maro", "spatar")
print(f"Scaunul s2 este din: {s2.material}, are culoarea {s2.culoare} si are {s2.format}")

s3 = Scaun("burete", "multicolor", "simplu")
print(f"Scaunul s3 este din: {s3.material}, are culoarea {s3.culoare} si are {s3.format}")
