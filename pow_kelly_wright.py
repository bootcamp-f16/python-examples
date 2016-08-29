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





