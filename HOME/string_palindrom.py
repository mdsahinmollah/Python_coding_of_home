#Write a program to check wheather a string is palindrom or not?

# a = []
# b = []
# str = input("Enter a string : ")
# for i in str:
#     a.append(i)
# # print(a)
# length = len(str)
# for i in range(-1,(-length-1),-1):
#     arr = str[i]
#     b.append(arr)
# # print(b)
# if b == a:
#     print(f"{str} is palindrom.")
# else:
#     print(f"{str} is not palindrom")

#Another method...
str = input("Enter a string : ")
reverse = str[::-1]
if str == reverse:
    print("string in palindrom.")
else:
    print("String is not palindrom!")