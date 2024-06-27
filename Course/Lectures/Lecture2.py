"""This program demonstrates some basic python features"""
# The line above creates a module docstring. This string can be accessed
# via the __doc__ variable. This is a triple quote string and is most commonly
# used to create docstrings and multi-line "comments"

print(__doc__)

input("\nPress Enter to continue...")

# print average of the first 5 positive numbers
average = (1 + 2 + 3 + 4 + 5) / 5

print("The average is", average)

input("\nPress Enter to continue...")

# print the average of 3 ages
age1 = 23
age2 = 19
age3 = 31

ave_age = (age1 + age2 + age3) / 3

print("\nThe average age is", format(ave_age, ".1f"))

input("\nPress Enter to continue...")

# print the number of times 7 goes into 20
# and the remainder when 20 is divided by 7
numerator = 20
denominator = 7

quotient = numerator // denominator
remainder = numerator % denominator

print()
print(denominator, "goes into", numerator, quotient, "times")
print("The remainder when", numerator, "is divided by",
      denominator, "is", remainder)
      
input("\nPress Enter to continue...")

# print 2 to the 10th, 100th, 1000th, and 10000th power
base = 2
exponent1 = 10
exponent2 = 100
exponent3 = 1000
exponent4 = 10000

# operations in print
print()
print(base, "^", exponent1, " = ", base ** exponent1, sep="")
print(base, "^", exponent2, " = ", base ** exponent2, sep="")
print(base, "^", exponent3, " = ", base ** exponent3, sep="")
print(base, "^", exponent4, " = ", base ** exponent4, sep="")

input("\nPress Enter to continue...")

# prompt user for a side of a square, print area
side_str = input("\nEnter the side of a square: ") # get side
side = float(side_str)

area = side ** 2 # calculate area

print("\nThe area of the square is", format(area, ".2f")) # print area

input("\nPress Enter to continue...")

# prompt user for 3 numbers, print average (2 ways)
# new use of format (format method)
num1 = int(input("\nEnter an int: ")) # prompt and convert at the same time
num2 = int(input("Enter an int: "))
num3 = int(input("Enter an int: "))

average = (num1 + num2 + num3) / 3

# the arguments of format replace the {} in order
statement = ("\nThe average of {}, {}, and {} is {:.2f}".
             format(num1, num2, num3, average))
print(statement)

# What changes to the program above are needed to allow the user to type floats?

input("\nPress Enter to continue...")

# playing with the format method
num1 = 1
num2 = 2
num3 = 3000000

# These two lines are the same
# The second line explicitly lists the index 
print("\n{}   {}   {}".format(num1, num2, num3))

input("\nPress Enter to continue...")

print("\n{0}   {1}   {2}".format(num1, num2, num3))

input("\nPress Enter to continue...")

# You can switch the order and repeat when including index
print("\n{1}   {2}   {0} : {0}   {2}   {1}".format(num1, num2, num3))

input("\nPress Enter to continue...")

# You can use all the same formatting shown before.
# Default justification is right.
# Field width is the minimum field width - does not restrict output.
# Pad with 0 in a field width of 10, display as standard float with
# 2 digits after decimal point.
# Pad with #, right-justified in a field width of 15 (integer only).
# Pad with space, in a field width of 10, show comma and display as standard
# float with 2 digits after point.
print("\n<{:010.2f}>   <{:#>15d}>   <{:10,.2f}>".format(num1, num2, num3))

input("\nPress Enter to continue...")

print("\n<{0:_<10.2f}>   <{1:0<15d}>   <{2:<10,.2f}>".format(num1, num2, num3))

input("\nPress Enter to continue...")

print("\n<{0:_^10.2f}>   <{1:0^15d}>   <{2:^10,.2f}>".format(num1, num2, num3))

input("\nPress Enter to continue...")

# A new data type - bool (True or False)
T = True
F = False

num1 = 5 + T
num2 = 5 + F

print("\nnum1 is {} and num2 is {}".format(num1, num2))

input("\nPress Enter to continue...")

# Quick relational operator intro
boolVal = 10 > 1
print("\n10 > 1 is", boolVal)

input("\nPress Enter to continue...")

boolVal = 10 < 1
print("\n10 < 1 is", boolVal)

input("\nPress Enter to continue...")

boolVal = 10 >= 1
print("\n10 \u2265 1 is", boolVal)

input("\nPress Enter to continue...")

boolVal = 10 <= 1
print("\n10 \u2264 1 is", boolVal)

input("\nPress Enter to continue...")

boolVal = 10 == 1
print("\n10 = 1 is", boolVal)

input("\nPress Enter to continue...")

boolVal = 10 != 1
print("\n10 \u2260 1 is", boolVal)

input("\nPress Enter to continue...")

#Quick if else intro
if 10 > 1:
    print("\n10 is greater than 1")

input("\nPress Enter to continue...")

if 10 < 1:
    print("\n10 is less than 1")

input("\nPress Enter to continue...")

num = int(input("\nEnter an int: "))

# Only one suite (if or else) will execute
if num > 10:
    print(num, "is greater than 10")
else:
    print(num, "is less than or equal to 10")
    
input("\nPress Enter to continue...")

num = int(input("\nEnter an int: "))

# Only one suite (if, elif, or else) will execute
if num > 10:
    print(num, "is greater than 10")
elif num < 10:
    print(num, "is less than 10")
else:
    print(num, "is 10")
