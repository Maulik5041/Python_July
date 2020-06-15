class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number

    def get_name(self):
        return self.__name

    def set_name(self, x):
        self.__name = x

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, x):
        self.__roll_number = x


obj1 = Student("Steve", 45)
print(f"Name before changing = {obj1.get_name()}")
print(f"Roll Number before changing = {obj1.get_roll_number()} \n")
obj1.set_name("Jessica")
print(f"Name after changing = {obj1.get_name()}")
obj1.set_roll_number(67)
print(f"Roll Number after changing = {obj1.get_roll_number()}")
