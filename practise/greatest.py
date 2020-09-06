
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    

num1 = int (input("Please enter Number 1=:"))
num2 = int (input("Please enter number 2=:"))
num3 = int (input("Please enter number 3=:"))

bigger = greatest(num1,num2,num3)

print(f"Greatest Amount Amount 3 is:{bigger}")
    
