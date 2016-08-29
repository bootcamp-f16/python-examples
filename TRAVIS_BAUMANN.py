"""
# Number one will be a random number generator using the "random" function.

In the print section I get to choose my chosen integer range, dissected by commas.
This program basically simulates a 6-sided dice
"""

from random import randint
print (randint(1,6))



"""
# HEX function

this will convert any number into a hexidecimal number.
 In my example I had 154 carrots and wanted to see that value in hexidecimal.
"""
print ("\n\n")


Carrots = 154

print hex(Carrots)


"""
# The int() function generates a static identity of an object that will be constant throughout the program.
could be used to make sure two id's are the same thing.
ex. a=b.  id(a) and id(b) will show up with the same number.
"""
randomobj = int(1)

print(id(randomobj))