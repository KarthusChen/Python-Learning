# A class is a blueprint, or prototype, that defines data members
# that characterize an object of the class.
# Data members can be instance variables or functions. Functions
# defined within a class are usually referred to as methods.
# Classes allow us to encapsulate, or bundle, variables and methods
# within an object.

# Object-oriented programming uses objects to solve problems or
# write algorithms.

# Below is some basic syntax for defining a class.

# class <ClassName>:
#     <statements>

class MyFirstClass:
  
    # This method is available to all MyFirstClass objects.
    # It will be called using the dot operator on a MyFirstClass object.
    # self is a parameter that refers to the specific object that
    # invokes or calls the method. self (or another name referring to the instance)
    # is a required parameter when writing instance methods.
    # You should only use self. It is the Python way.
    def instance(self):
        print("I'm a MyFirstClass object!", self)
    
# The line below constructs a MyFirstClass object.
# We have given it the variable name obj.
# This is also referred to as instantiation.
# obj is an instance of the MyFirstClass class.
obj = MyFirstClass()
print('obj is a MyFirstClass object ->', isinstance(obj, MyFirstClass))

obj1 = MyFirstClass()
obj2 = MyFirstClass()

# This line just prints the internal representation of a
# MyFirstClass object.
# We expect to see something about a MyFirstClass object.
print(obj)

input('\nPress Enter to continue...')

# Here we are calling the instance method named instance
# on the MyFirstClass object named obj.
# The following two lines are equivalent
# Understanding the second line will be important when we discuss inheritance
obj.instance()
MyFirstClass.instance(obj)

obj1.instance()
obj2.instance()

input('\nPress Enter to continue...')

# A square has 4 sides. All side lengths are equal.
# If we have the side length of a square, we can easily find the
# area and perimeter.
# We can represent a square using a Python class.

class Square:
    # We need to create a variable, side, to represent the side
    # length of a square. This is an instance variable. Different
    # instances of squares will have different side lengths.
    # An instance variable is created by including an assignment
    # statement with self.variableName as the left-hand operand.
    # An instance variable is sometimes referred to as an object attribute.
	
    # This method assigns a value to the instance variable side.
    # This is a setter or mutator
    def setSide(self, side):
        self.side = side

    # This method returns the value of the instance variable side.
    # It must be set first.
    # This is a getter or accessor.
    def getSide(self):
        return self.side

    # This method returns the area of a square. The instance variable,
    # side, must be set first.
    def area(self):
        return self.side ** 2

    # This method returns the perimeter of a square. The instance variable,
    # side, must be set first.
    def perimeter(self):
        return 4 * self.side

# This is how you construct a Square. We will introduce a very important
# method for classes called a constructor later. A default constructor is
# provided if we do not include our own. The variable mySquare is an
# object of type Square.
mySquare = Square()
print('mySquare is a Square object ->', isinstance(mySquare, Square))

# At this point, mySquare has no side attribute. We cannot call the methods
# or refer to the side attribute in any way.

# Here we call the setSide method to provide a value for the instance
# variable side.
mySquare.setSide(7)

# We call the getSide method to get the value of the instance
# variable side. 
print('mySquare has side length', mySquare.getSide())

input('\nPress Enter to continue...')

# We call the area method to return the area of the Square object,
# mySquare.
print('mySquare has area', mySquare.area())

input('\nPress Enter to continue...')

# We call the perimeter method to return the perimeter of the Square
# object, mySquare.
print('mySquare has perimeter', mySquare.perimeter())

input('\nPress Enter to continue...')

# Benefits:
#    - When we want to find the area of a square, we don't multiply
#      regular variables, we call a method on a square object.
#      This prevents errors when coding.
#    - We can reuse the code in many ways. Other programs can use the
#      the classes we write. We can also create classes with user defined 
#      objects as data members (composition). And inherit attributes from classes
#      when writing new classes (inheritance).

# Redefining Square - this time we have included a constructor
class Square:
    # This is a constructor. We no longer have the default constructor.
    # This is the method that's called when you construct Square
    # objects. We can still call the constructor without an argument
    # because we are using a default argument. The instance variable
    # side is set to 1 if it is not included in the method call.
    # This is our first case of method overloading and the most common
    # in Python.
    def __init__(self, side=1):
        self.side = side

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

mySquare1 = Square()

print('mySquare1 has side length', mySquare1.getSide())
print('mySquare1 has area', mySquare1.area())
print('mySquare1 has perimeter', mySquare1.perimeter())

input('\nPress Enter to continue...')

mySquare2 = Square(7)

print('mySquare2 has side length', mySquare2.getSide())
print('mySquare2 has area', mySquare2.area())
print('mySquare2 has perimeter', mySquare2.perimeter())

input('\nPress Enter to continue...')

mySquare2.side = 3

print('mySquare2 has side length', mySquare2.getSide())
print('mySquare2 has area', mySquare2.area())
print('mySquare2 has perimeter', mySquare2.perimeter())

input('\nPress Enter to continue...')

# Redefining Square - this time we have made all the instance variables
# 'private.' There is actually no concept of private in Python. 
# The __ causes the name to be mangled.
# We will only be allowed to modify instance variables if we
# provide setters. This way we can control how the data is modified and
# prevent corruption. An instance variable name is mangled by preceding
# the name with two underscores.
class Square:
    # slightly different implementation because we provide error
    # checking in setSide
    def __init__(self, side):
        self.__side = 1
        self.setSide(side)

    # Some error checking has been added
    def setSide(self, side):
        if side > 0:
            self.__side = side

    def getSide(self):
        return self.__side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

mySquare2 = Square(7)

print('mySquare2 has side length', mySquare2.getSide())
print('mySquare2 has area', mySquare2.area())
print('mySquare2 has perimeter', mySquare2.perimeter())

input('\nPress Enter to continue...')

# This will not be allowed
# Code runs but side is unchanged nothing is done.
mySquare2.side = -2

print('mySquare2 has side length', mySquare2.getSide())
print('mySquare2 has area', mySquare2.area())
print('mySquare2 has perimeter', mySquare2.perimeter())

input('\nPress Enter to continue...')


class Student:

    def __init__(self, name, email, gpa):
        self.name = name
        self.email = email
        self.gpa = 0.0
        # We can use setters to do error checking
        # Anytime we set the GPA we should call setGPA
        # so the logic is written once and not replicated.
        self.setGPA(gpa)

    def setName(self, name):
        self.name = name
        
    def setEmail(self, email):
        self.email = email

    def setGPA(self, gpa):
        if gpa >= 0:
            self.gpa = gpa

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email
    
    def getGPA(self):
        return self.gpa

    # This is a function that is called if we try to print a Student
    # object. It should return a string that represents the object
    # in a human-readable format.
    # i.e.
    # s = Student("Tin", "tin@school.edu", 3.6)
    # print(s)
    def __str__(self):
        return "Name: {}\nEmail: {}\nGPA: {}".format(self.name, self.email, self.gpa)

lisa = Student("Lisa", "lisa@school.edu", 3.9)

print("Name:", lisa.getName())
print("Email:", lisa.getEmail())
print("GPA:", lisa.getGPA())

input('\nPress Enter to continue...')

sal = Student("Sal", "sal@school.edu", -2)

print(sal)

# This is allowed because Employee instance variables are not mangled.
# They can be referred to outside the class.
sal.gpa = -1

input('\nPress Enter to continue...')

print(sal)
