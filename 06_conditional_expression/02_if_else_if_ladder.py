a = int(input("enter your age: "))

if(a>=18):
    print("You are eligible")
    
elif(a==0):
    print("Age is invalid")

elif(a<18):
    print("Age is below eligibility")

else:
    print("You are not eligible")
