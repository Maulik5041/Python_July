# Divisible numbers between 2000 and 3000

list = []
for i in range(2000, 3001):
    if i % 5 == 0:
        list.append(i)

print(list)