n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[150000] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n + 1):
    graph[i][i] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
# 저장한 최댓값을 출력
for x in range(1, n + 1):
    ssum = 0
    for y in range(1, n + 1):
        if graph[x][y] <= m:
            ssum += items[y]
            
    ans = max(ans, ssum)
    
print(ans)