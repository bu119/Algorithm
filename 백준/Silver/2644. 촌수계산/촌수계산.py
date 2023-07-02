n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [0]*(n+1)
def dfs(k, cnt):

    if k == p2:
        print(cnt)
        exit(0)

    for i in arr[k]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)


dfs(p1, 0)

print(-1)