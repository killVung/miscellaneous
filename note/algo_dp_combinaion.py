'''
1??5 -> 15
123 -> 1
7?1 -> 0
15? -> 5
1?5 -> 5
?15 -> 1
1?2? -> 2
'''

'''
Jez, this problem takes me 7 hours to figure out
Declare the size of the matrix to keep tracking of the combination
x is the entire length of the given string + 1, whreas the
y is based on the largest digit on the right + 1, if the digit is "?", then use
the maximum digit 9 + 1.
So for 1??5 I will have

  0 1 ? ? 5
0
1
2
3
4
5

Whreas for 1 ? 2 ? I will have

  0 1 ? 2 ?
0
1
2
3
4
5
6
7
8
9
'''

def withinBound(currentDigit,currentPosition,x):
    #Recall: x = holder + string, so if 1??5, it would be [0,1,?,?,5]
    if currentPosition == 1:
        #Only need to compare the bigger digit
        if x[currentPosition + 1] != "?":
            return currentDigit <= int(x[currentPosition + 1])
        return True
    elif currentPosition == len(x) - 1:
        #Only need to compare the smaller digit
        if x[currentPosition - 1] != "?":
            return int(x[currentPosition - 1]) <= currentDigit
        return True
    else:
        #Compare both boundary
        if x[currentPosition - 1] == "?" and x[currentPosition + 1] == "?":
            return True
        elif x[currentPosition - 1] != "?" and x[currentPosition + 1] != "?":
            return int(x[currentPosition - 1]) <= currentDigit and currentDigit <= int(x[currentPosition + 1])
        elif x[currentPosition - 1] != "?":
            return int(x[currentPosition - 1]) <= currentDigit
        elif x[currentPosition + 1] != "?":
            return currentDigit <= int(x[currentPosition + 1])
        return True




from pprint import pprint
def compute_this_hard_question(string):
    x = list(string)
    x.insert(0,">.<")
    y_len = int(9 if string[len(string) - 1] == '?' else string[len(string) - 1])
    y = list(range(0,y_len + 1))
    dp = [[0 for _ in range(len(x)) ] for _ in range(y_len + 1)]


    for i in range(1,len(dp)):
        dp[i][0] = 1

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            #Begin calculation
            if x[j] != "?":
                dp[i][j] = dp[i][j-1]
            elif withinBound(i,j,x):
                #Perform calculation
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            else:
                #Use the previous value on the top
                dp[i][j] = dp[i-1][j]
    print(dp[len(dp) - 1][len(dp[0])-1])

testCase = input()
for _ in range(int(testCase)):
    compute_this_hard_question(input())
