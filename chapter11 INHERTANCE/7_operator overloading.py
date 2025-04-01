"""Why Use Operator Overloading?

Operator overloading allows your custom objects to behave like built-in types and gives you a more intuitive way to work with your classes. For example, it allows you to use the + operator to add two objects of a custom class, just as you would with integers or strings.

Common Magic Methods for Operator Overloading:
Here are some of the most commonly used magic methods:

__add__(self, other): Defines the behavior for the + operator.

__sub__(self, other): Defines the behavior for the - operator.

__mul__(self, other): Defines the behavior for the * operator.

__truediv__(self, other): Defines the behavior for the / operator.

__eq__(self, other): Defines the behavior for the == operator.

__lt__(self, other): Defines the behavior for the < operator.

__le__(self, other): Defines the behavior for the <= operator.

__ne__(self, other): Defines the behavior for the != operator."""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload the + operator
    def __add__(self, other):
        # Ensure the other object is also a Point
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    # Overload the == operator
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage:
p1 = Point(2, 3)
p2 = Point(1, 1)

# Adding two Point objects
p3 = p1 + p2
print(p3)  # Output: Point(3, 4)

# Checking equality of two Point objects
print(p1 == p2)  # Output: False


'''Explanation of the Code:
__add__ method: This method is called when the + operator is used between two Point objects. It returns a new Point object with the sum of the respective x and y coordinates.

__eq__ method: This method is called when == is used to compare two Point objects. It checks whether the x and y values of both points are the same.

__repr__ method: This method is used to define how the object is represented when printed. It helps with a clean and readable output when we print a Point object.'''