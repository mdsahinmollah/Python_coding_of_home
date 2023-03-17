list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

combined_dict = {}

for i in range(len(list1)):
    combined_dict[list1[i]] = (list2[i], list3[i])

print(combined_dict)
