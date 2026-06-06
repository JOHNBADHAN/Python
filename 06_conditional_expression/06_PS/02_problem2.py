marks1 = int(input("Enter sub1 marks: "))
marks2 = int(input("Enter sub1 marks: "))
marks3 = int(input("Enter sub1 marks: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

# print(total_percentage)

# if(total_percentage>=40):
#     print("You are passed")

# elif(total_percentage<40):
#     print("You are failed:")

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)