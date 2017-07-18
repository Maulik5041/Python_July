# Calculate the number of occurence of a given number in a list

n = []

for i in range(0, 10):
    num = input("Enter the value: ")
    n.append(num)
    print(n)

Char = input("Enter the character you want to count: ")
total = 0

for occ in n:
    if occ == Char:
        total += 1

if total == 0:
    print ("Not in the list")

else:
    print("The occurence of", Char, "is", total, "number of times")