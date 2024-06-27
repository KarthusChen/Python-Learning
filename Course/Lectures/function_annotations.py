"""
Some examples of function annotations and function docstrings
"""

# Function annotations allow the library writer to communicate expected
# arguments and return types of functions

# num1 and num2 are expected to be an int and float, respectively
# The function annotations_example1 does not return anything (None in Python)
def annotations_example1(num1: int, num2: float) -> None:
    # A function docstring is a string on the first executable line of a function
    "This function prints something" # function docstring
    print("num1: {}\nnum2: {}".format(num1, num2))

# chars is expected to be a str and a tuple is expected for collection
# The function annotations_example2 returns a str (type string)
def annotations_example2(chars: str, collection: (int, int)) -> str:
    "This function returns a string"
    return chars * (collection[0] + collection[1])

# The style of annotations used is decided by the software used to check
# the annotations. Python does not provide this behavior built-in.
def annotations_example3(chars: "a string", collection: tuple) -> object:
    "This function returns a string"
    return chars * (collection[0] + collection[1])

# This condition is True only when the file is run as the
# top-level program. Otherwise, only the functions are imported
# for use when included in an import statement.
if __name__ == "__main__":
    print("-" * 80, "I am in the if __name__ == __main__ part", "-" * 80, sep="\n")

    input("\nPress Enter to continue")

    annotations_example1(1, 1.5)

    input("\nPress Enter to continue")

    print(annotations_example2("hello", (1, 2)))

    input("\nPress Enter to continue")
    
    print(annotations_example3("hello", (5, 10)))
        
    
