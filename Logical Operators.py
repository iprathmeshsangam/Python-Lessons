#Logical Operators - or , and , not

age = int(input("Enter your age -> "))
aadhar = input("Do you have aadhar card / UID ? (Type yes or no)-> ")



if age >= 18 and not aadhar == "yes":
    print("Your admission is accepted")
else:
    print("Your admission is rejected")
    if age < 18:
        print("Your admission cannot proceed as you are not adult")
    else:
        print("Please bring your UID / Aadhar card")