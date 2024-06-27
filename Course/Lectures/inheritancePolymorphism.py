# Composition occurs when an object has another object
# as an instance variable.
# It is a has-a relationship.

# We will create a class, Vehicle, that has a Person
# instance variable to represent the owner.

class Person:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName
        
    def getFirstName(self):
        return self.firstName
        
    def getLastName(self):
        return self.lastName
        
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def __str__(self):
        return self.firstName + " " + self.lastName

# Inheritance occurs when a class inherits data members,
# both instance variables and methods.
# It is an is-a relationship.
# The subclass inherits from the superclass.
# The derived class inherits from the base class.

# An inherited method may be inherited (used as is) or
# overwritten (given a new implementation).
# We can also extend the subclass by writing new 
# methods.

# This is the super class (or base class).
class Vehicle:
    # static variable - shared by all Vehicle objects
    __idNums = 1
  
    def __init__(self, owner=None):
        # static members can be used in instance methods
        # but not the other way
        # static members are called by the class name
        self.__idNumber = Vehicle.__idNums
        Vehicle.__idNums += 1
        if owner == None:
            self.owner = Person()
        else:
            # Objects are mutable
            # This is an alias and may be a good idea
            self.owner = owner
            
    def getOwner(self):
        return self.owner
            
    def setOwner(self, owner):
        self.owner = owner
        
    def __str__(self):
        return ("Registration Number: {}\nOwner: {}\n"
                .format(self.__idNumber, self.owner))

# This is a subclass (or derived class)
class Car(Vehicle):
    def __init__(self, numDoors, owner=None):
        # Calling super class constructor
        # to initialize the super class object
        Vehicle.__init__(self, owner)
        self.numDoors = numDoors
        
    def getNumDoors(self):
        return self.numDoors
        
    def __str__(self):
        return ("{}Type: Car\nNumber of doors: {}"
                .format(Vehicle.__str__(self), self.numDoors))
        
# This is a subclass (or derived class)       
class Truck(Vehicle):
    def __init__(self, numAxles, owner=None): 
        # Calling super class constructor
        # to initialize the super class object
        # A different way - Becomes less explicit
        # with more than one level of inheritance and/or
        # multiple inheritance
        super().__init__(owner)
        self.numAxles = numAxles
        
    def getNumAxles(self):
        return self.numAxles
        
    def __str__(self):
        return ("{}Type: Truck\nNumber of axles: {}"
                .format(super().__str__(), self.numAxles))

# This is a subclass (or derived class)        
class Motorcycle(Vehicle):
    def __init__(self, hasSidecar, owner=None):
        super().__init__(owner)
        self.hasSidecar = hasSidecar
        
    def setHasSidecar(self, hasSidecar):
        self.hasSidecar = hasSidecar

    def getHasSidecar(self):
        return self.hasSidecar
        
    def __str__(self):
        return ("{}Type: Motorcycle\nHas sidecar: {}"
                .format(super().__str__(), self.hasSidecar))
        
ed = Person("Ed", "Lee")
sue = Person('Sue', 'Smith')
        
pinto = Car(2, ed)
boxtail = Truck(2, ed)
zoom = Motorcycle(False, ed)

print(pinto)
input('\nPress Enter to continue...')
print(boxtail)
input('\nPress Enter to continue...')
print(zoom)
input('\nPress Enter to continue...')

print(pinto.getOwner())
input('\nPress Enter to continue...')

zoom.setOwner(sue)
zoom.setHasSidecar(True)
print(zoom)
input('\nPress Enter to continue...')

atv = Vehicle(sue)
print(atv)

# Polymorphism - many forms
# The ability to write code to process objects of 
# different types as long as they share common
# attributes

class Animal:
    def speak(self):
        pass
        
class Dog(Animal):
    name = 'Dog'
    def speak(self):
        print("I am a dog. I go ruff!")
        
class Cat(Animal):
    name = 'Cat'
    def speak(self):
        print("I am a cat. I go meow!")

class Duck():
    name = 'Duck'
    def speak(self):
        print("I am a duck. I go quack!")
        
fido = Dog()
whiskers = Cat()
aflac = Duck()

zoo = [fido, whiskers, aflac]

for animal in zoo:
    input('\nPress Enter to continue...')
    animal.speak()
    print(animal.name, 'is an Animal ->', isinstance(animal, Animal))
    print('Class name: {}\nBase class: {}'
          .format(animal.__class__, animal.__class__.__bases__))

# Python uses 'Duck typing'.
# https://en.wikipedia.org/wiki/Duck_typing
# Functionality is determined by the presence of
# methods/attributes, rather than the type of the object.
# The ability to 'speak' is determined by the
# implementation of a speak method.
# A common base class is not required.
