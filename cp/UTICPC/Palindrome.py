import sys
r = sys.stdin
w = sys.stdout

def isPali(w):
	#Increm number of different letter, and return error < 1
	wrong = 0
	wrd = list(w)	
	if wrd[len(wrd) - 1] != '\n':
		trueLen = len(wrd)
	else:
		trueLen = len(wrd) - 1	
	for i in (range(trueLen // 2)):
		if wrd[i] != (wrd[trueLen - 1]):
			wrong += 1	
	return wrong <= 1	

line = r.readline()
while line is not "":
	line = line.split()
	test = int(line[0])
	for i in range(test):
		test = r.readline()		
		a = isPali(test)
		if a == False:			
			w.write(str("NO") + "\n")
		else:
			w.write(str("YES") + "\n")
	line = r.readline()

