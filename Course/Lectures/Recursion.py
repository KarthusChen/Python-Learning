def hello3():
    print("entering hello3")
    print("Hello")
    print("leaving hello3")

def hello2():
    print("entering hello2")
    print("Hello")
    hello3()
    print("leaving hello2")

def hello1():
    print("entering hello1")
    print("Hello")
    hello2()
    print("leaving hello1")
    
def main():
    print("entering main")
    hello1()
    print("leaving main")
    
main()
    
input('\nPress Enter to continue...')

# A recursive function is a function that calls itself
# directly or indirectly

# directly - the function contains a call to itself

# indirectly - the function calls others function(s)
# that eventually call the original function

# In most cases, iterative functions are more efficient
# than recursive functions

# def message():
#     print("This is a recursive function")
#     message()

# There are 2 parts to recursion
# 1. Base/Terminating/Stopping case - a condition that 
#    causes the recursive calls to terminate
# 2. Recursive call - A call to itself with an argument
#    that is closer to the base case.

def message(n):
    if n < 1:
        print("This is the end")
    else:
        print("This is a recursive function")
        message(n - 1)
        
message(3)

input('\nPress Enter to continue...')

# Factorial (n >= 0)
# n! = n * (n - 1)!,   if n > 0
# 0! = 1

def factorial(n):
    if n == 0:
        print(1)
        return 1
    else:
        print(n, "*", end=" ")
        return n * factorial(n - 1)

n = 3        
print("{}! = {}".format(n, factorial(n)))

input('\nPress Enter to continue...')

###################################################################

def printDigits(n):
    digit = n % 10
    if n >= 10:
        printDigits(n // 10)

    print(digit, end=" ")

printDigits(463)

# When is this actually useful?
# Traversing irregular data\file structures like
# Trees, file hierarchies
# Sorting algorithms like mergesort and quicksort
