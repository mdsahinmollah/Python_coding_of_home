list = [2,4,7,3,2,7,9,5,1,9,3,1,3,35,23,70,3,32,70]

uniqueList = []
duplicateList = []

for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
    # else:
        duplicateList.append(i)

print(duplicateList)