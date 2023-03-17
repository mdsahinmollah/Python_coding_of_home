base = int(input("Enter the base : "))
exponent = int(input("Enter the exponent : "))
sum = 1
for i in range(1,exponent+1):
    sum = sum * base

print(sum)