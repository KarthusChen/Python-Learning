# Sets are used for storing collections of elements.
# Unlike the other collection types we have discussed, 
# the elements are stored in no specific order and do not
# contain duplicate elements.

# Sets are mutable but the elements in the set must be immutable.
# They are enclosed within curly brackets (braces).

myFirstSet = {1, ("a", 1), 3.14, "test", False, None, 0}

print(myFirstSet)

input("\nPress Enter to continue.")

#############################################################

# constructing an empty set
set1 = set()

print(set1)

# set1 = {} # this constructs an empty dictionary

input("\nPress Enter to continue.")

#############################################################

# constructing sets with lists
set2 = set([1, 2, 3])

print(set2)

input("\nPress Enter to continue.")

#############################################################

# constructing sets with tuples
set3 = set((3, 4, 5, 5))

print(set3)

input("\nPress Enter to continue.")

#############################################################

# constructing sets with strings
set4 = set("Aabbc")

print(set4)

input("\nPress Enter to continue.")

#############################################################

# constructing lists with sets
list1 = list(myFirstSet)

print(list1)

input("\nPress Enter to continue.")

#############################################################

# constructing tuples with sets
tup1 = tuple(myFirstSet)

print(tup1)

input("\nPress Enter to continue.")

#############################################################

# The in operator works with sets
if "test" in myFirstSet:
    print("test was found")
    
input("\nPress Enter to continue.")

# elements are collections so we can use a for loop to
# iterate the set
for element in myFirstSet:
    print(element)

input("\nPress Enter to continue.")

#############################################################

# print(set1[1]) # indexing is not allowed - There is no order

# Add element
set4.add("z")

print(set4)

# Removes element - does nothing if not found
set4.discard("b")

print(set4)

input("\nPress Enter to continue.")

# Removes element - raises error if not found
set4.remove("A")

print(set4)

input("\nPress Enter to continue.")

# Removes an arbitrary element - raises error if empty
set4.pop()

print(set4)

input("\nPress Enter to continue.")

#############################################################

# Mutable types and assignment - What happens?
set5 = set2

set5.add(4)

print(set5)
print(set2)

set5.remove(4)

input("\nPress Enter to continue.")

print(set5)
print(set2)

input("\nPress Enter to continue.")

#############################################################
    
a = {1, 2, 3}
b = {3, 4, 5}

# intersection operator
# return elements common to both sets
print(a & b) # &= to modify a

input("\nPress Enter to continue.")

# union operator
# return elements in both sets
print(a | b) # |= to modify a

input("\nPress Enter to continue.")

# difference operator
# return elements in set a that are not in set b
print(a - b) # -= to modify a

input("\nPress Enter to continue.")

# symmetric difference operator
# return elements in set a and set b, but not in both
print(a ^ b) # ^= to modify a

input("\nPress Enter to continue.")

#############################################################

c = {1, 2, 3, 4, 5}
d = {1, 2, 3}

# Does set a and set d have the same elements?
print(a == d)

input("\nPress Enter to continue.")

# Are there elements in one set that are not in the other?
print(a != c)

input("\nPress Enter to continue.")

# Checking for subset/proper subset

# Are all elements in set a also in set c?
print(a <= c)

input("\nPress Enter to continue.")

# Are all elements in set a also in set c?
# set a CANNOT equal set c
print(a < c)

input("\nPress Enter to continue.")

# Are all elements in set a also in set d?
print(a <= d)

input("\nPress Enter to continue.")

# Are all elements in set a also in set d?
# set a CANNOT equal set d
print(a < d)

input("\nPress Enter to continue.")

# Checking for superset/proper superset

# Does set c contain all the elements in set a?
print(c >= a)

input("\nPress Enter to continue.")

# Does set c contain all the elements in set a?
# set a CANNOT equal set c
print(c > a)

input("\nPress Enter to continue.")

# Does set d contain all the elements in set a?
print(d >= a)

input("\nPress Enter to continue.")

# Does set d contain all the elements in set a?
# set a CANNOT equal set d
print(d > a)
