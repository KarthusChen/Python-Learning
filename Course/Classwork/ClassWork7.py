import math

def GetNumbers():
    Number1=int(input("Enter number 1"))
    Number2=int(input("Enter number 2"))
    return Number1,Number2

def AddNumbers(Number1, Number2):
    TheSum=Number1+Number2
    return TheSum

Number1,Number2=GetNumbers()
print ("The Sum of the two numbers is: ",AddNumbers(Number1,Number2))
