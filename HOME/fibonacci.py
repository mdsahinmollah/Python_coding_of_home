#to print the fibonacci serise upto n numbers...

num = int(input("Enter the range : "))
fibonacci = [0,1]
for i in range(2,num):
    next = fibonacci[i-1] + fibonacci[i - 2]
    fibonacci.append(next)

for j in fibonacci:
    print(j)


# Another method...............
num = int(input("Enter the range : "))
f,s= 0,1,
print(f)
print(s)
for i in range(2,num):
    next = f + s
    print(next)
    f = s
    s = next
