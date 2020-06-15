class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    # Overloading the '-' operator
    def __sub__(self, other):
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp


obj1 = Com(3, 7)
obj2 = Com(2, 5)

# Because of overloading operators, this is possible
# On commenting line 7-9 this would not work
# obj1 --> self.obj and obj2 --> other.obj as defined in __add__ and __sub__
obj3 = obj1 + obj2
obj4 = obj1 - obj2

print(f"Real of obj3: {obj3.real}")
print(f"Imag of obj3: {obj3.imag}")
print(f"Real of obj4: {obj4.real}")
print(f"Imag of obj4: {obj4.imag}")
