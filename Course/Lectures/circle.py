# import all names from point.py that do not start with an underscore
# It also imports all modules imported in point.py
# Generally, this is a bad idea.
from point import *
print(math.sqrt(16))

# Import what you need explicitly.
# Note, names that start with _ can still be imported in this way
# from point import Point, _hiddenInStarImports
# print(_hiddenInStarImports)

input("\nPress enter to continue...")

# Another thing to note is where Python looks for files in import statements
import sys
print(sys.path)

# To easily add locations to this path check, use a .pth file.
# Add the .pth file to the site packages folder
r"""my_libraries.pth (Windows)
C:\Users\me\python_libs
C:\some_dir\python_helper_funcs
"""

"""my_libraries.pth (Unix based)
~/python_libs
/some_dir/python_helper_funcs
"""

input("\nPress enter to continue...")

# Composition occurs when an object has another object
# as an instance variable
# It is a has-a relationship
class Circle:

    # Object references are mutable.
    # Assignment creates an alias
    def __init__(self, center, ext_point):
        self.center = center
        self.ext_point = ext_point
    
##    # Constructing new objects based on input
##    def __init__(self, center, ext_point):
##        self.center = Point(center.x, center.y)
##        self.ext_point = Point(ext_point.x, ext_point.y)

    def get_radius(self):
        return self.center.distance_from(self.ext_point)

    def get_diameter(self):
        return 2 * self.get_radius()

if __name__ == "__main__":

    # If we used import point,
    # we would call the constructor via point.Point()
    p1 = Point()
    p2 = Point(x=1)

    c1 = Circle(p1, p2)

    print("Circle c1 has radius", c1.get_radius())
    print("Circle c1 has center with y =", c1.center.y)

    input("\nPress enter to continue...")

    p1.y = 1

    print("Circle c1 has radius", c1.get_radius())
    print("Circle c1 has center with y =", c1.center.y)
