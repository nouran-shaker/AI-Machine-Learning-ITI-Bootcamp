#program to create a class representing a Circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self): 
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
