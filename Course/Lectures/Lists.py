# A list is a sequence of elements

# A sequence is a special kind of collection
# type in Python.

# A sequence type has its collection of objects
# organized in some order.

# The elements can be of any data type and elements
# in a list do not have to be the same data type

# index:     0  1  2  3  4  5
even_nums = [0, 2, 4, 6, 8, 10]

# index:  0       1        2
names = ["Mary", "Aimen", "Lynn"]

mixed = ["Kim", 10, 2.718281828459045]

items = ["string",
         1,
         2.36548,
         [1, 2, 3]]

# We can access, or get, individual elements using
# square brackets

print(even_nums[3])

input("\nPress Enter to continue")

print(names[2])

print(mixed[-2])

input("\nPress Enter to continue")

# print(mixed[3]) # error index out of range

# elements of nested structures can be accessed by multiple
# index operations - indexing operations associate left to right
print(items[3])
print(items[3][1])

input("\nPress Enter to continue")

# Lists, UNLIKE strings, are mutable. They can be changed.

# print the entire list at one time
print(mixed)

input("\nPress Enter to continue")

# changing element at index 1
mixed[1] = 11

print(mixed)

input("\nPress Enter to continue")

print(names)

input("\nPress Enter to continue")

# changing element at index -1
names[-1] = "Tim"

print(names)

input("\nPress Enter to continue")

# list slicing - same idea as string slicing

# sublist of elements from index 1 to 4 (not including 4)
print(even_nums[1:4])

input("\nPress Enter to continue")

# sublist of elements from index 1 to end of list
print(even_nums[1:])

# sublist of elements from beginning of list to index 4 (not including 4)
print(even_nums[:4])

input("\nPress Enter to continue")

# sublist of elements from ?
print(even_nums[1:-2])

input("\nPress Enter to continue")

# will not fail - 
# "Out of Bounds" slice indices default to beginning (0) 
# and end (len(even_nums))
print(even_nums[-100:100])

input("\nPress Enter to continue")

# sublist of elements from ?
print(even_nums[::2])

input("\nPress Enter to continue")

# sublist of elements from ?
print(even_nums[::-1])

input("\nPress Enter to continue")

# sublist of elements from ?
print(even_nums[4:0:-2])

input("\nPress Enter to continue")

print(items[3][1:])

# You can also use list slices in assignment
# We will not discuss it here

input("\nPress Enter to continue")

# lists are iterable collections

for element in even_nums:
    print(element)

input("\nPress Enter to continue")

for i in range(len(names)):
    print("names[{}] = {}".format(i, names[i]))

input("\nPress Enter to continue")

for i, elem in enumerate(names):
    print("names[{}] = {}".format(i, elem))

input("\nPress Enter to continue")

# Adding lists - add elements on right side of
# operand to end of list on left side of operand
even_nums = even_nums + [12, 14, 16, 18, 20]

print(even_nums)

input("\nPress Enter to continue")

# Augmented assignment with lists (+)
even_nums += [22]

print(even_nums)

input("\nPress Enter to continue")

# even_nums += 22 # Needs to be iterable object, like list extend method

zeros = [0] * 5

# What do you think?
print(zeros)

input("\nPress Enter to continue")

# Augmented assignment with lists (*)
zeros *= 2

print(zeros)

input("\nPress Enter to continue")

# The list constructor function takes 0 to 1 arguments.
# The argument must be iterable

# construct an empty list
lst1 = list()
lst2 = []

print(lst1)
print(lst2)

input("\nPress Enter to continue")

# construct a list with the given elements
lst1 = list("test")

print(lst1)

input("\nPress Enter to continue")

# lst2 = list(22) # error - int not iterable

# Here a few of things to pay attention to
# when dealing with mutable objects
a = [1, 2, 3]

b = a

print(a)
print(b)

input("\nPress Enter to continue")

# deleting an element
del b[2]

print(a)
print(b)

input("\nPress Enter to continue")

a = [1, 2, 3]

b = list(a) # a[:]

print(a)
print(b)

input("\nPress Enter to continue")

# deleting an element
del b[2]

print(a)
print(b)
