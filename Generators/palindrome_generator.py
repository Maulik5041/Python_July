"""Implementation of advanced generators: .send(), .throw(), .close()"""


def is_palindrome(num):
    # skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    if num == reversed_num:
        return True
    return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    DIGITS = len(str(i))
    if DIGITS == 5:
        # .close() causes the generator to stop
        pal_gen.close()
        # .throw() is used to throw an exception
        pal_gen.throw(ValueError("We don't like large palindromes"))
    # .send() is used to add a digit to the last state
    pal_gen.send(10 ** (DIGITS))
