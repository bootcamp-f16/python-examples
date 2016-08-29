def exec_example():
    """This function shows how the built in exec function works."""
    print('Starting Exec Example')
    exec('print(abs(-1) == 1)')
    print('Ending exec example')

exec_example()


def filter_example():
    """This function shows how the filter function in python works."""
    print('Starting filter_example()')

    def is_even(number):
        return True if number % 2 == 0 else False

    myNums = [1, 2, 3, 4, 5, 6]

    # Filter returns function
    evenNums = filter(is_even, myNums)
    print(str(evenNums.__next__()))
    print(str(evenNums.__next__()))
    assert evenNums.__next__() == 6

filter_example()


def has_attr_example():
    """This function tries out the has attr built in function."""

    class MyObject():
        def __init__(self):
            self.height = '10 feet'
            self.width = '20 feet'

        def print_h_and_w(self):
            print(self.height + ' tall and ', + self.width + ' high.')

    my_object = MyObject()
    assert hasattr(my_object, 'height')
    assert hasattr(my_object, 'width')
    assert not hasattr(my_object, 'superpowers')

has_attr_example()
