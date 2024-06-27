"""
This program introduces the list and tuple types.
These are both built-in collection types.
"""
print(__doc__)

numbers = [1, 2, 3, 4, 5]

print(numbers)

input("\nPress Enter to continue...")
print()

print(numbers[2])

input("\nPress Enter to continue...")
print()

if 3 in numbers:
    print("3 is found")

input("\nPress Enter to continue...")
print()

if 10 not in numbers:
    print("10 was not found")

input("\nPress Enter to continue...")
print()

words = ["programming", "fun", "python", "is"]

print(words[2], words[0], words[3], words[1])

input("\nPress Enter to continue...")
print()

# add the numbers in the list
print(sum(numbers))

input("\nPress Enter to continue...")
print()

# find the largest number
print(max(numbers))

input("\nPress Enter to continue...")
print()

# find the smallest number
print(min(numbers))

input("\nPress Enter to continue...")
print()

numbers[0] = 0

# add the numbers in the list
print(sum(numbers))

input("\nPress Enter to continue...")
print()

# find the largest number
print(max(numbers))

input("\nPress Enter to continue...")
print()

# find the smallest number
print(min(numbers))

input("\nPress Enter to continue...")
print()

numbers_tuple = (1, 2, 3, 4, 5)

print(numbers_tuple)

input("\nPress Enter to continue...")
print()

print(numbers_tuple[2])

input("\nPress Enter to continue...")
print()

if 3 in numbers_tuple:
    print("3 is found")

input("\nPress Enter to continue...")
print()

if 10 not in numbers_tuple:
    print("10 was not found")

input("\nPress Enter to continue...")
print()

# add the numbers in the list
print(sum(numbers_tuple))

input("\nPress Enter to continue...")
print()

# find the largest number
print(max(numbers_tuple))

input("\nPress Enter to continue...")
print()

# find the smallest number
print(min(numbers_tuple))

# numbers_tuple[0] = 0
