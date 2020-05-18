"""Check if the given strings are anagram"""


FIRST_STRING = "fairy tales"
SECOND_STRING = "rail safety"

FIRST_STRING = FIRST_STRING.replace(" ", "").lower()
SECOND_STRING = SECOND_STRING.replace(" ", "").lower()

# Time Complexity = O(N logN)
# That is due to the fact that any sorting algorithm
# requires at least n logn time to sort
# print(sorted(FIRST_STRING) == sorted(SECOND_STRING))


# Solution 2: Using dictionary for individual string
def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1

        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1

        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True


print(is_anagram(FIRST_STRING, SECOND_STRING))
