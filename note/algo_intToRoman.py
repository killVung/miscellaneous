'''
Given an integer, convert it to roman number
For exmaple:
1	I	1
2	II	1+1
3	III	1+1+1
4	IV	5-1
5	V	5
6	VI	5+1
7	VII	5+1+1
8	VIII	5+1+1+1
9	IX	10-1
10	X	10
'''

'''
Special case in Roman are :
1 = I
4 = IV
5 = V
9 = IX
10 = X
40 = XL
50 = L
90 = XC
100 = C
'''

'''
Traverse the map from the largest value, so it will arive on the lower value
For instance if the number is 3, then it will arrive to 1 instead of 4

'''
