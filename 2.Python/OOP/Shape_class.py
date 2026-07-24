import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(4)

print("Circle area:%.2f" % circle.area())
print("Circle perimeter:%.2f" % circle.perimeter())
print("Triangle area:%.2f" % triangle.area())
print("Triangle perimeter:%.2f" % triangle.perimeter())
print("Square area:%.2f" % square.area())
print("Square perimeter:%.2f" % square.perimeter())
