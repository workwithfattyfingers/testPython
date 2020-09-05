# # String Formatting between different versions

# name= "Waqar"
# age= 28

# print("Hello!\t" + name + "\tyour age is\t" + str(age))  # Ugly Synatx

# print("hello {} your age is {}".format(name,age))  # python 3

# # 3.6 
# print(f"hello {name} your age is {age}")  # clean method of programming

# Exercise
# Ask user to input 3 number and print average of 3 numbers using formatting

print("Welcome to Average Zone!!\t")

# number_one =  int (input ("Please enter any number\t"))
# number_two = int (input ("Please enter other number\t"))
# number_three = int (input ("Please enter any number\t"))

# average = (number_one + number_two + number_three)/3

# print(f"Average of 3 numbers is=\t{average}")

# Same Line Input



# num1, num2, num3 =  input ("Please enter 3 numbers for average=\t").split(",")

# additon = int (num1)+int (num2) + int (num3)

# average = additon/3

# print(f"Average=\t{average}")

#################################################

name = input ("Please enter any name=\t")
reverse = name [-1 : : -1]

print(f"Reverse of your name=\t {reverse}")