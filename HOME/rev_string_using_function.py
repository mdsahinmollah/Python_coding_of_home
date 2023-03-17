# string = input("Enter a string : ")
# rev = string[::-1]
# print(rev)

#string reverse using recarsion....
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]
        
word = input("Enter a string : ")
print(reverse_string(word))