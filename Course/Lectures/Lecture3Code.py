"""
This program goes over some simple instructional examples 
of if/elif/else selection structure.
"""
# The string above is an example of a module docstring. It is not
# a comment. It is stored in a variable named __doc__ that can be 
# accessed by your program.
print(__doc__)

print(("Hello " * 3 + "\n") * 10)

input("Press Enter to continue...")

# This program prompts the user for 3 test scores.
# The average is calculated and the corresponding letter
# grade is printed out.

# input
test1 = int(input("\nEnter test score 1: "))
test2 = int(input("Enter test score 2: "))
test3 = int(input("Enter test score 3: "))

# calculations
avg = (test1 + test2 + test3) / 3

# every condition will be checked because these are all
# if statements - separate structures
# output
if avg >= 90:
    print("The average is an A")
if 80 <= avg < 90:
    print("The average is a B")
if 70 <= avg < 80:
    print("The average is a C")
if 60 <= avg < 70:
    print("The average is a D")
if 0 <= avg < 60:
    print("The average is an F")
if avg < 0:
    print("Input Error")

input("\nPress Enter to continue...")

# input
test1 = int(input("\nEnter test score 1: "))
test2 = int(input("Enter test score 2: "))
test3 = int(input("Enter test score 3: "))

# calculations
avg = (test1 + test2 + test3) / 3

# output
if avg >= 90:
    print("The average is an A")
if avg >= 80 and avg < 90:
    print("The average is an B")
if avg >= 70 and avg < 80:
    print("The average is an C")
if avg >= 60 and avg < 70:
    print("The average is an D")
if avg >= 0 and avg < 60:
    print("The average is an F")
if avg < 0:
    print("Input Error")

input("\nPress Enter to continue...")

# input
test1 = int(input("\nEnter test score 1: "))
test2 = int(input("Enter test score 2: "))
test3 = int(input("Enter test score 3: "))

# calculations
avg = (test1 + test2 + test3) / 3

# output
if avg >= 90:
    print("The average is an A")
elif avg >= 80:
    print("The average is a B")
elif avg >= 70:
    print("The average is a C")
elif avg >= 60:
    print("The average is a D")
elif avg >= 0:
    print("The average is an F")
else:
    print("Input Error")

input("\nPress Enter to continue...")

# This program prompts for an age and prints
# privileges attained
age = int(input("\nEnter your age: "))

if age < 18:
    print("Enjoy your youth!")

if age >= 18:
    print("You can vote.")
    
if age >= 21:
    print("You can go to a casino.")

if age >= 25:
    print("You can rent a car.")

if age >= 35:
    print("You can run for President.")

if age >= 65:
    print("You get a senior citizen discount")
    print("You can retire")

input("\nPress Enter to continue...")

# This program prompts for a color and identifies it as
# a primary color or not
color = input("\nEnter a color: ")
color = color.lower()

if color == "red" or color == "yellow" or color == "blue":
    print("You entered a primary color.")
else:
    print("That is not a primary color.")

input("\nPress Enter to continue...")

# This program prompts for two ints and identifies if the
# second number entered is divisible by the first
num1 = int(input("\nEnter an int: "))
num2 = int(input("Enter an int: "))

if num2 % num1 == 0:
    print(num2, "is divisible by", num1)
else:
    print(num2, "is not divisible by", num1)

input("\nPress Enter to continue...")

# This program prompts for two words and finds which comes first

word1 = input("\nEnter a word: ")
word2 = input("Enter a word: ")
word1_lower = word1.lower()
word2_lower = word2.lower()

if word1_lower < word2_lower:
    print(word1, "comes before", word2)
elif word1_lower > word2_lower:
    print(word2, "comes before", word1)
else:
    print(word1, "and", word2, "are the same")

input("\nPress Enter to continue...")    

# This program prompts for x and y values of a point and
# determines if the point lies in a circle with radius 8
# centered at the origin

# We need the math library
import math

# input
x = float(input("\nEnter x: "))
y = float(input("Enter y: "))

# calculate distance from origin
d = math.sqrt(x ** 2 + y ** 2)

# print output 
if d < 8:
    print("You hit the dart board!")
else:
    print("Sorry, you missed.")
