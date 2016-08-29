def pow_example(x,y):
	"""
	Return x to the power y. 
	If z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z). 
	"""
	print("x = %s \ny = %s" % (x,y))
	print("\tpow(x,y): %s" % pow(x,y))
	print("\tx**y: %s" % (x**y))

pow_example(2,3)
pow_example(1,10)
pow_example(9,2)

def round_example(x):
	"""
	This function rounds the floating number to a specified length.
	"""
	print("x = %s" % x)
	print("round(%s)" % x)
	print(round(x))

round_example(5.34)
round_example(6543.123554)



def divmod_example(x,y):
	"""
	Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder.
	First resulting number is the result of division (rounded down)
	Second resulting number is modulo (remainder)
	"""
	print("x = %s \ny = %s" % (x,y))
	print("\tdivmod(%s,%s)" % (x,y)) 
	print(divmod(x,y))	

divmod_example(1,2)
divmod_example(6,4)

