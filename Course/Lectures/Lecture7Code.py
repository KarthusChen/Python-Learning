# This function has a default parameter/argument

def default_args(val=0): # def default_args(val: object = 0) -> None:
    print(val)
	
# print(default_args.__annotations__)
    
# It can be called/invoked in more than one way

# Here the the default value, 0, is used
# because no argument was specified
default_args()

input("\nPress Enter to continue")

# Here an argument is provided
# The argument provided will be used
default_args(3)

input("\nPress Enter to continue")

# A function with default arguments can be called
# with or without these default arguments.
# If they are omitted, the default values are used.
# If they are given, the values given are used.

# Default values are used in place of missing arguments

###############################################################

# This function prints a greeting
# If no argument is given, "World" is used
def hello(name="World"):
    print("Hello", name)
    
hello()

input("\nPress Enter to continue")

hello("Stella")

input("\nPress Enter to continue")

###############################################################
  
# This function prints the numbers from 0 to 10
# default step of 1  
def count_0to10(step=1):
    
    if step < 1:
        print("Error - step must be positive")
        return
    
    for i in range(0, 11, step):
        print(i, end=" ")
        
    print()
        
count_0to10()

input("\nPress Enter to continue")

count_0to10(2)

input("\nPress Enter to continue")

count_0to10(-1)

input("\nPress Enter to continue")

count_0to10(12)

input("\nPress Enter to continue")

###############################################################

# Calling a function using keywords

# This function prints the value of the arguments
def keywords(x, y):
	print("x is", x, "and y is", y)
	
keywords(x = 1, y = 2)

input("\nPress Enter to continue")

keywords(y = 1, x = 2)

input("\nPress Enter to continue")

keywords(2, y = 3)

input("\nPress Enter to continue")


# Not allowed - keyword arguments must follow all positional arguments
# syntax
# keywords(y = 2, 3)

# Not allowed - multiple values for x
# runtime
# keywords(2, x = 2)

# Not allowed - multiple values for x
# syntax
# keywords(x = 2, x = 2)

###############################################################

# This function returns the sum of x and y
# y has default value of 1
# NOTE: if the parameters are mixed non-default/default
# non-default must be first in the definition
def add_nums(x, y = 1):
    return x + y
    
a = 1
a = add_nums(a)
print(a)

input("\nPress Enter to continue")

a = add_nums(a, 2)
print(a)

input("\nPress Enter to continue")

###############################################################

def example(x = 1, y = 1, z = 1):
    print("{} * {} * {} = {}".format(x, y, z, x * y * z))
    
example()
example(1, 2, 3)
example(2, 3, z = 4)
example(2, z = 4, y = 2)
example(z = 4, y = 3, x = 1)
# example(x = 1, 2, 3)
# example(2, 2, y = 3)
# example(x = 2, y = 2, x = 2)
example(y = 2, z = 2)
