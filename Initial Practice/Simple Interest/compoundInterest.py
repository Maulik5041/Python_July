# Python3 program to find compound interest

def compound_interest(principal, rate, time):
    """

    :param principal: int
    :param rate: float
    :param time: int
    :return: Compound interest in float
    """

    # Calculate compound interest
    CI = principal * (pow((1 + rate/100), time))
    print("Compound interest is: ", CI)

compound_interest(10000, 10.25, 7)