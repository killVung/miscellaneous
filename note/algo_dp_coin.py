import sys
C = (2,4,7,11,14)
def coin(W):		
	M = [sys.maxsize for i in range(W+1)]
	M[0] = 0

	for index, minCoin in enumerate(M): #enumerate helps accessing index
		for c in C:			
			if c <= index:
				v = 1 + M[index-c]				
				if v < minCoin:
					M[index] = v
	return M
print(coin(27))
