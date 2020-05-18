def normalize_str(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def is_unique_1(input_str):
    ht_1 = dict()
    for i in input_str:
        if i in ht_1:
            return False
        ht_1[i] = 1
    return True


def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


def is_unique_4(input_str):
    i = 1
    for a_val in input_str:
        if a_val in input_str[i:]:
            return False
        i += 1
    return True


UNIQ_STR = "AbCDefG"
NON_UNIQ_STR = "non Unique STR"

UNIQ_STR = normalize_str(UNIQ_STR)
NON_UNIQ_STR = normalize_str(NON_UNIQ_STR)

print("Unique String")
print(UNIQ_STR)
print("Non-Unique String")
print(NON_UNIQ_STR, "\n")

print("Solution 1 where input string is unique string")
print(is_unique_1(UNIQ_STR))
print("Solution 1 where input string is non-unique string")
print(is_unique_1(NON_UNIQ_STR), "\n")


print("Solution 2 where input string is unique string")
print(is_unique_2(UNIQ_STR))
print("Solution 2 where input string is non-unique string")
print(is_unique_2(NON_UNIQ_STR), "\n")

print("Solution 3 where input string is unique string")
print(is_unique_3(UNIQ_STR))
print("Solution 3 where input string is non-unique string")
print(is_unique_3(NON_UNIQ_STR), "\n")

print("Solution 4 where input string is unique string")
print(is_unique_4(UNIQ_STR))
print("Solution 4 where input string is non-unique string")
print(is_unique_4(NON_UNIQ_STR))
