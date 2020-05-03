"""Find uppercase letter in String by Iteration and Recursion"""


def find_uppercase_iterative(input_str):
    for i, _ in enumerate(input_str):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase found"


def find_uppercase_recursion(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase found"
    return find_uppercase_recursion(input_str, idx + 1)


print("Results from the Iterative Approach")
print(find_uppercase_iterative("lucidProgramming"))
print(find_uppercase_iterative("LucidProgramming"))
print(find_uppercase_iterative("lucidprogramming"))
print("-----------------------------------\n")

print("Results from the Recursive Approach")
print(find_uppercase_recursion("lucidProgramming"))
print(find_uppercase_recursion("LucidProgramming"))
print(find_uppercase_recursion("lucidprogramming"))
print("------------------------------------")
