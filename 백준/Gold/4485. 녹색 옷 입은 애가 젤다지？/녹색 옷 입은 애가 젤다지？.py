import sys, heapq
input = sys.stdin.readline

def dijkstra(i, j):
    # 최대 잃을 수 있는 금액은 10*n*n
    visited = [[10*n*n+1]*n for _ in range(n)]
    heap = [(graph[i][j], i, j)]
    visited[i][j] = graph[i][j]

    while heap:
        cost, i, j = heapq.heappop(heap)

        if visited[i][j] < cost:
            continue

        if i == n-1 and j == n-1:
            return visited[n-1][n-1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                next_cost = cost + graph[ni][nj]
                if next_cost < visited[ni][nj]:
                    visited[ni][nj] = next_cost
                    heapq.heappush(heap, (next_cost, ni, nj))
    return visited[n-1][n-1]


# 도둑루피를 최소한으로 만나기
# (0,0) -> (n-1,n-1)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
idx = 0
while True:
    idx += 1
    n = int(input())
    # 종료 조건
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {idx}: {dijkstra(0, 0)}')