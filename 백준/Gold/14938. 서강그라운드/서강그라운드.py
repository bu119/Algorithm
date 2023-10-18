import heapq

def dijkstra(start):
    # 최소 거리, 위치
    heap = [(0, start)]
    visited[start] = 0
    # 범위 내 지역 저장
    getItem.add(start)

    while heap:
        dist, curr = heapq.heappop(heap)

        if visited[curr] < dist:
            continue

        for next, d in graph[curr]:
            sumDist = dist + d
            if sumDist < visited[next]:
                visited[next] = sumDist
                getItem.add(next)
                heapq.heappush(heap,(sumDist, next))

                
# 각 지점에서 최소거리를 구한다. (다익스트라)
# 최소거리가 m이하인 지점의 아이템을 더한다.
# 각 점의 아이템을 더한 값을 비교하여 최소값을 찾는다.
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

ans = 0
for i in range(1,n+1):
    # 범위 내 지역
    getItem = set()
    # 거리 저장
    visited = [m+1]*(n+1)
    dijkstra(i)
    # 아이템 최대 개수
    totalItems = 0
    for j in getItem:
        totalItems += items[j]
    ans = max(ans, totalItems)
print(ans)