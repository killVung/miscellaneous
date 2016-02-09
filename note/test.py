i = 100
j = 200
cyc_len_max = 0
for a in range(i,j + 1):
    cur = a
    cyc_len = 1

    while(cur != 1):
        '''
        Following the Collatz conjecture, 
        If the number is even, dividied by 2,
        otherwise multiply by 3 and then plus 1
        Finally increase the cycle length by one
        '''
        if(cur % 2 == 0):
            cur /= 2
            cyc_len+=1

        else:
            cur *= 3
            cur += 1
            cyc_len+=1

    if(cyc_len > cyc_len_max):
        cyc_len_max = cyc_len

#print(cyc_len_max)
return cyc_len_max