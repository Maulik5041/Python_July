# Sort the integers

list = []
sorted_list = []
for i in range(0,10):
    n = int(input("Enter the integer: "))
    list.append(n)

print(list)

# Now comes the sorting part:

for t in range(len(list)):
    for j in range(len(list) - 1):
        if list[j] > list[j+1]:
            list[j+1], list[j] = list[j], list[j+1]

print (list)