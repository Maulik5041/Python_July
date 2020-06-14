class User():
    def __init__(self, username=None):
        self.__username = username

    def __set_username(self, x):
        self.__username = x
        return x

    def change_username(self, x):
        return self.__set_username(x)

    def get_username(self):
        return (self.__username)


Steve = User('steve1')
print(f"Before setting : {Steve.get_username()}")
# Overriding Private method access
Steve._User__set_username('steve2')
print(f"After setting : {Steve.get_username()}")
# Using getter and setter method efficiently for encapsulation
Steve.change_username('steve3')
print(f"After changing: {Steve.get_username()}")
