a = int(input("Enter first global variables : "))
b = int(input("Enter second global variables : "))

def swap():
    global a,b
    a,b = b,a
    
swap()   

print("a = ",a)
print("b = ",b)


