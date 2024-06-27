# String methods

# len(s) -- returns the length (the number of items) of string s
# This is a built-in function that can be used with sequences and other
# collection types.

text = "Python programming is cool!"

print("The string '{}' has {} characters".format(text, len(text)))

input("\nPress Enter to continue...")

###############################################################################

word1 = "Hello"
word2 = "World"

wordsLen = len(word1) + len(word2)

print("'{}' and '{}' have a total of {} characters.".format(word1, word2, wordsLen))

input("\nPress Enter to continue...")

###############################################################################


# s.upper() -- returns a copy of the string with all cased characters converted
# to uppercase

print("'{}' can be printed as upper case - '{}'.".format(word1, word1.upper()))

input("\nPress Enter to continue...")

###############################################################################

# s.lower() -- returns a copy of the string with all cased characters converted
# to lowercase

print("'{}' can be printed as lower case - '{}'.".format(word2, word2.lower()))

input("\nPress Enter to continue...")

###############################################################################

# adding extra whitespace

text = "               " + text + "        "

print("text:\n{}".format(text))

input("\nPress Enter to continue...")

###############################################################################

# s.strip() -- returns a copy of the string with leading and trailing  
# whitespace removed
# s.strip(chars) -- returns a copy of the string with leading and trailing  
# chars removed - chars is the "set" of characters to be removed

text = text.strip()

print("text (after removing leading and trailing whitespace):\n{}".format(text))

input("\nPress Enter to continue...")

text = "cscscscssscsc" + text + "cscscsccsXcscsccsccs"

print("text:\n{}".format(text))

input("\nPress Enter to continue...")

text = text.strip("cs")

print("text (after removing leading and trailing c's and s's):\n{}".format(text))

input("\nPress Enter to continue...")

# s.lstrip, s.rstrip

###############################################################################


# s.isalpha() -- returns true if all characters in the string are alphabetic,
# false otherwise

if "abc".isalpha():
  print("abc is composed of alphabet letters")

input("\nPress Enter to continue...")

###############################################################################


# s.isdigit() -- returns true if all characters in the string are numeric,
# false otherwise
  
if "0123456789".isdigit():
  print("0123456789 is composed of digits")

input("\nPress Enter to continue...")

# s.isalnum, s.isdecimal, s.isdigit, s.isidentifier, s.islower, s.isnumeric, 
# s.isprintable, s.isspace, s.istitle, s.isupper

###############################################################################

  
if "p" in text:
  print(text, "contains a p")
  
input("\nPress Enter to continue...")

###############################################################################

if "z" not in text:
  print(text, "does not contain z")
  
input("\nPress Enter to continue...")

###############################################################################

# s.find(sub) -- returns the lowest index in the string where the substring sub 
# is found, -1 if not found - There are optional arguments start and end to  
# reduce the search string to s[start:end]

if text.find("p") != -1:
  print(text, "contains a p")
  print("p is found at index", text.find("p"))
else:
  print(text, "does not contain a p")

input("\nPress Enter to continue...")

if text.find("z") != -1:
  print(text, "contains a z")
  print("z is found at index", text.find("z"))
else:
  print(text, "does not contain a z")

input("\nPress Enter to continue...")

# s.rfind

###############################################################################

# s.index(sub) -- returns the lowest index in the string where the substring  
# sub is found, raises Valuerror if not found - There are optional arguments 
# start and end to reduce the search string to s[start:end]


index = text.index("p")
print("p is found at index", index)

input("\nPress Enter to continue...")

# s.rindex

###############################################################################

print("cool is found at index", text.find("cool"))

input("\nPress Enter to continue...")

###############################################################################

# s.replace(old, new) -- returns a string where all occurrences of old have
# been replaced by new - There is an optional count that restricts replacements
# to the first count occurrences of old

text = text.replace(" ", "|")

print(text)

input("\nPress Enter to continue...")

###############################################################################

text = text.replace("|", " ")

print(text)

input("\nPress Enter to continue...")

###############################################################################

# s.split(delimeter) -- returns a list of substrings separated by the given 
# delimiter. As a convenient special case s.split() (with no arguments) splits 
# on all whitespace chars.
# e.g. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']
# Optional argument of maxsplit can limit the number of splits

wordList = text.split()

print(wordList)

input("\nPress Enter to continue...")

###############################################################################

text = text.replace(" ", "||")

print(text)

input("\nPress Enter to continue...")

wordList = text.split("||")

print(wordList)

input("\nPress Enter to continue...")

###############################################################################

# s.join(iterable) -- opposite of split(), joins the elements in the given  
# iterable together using the string as the delimiter.
# e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

sentence = " ".join(["Hello", "world!", "Python", "programming", "is", "cool"])

print(sentence)

input("\nPress Enter to continue...")

# Other str methods
# s.capitalize, s.casefold, s.center, s.count, s.encode, s.endswith, 
# s.expandtabs, s.format_map, s.ljust, s.maketrans, s.rjust, s.splitlines, 
# s.startswith, s.swapcase, s.title, s.translate

###############################################################################

print(r"This is a raw string\n - Notice no escape sequences")

input("\nPress Enter to continue...")

# shorthand if else

# <expression1> if <condition> else <expression2>

# evaluate to expression1 if condition is True, expression2 otherwise

x = 11
var = "even" if x % 2 == 0 else "odd"
print(var)

input("\nPress Enter to continue...")

# List comprehension

# [<expression> for item in <collection>]

# evaluate expression for each item in the collection

easy_list = [i**2 for i in range(10)]
print(easy_list)
