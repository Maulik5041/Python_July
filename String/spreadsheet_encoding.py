"""Implementing the column ID to an integer value in a spreadsheet"""


# By default unicode values of the characters
print(ord('A'))
print(ord('B'))
print(ord('Z'))


# To make A = 1, B = 2, ..., Z = 26 we need to modify the values
print(ord('A') - ord('A') + 1)
print(ord('B') - ord('A') + 1)
print(ord('P') - ord('A') + 1)
print(ord('Z') - ord('A') + 1)


# Converting the spreadsheet columns: A = 1, Z = 26, AA = 27, AZ = 52, ...
def spreadsheet_encode(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1

    return num


print(spreadsheet_encode("ZZXCA"))
