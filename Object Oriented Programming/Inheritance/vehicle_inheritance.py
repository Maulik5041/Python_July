class Vehicle:
    fuel_cap = 90

    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print(f"Manufacturer: {self.make}")
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    fuel_cap = 50

    def __init__(self, make, color, model, doors):
        # without using super()
        # Vehicle.__init__(self, make, color, model)
        super().__init__(make, color, model)
        self.doors = doors

    def print_details(self):
        super().print_details()
        print(f"Doors: {self.doors}")
        print("I am from the Car class")

    def display(self):
        print(f"Fuel cap from the Vehicle Class: {super().fuel_cap}")
        print(f"Fuel cap from the Car Class: {self.fuel_cap}")


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.print_details()
obj1.display()
