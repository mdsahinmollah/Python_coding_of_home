import random
num1 = int(input("Enter lower range : "))
num2 = int(input("Enter upper range : "))
for i in range(5):
    num = random.randint(num1,num2)
    print(num)