n, m = map(int,input().split())
fuel = [list(map(int,input().split())) for _ in range(n)]

ans = 100*n

def dfs(i, j, ssum, d):
    global ans

    if i == n-1:
        if ans > ssum:
            ans = ssum
        return

    if ans < ssum:
        return

    for k in [-1,0,1]:
        if k == d:
            continue
        nj = j + k
        if 0 <= nj < m:
            dfs(i+1, nj, ssum+fuel[i+1][nj], k)

for j in range(m):
    dfs(0, j, fuel[0][j], 2)

print(ans)