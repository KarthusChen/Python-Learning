class NegativeIntegerError(ValueError):
    pass

try:
    num=int(input("Enter a non-negative number:"))
    if num<0:
        raise NegativeIntegerError
except NegativeIntegerError as NIE:
    print("NegativeIntegerError:",NIE)
except ValueError:
    print("You didn't enter a valid Integer.")
