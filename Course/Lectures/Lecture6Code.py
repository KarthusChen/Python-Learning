# A function is a block of code (series of statements) designed
# to perform a specific task

# We have used quite a few functions already, print, input
# int, float, random.randint, math.sqrt, ...

# Most of the functions we have used are built-in Python 3 functions.
# They are available to all Python programs and need NO import statement.

# We have also used a few functions from the Python Standard Library.
# These require an import statement.

# We don't have to understand the implementation of print, input, etc.
# The ability to call/invoke these functions makes our lives as
# programmers much easier.

# We can also use Python to write our own functions. 
# The functions we write are sometimes referred to as programmer- or
# user-defined functions.

# You should write your own functions if you seem to be performing
# the same routine again and again. If you're copying and pasting
# a lot. Consider using a function.

# Function Syntax:
#
# def <functionName>([parameterList]):
#     <function body or block>
#
# The function body (or block) includes the code you want to perform
# in your function.
# The rules for variable names apply to function names too.
#   * No Python keywords
#   * Letters, underscore, and numbers are ok - cannot start with a number
#   * Case sensitive

# To use a function we need two things in Python. We need a
# function implementation/definition and we need to call/invoke
# the function.

# To invoke the function, write the function name and parentheses.

##########################################################################

# The parameter list can be empty. If not empty, multiple
# parameters are separated by commas

# Parameters should be used in some way. It is wasteful to send an
# unused parameter.

# The function may return a value, but this is not required.

# If the function returns a value and we want to use that value in our 
# program we must assign the return value to a variable or use it as 
# an input for another function.

# When we run our programs we execute lines of code sequentially. If
# there is a selection or loop structure, the code executes as we
# have explained for those structures. But control never leaves the
# global namespace. When we call a function we are giving control of
# the execution of our program to the function. The execution of the
# function occurs in a separate namespace.

# The local variables of the function (those created in the function)
# are lost once the function returns. If we want to keep a calculated
# value, we must return the value and assign or use the value as
# mentioned above.

# The following is only true for immutable data types.
# When variables are used as arguments of a function they are copied to 
# variables in the function namespace and are valid only while the 
# function executes. The copy can be manipulated in many ways but the 
# value of the original variable remains unchanged - changes only affect the
# copy.

# Only one return value is allowed (misleading). We will just return a
# tuple and use tuple assignment.

# Benefits of functions:
#   * Functions allow complex code to be broken into smaller units.
#   * Functions allow for code reuse.
#   * Functions make it easier to debug and fix errors.
#   * Functions increase team productivity.


########################## Function Definitions ##############################
# This function prints Hello!
def hello(): # has no parameter / takes no argument
    print("Hello!")
    return # returns None - return statement optional if None returned

# This function prints the value of arg
def print_arg(arg): # has one parameter / takes one argument
    print("The argument is", arg)
    return # optional

# This function returns the sum of x and y
def add_nums(x, y): # has two parameters / takes two arguments
    total = x + y
    return total # returns the sum

# This function prints a date
def print_date(month, day, year):
    print("The date is {}/{}/{}".format(month, day, year))

# This function returns a date string
def return_date(month, day, year):
    return "{}/{}/{}".format(month, day, year)

# This function prints some math
# NOTE: 2 return statements
def print_math(a, b):

    if b == 0:
        print("You cannot divide by 0")
        return
    
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", format(a / b, ".2f"))
    print(a, "%", b, "=", a % b)
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    return

# This function swaps variable values maybe?
def swap_nums(x, y):
    temp = x
    x = y
    y = temp
    print("In swap_nums: x is", x, "y is", y)

# This functions gets a name and email address
def get_input():
    hello()
    name = input("Enter name: ")
    address = input("Enter email: ")
    return name, address

# Nested functions
def nested():
    print("Start of nested")
    n, a = get_input()
    print("Thank you", n)
    print("Your email has been updated.")

# This function calculates the sum of 1 to n
def sum_to(n):
    
    total = 0
    
    for i in range(1, n + 1):
        total += i

    return total


########################## Function Calls ##############################
# Calling the hello function
# Invoking the hello function
# This is a function call
hello()

input("\nPress Enter to continue")

# Calling the hello function in a loop
for _ in range(2):
    hello()

input("\nPress Enter to continue")

# print_arg calls
print_arg(1)

input("\nPress Enter to continue")

print_arg(2.0)
print_arg("three")

x = "a string"
print_arg(x)

input("\nPress Enter to continue")

for i in range(2):
    print_arg(i)
    
input("\nPress Enter to continue")

returnValue = add_nums(2, 3)
print("The sum is", returnValue)

input("\nPress Enter to continue")

a = 99
b = 1

returnValue = add_nums(a, b)
print("The sum is", returnValue)

input("\nPress Enter to continue")

print("The sum is", add_nums(8, 5))
print("The sum is", add_nums("Hello, ", "World!"))

input("\nPress Enter to continue")

print_date(3, 8, 2022)

input("\nPress Enter to continue")

print("The date is", return_date(3, 8, 2022))

input("\nPress Enter to continue")

print_math(5, 4)

input("\nPress Enter to continue")

print_math(2, 0)

input("\nPress Enter to continue")

x = 1
y = 2

print("Outside swap_nums: x is", x, "y is", y)

swap_nums(x, y)

print("Outside swap_nums: x is", x, "y is", y)

input("\nPress Enter to continue")

# Easy swap with Python

x = 1
y = 2

print("Before reordering: x is", x, "y is", y)

x, y = y, x # tuple assignment

print("After reordering: x is", x, "y is", y)

input("\nPress Enter to continue")

n, a = get_input()

# name is not a valid variable here
# print("The name entered is", name)
print("The name entered is", n)
print("The email entered is", a)

input("\nPress Enter to continue")

nested()

input("\nPress Enter to continue")

returnValue = sum_to(10)

print("The sum from 1 to 10 is", returnValue)

x = 100

print("The sum from 1 to {} is {}".format(x, sum_to(x)))
