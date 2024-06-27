import sys
sys.setrecursionlimit(1500)

def factorial(num):
    if num==0:
        return 0
    else:
        return num+factorial(num-1)
    
print("The sum from 1 to 123 is ",factorial(123))