#b8
dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print(dict1.keys())
#b9
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
#b10
dict1["Dorel"] = 6
print(dict1)
#b11
dict1.pop("Gigel")
dict1["Ionica"] = 9
print(dict1)