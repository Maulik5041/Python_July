# Factorial of a number is multiplication of all integers smaller than or equal to n.
# Factorial of 6 = 6*5*4*3*2*1 -> 720

"""Factorial can be calculated using the following recursive formula:

n! = n * (n - 1)!
n! = 1 if n = 0 or n = 1

THE TIME COMPLEXITY OF THIS METHOD IS O(n)
"""

def factorial(n):

    #single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

num = 5
print("Factorial of {0} is {1}".format(num, factorial(num)))