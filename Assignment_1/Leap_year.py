# Check if the number is Leap Year

print("The leap year has 29 days in february and a total of 366 days in a year")

d = int(input("Enter the year: "))

if (d % 400 == 0):
    print("%s is a Leap Year" % d)
elif (d % 100 == 0):
    print("%s is Not the Leap Year" % d)
elif (d % 4 == 0):
    print("%s is a Leap Year" % d)
else:
    print("%s is Not the Leap Year" % d)