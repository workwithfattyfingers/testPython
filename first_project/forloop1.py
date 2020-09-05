#for loop

# num= int(input("Please enter any number"))
# sum=0
# i=1
# for i in range(num+1):
#     sum= sum+i
#     print("Current I number=:\t" + str(i))
#     # i=i+1
# print("Total Addition:\t" + str(sum))

# number= input("Please enter any number:\t")
# total = 0

# for i in range(0,len(number)):
#     total=total+ int(number[i])
    
# print(total)

name= input("Plese enter name:\t")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")