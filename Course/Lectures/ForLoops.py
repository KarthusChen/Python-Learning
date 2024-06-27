"""
This program introduces for loops.
"""

# for loops are used to repeat statements by
# iterating a collection - repeat statements
# for every element in a collection

# for <element> in <collection>:
#     <statements>

# The variable name chosen for element does
# not have to be defined before the for header.
# It represents the current element in the collection.

chars = input("Enter a string: ")

for char in chars:
    print(char)

input("Press enter to continue...")

# This is a Python list - another collection type
# These will be discussed in detail later

for number in [1, 2, 3, 4, 5]:
    print(number)

input("Press enter to continue...")

for number in range(10):
    print(number)

input("Press enter to continue...")

# range returns a sequence of numbers

# range(10):            0, 1, 2, ... , 9
# range(1, 10):         1, 2, 3, ... , 9
# range(10, 100, 10):   10, 20, 30, ... , 90
# range(10, 0, -1):     10, 9, 8, ... , 1

for number in range(1, 6):
    print(number)

input("Press enter to continue...")

for number in range(5):
    print(number + 1)

input("Press enter to continue...")

for number in range(10, 100, 10):
    print(number)

input("Press enter to continue...")

for number in range(10, 0, -1):
    print(number)

input("Press enter to continue...")

import random

for _ in range(5):
    print(random.randint(1, 10), end=" ")

print()

####################################################

num = int(input("Enter an int: "))

print("\nNumber\tSquare")

for i in range(num):
    print(i + 1, (i + 1) ** 2, sep="\t")

input("Press enter to continue...")

for word in ["Python", "dog", "triangle"]:
    # the len function returns the number of characters in a collection
    print(word * len(word))

# break and continue work the same in for loops
# For loops can also have an else suite.
