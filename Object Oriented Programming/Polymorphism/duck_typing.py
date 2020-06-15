"""Implementation of Duck typing"""


class Dog:
    def speak(self):
        print("Woof Woof!!")


class Cat:
    def speak(self):
        print("Meow Meow!!")


class AnimalSound:
    def sound(self, animal):
        animal.speak()


# This is a way of achieving polymorphism without inheritance
# It does not matter what animal is created as long as all of them
# have same method and there is a class which calls that method
sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.sound(dog)
sound.sound(cat)
