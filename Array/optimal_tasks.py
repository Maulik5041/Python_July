"""Using greedy algorithm to solve the optimal task problem"""


A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i]) # ~i is the bitwise complement operator which puts a negative sign in front of i
