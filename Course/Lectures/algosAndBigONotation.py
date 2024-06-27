# An algorithm is a detailed sequence of steps for solving
# a problem.

# There are different algorithms that solve the same problem.

# Here are four different solutions to Homework 8

def makeStr1(string1, string2):
    for char in string2:
        if char not in string1:
            print("No")
            return
    print("Yes")

def makeStr2(string1, string2):
    count = 0
    for char in string2:
        if char in string1:
            count += 1
            
    if count == len(string2):
        print("Yes")
    else:
        print("No")
    
def makeStr3(string1, string2):
    print("No" if string2.strip(string1) else "Yes")
    
def makeStr4(string1, string2):
    print("Yes" if set(string2) <= set(string1) else "No")
    
str1 = "hello"
str2 = ""
str3 = "heleoeleoeheleheheheloeoooeoel"
str4 = "heleoeleoehehetleoe"

makeStr1(str1, str2)
makeStr1(str1, str3)
makeStr1(str1, str4)

input("\nPress Enter to continue...")

makeStr2(str1, str2)
makeStr2(str1, str3)
makeStr2(str1, str4)

input("\nPress Enter to continue...")

makeStr3(str1, str2)
makeStr3(str1, str3)
makeStr3(str1, str4)

input("\nPress Enter to continue...")

makeStr4(str1, str2)
makeStr4(str1, str3)
makeStr4(str1, str4)

input("\nPress Enter to continue...")

# Computer scientists have identified ways to compare
# algorithms that solve the same problem and state which
# are better.

# One of the ways to compare an algorithm is "time".
# Time is identified as how many "steps" are required
# to complete an algorithm

# One of the notations used is Big-O notation O().
# It identifies how algorithm is affected by input size.
# How much slower will an algorithm be as input gets large?

# O(1) - Constant running time
# Dictionaries - They use a hashtable to locate an element (key)
# Hashtables use a function to identify where elements should be
# stored. To find an element, we run the function with the input
# we are searching for, and search where it should be stored.
# If we find it there or not, we are done.

# O(log n) - Logarithmic running time
n = 100
count = 0
while n > 0:
    n = n // 2
    count += 1

print(count)

input("\nPress Enter to continue...")

# O(n) - Linear running time
n = 100
count = 0
while n > 0:
    n -= 1
    count += 1

print(count)

input("\nPress Enter to continue...")

# O(n log n) - Linearithmic running time
# The outer loop executes log n times. The inner loop executes n times.
# The complexity (how many times the statement(s) in the inner loop run)
# is found by multiplying n by log n, n * log n.
n = 100
count = 0
while n > 0:
    n = n // 2
    for i in range(100):
        count += 1

print(count)

input("\nPress Enter to continue...")

# O(n^2) - Quadratic running time
# The outer loop executes n times. The inner loop executes n times.
# The complexity (how many times the statement(s) in the inner loop run)
# is found by multiplying n by n, n * n = n^2.
n = 100
count = 0
for i in range(n):
    for j in range(n):
        count += 1

print(count)

# O(2^n) - Exponential running time
# O(n!) - Factorial running time

# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

# Sites that show how common algorithms work visually (code included)
# https://www.toptal.com/developers/sorting-algorithms
# https://visualgo.net/en/sorting

# Time and space complexity cheat sheet for sorting algorithms
# https://www.bigocheatsheet.com/
