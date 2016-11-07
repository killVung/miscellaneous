'''
Return the minumum number to jump from beginning of the index to the end of the index

[2,3,1,1,2,4,2,0,1,1] -> 4
[5,1] -> 1
[0,3] -> 0
[2,2,2,2,2,2] -> 3
'''
def minJump(l):
    minJumpDP = [float("inf")] * len(l)

    #Base case: single element always reutrn 0 step
    minJumpDP[0] = 0

    #Memoize each minimum jump on each subrange
    for i in range(1,len(l)):
        for j in range(i):
            #Check whether it's possible to jump to i from j
            if j + l[j] >= i:
                #If so, then check whether the jump is minimum
                if 1 + minJumpDP[j] < minJumpDP[i]:
                    minJumpDP[i] = 1 + minJumpDP[j]
    return minJumpDP[-1]

l = [2,3,1,1,2,4,2,0,1,1]
assert(minJump(l) == 4)
l = [5,1]
assert(minJump(l) == 1)
l = [0,3]
assert(minJump(l) == float('inf'))
l = [2,2,2,2,2,2]
assert(minJump(l) == 3)
