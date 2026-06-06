a = int(input("enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are eligible")
    
elif(a==0):
    print("Age is invalid")

elif(a<18):
    print("Age is below eligibility")

else:
    print("You are not eligible")
