sentense = input("Enter a sentense : ").upper()
# print(sentense)
v = 0
a = []
for i in sentense:
    if(i == "A" or i == "E" or i == "I" or i == "O" or i =="U"):
        a.append(i)
        v += 1
print(f"Total vowels are : {v}")
print(a)