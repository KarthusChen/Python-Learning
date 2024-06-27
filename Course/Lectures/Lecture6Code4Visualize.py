# Function Definitions
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


# Function Calls
# Calling the hello function
# Invoking the hello function
# This is a function call
hello()

# Calling the hello function in a loop
for _ in range(2):
    hello()

# print_arg calls
print_arg(1)

print_arg(2.0)
print_arg("three")

x = "a string"
print_arg(x)

for i in range(2):
    print_arg(i)

returnValue = add_nums(2, 3)
print("The sum is", returnValue)

a = 99
b = 1

returnValue = add_nums(a, b)
print("The sum is", returnValue)

print("The sum is", add_nums(8, 5))
print("The sum is", add_nums("Hello, ", "World!"))

print_date(3, 8, 2022)

print("The date is", return_date(3, 8, 2022))

print_math(5, 4)

print_math(2, 0)

x = 1
y = 2

print("Outside swap_nums: x is", x, "y is", y)

swap_nums(x, y)

print("Outside swap_nums: x is", x, "y is", y)

# Easy swap with Python

x = 1
y = 2

print("Before reordering: x is", x, "y is", y)

x, y = y, x # tuple assignment

print("After reordering: x is", x, "y is", y)

n, a = get_input()

# name is not a valid variable here
# print("The name entered is", name)
print("The name entered is", n)
print("The email entered is", a)

nested()

returnValue = sum_to(10)

print("The sum from 1 to 10 is", returnValue)

x = 100

print("The sum from 1 to {} is {}".format(x, sum_to(x)))
