def average(l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    a = s / len(l)
    print(a)

l = [4, 5, -5, 0, 9, 15, 19, -21]
average(l)
