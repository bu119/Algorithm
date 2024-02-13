t = int(input())
for _ in range(t):
    # 동전 개수
    n = int(input())
    # 동전의 각 금액
    coins = [0] + list(map(int, input().split()))
    # 만드는 금액
    m = int(input())
    dp = [[0] * (m+1) for _ in range(n+1)]
    # 각 동전으로 0을 만들 수 있는 경우는 무조건 1가지씩 존재
    for i in range(1, n+1):
        dp[i][0] = 1

    # 행: 동전 번호
    for k in range(1, n+1):
        # 열: 최대 가치
        for w in range(1, m+1):
            # dp[2][10]: 1 ~ 2번째 동전을 사용하여 10을 만드는 경우의 수 (최대 가치를 배낭의 무게라 칭하겠다.)
            # 이전 동전까지 w를 만드는 경우의 수를 추가 (k번째 동전을 사용하지 않음)
            dp[k][w] = dp[k-1][w]
            # 배낭에 동전을 넣을수 있으면 k 번째 동전을 사용한 경우의 수 추가
            if w - coins[k] >= 0:
                # 동전 크기를 뺀 무게 배낭까지 만들수 있는 경우의 수를 추가
                dp[k][w] += dp[k][w-coins[k]]
    print(dp[n][m])