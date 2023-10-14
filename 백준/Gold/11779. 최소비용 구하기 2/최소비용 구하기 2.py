import sys, heapq
input = sys.stdin.readline
def dijkstra(start, end):
    global route
    # 비용 저장
    visited = [10000000001] * (n + 1)
    # 비용, 현재 위치
    heap = [(0, start)]
    # 최소 비용 저장
    visited[start] = 0
    # 경로
    route[start] = [start]

    while heap:
        currCost, city = heapq.heappop(heap)

        # 저장된 비용보다 크면 탐색 안함
        if visited[city] < currCost:
            continue

        for nextCity, moveCost in graph[city]:
            totalCost = currCost + moveCost
            # 비용이 적으면 갱신
            if totalCost < visited[nextCity]:
                # 최소 비용 저장
                visited[nextCity] = totalCost
                # 경로 갱신
                route[nextCity] = route[city] + [nextCity]

                heapq.heappush(heap, (totalCost, nextCity))

    return visited[end]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())

route = [[] for _ in range(n+1)]
print(dijkstra(start, end))
print(len(route[end]))
print(*route[end])