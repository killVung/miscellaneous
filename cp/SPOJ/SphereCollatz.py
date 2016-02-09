import sys
r = sys.stdin
w = sys.stdout

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    assert(i > 0 and j > 0)

    #Assuming reverse range count
    if i > j:
        i,j = j,i

    #Otherwise
    #assert(i > j)

    #Declare a dictionary to store the computed cyc_len
    cache = {}

    cyc_len_max = 0

    for a in range(i,j + 1):
        cur = a
        cyc_len = 1        

        #print("a is: %d" % a)                
        
        while (cur != 1):
            #print("At while loop for a: %d" % a)
            #Find the cycle_length of this number in the dictionary
            #If it is not existed then compute it, else sum it up and 

            '''
            Following the Collatz conjecture, 
            If the number is even, dividied by 2,
            otherwise multiply by 3 and then plus 1
            Finally increase the cycle length by one
            '''
            if(cur % 2 == 0):
                cur //= 2                

            else:
                cur *= 3
                cur += 1
                
            cyc_len +=1             

            #Look up the dictionary here
            #print("is cur %d in cache? " % cur)
            if cur in cache:
                #print("cur %d is in cache" % cur)
                cyc_len += cache[cur] - 1
                cur = 1

            
            #     print("Looking up cache for a: %d" % cur)
            #     cyc_len += cache[cur]
            #     got_cached = True

            assert(cyc_len > 0)

        #After you compute it, store it in the list, so you don't have to caluclate again in the next time
        #Store key a and val cyc_len
        cache[a] = cyc_len

        #print out the cache for debug
        #print("cache:")
        #print(cache)

        if(cyc_len > cyc_len_max):
            cyc_len_max = cyc_len
    
    assert(cyc_len_max > 0)
    return cyc_len_max


for s in r:
	a = s.split()
	i,j = [int(a[0]),int(a[1])]
	v = collatz_eval (i, j)
	w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

