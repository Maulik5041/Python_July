"""A game of advancing till the end of the list using an array"""


def array_advance(an_array):
    furthest_reached = 0
    last_idx = len(an_array) - 1

    i = 0

    while i <= furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, an_array[i] + i)
        i += 1
    return furthest_reached >= last_idx


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))


# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
