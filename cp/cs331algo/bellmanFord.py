import sys
''' 
given graph 'g': 
s --> a --> b --> t

Expected Matrix 'm':
 0 1 2 3 
s
a
b
t
'''

g = { 's':{'a':-9,'b':-4,'g':99},'a':{'b':3},'b':{'c':-3},'c':{'a':-2,'t':4},'d':{'c':5,'t':-7},'t':{'t':0},'g':{'g':0}}

'''
Function accepts the given matrix, and current vertices
Return the smallest number from the given matrix if possible
'''
def createMatrix(g):
	return {n:([sys.maxsize] * len(g)) for n in g}

def getMin(g,m,v,i):		
	small = m[v][i-1]		
	for nei in g[v]:				
		if (g[v][nei] + m[nei][i-1]) < small:
			small = g[v][nei] + m[nei][i-1]
	return small

m = createMatrix(g)
m['t'][0] = 0

for i in range(1,len(g)):		
	for v in m:
		m[v][i] = getMin(g,m,v,i)		

print("s-t path: " + str(m['s'][len(g) - 1]))