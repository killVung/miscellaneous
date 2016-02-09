import sys
r = sys.stdin
w = sys.stdout

def isStrict(i,j,k,l):
	return (k == (j + 1) and (l == k + 1))

line = r.readline()
while line is not "":
	line = line.split()
	test = int(line[0])
	for i in range(test):
		test = r.readline()
		test = test.split()
		i,j,k,l = [int(test[0]),int(test[1]),int(test[2]),int(test[3])]
		a = isStrict(i,j,k,l)
		if a == False:			
			w.write(str("NO") + "\n")
		else:
			w.write(str("YES") + "\n")
	line = r.readline()

