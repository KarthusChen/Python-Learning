a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

print(a)
print(b)

input("\nPress Enter to continue")

print(a[0])

print(b[-1])

input("\nPress Enter to continue")

# tuples are immutable - cannot change
# a[1] = 100 # item assignment not allowed

print(a[1:])
print(b[:-1])

input("\nPress Enter to continue")

c = a + b

print(c)
print(len(c))

input("\nPress Enter to continue")

# single element tuple?
x = (1)

print(type(x))

input("\nPress Enter to continue")

y = (1,)

print(type(y))

input("\nPress Enter to continue")

for item in a:
    print(item)

input("\nPress Enter to continue")

if 8 in b:
    print(8, "is in", b)

input("\nPress Enter to continue")

if 10 not in b:
    print(10, "is not in", b)

input("\nPress Enter to continue")

print(a.count(1))

input("\nPress Enter to continue")

if 1 in a:
    print(1, "is at index", a.index(1))
