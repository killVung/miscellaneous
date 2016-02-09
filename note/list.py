def f (x, y, *z) :
	return [x, y, z]

u = ((2,))
print(f(3,4,*u))