def sumOfArray(arr):
    """
    :param arr: List of integers
    :return: sum of all the integers

    :timecomplexity: It goes through all the numbers in the list and so O(n)
    """
    count = 0

    for num in arr:
        count += num
        # print(count)

    print("The sum of all elements in the array is: ", count)


sumOfArray([1, 4, 5, 65, 345, 2, 4, 645, 35, 45, 6, 43, 90])
