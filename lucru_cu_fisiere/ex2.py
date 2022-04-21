

# f = open("date_ex1.txt", "r")
with open("date_ex1.txt", "r") as f:
    i = 1
    linie = f.readline()
    linie = linie.strip("\n")
    while len(linie) > 0:
        print(f"linia {i}: {linie}")
        i += 1
        linie = f.readline()
        linie = linie.strip("\n")

# f.close()