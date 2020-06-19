class MyClass:
    pass


c = MyClass()
print(dir(c))

o = object()
print(dir(o))


class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)


raise MyError("Something went wrong")
