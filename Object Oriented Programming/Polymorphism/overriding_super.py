"""Even if the method in child class has overridden from base, it can still be called"""


class Shape:
    sname = "Shape"

    # Overridden Method by child
    def get_name(self):
        return self.sname


class XShape(Shape):
    def __init__(self, name):
        self.xsname = name

    # Overridding method
    def get_name(self):
        return super().get_name() + ", " + self.xsname


# get_name method will call both, overridden and overriding, method
circle = XShape("Circle")
print(circle.get_name())
