# Take 2 inputs from the user
# 1) user name
# 2) any letter from user which we can count in SyntaxWarning

# OUTPUT

# 1) user's name in length
# 2) count the number of character that user inputed

user_name=input(print("Please enter any name"))
char_count=input(print("Please enter any character which you want to count"))

#name_count = len(user_name)

#Output

print("String/Name input by you:\t" + user_name)
print("Length of your name is:\t" + str(len(user_name)))

print("Characters which you want to count:\t" + str(user_name.count(char_count)))