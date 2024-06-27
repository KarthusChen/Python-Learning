import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)

input("\nPress Enter to continue...")

###############################################################################

# importing string.printable - bringing printable to global namespace
from string import printable

def caesar_encode(text, offset):
    'Super simple caesar cipher code'
    'Printable characters are encoded'
  
    # create empty list to store encoded characters
    char_list = []
    # used for calculating index of encoded character
    printable_len = len(printable)

    # iterate the string, text, that we want to encode
    # go through the string, text, one-by-one and in order
    for char in text:

        # if the character is a prinrable character
        if char in printable:

            # encode it and add it to encoded characters list
            index = printable.find(char)
            char_list.append(printable[(index + offset) % printable_len])

        # otherwise
        else:

            # leave the character as-is and add it to encoded characters list
            char_list.append(char)

    # 
    return ''.join(char_list)


def caesar_encode1(text, offset):
    return ''.join([((printable[(printable.find(char) + offset) % len(printable)]
		if char in printable else char)) for char in text])

# Fake decode
def caesar_decode(text, offset):
    return caesar_encode(text, -offset)
    
def caesar_decode1(text, offset):
    return caesar_encode1(text, -offset)


encoded = caesar_encode('Attack at once', 2)
print(encoded)

input("\nPress Enter to continue...")

encoded1 = caesar_encode1('The answers for the exam are a, b, c, d, or e', 21)
print(encoded1)

input("\nPress Enter to continue...")

decoded = caesar_decode(encoded, 2)
print(decoded)

input("\nPress Enter to continue...")

decoded1 = caesar_decode1(encoded1, 21)
print(decoded1)  
