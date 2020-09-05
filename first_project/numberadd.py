total=0
i=0

input_user= input("Please eter any number:\t")

while i<len(input_user):
    total+= int(input_user[i])
    i= i+1
print("Total=\t" + str(total))
