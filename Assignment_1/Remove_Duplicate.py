# Remove the duplicate from the list

list = []

for i in range(0,10):
    n = int(input("Value: "))
    list.append(n)

print (list)

list_2 = []
for num in list:
    if num not in list_2:
        list_2.append(num)

print (list_2)