'''
用dp的algo去紀錄每次
'''
硬幣選擇 = [1,5,10,25]
測試數目 = int(input())
def 開始計算(目標):
    櫃統 = [1] * (目標 + 1)
    for 指標 in range(1,len(櫃統)):
        總和 = 0
        for 硬幣 in 硬幣選擇:
            if 硬幣 <= 指標:
                總和 += 櫃統[指標 - 硬幣]
        櫃統[指標] = 總和
    print(櫃統[len(櫃統)-1])
    return 指定數目
for _ in range(測試數目):
    指定數目 = int(input())
    開始計算(指定數目)
