def finite_sequence():
    nums = [1, 2, 3, 4, 5, 6, 7]
    for num in nums:
        yield num


finite = finite_sequence()

for _ in range(6):
    print(1)
    if next(finite) == 5:
        print('Hi')
        break
