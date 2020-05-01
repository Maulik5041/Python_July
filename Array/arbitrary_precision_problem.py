"""Arbitrary Precision problem using Arrays"""


A1 = [1, 4, 9]
A2 = [9, 9, 9]


def plus_one(an_array):
    an_array[-1] += 1
    for i in reversed(range(1, len(an_array))):
        if an_array[i] != 10:
            break
        an_array[i] = 0
        an_array[i - 1] += 1
    if an_array[0] == 10:
        an_array[0] = 1
        an_array.append(0)
    return an_array


print(plus_one(A1))
print(plus_one(A2))
