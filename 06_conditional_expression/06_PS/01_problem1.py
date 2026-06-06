a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))
d = int(input("Enter number d : "))

if(a>b and a>c and a>d):
    print("a is greater: ", a)

elif(b>a and b>c and b>d):
    print("b is greater: ", b)

elif(c>a and c>b and c>d):
    print("c is greater: ", c)

elif(d>a and d>b and d>c):
    print("d is greater: ", d)