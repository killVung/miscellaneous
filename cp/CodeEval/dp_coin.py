#3 coins of value 1, 3 and 5
#11 would be 3, 20 would be 4
import sys
def coin(W):		
	C = (1,3,5)
	M = [sys.maxsize for i in range(W+1)]
	M[0] = 0

	for index, minCoin in enumerate(M): #enumerate helps accessing index
		for c in C:			
			if c <= index:
				v = 1 + M[index-c]				
				if v < minCoin:
					M[index] = v
	return M[len(M) - 1]


"""Sample code to read in test cases:"""
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	givenCoin = int(test)
	print(coin(givenCoin))
test_cases.close()