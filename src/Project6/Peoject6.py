Menu = ["Latte","Espresso","Mocha","Tea","Water"]
customerOrder= []
total= 0
customerWantsToOrder=True

for i, item in enumerate(Menu) :
    print(str(i)+ ": "+str(item))

answer =input("Do you want to order? (Y,N) ")

if answer == "Y":
    customerWantsToOrder = True
elif answer =="N":
    customerWantsToOrder = False
else:
    print("Please enter a valid input")
    exit()
while customerWantsToOrder:
    customerOrder.append(Menu[int(input("What do you want to add? "))])
    total+=10
    answer =input("Do you want to order? (Y,N) ")
    if answer == "Y":
        customerWantsToOrder = True
    elif answer =="N":
        customerWantsToOrder = False
    else:
            print("Please enter a valid input")
            exit()
print("add a tip from 0 to 25")
tip = total *(int(input(""))/100)
total+= tip
print("Your total is: "+ str(total))
print(customerOrder)



