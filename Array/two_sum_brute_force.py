"""Using Brute Force to solve two-sum problem"""


def two_sum_brute_force(an_array, target):
    for i in range(len(an_array) - 1):
        for j in range(i + 1, len(an_array)):
            if an_array[i] + an_array[j] == target:
                print(an_array[i], an_array[j])
                return True

    return False


# Time Complexity = O(n^2)
# Space Complexity = O(1)


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
target = 20
print(two_sum_brute_force(A, target))
