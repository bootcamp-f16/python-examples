# one
""" divmod(a, b)
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b)."""
a=43
b=3

print (divmod(a,b)) 
print (divmod(3,2))

print("--"*10)

# two
"""enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable."""

b= range(1,10)
a=["a","b","c","d"]
print(a)
en=list(enumerate(a, 10))
print("list with numbers",en)

print("--"*10)


# Three
# id(object) - It gives unique id of the given object.

one = {"1","2",3,"a"}
two = {"aa","bb"}
print ("id of object 'one' is {}".format(id(one)))
print ("id of object 'two' is {}".format(id(one)))


print("--"*10)

#input([prompt])
"""If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised."""
a = input ("Type something here -->  ")
print (a+a) # input store the value as string

print("--"*10)
# pow(x,y) = x**y
print("Two to the power four is: ",pow(2,4)) #prints 2 to the power four.

print("--"*10)


