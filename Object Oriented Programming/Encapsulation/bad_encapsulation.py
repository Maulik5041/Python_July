"""An example of a bad encapsulation for an application for login"""


class User:
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password

    def login(self, user_name, password):
        if self.user_name.lower() == user_name.lower() and self.password == password:
            print("Access Granted")

        else:
            print("Invalid Credentials!")


# An event where anyone could access the data and change it
# Not a good practice while designing an application
Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")


"""An example of how to improve the good coding practices"""


class User2:
    def __init__(self, user_name=None, password=None):
        self.__user_name = user_name
        self.__password = password

    def login(self, user_name, password):
        if self.__user_name.lower() == user_name.lower() and self.__password == password:
            print(f"Access granted against username: {self.__user_name.lower()}")
        else:
            print("Invalid Credentials")


# This will keep the data private and secured
Steve = User2("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.__password