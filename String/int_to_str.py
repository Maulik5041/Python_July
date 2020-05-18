# Intro to ord() and chr() functions in Python


# # Prints 48 which is the Unicode code point of the character '0'
# print(ord('0'))
# # Prints the character '0' as 48 is Unicode code point of the character '0'
# print(chr(ord('0')))
# # Prints 49
# print(ord('0') + 1)
# # Prints 49 which is Unicode code point of the character '1'
# print(ord('1'))
# # Prints the character '2' as 50 is Unicode code point of the character '2'
# # ord('0') + 2  = 48 + 2 = 50
# print(chr(ord('0') + 2))
# # Prints the character '3' as 51 is Unicode code point of the character '3'
# # ord('0') + 3  = 48 + 2 = 51
# print(chr(ord('0') + 3))

# for i in range(40, 100):
#     print(f"{i} --> {(chr(i))} -----> {(type(chr(i)))}")


def int_to_str(input_int):
    print(f"The given integer is {input_int}")

    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        print(f"Number to be focussed is {input_int} \n")
        print(f"Using chr and ord functions --> {(ord('0'))} and adding to it\
 {(input_int % 10)} and then convert the sum back to the character")
        output_str.append(chr(ord('0') + input_int % 10))
        print(f"Output is {output_str} \n\n")
        input_int //= 10
    output_str = output_str[::-1]
    print(f"The final output after reversing is {output_str} \n")

    output_str = ''.join(output_str)
    print(f"-------{output_str}--------")

    if is_negative:
        return '-' + output_str
    return output_str


INP_INT = 123
print(INP_INT)
print(type(INP_INT))

OUT_STR = int_to_str(INP_INT)
print(OUT_STR)
print(type(OUT_STR))
