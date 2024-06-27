# This program first prompts for input, a name and monthly salary. It then
# calculates the yearly salary. Finally, it prints the name and yearly salary.

# input
# The input function will write the prompt to the shell and wait for the user to
# type something and then press enter. Everything typed before the enter is
# stored in the assigned variable as a string.
name = input("Enter name: ")
# The float function converts a string to a floating-point number.
month_salary = float(input("Enter monthly salary: "))

# calculation
year_salary = month_salary * 12

# output
print("Name:", name, "\nYearly Salary:", year_salary)

# The line of code below writes the prompt to the shell and waits for the user
# to type enter. We do not assign the typed input to a variable. This will cause
# the program to pause.
input("\nPress Enter to continue...")

# The code below shows some behavior of the print function.
print("\nThis is a super long string.\n"
      "I don't want to continue writing on the same line "
      "so I can break the string into smaller strings.\n"
      "print will automagically make this one string.")

input("\nPress Enter to continue...")

# A small introduction to operators and more print function options.
num = 5

print("\nThe value of num is", num, end=".\n")

input("\nPress Enter to continue...")

print("\n2 times num squared plus one is ", 2 * num ** 2 + 1, ".", sep="")

input("\nPress Enter to continue...")

# The only prints a newline since there are no arguments
print()

print("Hip, " * 2 + "Hurray!")


