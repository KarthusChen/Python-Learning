def min2(num1,num2=0):
    if num1>num2:
        return num2
    elif num1==num2:
        print("Those two numbers are the same.")
    else:
        return num1

Num1=int(input("Enter an int:"))
Num2=int(input("Enter an int:"))

print("The minimum of ",Num1," and ",Num2," is ",min2(Num1,Num2),sep="")