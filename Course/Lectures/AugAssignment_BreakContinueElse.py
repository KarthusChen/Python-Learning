# Augmented assignment
# A more compact way to assign
# a result of a binary operation

# Regular algebraic operators
# **, *, /, %, //, +, -

# Augmented algebraic assignment
# **=, *=, /=, %=, //=, +=, -=

x = 1
y = 2
z = 3

x = x + 1
print(x)

input("Press enter to continue...")

# adds the value on the right, 1, to the 
# value of the variable on the left, x = 2, and
# assigns the result to the variable on
# the left, x

x += 1 # x = x + 1
print(x)

input("Press enter to continue...")

x += y # x = x + y
print(x)

input("Press enter to continue...")

x -= z # x = x - z
print(x)

input("Press enter to continue...")

x *= y # x = x * y
print(x)

input("Press enter to continue...")

x *= (z % y + 1) # x = x * (z % y + 1)
print(x)

input("Press enter to continue...")

#############################################

i = 0

while i < 10:
    print(i)

    if i == 7:
        # break will cause execution to exit the
        # loop immediately
        break 
        
    i = i + 1

input("Press enter to continue...")

###############################################

i = 0

while i < 10:

    i = i + 1

    if i == 7:
        # continue will cause the execution to
        # return to the while header immediately
        continue

    print(i)

input("Press enter to continue...")

#############################################

# the else suite executes if the exit of the loop
# is caused by a false condition
# the else suite does not execute if a break statement is
# reached

val = 0

while val != -999:
    val = int(input("Enter an int (-999 to quit): "))
    print(val)
else:
    print("This statement will always run")


#############################################

while True:
    val = input("Enter a word (q to quit): ")
    
    if val == "q":
        break
      
    print(val)
else:
    print("This statement will never run")


############################################

print("This program calculates the average of 10 numbers.")

count = 0
total = 0

while count < 10:
    val = int(input("Enter an int (-999 to quit): "))

    if val == -999:
        print("You did not enter 10 numbers.")
        break

    total += val
    count += 1
else:
    average = total / 10
    print("\nThe average of the 10 numbers entered is", average)
