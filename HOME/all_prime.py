#Write a program to print all prime numbers.........
while 1:

    lower_range = input("Enter lower range : ")
    if lower_range == "":
        print("Thank you!")
        break
    if lower_range.isdigit:
        lower_range = int(lower_range)
        upper_range = int(input("Enter upper range : "))
        flag = 0
        for i in range(lower_range,upper_range + 1):
            if i > 1:
                        
                for j in range(2,i):
                    if i % j == 0 :
                        break
                else:
                    print(i)

            else:
                print("Enter a number greater than 1 !")
                print("\n")
                break
    continue