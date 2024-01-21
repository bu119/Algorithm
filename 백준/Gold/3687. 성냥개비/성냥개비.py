t = int(input())
dp = ['', '', '1', '7', '4', '2', '6', '8', '10', '18', '22']

for _ in range(t):
    n = int(input())

    # 가장 큰 수
    if n % 2 == 0:
        maxNum = (n // 2) * '1'
    else:
        maxNum = '7' + (n // 2 - 1) * '1'

    # 가장 작은 수
    if n <= 10:
        minNum = dp[n]
    else:
        if n % 7 == 0:
            minNum = '8' * (n // 7)
        elif n % 7 == 1:
            minNum = '10' + '8' * (n // 7 - 1)
        elif n % 7 == 2:
            minNum = '18' + '8' * (n // 7 - 1)
        elif n % 7 == 3:
            minNum = '200' + '8' * (n // 7 - 2)
        elif n % 7 == 4:
            minNum = '20' + '8' * (n // 7 - 1)
        elif n % 7 == 5:
            minNum = '28' + '8' * (n // 7 - 1)
        elif n % 7 == 6:
            minNum = '68' + '8' * (n // 7 - 1)

    print(minNum, maxNum)