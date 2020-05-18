"""Converting string to integer without using the int() python function"""


def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    return output_int


STR = "554"
x = str_to_int(STR)
print(type(x))

STR = "123"
print(str_to_int(STR))

STR = "-123"
print(str_to_int(STR))
