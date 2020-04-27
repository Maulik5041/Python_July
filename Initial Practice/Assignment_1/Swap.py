# Swap the 2 variables

V1 = int(input("The first variable is: "))
V2 = int(input("The second variable is: "))

if V1 != V2:
    V1 = V1 + V2
    V2 = V1 - V2
    V1 = V1 - V2
    print("The new value of first variable is %s" % V1)
    print("The new value of second variable is %s" % V2)
else:
    print("Please enter different values")