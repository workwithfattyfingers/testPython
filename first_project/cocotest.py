#COCO TEST
# Take Input, If start with A , allow to watch movie

user_input = input("Please enter your name:\t")
user_age = int(input("Please enter your age:\t"))
user_input= user_input.lower()
print("Name=" + user_input)

if user_input[0]== "a" and user_age>10:
    print("Welcome" + user_input)
    print("You can watch COCO Movie")
else:
    print("Sorry you are not allowed")