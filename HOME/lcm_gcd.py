while 1:
    a = float(input("enter first number : "))
    b = float(input("enter second number : "))

    if a < b:
        a,b = b,a

    m = a
    n = b 

    while(a%b):
        c = a%b
        a = b
        b = c

    print("GCD is ",b)
    
    lcm = (m*n)/b
    print("LCM is ",lcm)