# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1 # sets variables a and b 
    while b < n: # while b less than n(the last number in our string)
        print b, # print b if it is less than b
        a, b = b, a+b #sets the varialbles and method for the 2nd function

def fib2(n):   # return Fibonacci series up to n
    result = [] # the result is a set of integers 0 - n
    a, b = 0, 1 # set's a and b as 0 and 1 respectively
    while b < n: # while b is less than n (the last integer in the set)
        result.append(b) #stores the value of b for each loop
        a, b = b, a+b # performs the fibonacci equation 
    return result     # returns the fibonacci sequece between a and n


#Function output

# fibo.fib(1000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

# fibo.fib2(1000)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


