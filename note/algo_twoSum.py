'''
This is an exmaple of two sum algorithm in O(N) time
'''
def twoSum(list, a):
    '''
    Having a lower pointer and a higher pointer
    point at the start and the end
    Move the lower pointer if the currentSum is less
    Move the higher pointer if the fcurrentSum is more
    Return the index if it equals to a
    Return None if the higher meets the lower
    '''
    list = sorted(list)
    l,h = 0, len(list) - 1
    for _ in range(len(list)):
        #Think of the expected case first
        currentSum = list[l] + list[h]
        if currentSum == a:
            return (list[l],list[h])
        elif currentSum < a:
            l += 1
        elif currentSum > a:
            h -= 1
        else:
            return None
a = [0,1,6,8,2]
print(twoSum(a,-1))
