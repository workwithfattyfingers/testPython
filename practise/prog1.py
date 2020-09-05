def Coffee_total(quantity):
    coffee = 34
    return (coffee*quantity)

def Tea_total(quantity):
    tea = 17
    return (tea*quantity)

print("Hello! Welcome to Waqs cafe")
print("What you want to have, please choose from Menu")
print("Manu:\t \n 1. Coffee \n 2. Tea \n 3. Latte \n 4. Chicken Sandwich")


cust_name = input("Please enter your name:\t")
print("Hello\t" + cust_name + "\t Order Please!!")
choice = int(input("Please enter your choice code:\t"))

if choice == 1:
    quantity = int(input("Please enter the number of quantity:\t"))
    total = Coffee_total(quantity)
    print("Total Coffee Bill=\t" + str(total))
    # print("Thank You for visit:" + cust_name)

    
if choice == 2:
    quantity = int(input("Please enter number of quantity\t"))
    total = Tea_total(quantity)
    print("Total Tea Bill=\t" + str(total))
    # print("Thank You for visit:" + cust_name)
    # asking = input(print("Would you like to continue buying"))
    # # if asking == 'y' or asking == "Y":
    # #     Welcome_Menu(asking)

else:
    print("Thank You for visit:\t" + cust_name)



    
    
