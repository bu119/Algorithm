def dfs(idx, ssum):

    if idx == n:
        return

    visited[ssum+s[idx]] = 1
    dfs(idx + 1, ssum)
    dfs(idx + 1, ssum+s[idx])


n = int(input())
s = list(map(int, input().split()))
total = sum(s)
visited = [0]*(total+2)
dfs(0,0)

for j in range(1, total+2):
    if not visited[j]:
        print(j)
        break