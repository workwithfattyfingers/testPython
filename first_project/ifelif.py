#Make Ticket entry ifelif concept


user_age= int(input("Please enter your age=:\t"))

if 0<user_age<=3:
    print("Your Ticket is free")
elif 4<user_age<=30:
    print("Your Ticket is 100")
elif  31<user_age<=60:
    print("Ticket is 200")
else:
    print("Ticket is 150") 