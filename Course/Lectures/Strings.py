# A string is a sequence of characters.

# A sequence is a special kind of collection
# type in Python.

# A sequence type has its collection of objects
# organized in some order.

hello_str = "Hello"

# index:        0 1 2 3 4
# character:    H e l l o

# We can access, or get, individual characters using
# square brackets 

print(hello_str[0])

input("\nPress Enter to continue")

print(hello_str[1])
print(hello_str[3])

input("\nPress Enter to continue")

# A negative index starts at the end of the string
# index:        -5  -4  -3  -2  -1
# character:     H   e   l   l   o
print(hello_str[-1])
print(hello_str[-5])

input("\nPress Enter to continue")

# print(hello_str[5]) # error - index out of range

# Strings are immutable. This means they cannot be changed.

# hello_str[0] = "J" # error item assignment not allowed

# String Slicing - constructing
# substrings - a sequence of characters within a string

# substring from index 1 to 4, but not including 4
print(hello_str[1:4])

input("\nPress Enter to continue")

# substring from index 1 to end of string
print(hello_str[1:])

# substring from index beginning of string to index 2 (2 not included)
print(hello_str[:2])

input("\nPress Enter to continue")

# substring from index 1 to -1 (-1 not included)
print(hello_str[1:-1])

input("\nPress Enter to continue")

# substring from index beginning to end of string with step 2
print(hello_str[::2])

input("\nPress Enter to continue")

# reverse a string - end to beginning of string 
print(hello_str[::-1])

input("\nPress Enter to continue")

# if the slice start index comes after the end index
# the slice will be empty
print("*" * 10)
print(hello_str[3:0])
print("*" * 10)

input("\nPress Enter to continue")

# len(string) - returns the number of characters in string

print(len(hello_str))

input("\nPress Enter to continue")

# Strings are iterable

for char in hello_str:
    print(char)

input("\nPress Enter to continue")

# range(len(hello_str)) = 0, 1, 2, 3, 4
for i in range(len(hello_str)):
    print("hello_str[{}] = {}".format(i, hello_str[i]))
    
input("\nPress Enter to continue")

# enumerate returns index, value pairs
for i, char in enumerate(hello_str):
    print("hello_str[{}] = {}".format(i, char))

input("\nPress Enter to continue")

# Concatenation - augmented assignment
hello_str += " "

# String multiplication - augmented assignment
hello_str *= 3

print(hello_str)

input("\nPress Enter to continue")

zip_code = 92618

# construct a string
zip_code = str(zip_code)

print("Irvine, CA " + zip_code)
