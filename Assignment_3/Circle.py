# Circle, radius, area and perimeter
from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = pi * (self.radius ** 2)
        print("The area of the given circle will be", a)

    def perimeter(self):
        p = 2 * pi * self.radius
        print("The perimeter of the given circle is", p)

moon = Circle(25)
moon.area()
moon.perimeter()