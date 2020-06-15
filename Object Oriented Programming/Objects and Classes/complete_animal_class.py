"""Implementing an animal class and its subclass from scratch"""


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def animal_details(self):
        print(self.name, self.sound)


class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    # Overridding Method along with base class method
    def animal_details(self):
        super().animal_details()
        print(self.family)


class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    # Overridding method along with base class method
    def animal_details(self):
        super().animal_details()
        print(self.color)


dog = Dog("Pongo", "Woof Woof", "Carnivore")
sheep = Sheep("Billy", "Baaa Baaa", "White")

dog.animal_details()
sheep.animal_details()
