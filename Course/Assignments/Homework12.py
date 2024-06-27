class Triangle:
    def __init__(self, base, height):
        """Initialize the base and height of the triangle."""
        self.base = base
        self.height = height

    def get_base(self):
        """Return the base of the triangle."""
        return self.base

    def get_height(self):
        """Return the height of the triangle."""
        return self.height

    def set_base(self, base):
        """Set the base of the triangle."""
        self.base = base

    def set_height(self, height):
        """Set the height of the triangle."""
        self.height = height

    def area(self):
        """Return the area of the triangle calculated using the formula (1/2 * base * height)."""
        return 0.5 * self.base * self.height

# Instantiate a triangle object
triangle = Triangle(3, 6)

# Print initial base and height
print("Initial base:", triangle.get_base())
print("Initial height:", triangle.get_height())

# Change base and height using setters
triangle.set_base(5)
triangle.set_height(10)

# Print the area with new base and height
print("Area of triangle:", triangle.area())
