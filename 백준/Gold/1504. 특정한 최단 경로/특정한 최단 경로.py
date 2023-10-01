import heapq
import sys
input = sys.stdin.readline

# start에서 각 점의 최단거리
def dijkstra(start):
    visited = [INF]*(n+1)
    heap = []
    # 최단거리, 시작 위치 저장
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        dist, v,  = heapq.heappop(heap)

        if visited[v] < dist:
            continue

        for w, nextDist in graph[v]:
            totalDist = dist + nextDist
            if totalDist < visited[w]:
                heapq.heappush(heap, (totalDist, w))
                visited[w] = totalDist

    return visited


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

# 최댓값
INF = int(1e9)

# 출발점이 다른 3가지 경우
start1 = dijkstra(1)
startV1 = dijkstra(v1)
startV2 = dijkstra(v2)
# 1, v1, v2, n
case1 = start1[v1] + startV1[v2] + startV2[n]
# 1, v2, v1, n
case2 = start1[v2] + startV2[v1] + startV1[n]

ans = min(case1, case2)
if ans < INF:
    print(ans)
else:
    print(-1)