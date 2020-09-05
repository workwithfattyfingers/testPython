def greater_num(a,b):
    if a>b:
        return a
    else:
        return b

number= int(input("Please enter any number:\t"))
number1= int(input("Please enter any number:\t"))

greater = greater_num(number, number1)

print("Greater Number is:=\t" + str(greater))