"This module includes a Point class"

import math

_hiddenInStarImports = True

class Point:
    "This class represents a point in 2D"

    def __init__(self, x=0, y=0):
        "This is the Point class constructor"
        self.x = x
        self.y = y

    def distance_from(self, point2):
        return math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)

    # Part 2 - Operator Overloading
    # This method is used in print and str when __str__ is not implemented
    # It is used in other contexts as well.
    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # This will overload the addition operator
    # __radd__ is right addition, object is on right
    # __iadd__ is in place addition, +=
    def __add__(self, point2):
        return Point(self.x + point2.x, self.y + point2.y)

    # This will overload the subtraction operator
    # __rsub__ is right subtraction, object is on right
    # __isub__ is in place subtraction, -=
    def __sub__(self, point2):
        return Point(self.x - point2.x, self.y - point2.y)

    def __iadd__(self, point2):
        self.x += point2.x
        self.y += point2.y
        return self

    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y

    def __ne__(self, point2):
        return not self == point2

if __name__ == "__main__":
    # Three levels of docstrings
    print("Module docstring:", __doc__)
    print("Class docstring:", Point.__doc__)
    print("Function/Method docstring:", Point.__init__.__doc__)

    # Running some test code
    
    p1 = Point()        # (0, 0)
    p2 = Point(x=1)     # (1, 0)
    p3 = Point(y=1)     # (0, 1)
    p4 = Point(1, -1)   # (1, -1)

    input("\nPress enter to continue...")

    if math.isclose(p1.distance_from(p4), math.sqrt(2)):
        print(p1, "is sqrt(2) units from", p4)

    input("\nPress enter to continue...")

    # Using overloaded __add__ method
    print(p1, "+", p2, end=" = ")
    p = p1 + p2
    print(p)

    input("\nPress enter to continue...")

    # Using overloaded __eq__ method
    print(p, "==", p2, end=" = ")
    print(p == p2)
    
    input("\nPress enter to continue...")

    # Using overloaded __sub__ method
    print(p1, "-", p3, end=" = ")
    p = p1 - p3
    print(p)

    input("\nPress enter to continue...")

    # Using overloaded __ne__ methods
    print(p, "!=", p2, end=" = ")
    print(p != p2)

    input("\nPress enter to continue...")

    # Using overloaded __repr__ method to print here.
    # Changing __repr__ to __str__ in class definition
    # would change the display.
    points = [p1, p2, p3, p4]
    print(points)

    input("\nPress enter to continue...")
    
    new_points1 = list(points)
    for i, new_point in enumerate(new_points1):
        print(new_point, points[i])
        # using our method we defined above
        print(new_point == points[i])
        # Is object reference the same?
        # i.e. Does new_point and points[i] refer to the same memory location?
        print(new_point is points[i])

    input("\nPress enter to continue...")

    # The repr function calls the __repr__ method which 
    # can be used to construct an object with the same attributes
    # using eval.
    # eval executes a string as if it were Python code.
    print(repr(p4))
    print(type(repr(p4)))
    input("\nPress enter to continue...")
    
    p5 = eval(repr(p4))
    print(p4, p5)
    print(p4 == p5)
    print(p4 is p5)

    input("\nPress enter to continue...")

    print(repr(points)) # str(points) returns the same string
    new_points2 = eval(repr(points))
    for i, new_point in enumerate(new_points2):
        print(new_point, points[i])
        print(new_point == points[i])
        print(new_point is points[i])

    input("\nPress enter to continue...")
    
    # The __iadd__ modifies the object on the left and returns it.
    # We implemented it that way.
    print(p1, p4)
    p1 += p4
    print(p1)
