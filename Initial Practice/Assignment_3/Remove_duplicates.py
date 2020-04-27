#  Remove the duplicates

list = [1, 2, 4, 4, 7, 8, 8, 9, 7]
new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print (list)
print (new_list)