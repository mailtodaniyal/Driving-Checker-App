a = int(input("Enter your age: "))
print("Your age is:",a)
if(a < 0):
    print("Write again")
elif(a > 18):
    if(a >= 18 and a <= 60):
        print("You are eligible to drive")
    elif(a >= 61 and a <= 89):
        print("You are too old to drive")
    elif(a >= 90):
        print("You are probably dead")
else:
    print("You are not eligible to drive")
