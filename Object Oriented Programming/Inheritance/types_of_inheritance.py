"""Different types of inheritance based upon parent and child classes"""


# Single Inheritance
class Vehicle:
    def set_top_speed(self, speed):
        self.top_speed = speed
        print(f"Top speed is set to: {self.top_speed}")


class Car(Vehicle):
    def open_trunk(self):
        print("Trunk is now open")


corolla = Car()
corolla.set_top_speed(220)
corolla.open_trunk()


# Multi-level Inheritance
class Hybrid(Car):
    def turn_on_hybrid(self):
        print("Hybrid mode is now switched on!")


priusPrime = Hybrid()
priusPrime.set_top_speed(250)
priusPrime.open_trunk()
priusPrime.turn_on_hybrid()


# Hierarchical Inheritance
class Truck(Vehicle):
    def identity(self):
        print("This is a Truck")


eicher = Truck()
eicher.identity()


# Hybrid Inheritance
class Engine:
    def set_power(self, power):
        self.power = power


# Multiple Inheritance
class CombustionEngine(Engine):
    def set_tank_capacity(self, tank_capacity):
        self.tank_capacity = tank_capacity


class ElectricEngine(Engine):
    def set_charge_capacity(self, charge_capacity):
        self.charge_capacity = charge_capacity


class HybridEngine(CombustionEngine, ElectricEngine):
    def print_details(self):
        print(f"Power: {self.power}")
        print(f"Tank Capacity: {self.tank_capacity}")
        print(f"Charge Capacity: {self.charge_capacity}")


car = HybridEngine()
car.set_power("2000 cc")
car.set_charge_capacity("250 W")
car.set_tank_capacity("20 Litres")
car.print_details()
