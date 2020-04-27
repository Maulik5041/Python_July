# Find if the number is PRIME NUMBER

n = int(input("Enter the number: "))

print("This number should only be divisible by '1' and the mumber itself to be a prime number")

if n >= 8:
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n % 11 != 0:
        print("It is a prime number")
    else:
            print("It is NOT a Prime Number")
else:

    if n == 2 or n == 3 or n == 5 or n == 7:
        print ("it is a Prime Number")
    else:
        print ("it is not a Prime Number")
