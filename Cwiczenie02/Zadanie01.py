list_a = [1, 2, 3, 4, 5]
list_b = [6, 5, 6, 5, 6, 6]


def better_list(lista, listb):
    templist1 = [i for idx, i in enumerate(lista) if idx % 2 == 0]
    templist2 = [i for idx, i in enumerate(listb) if idx % 2 == 1]

    return templist1 + templist2


print(better_list(list_a, list_b))
