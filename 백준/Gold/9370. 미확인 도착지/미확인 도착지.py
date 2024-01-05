import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    visited = [maxV] * (n+1)
    visited[x] = 0
    # 총 거리, 현재 위치
    heap = [(0, x)]

    while heap:
        currDist, x = heapq.heappop(heap)

        if visited[x] < currDist:
            continue

        for next, dist in graph[x]:
            total = dist + currDist
            if total < visited[next]:
                visited[next] = total
                heapq.heappush(heap, (total, next))

    return visited


tc = int(input())
maxV = 50000001
for _ in range(tc):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    # s는 출발지, g-h 도로를 지남
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    checkGH = {(g, h), (h, g)}
    for _ in range(m):
        a, b, d = map(int, input().split())
        # g-h 도로를 지나면 소수점으로 차별화한다. (같은 거리일 때도 차별회된다.)
        if (a, b) in checkGH:
            d -= 0.5
        graph[a].append((b, d))
        graph[b].append((a, d))
    destination = sorted(int(input()) for _ in range(t))
    visitedDist = dijkstra(s)
    for i in destination:
        # g-h 도로를 지나면 출력
        if type(visitedDist[i]) != int:
            print(i, end=" ")