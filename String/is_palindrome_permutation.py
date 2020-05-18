"""Check if the string is a palindrome permutation or not"""


# Even if the word is not a dictionary word, it could be
# a palindrome if the words are arranged appropriately
def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "").lower()
    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for val in d.values():
        if val % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif val % 2 != 0 and odd_count != 0:
            return False

    return True


palin_perm = "m2ax4damx2343lool"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
