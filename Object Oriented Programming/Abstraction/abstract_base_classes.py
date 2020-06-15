from abc import ABC, abstractmethod


# Shape is a child class of ABC
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


# this will code will not compile since Shape has abstract methods without
# method definitions in it
shape = Shape()

# this will code will not compile since abstarct methods have not been
# defined in the child class, Square
square = Square(4)
