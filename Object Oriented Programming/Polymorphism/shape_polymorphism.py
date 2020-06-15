"""Basic use of Polymorphism using 2 classes"""


class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def get_area(self):
        return self.width * self.height


class Circle():
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def get_area(self):
        return self.radius * self.radius * 3.142


shape1 = Rectangle(6, 10)
shape2 = Circle(7)
print(f"Sides of a Rectangle are: {str(shape1.sides)}")
print(f"Area of a Rectangle is: {str(shape1.get_area())}")
print(f"Sides of a Circle are: {str(shape2.sides)}")
print(f"Area of a Circle is: {str(shape2.get_area())}")


"""Use of Polymorphism alongwith Inheritance"""


class ShapeMain:
    def __init__(self):
        self.sides = 0

    def get_area(self):
        pass


class Rectangle1(ShapeMain):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.sides = 4

    # Method Overriding alongwith Polymorphism
    def get_area(self):
        return self.width * self.height


class Circle1(ShapeMain):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.sides = 0

    # Method Overriding alongwith Polymorphism
    def get_area(self):
        return self.radius * self.radius * 3.142


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].get_area()))
print("Area of circle is:", str(shapes[1].get_area()))
