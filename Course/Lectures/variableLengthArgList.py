# Functions can also be defined to take a variable number
# of arguments, or variable length argument list
# The asterisk designates variable length positional
# argument list
# Inside the function args is a tuple
def variable_args(*args):
    print(args)
    for item in args:
      print(item)
      
variable_args("Python", "Spam", "Flying Circus", 1, 2, 3, 4)

input("\nPress Enter to continue...")
      
def sum_them_up(*args):
    total = 0
    for num in args:
      total += num
    return total
    

print("The sum is", sum_them_up(1, 2, 3, 4, 5))

input("\nPress Enter to continue...")
    
print("The sum is", sum_them_up(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

input("\nPress Enter to continue...")

print("The sum is", sum_them_up())

input("\nPress Enter to continue...")

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print("The sum is", sum_them_up(tup))

# Unpacking collections

print("The sum is", sum_them_up(*tup))

input("\nPress Enter to continue...")

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("The sum is", sum_them_up(*lis))

input("\nPress Enter to continue...")

a, b, c, *d = tup

print(a, b, c)
print(d)
