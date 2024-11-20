from copy import deepcopy

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]
# 왼쪽, 오른쪽, 아래쪽으로 이동 가능
# 첫번째 행은 왼쪽으로만 이동 가능
for k in range(1, m):
    dp[0][k] += dp[0][k-1]

# 나머지 행은 위에서 왼쪽에서
for i in range(1, n):
    # 왼쪽에서 출발하는 값 저장
    left = deepcopy(dp[i])
    # 오른쪽에서 출발하는 값 저장
    right = deepcopy(dp[i])

    for j in range(m):
        # 처음 시작 부분은 위에서 오는 것만 체크
        if j == 0:
            left[j] += dp[i-1][j]
            right[m-1-j] += dp[i-1][m-1-j]
            continue

        # 왼쪽에서 오른쪽으로
        left[j] += max(left[j - 1], dp[i - 1][j])

        # 마지막 행이면 왼쪽, 아래쪽 방향만 체크하므로 오른쪽 방향 체크 안함
        if i == n - 1:
            continue

        # 오른쪽에서 왼쪽으로
        right[m-1-j] += max(right[m-j], dp[i - 1][m-1-j])

    # (i, j) 까지의 최대 가치 찾기 (모든 방향 비교)
    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[n-1][m-1])