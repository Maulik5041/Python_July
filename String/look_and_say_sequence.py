def next_number(a_string):
    result = []
    i = 0

    while i < len(a_string):
        count = 1
        while i + 1 < len(a_string) and a_string[i] == a_string[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + a_string[i])
        i += 1
    return ''.join(result)


START_NUM = "1"
print(START_NUM)
COUNT_NUMS = 10
for i in range(COUNT_NUMS - 1):
    START_NUM = next_number(START_NUM)
    print(START_NUM)
