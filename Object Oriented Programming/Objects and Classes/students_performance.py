"""Create a class that calculates students marks and percentage"""


class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total_obtained(self):
        return (self.phy + self.chem + self.bio)

    def percentage(self):
        return (self.total_obtained()/300) * 100


obj1 = Student('Mark', 65, 89, 78)
print(obj1.total_obtained())
print(obj1.percentage())
