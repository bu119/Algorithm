import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
maxCost = sum(cost) + 1
# 최소 비용 저장
ans = maxCost
# 각 앱 까지 각 비용에 해당하는 최대 메모리 저장
dp = [[0]*maxCost for _ in range(n+1)]
# 앱 번호
for i in range(1, n+1):
    # 최대 비용 (배낭 무게) / 비활성화 안할 때(0원)도 고려
    for j in range(maxCost):
        # i번째 앱까지 활용해 j비용으로 비활성화 할 수 있는 최대 메모리 계산
        # 앱의 비용이 현재 배낭 무게보다 크면 이전 최대 가치를 가져온다.
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            # 현재 앱의 비용이 배낭 무케보다 크거나 같으면 j비용으로 확보 가능한 최대 메모리 갱신
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])
# 최소 비용 구하기          
for k in range(maxCost):
    if m <= dp[n][k]:
        print(k)
        break