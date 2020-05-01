"""Finding the intersection of two sorted arrays"""


# The quick pythonic way to solve the problem is given below
# But it is not advisable to use in an interview setup
"""
array_1 = [2, 3, 3, 5, 7, 11]
array_2 = [3, 3, 7, 15, 31]

print(set(array_1).intersection(array_2))
"""


def intersect_sorted_array(array_1, array_2):
    i = 0
    j = 0
    intersection = []

    while i < len(array_1) and j < len(array_2):
        if array_1[i] == array_2[j]:
            if i == 0 or array_1[i] != array_1[i - 1]:
                intersection.append(array_1[i])
            i += 1
            j += 1

        elif array_1[i] < array_2[j]:
            i += 1
        else:
            j += 1

    return intersection


array_A = [2, 3, 3, 5, 7, 11]
array_B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(array_A, array_B))
