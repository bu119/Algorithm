n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                continue

            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 수행된 결과를 출력
for a in range(n):
    for b in range(n):
        print(graph[a][b], end=' ')
    print()