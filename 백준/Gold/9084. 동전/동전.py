import sys
input = sys.stdin.readline

def findNumberOfCases():
    # 경우의 수 저장
    dp = [0] * (m + 1)
    # 0을 만들 수 있는 경우의 수 1
    dp[0] = 1
    
    for coin in coins:
        # 최대 가치 (배낭 무게)
        for w in range(coin, m + 1):
            # dp[10]: k번째 동전까지 사용해서 10을 만드는 경우의 수
            # 배낭에 k번째 동전이 들어가면 k번째 동전을 뺀 무게 배낭의 경우의 수 추가
            # 1번째, 2번째, ..., k번째 각 동전까지만 사용한 경우의 수를 순차 적으로 추가
            dp[w] += dp[w - coin]
    print(dp[m])

    
t = int(input())
for _ in range(t):
    # 동전 개수
    n = int(input())
    # 동전의 각 금액
    coins = list(map(int, input().split()))
    # 만드는 금액
    m = int(input())
    # 경우의 수 찾기
    findNumberOfCases()