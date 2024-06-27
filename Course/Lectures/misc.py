# Another way to get input from the user
print("Enter name: ", end="")
name = input()

print("Hi ", name, ", enter an integer: ", sep="", end="")
num = int(input())

print(name, ", you typed ", num, ". Enter a float: ", sep="", end="")
f = float(input())

print("\nName:", name, "\nInt:", num, "\nFloat:", f)

input("\nPress Enter to continue...")

# Watch out for floats - They are not precise
print(1/3 + 1/2 == 5/6)

input("\nPress Enter to continue...")

import fractions

f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(1, 2)
f3 = fractions.Fraction(5, 6)

print(f1 + f2 == f3)

input("\nPress Enter to continue...")

# Looping using enumerate

shopping_list = ["apples",
                 "bananas",
                 "broccoli",
                 "ice cream",
                 "bread",
                 "peanut butter",]

print("Shopping List")
for order, item in enumerate(shopping_list, start=1):
    print("Item ", order, ": ", item, sep="")

