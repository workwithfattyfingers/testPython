# user_input = input("Please enter Name")

# i=1
# while i<10:
#     print("Welcome:\t" + user_input)
#     i=i+1

# i=1
# total=0
# while i<=10:
#     print("Number=\t" + str(i))
#     total = total + i
#     i=i+1
#     print("Total Sum=" + str(total))

#Input by user program

user_input= int(input("Please enter any number:\t"))
total=0
i=1
while i<=user_input:
    print("Number=\t" + str(i))
    total+= i
    i=i+1
    print("Total Sum=\t" + str(total))