# Usage of Constructor

class Juice():

    def __init__(self, fruit, color, taste, days):   # This is the constructor and it defines the attributes
        self.fruit = fruit
        self.color = color
        self.taste = taste
        self.days = days

    def is_ripe(self):
        if self.days > 4:
            print("This %s, of %s color, tastes very %s and so it should not be consumed" % (self.fruit, self.color, self.taste))
        else:
            print("This %s of %s color, tastes very %s and so it should be consumed" % (self.fruit, self.color, self.taste))

Apple = Juice("apple", "green", "sour", 5)
Orange = Juice("orange", "orange", "sweet", 1)

Apple.is_ripe()
Orange.is_ripe()