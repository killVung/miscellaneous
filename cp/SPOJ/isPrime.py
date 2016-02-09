import sys

cache = {}
r = sys.stdin
w = sys.stdout

def isPrime(input):
    if input in cache:
        return cache[input]

    if input == 1:
        cache[input] = False
        return False
    
    for i in range(2,input):
        if input % i == 0:
            cache[input] = False
            return False
    cache[input] = True
    return True

testCase = r.readline()
for test in range(int(testCase)):
    line = r.readline().split()
    head,tail = [int(line[0]),int(line[1])]
    for i in range(head,tail + 1):
        if isPrime(i):
            w.write(str(i) + "\n")
    w.write("\n")