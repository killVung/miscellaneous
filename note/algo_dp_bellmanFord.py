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

g = {'1':{'2':4,'3':-3,'6':19},'2':{'1':4,'4':2},'3':{'1':-3,'4':1,'5':-5},'4':{'2':2,'6':4,'3':1,'5':2},'5':{'3':-5,'4':2,'6':6},'6':{'1':19,'4':4,'5':6}}

g= {
	'1':{'4':-2},
	'2':{'3':2,'4':3},
	'3':{'4':-5,'2':2},
	'4':{'1':-2,'2':3,'3':-5}	
}

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
m['4'][0] = 0

for i in range(1,len(g)):		
	for v in m:
		m[v][i] = getMin(g,m,v,i)		

print("s-t path: " + str(m['1'][len(g) - 1]))
from pprint import pprint
print(pprint(m))