l = input().split(' ')
n, k = int(l[0]), int(l[1])
left, right = 1, n
while left != right:
    x = middle = (left + right) // 2
    sum = 0
    while x != 0:
        '''
        Realizing the fact that x + (x/k) + (x/k^2) is
        equal to x + x/k + x/k/k + x/k/k/k ...
        '''
        sum += x
        x //= k
    if sum >= n:
        right = middle
    else:
        left = middle + 1
print(left)
