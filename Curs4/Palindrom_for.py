x = ['Ana', 'Monom', '101', 'cartof', '543', 'bob']
l = len(x)
i = 0
for i in range(l) :
    s = x[i].lower()
    if s[::-1] == s:
        print(f"Sirul {s} este un palindrom")
    else:
        print(f"Sirul {s} nu este un palindrom")
else:
    print('bucla while s-a terminat')