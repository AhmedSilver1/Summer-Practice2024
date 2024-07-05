country = input("Where are you from? ")
age = input("What is your age? ")

if (country == "South Africa"):
    if (int(age) >= 17):
        print("Allowed to drive")
    else:
        print("Not allowed to drive")

elif (country == "France"):
    if (int(age) >= 17):
        print("Allowed to drive")
    elif (int(age) >= 15):
        print("Allowed with parents supervision")
    else:
        print("Not allowed to drive")

elif (country == "Maxico"):
    if (int(age)>= 18):
        print("Allowed to drive")
    elif (int(age)>= 16):
        print("Allowed with parents agreement")
    elif (int(age) >= 15):
        print("Allowed with parents supervision ")
    else:
        print("Not allowed to drive")

elif (country == "India"):
    if (int(age) >= 18):
        print("Allowed to drive")
    else:
        print("Not allowed to drive")

else:
    print("Error! Enter a valid country!")
