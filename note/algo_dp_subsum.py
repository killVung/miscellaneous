import sys
def sum_seq(x):
    cur_max = 0
    max_num = -1 * sys.maxsize
    cur_start = 0
    start = 0
    stop = 0

    for i,ele in enumerate(x):
        cur_max += ele
        
        if cur_max > max_num:
            max_num = cur_max
            start = cur_start
            stop = i

        if cur_max < 0:
            cur_max = 0
            cur_start = i + 1
    return start,stop,cur_max            

A = [1, 2, -3, 4, -1, 2, -6]
print(sum_seq(A))