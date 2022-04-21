# i = 0
# pare = []
# impare = []
# while i <= 10:
#     if i % 2 == 0:
#         pare.append(i)
#         print(i)
#     else:
#         impare.append(i)
#         print(f"nr {i} este impar")
#     i += 1
# print(pare)
# print(impare)

x = ['Ana', 'Monom', '101', 'cartof', '543', 'bob']
l = len(x)
i = 0
while i < l :
    s = x[i].lower()
    if s[::-1] == s:
        print(f"Sirul {s} este un palindrom")
    else:
        print(f"Sirul {s} nu este un palindrom")
    i += 1
else:
    print('bucla while s-a terminat')