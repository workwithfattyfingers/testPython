name= input("Please enter name")
i=0
tem_var = ""
while i < len(name):
    if name[i] not in tem_var:
        tem_var += name[i]
    print(f"{name[i]} : {name.count(name[i])}")
    # i=i+1
    i += 1
