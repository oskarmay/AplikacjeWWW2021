list1 = [i for i in range(1, 11)]
list2 = list1[5:]
list1 = list1[:5]

print(list1)
print(list2)

new_list = [0] + list1 + list2

print(new_list)
