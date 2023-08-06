# 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야
# 도로들은 단방향
# 가장 많은 시간을 소비하는 학생
# 모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있
import heapq

def dijkstra(start):
    visited = [100001]*(n+1)
    heap = [(0,start)]
    visited[start] = 0

    while heap:
        totalTime, curr = heapq.heappop(heap)

        # 저장된 시간 보다 많으면 탐색 안할래
        if visited[curr] < totalTime:
            continue

        for next, nextTime in graph[curr]:
            ssumTime = totalTime + nextTime
            if ssumTime < visited[next]:
                visited[next] = ssumTime
                heapq.heappush(heap, (ssumTime, next))
    return visited


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    # 단방향 도로
    graph[s].append((e,t))

ans = 0

# x에서 출발하여 각 마을에 도착하는 최단시간 구하기
startX = dijkstra(x)

# 각 마을에서 x까지 최단시간 구하기
for i in range(1,n+1):
    if i == x:
        continue

    total = dijkstra(i)[x] + startX[i]
    ans = max(ans, total)

print(ans)