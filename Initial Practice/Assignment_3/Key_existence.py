# Key existence in dictionary

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
n = input("Find the key: ")
if n in dict:
    print("The key already exists")
else:
    print("The key does not exist")