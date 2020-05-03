"""Counting the consonants in String"""


def iterative_count_consonants(input_str):
    vowels = 'aeiou'
    count = 0

    for a_char in input_str:
        if a_char.lower() not in vowels and a_char.isalpha():
            count += 1

    return count


def recursive_count_consonants(input_str):
    vowels = 'aeiou'
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    return recursive_count_consonants(input_str[1:])


print(iterative_count_consonants("Welcome to Educative!"))
print(recursive_count_consonants("Welcome to Educative!"))
