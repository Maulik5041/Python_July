# Greatest element from the list

list = []

for i in range(0, 10):
    Element = int(input("Enter the value: "))
    list.append(Element)

print(list)
print ("The greatest element from this list is ", max(list))