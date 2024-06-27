"""
This program introduces random numbers and while loops.
"""

# Allows the programmer to use the random module
# The random module includes randint, randrange, random,
# and uniform functions, and many more features.
# This module is not secure. Use secrets if you want secure
# random numbers
import random # allows to access objects using random.
from random import randrange # brings the name randrange to the top level

# generates a random integer from 1 to 6
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print("\ndie1 is", die1)
print("die2 is", die2)

print("sum of die1 and die2 is", die1 + die2)

input("\nPress Enter to continue...")

# generates a random integer from 0 to 5, then we add 1
# NOTE: Because of the way randrange was imported
# we no longer need random. before randrange
die1 = randrange(6) + 1
die2 = randrange(6) + 1
print("\ndie1 is", die1)
print("die2 is", die2)

print("sum of die1 and die2 is", die1 + die2)

input("\nPress Enter to continue...")

# random.randrange(10) -> one number from 0,1,...,9
# random.randrange(1, 10) -> one number from 1,2,...,9
# random.randrange(10, 100, 10) -> one number from 10,20,...,90

print("\nA random number from 13 to 101 (101 not included) with a step of 7:",
      random.randrange(13, 101, 7))

input("\nPress Enter to continue...")

# Notes on random integers (above)
# Order of arguments must make sense
# randint must have smallest number first and largest second (can be equal)
# same idea for randrange
#    - one argument case must be positive integer
#    - two argument case must have smallest number
#      as first argument and largest number as
#      second argument (cannot be equal)
#    - three argument case adding step (third argument)
#      to first argument must move towards second argument

# generating floating-point numbers
# random.random() takes no arguments
random_float = random.random()
print("\nA float in the interval [0, 1):", random_float)
print("A float in the interval [0, 1):", random.random())

input("\nPress Enter to continue...")

# random.uniform() always takes two arguments - left and right bounds
# order doesn't seem to matter
random_float = random.uniform(-1,1)
print("\nA float in the interval [-1, 1):", random_float)
print("A float in the interval [-100, 100):", random.uniform(-100, 100))

input("\nPress Enter to continue...")

# while ######################################################

# Loops are structures that allow the programmer
# to run statements repetitively.
#
# while loops are condition controlled loops
# The statements will repeat until a condition is false.
# In other words, the statements will repeat while the condition is true
# The suite is initially entered only if the condition is true
# The suite must contain statements that cause the condition
# to become false (or a break statement).
# 
# while <condition>:
#     <statements/suite>

# Simple examples

x = 0

while x < 10:
    print(x)
    x = x + 1 

input("\nPress Enter to continue...")
print()

x = 0

while x < 10:
    print(x)
    x = x + 2

input("\nPress Enter to continue...")
print()

x = 10

while x > 0:
    print(x)
    x = x - 1

input("\nPress Enter to continue...")
print()

# Nested loops

tens = 0
ones = 0

while tens < 10:
    while ones < 10:
        print(tens, ones, sep="", end=" ")
        ones = ones + 1
    print()
    tens = tens + 1
    ones = 0

input("\nPress Enter to continue...")
print()

# sentinel controlled loop
# This loop runs until a sentinel value, or flag, is typed
# or, in other words, while val is not the sentinel value

val = int(input("Enter a positive int (-1 to quit): "))

total = 0

while val > 0:
    total = total + val
    val = int(input("Enter a positive int (-1 to quit): "))

print("The sum of the numbers entered is", total)
