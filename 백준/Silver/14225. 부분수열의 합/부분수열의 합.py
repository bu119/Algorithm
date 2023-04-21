def dfs(idx, ssum):

    if idx == n:
        visited[ssum] = 1
        return

    dfs(idx + 1, ssum)
    dfs(idx + 1, ssum+s[idx])


n = int(input())
s = list(map(int, input().split()))
total = sum(s)
visited = [0]*(total+2)
dfs(0,0)

for i in range(1, total+2):
    if not visited[i]:
        print(i)
        break