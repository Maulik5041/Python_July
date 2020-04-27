# Utilizing Inheritance

class Vehicle(object):
    """Let's begin our Auto Show today"""
    def __init__(self, type, company, bhp, used):
        self.type = type
        self.company = company
        self.bhp = bhp
        self.used = used

    def look(self):
        print("Dominic Toretto rides a %s of %s, having %s brake horse power and it is brand new" % (self.type, self.company, self.bhp))


class Bike(Vehicle):

    def __init__(self, type, company, bhp, used, color):
        Vehicle.__init__(self, type, company, bhp, used)
        self.color = color

    def intro(self):
        print("I have a %s of %s with %s brake horse power, but it is used and of %s color" % (self.type, self.company, self.bhp, self.color))


Car = Vehicle("Car", "Dodge", 700, "No")
Pulsar = Bike("Bike", "Bajaj", 250, "Yes", "Black")

(Car.look())
(Pulsar.intro())