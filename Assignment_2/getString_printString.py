# Use getString and printString

class House():
    def __init__(self, floors, color, type):
        self.floors = floors
        self.color = color
        self.type = type
        print("This house has %s floors, of %s color and is a %s" % (self.floors, self.color, self.type))

    def getString(self, used):
        self.used = used
        self.used = int(input("How old is this house: "))
        print("The house has been abandoned since %s years" % self.used)

    def printString(self, s):
        print(self.s.upper())

Neverland = House(25, "Orange", "Mansion")
Neverland.getString(45)
Neverland.printString("The house has been abandoned since all these years")