# In some programs, errors may occur.
# Up until now we have been writing programs that terminate
# abruptly when an run-time error occurs.
# The program stops and prints an error to the shell.
# This is the default exception handling behavior.
# This is not ideal in some cases. Programs should be able
# to deal with these errors in an elegant manner.

# Examples of built-in exception types
# ------------------------------------------------------------------------
# KeyboardInterrupt  Raised when user hits Ctrl-C, the interrupt key
#
# OverflowError      Raised when a floating-point expression evaluates to 
#                    a value that is too large
#
# ZeroDivisionError  Raised when attempting to divide by zero
#
# OSError            Raised when a system function returns a
#                    system-related error including I/O failures.
#
# IndexError         Raised when a sequence index is outside the range of 
#                    valid indexes
#
# NameError          Raised when attempting to evaluate an unassigned
#                    identifier (name)
#
# TypeError          Raised when an operation or function is applied to an
#                    an object of the wrong type
#
# ValueError         Raised when an operation or function has an argument 
#                    of the right type but incorrect value
# ------------------------------------------------------------------------

# Python provides error-handling abilities via the
# try statement

# Syntax:
# try:
#     <code that can raise an error>
# except:
#     <error handling code>

# Catching any error and printing a generic message

# The try clause should contain the code that may raise an error
try:
    x = y
# The except clause should contain the error handling code
except:
    print("An error occurred.")
    # The info is available via the sys module
    # Normally an exception type should be specified.
    import sys
    print(sys.exc_info())

input('\nPress Enter to continue...')
  
# Catching an error object and printing an error specific message

try:
    x = y
except Exception as e:
    # Note the object e is garbage collected automatically
    # If you need access after the try/except assign it to a variable
    error = e
    print(e)

# print(e)

input('\nPress Enter to continue...')

print(error)

input('\nPress Enter to continue...')

# Catching a ValueError object

val = input("Enter an integer: ")

try:
    number = int(val)
    print("You entered an integer.")
except ValueError as ve:
    print("You did not enter an integer.")
    print(ve)

input('\nPress Enter to continue...')

# Exceptions raised inside nested code (here multiple functon calls),
# will cause the program to skip code after the raised exception unless
# it is nested inside a try/except suite.

def throw_error():
    raise Exception("Exception raised in throw_error()")

def stack2():
    print("In stack2() before calling throw_error()")

    throw_error()

    # this call will not be reached
    print("In stack2() after calling throw_error()")

def stack1():
    print("In stack1() before calling stack2()")

    stack2()

    # this call will not be reached
    print("In stack1() after calling stack2()")

try:
    stack1()
except Exception as e:
    print("In except suite.")
    print(e)

input('\nPress Enter to continue...')

# Defining our own error class
# All classes for error-handling should either directly or
# indirectly inherit from the Exception class
# __str__ is preferred by Python in some contexts. With this
# in mind, implementing __repr__ in a subclass may not work as
# expected if the super class implements an __str__ method

class AgeError(ValueError):
    pass

class NegativeAgeError(AgeError):
    def __str__(self): return "This person has not been born."

class ImpossibleAgeError(AgeError):
    def __str__(self): return "This person is not alive."

MIN_AGE = 0
MAX_AGE = 125

def age(num):
    # Use raise to construct an error object that needs to be
    # handled.
    if num < MIN_AGE:
        raise NegativeAgeError
    elif num > MAX_AGE:
        raise ImpossibleAgeError
    else:
        return num

def test_age():
    val = input("Enter your age: ")

    # Catching a NegativeAgeError, ImpossibleAgeError, AgeError, etc.
    # You can have multiple except clauses.
    # The exception is handled by only 1 except clause, the first match.
    # A NegativeAgeError is-an AgeError.
    # A AgeError is-a ValueError.
    # A ValueError is-an Exception.
    # They should be listed from specific to general.
    try:
        number = int(val)
        valid_age = age(number)
        if input("Throw a NameError? ") == "yes":
            raise NameError("You told the program to throw NameError", val, valid_age)
    except NegativeAgeError as nae:
        print("You did not enter a valid age.")
        print(nae)
    except ImpossibleAgeError as iae:
        print("You did not enter a valid age.")
        print(iae)
    # If we handle errors using a common base type,
    # new exceptions types derived from the same base class
    # can be added and our code will run without being updated.
##    except AgeError as ae:
##        print("You did not enter a valid age.")
##        print(ae)
    except ValueError as ve:
        print("You did not enter an integer.")
        print(ve)
    except Exception as e:
        print("An error occurred.")
        print(e.args)
    else:
        print("A valid age, {}, was entered".format(valid_age))
        print("This code executes if an exception does NOT occur.")
    finally:
        print("This code will always execute")

test_age()

