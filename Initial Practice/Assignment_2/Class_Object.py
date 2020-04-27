# Usage of class and object

class Animals(object):
    """Let's enter the animal kingdom and understand them"""
    def __init__(self, type, name, age, mammal, location):
        self.type = type
        self.name = name
        self.age = age
        self.mammal = mammal
        self.location = location

    def intro(self):
        print ("I'm a %s, known as %s, of age %s and I reside at %s." % (self.type, self.name, self.age, self.location))

    def is_mammal(self):
        if self.mammal:
            print("I give birth to babies!")
        else:
            print("I lay eggs!")

Sebastian = Animals("Husky Dog", "Sebastian", 7, True, "Canada")

Sebastian.intro()
Sebastian.is_mammal()