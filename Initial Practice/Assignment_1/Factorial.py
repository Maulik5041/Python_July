# Factorial of a number

n = int(input("Enter the number: "))

print("Factorial is the product of all positive integers from '1' till the given number")
p = range(1, n+1)
N = 1
for i in p:
    N = N * i
print("So, the factorial of this number is %s" % N)