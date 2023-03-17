# Write a program to check wheather a number is prime or not...
while 1 :
    
    num = input("Enter a number : ")
    if num.isdigit():
        num = int(num)
    
        flag = 0
        for i in range(2,num):
            if num % i == 0:
                flag = 1
                break
        if flag == 0 :
            print(f"{num} is prime! \n")

        else:
            print(f"{num} is not prime! \n")   
    elif num.isalpha():
        print("Enter a integer number! \n")
    else:
        print("Thank you ! \n")
        quit()
    