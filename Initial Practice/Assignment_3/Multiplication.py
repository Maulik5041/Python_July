# Multiplying items in list

list = []
product = 1

for i in range(0, 10):
    num = int(input("Enter the value: "))
    list.append(num)
print(list)

for n in list:
    product *= n

print(product)