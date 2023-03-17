while 1:
    str1 = input("Enter the first string : ")
    if str1 == "":
        print("Thank you !")
        quit()
    str2 = input("Enter the second string : ")
    
    print("\n")

    length = len(str1)

    mid = length // 2

    str3 = str1[:mid] + str2 + str1[mid:]

    print(f"Final string is : {str3}")

    print("\n")