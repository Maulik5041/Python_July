"""Using Hash Table to solve two-sum problem"""


def two_sum_hash_table(an_array, target):
    hash_table = dict()
    for i, _ in enumerate(an_array):
        if an_array[i] in hash_table:
            print(hash_table[an_array[i]], an_array[i])
            return True
        hash_table[target - an_array[i]] = an_array[i]
    return False


# Time Complexity = O(n)
# Space Complexity = O(n)


print(two_sum_hash_table([-2, 1, 2, 4, 7, 11], 13))
print(two_sum_hash_table([-2, 1, 2, 4, 7, 11], 20))
