class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        self.interest_rate = interest_rate
        super().__init__(title, balance)

    def interest_amount(self):
        return (self.interest_rate * self.balance)/100


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.get_balance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.get_balance())
obj1.deposit(500)
print("Balance after deposit:", obj1.get_balance())
print("Interest on current balance:", obj1.interest_amount())
