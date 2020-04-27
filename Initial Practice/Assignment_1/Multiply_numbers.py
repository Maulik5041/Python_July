# Multiply all the elements in the list

list = []

for i in range(0,10):
    n = int(input("Value: "))
    list.append(n)

print (list)
product = 1

for element in list:
    product *= element

print(product)