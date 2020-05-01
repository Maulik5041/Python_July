"""Using 2 pointers to solve two-sum problem"""


def two_sum(an_array, target):
    i = 0
    j = len(an_array) - 1
    while i < j:
        if an_array[i] + an_array[j] == target:
            print(an_array[i], an_array[j])
            return True
        if an_array[i] + an_array[j] < target:
            i += 1
        else:
            j -= 1
    return False

# Time Complexity = O(n)
# Space Complexity = O(1)


print(two_sum([-2, 1, 2, 4, 7, 11], 13))
print(two_sum([-2, 1, 2, 4, 7, 11], 20))
