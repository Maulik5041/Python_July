"""Create a calculator class that does different operations"""


class Calculator:
    def __init__(self, num1=25, num2=10.5):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2/self.num1


obj1 = Calculator()
print(obj1.add())
print(obj1.subtract())
print(obj1.multiply())
print(obj1.divide())
