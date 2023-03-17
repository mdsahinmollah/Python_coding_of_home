fib_range = int(input("Enter the range : "))
print("Fibonacci serise is :")
sum = 1
f,s = 0,1
print(f)
print(s)
for i in range(2,fib_range):
    
    next = f + s
    sum = sum + next
    print(next)
    f = s
    s = next
print(f"The sum of  {fib_range} fibonacci number is : ",sum)