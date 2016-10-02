def get_max_sum_subset(x):
    max_num = 0
    cur_max = 0
    start = -1
    stop = -1
    cur_start = -1

    for i in xrange(len(x)):
        value = cur_max + x[i]
        if value > 0:
            if cur_max == 0:
                cur_start = i
            cur_max = value
        else:
            cur_max = 0


        if cur_max > max_num:
            max_num = cur_max
            stop = i
            start = cur_start

    return max_num, start, stop
print(get_max_sum_subset([1,2,-4,1,1]))