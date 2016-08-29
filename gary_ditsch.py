
husker_rankings = [27, 24, 18, 16, 10, 6, 4, 1]
final_rankings = []

print "husker rankings: ", husker_rankings

"""
reversed()
a. reversed takes a sequence and returns the elements in reverse order
b. it requires the sequence to be something that can be iterated over: strings, lists, unicode and tuples
c. this does Not create a new list but does allow you to iterate over reversed list
"""

print "+++++++++++"
print "example one: reversed" 
print "+++++++++++"

"""
Good Example: reversed object is able to be iterated over
In this case to create a new list with reversed order
"""
def reversed_example():
    for rank in reversed(husker_rankings):
        final_rankings.append(rank)
    print final_rankings
    print husker_rankings, "The original list still in place"

    if final_rankings == husker_rankings[::-1]:
        print "Go Big Red"
    else: 
        print "College Football is rigged!"


reversed_example()

print "+++++++++++"
print "example two: reversed"
print "+++++++++++++"

"""
Good Example: reversed used on a string, then iterated over
"""
def reversed_example2():
    new_str = ""
    x = "Huskers"
    for letter in reversed(x):
        new_str = new_str + letter
    print new_str
    print x, ": original string still in place"

reversed_example2()

"""
reverse()
a. reverse takes a sequence and returns the elements in reverse order
b. this does NOT work on strings  
c. this Does create a new list 
"""

print "+++++++++++"
print "example one: reverse" 
print "+++++++++++"

def reverse_example():
    husker_rankings.reverse()
    print husker_rankings, "original list is changed"

reverse_example()

"""
math.floor()
a. The method floor() returns floor of x - the largest integer not greater than x.
b. must impor the math module to access floor() 
"""

import math

print "+++++++++++"
print "example one: math.floor" 
print "+++++++++++"

def floor_example():
    print("Huskers starting rank {}".format(math.floor(27.5)))
    assert math.floor(27.9) == 27

    print("Huskers mid season rank {}".format(math.floor(16.9)))
    assert math.floor(16.9) == 16

    print("Huskers end of season rank {}".format(math.floor(1.5)))
    assert math.floor(1.5) == 1

floor_example()









