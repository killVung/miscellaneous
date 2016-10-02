'''
Building upon twoSum algorithm
For each number in the sorted list, you perform
two sum with the current element to find the number
equal to a
'''
list = [5,1,2,8,3,-2]
def Three_Sum(list,a):
    list = sorted(list)
    l,h = 0,len(list) - 1
    for i in list:
        for _ in range(len(list)):
            if list[l] != i and list[h] != i:
                currentSum = list[l] + list[h] + i
                if currentSum == a:
                    return (i,list[l],list[h])
                elif currentSum < a:
                    l += 1
                elif currentSum > a:
                    h -= 1
                else:
                    return None

            else:
                if list[l] == i:
                    l += 1
                else:
                    h -= 1
print(Three_Sum(list,0))
