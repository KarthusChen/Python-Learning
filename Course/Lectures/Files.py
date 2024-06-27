# Text files - data displays as a sequence of characters
# Text files can be opened with text editor and data is presented 
# in a human-readable format.

# Binary files (not covered) - data stored as a sequence of bytes
# Binary files can be opened with a text editor but are not
# encoded so data is often not human-readable.

# 3 steps to file processing: open file, process file, close file
# open file
myFirstFile = open("aTextFile.txt", "w")

# process file
myFirstFile.write("Hello File\t")
# myFirstFile.write(3) # only strings allowed
myFirstFile.write("3")

# close file
myFirstFile.close()

input('Press any key to continue...')

# Python File Modes
# 
# "r" - open file for reading (default)
#       error if file does not exist
#
# "w" - open file for writing 
#       if the file exists, erase content
#       if the file does not exist, create file
#
# "a" - open file for appending
#       if the file exists, put "cursor" at end of file
#       if the file does not exist, create file
#
# "+" - allows both reading and writing 
# "r+", "w+", "a+" - open file for reading and writing
#
# "b" - open file in binary mode
# "rb", "wb", "ab" - open file for reading, writing, or appending
#                    in binary mode

##########################################################################

# f.write(s) - Write a string to the file

# f.writelines(lst) - Write a list (or iterable sequence of strings) to the file.
# Line separators are not added

# f.read(n=-1) - Read and return n characters from the file.
#                If negative or omitted read and return the entire file.

# f.readline() - Read and return one line from the file.

# f.readlines() - Read and return a list of lines from the file.

##########################################################################

cities = ["New York\n", "Boston\n", "Irvine\n"]
outfile = open("cities.txt", "w")
outfile.writelines(cities)
outfile.close()

input('Press any key to continue...')

##########################################################################

outfile = open("mathematicians.txt", "w")
mathematicians = ["Leonhard Euler", "Carl Gauss", "Emmy Noether"]

for person in mathematicians:
    outfile.write(person + "\n")

outfile.close()

input('Press any key to continue...')

##########################################################################

# There is another default parameter for print - file=sys.stdout
outfile = open("computerScientists.txt", "w")
print("Grace Hopper", "John von Neumann", "Tony Hoare", sep="\n", file=outfile)
outfile.close()

input('Press any key to continue...')

##########################################################################

infile = open("cities.txt")
citiesFile = infile.read().strip()
infile.close()
print(citiesFile)

infile = open("cities.txt")
cities = infile.readlines()
infile.close()
print(cities)

input('Press any key to continue...')

index = 0
while index < len(cities):
    cities[index] = cities[index].rstrip()
    index += 1
print(cities)

input('Press any key to continue...')

##########################################################################

infile = open("mathematicians.txt")
mathematicians = list()
for line in infile:
    mathematicians.append(line.rstrip())
infile.close()
print(mathematicians)

input('Press any key to continue...')

##########################################################################

infile = open("computerScientists.txt", "r")

line = infile.readline()
while line != "":
    print(line.rstrip())
    line = infile.readline()
infile.close()

input('Press any key to continue...')

##########################################################################
    
def writeNums(fileName):
    outfile = open(fileName, "w")
    num = input("Enter an integer, q to quit: ")
    while num.lower() != "q":
        print(num, file=outfile)
        num = input("Enter an integer, q to quit: ")
    outfile.close()

def readNums(fileName):
    infile = open(fileName)
    numList = []
    for num in infile:
        num = int(num)
        numList.append(num)
    infile.close()
    return numList

myFile = "stuff.txt"
writeNums(myFile)

input('Press any key to continue...')

lst = readNums(myFile)
print(lst)
