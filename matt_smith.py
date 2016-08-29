def abs_example():
    """
    abs(number) returns the absolute value of number
    """
    print("abs({}) == 4".format(abs(-4)))
    assert abs(-4) == 4

    print("abs({}) == 10".format(abs(10)))
    assert abs(10) == 10

    print("abs({}) == 12".format(abs(-12)))
    assert abs(-12) == 12

abs_example()