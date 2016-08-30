# Usage example function for the python [bin] function.

def using_bin(x):
	# The `bin` function converts an integer number to a binary string.

    print(bin.__doc__)
    x = int(x)
    return bin(x)

# Usage example function for the python [type] function.
def using_type(val):
    # The `type` function returns the Python type of the value passed to it. 

    print(type.__doc__)
    ans = type(val)
    print(ans)

    # check for a certain type
    if type(val) == int:
    	print('val argument is an integer')

    return ans

# Usage example function for the python [open] function.
def using_open(fname, mode):
    print(open.__doc__)
    print(dir(open))

    """
    Open requires a filename and a 'mode' of usage for the file.
    Accepted file operations modes are:

    'r'	open for reading (default)
    'w'	open for writing, truncating the file first
    'x'	open for exclusive creation, failing if the file already exists
    'a'	open for writing, appending to the end of the file if it exists
    'b'	binary mode
    't'	text mode (default)
    '+'	open a disk file for updating (reading and writing)
    """

    example_file = open('my_file.txt', 'r')
    example_file.close()
