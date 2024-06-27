# Dictionaries are used to store collections of key, value pairs.
# The key must be an immutable type, just like the elements of sets.
# The value can be of any type. The key is used to "locate" a 
# specific value. They work very much like a real dictionary, where 
# the word is the key and the definition is the value.

# Dictionaries are mutable. Enclose dictionary literals within with braces.
# Keys and values are separated with a colon, and key-value pairs are 
# separated with a comma.

phonebook = {"Person 1": "555-1111", "Person 2": "555-2222", "Person 3": "555-3333"}

print(phonebook)

input("\nPress Enter to continue")

#############################################################

# We can access the value associated with a key
print(phonebook["Person 1"])

input("\nPress Enter to continue")

#############################################################

# We can use the in and not in operator to look for a key in
# a dictionary.
if "Person 1" in phonebook:
    print("Person 1's phone number is", phonebook["Person 1"])

if "Person X" not in phonebook:
    print("Person X is not in the phonebook")

input("\nPress Enter to continue")

#############################################################

# We can easily add key, value pairs using the assignment
# operator
phonebook["Person X"] = "555-4444"

print(phonebook)

input("\nPress Enter to continue")

#############################################################

# The key must be unique - overwrites existing value
phonebook["Person 1"] = "555-5555"

print(phonebook)

input("\nPress Enter to continue")

#############################################################

# Delete a key, value pair
del phonebook["Person 1"]

print(phonebook)

input("\nPress Enter to continue")

#############################################################

# The len() function can be used to find how many pairs are
# in a dictionary.
print("The phonebook has", len(phonebook), "pairs.")

input("\nPress Enter to continue")

#############################################################

# Constructing an empty dictionary
newPhonebook = {}
emptyDictionary = dict()

print(newPhonebook)
print(emptyDictionary)

input("\nPress Enter to continue")

#############################################################

# Iterating a dictionary
for key in phonebook:
    print(key, ": ", phonebook[key], sep="")
    

input("\nPress Enter to continue")

#############################################################

# The get function/method returns the value associated with
# a key. None or the optional second argument is returned if
# the key does not exist.
print(phonebook.get("Person 2"))
print(phonebook.get("Person Y"))    
print(phonebook.get("Person Y", "Not Found"))

input("\nPress Enter to continue")

#############################################################

# keys() returns an iterable object used to access keys
print(phonebook.keys())
print(list(phonebook.keys()))

input("\nPress Enter to continue")

#############################################################

# values() returns an iterable object used to access values
print(phonebook.values())
print(list(phonebook.values()))

input("\nPress Enter to continue")

#############################################################

# items() returns an iterable object used to access key-value pairs
# the first element is the key and the second element is the value
print(phonebook.items())
print(list(phonebook.items()))

input("\nPress Enter to continue")

# Iterating a dictionary   
for key, value in phonebook.items():
    print(key, ": ", value, sep="")

input("\nPress Enter to continue")

#############################################################

# pop(x, y) will remove the pair with key x and return the
# value associated with x. y is returned if x is not found.
phoneNum = phonebook.pop("Person 2", "Not Found")

print(phoneNum)

input("\nPress Enter to continue")

#############################################################

phoneNum = phonebook.pop("Person Y", "Not Found")

print(phoneNum)

input("\nPress Enter to continue")

#############################################################

phonebook["Person 1"] = "555-5555"
phonebook["Person 2"] = "555-1111"

print(phonebook)

input("\nPress Enter to continue")

# popitem() removes and returns an arbitrary key, value pair
# as a tuple - error if empty
key, value = phonebook.popitem()

print(key, ": ", value, sep="")

input("\nPress Enter to continue")

#############################################################

text = '''This is a triple-quote string. We talked about these
          a couple of weeks ago. Formatting is preserved. world
          is is is a a a weeks we we we of of of this hello'''

#################################################################################### 
# Not on any exams                                                                 #
####################################################################################          
import string                                                                      #
                                                                                   #
translationTable = str.maketrans(string.punctuation, " " * len(string.punctuation))#
                                                                                   #
text = text.translate(translationTable)                                            #
####################################################################################

words = text.split()

print(words)

input("\nPress Enter to continue")

wordCounter1 = dict()
wordCounter2 = dict()

# iterate the word list
for word in words:
    # convert word to lower case
    word = word.lower()
    
    # if word in dictionary, increment count
    if word in wordCounter1:
        wordCounter1[word] += 1
        
    # if word not in dictionary, add it with count = 1
    else:
        wordCounter1[word] = 1

    # same as if-else above in one line
    wordCounter2[word] = wordCounter2.get(word, 0) + 1

print(wordCounter1)
print("-" * 100)
print(wordCounter2)
