# calculate GCD of 2 numbers

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 > n2:

    for i in range(n1, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print("The GCD of", n1, "and", n2, "is %s" % i)
            break

else:
    for i in range(n2, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print("The GCD of", n1, "and", n2, "is %s" % i)
            break