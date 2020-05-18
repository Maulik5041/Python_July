"""Solutions to check if the input string is a palindrome"""


A_STRING = "Was it a cat I saw?"

# Solution uses extra space proportional to size of string "A_STRING"
# A_STRING = ''.join([i for i in A_STRING if i.isalnum()]).replace(" ", "").lower()
# print(A_STRING == A_STRING[::-1])


# Preferred Solution
def is_palindrome(a_string):
    i = 0
    j = len(a_string) - 1

    while i < j:
        while not a_string[i].isalnum() and i < j:
            i += 1
        while not a_string[j].isalnum() and i < j:
            j -= 1

        if a_string[i].lower() != a_string[j].lower():
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome(A_STRING))
