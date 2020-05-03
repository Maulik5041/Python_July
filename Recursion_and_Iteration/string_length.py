"""Calculating the lenth of the string"""


def iterative_str_length(input_str):
    length = 0
    for i in input_str:
        length += 1
    return length


def pythonic_str_length(input_str):
    return len(input_str)


def recursive_str_length(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_length(input_str[1:])


print("--------Result from the Iterative Approach--------")
print(iterative_str_length("LucidProgramming"), '\n')

print("--------Result from the Pythonic Approach-------")
print(pythonic_str_length("LucidProgramming"), '\n')

print("---------Result from the Recursive Approach-------")
print(recursive_str_length("LucidProgramming"))
