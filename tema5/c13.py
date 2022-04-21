def numaracifredinlista(olista, dict):
    for i in olista:
        dict[i] = dict.get(i) + 1
    # for i in olista:
    #     for key, value in dict.items():
    #         if i == key:
    #             dict[i] += 1
    return dict

listacifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
dictionar = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

print(numaracifredinlista(listacifre, dictionar))