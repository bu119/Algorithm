import sys, heapq
input = sys.stdin.readline

def dijkstra(start, roadGraph):
    visited = [100001]*(n+1)
    heap = [(0, start)]
    visited[start] = 0

    while heap:
        totalTime, curr = heapq.heappop(heap)

        # 저장된 시간 보다 많으면 탐색 안할래
        if visited[curr] < totalTime:
            continue

        for next, nextTime in roadGraph[curr]:
            ssumTime = totalTime + nextTime
            if ssumTime < visited[next]:
                visited[next] = ssumTime
                heapq.heappush(heap, (ssumTime, next))
    return visited


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverseGraph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int, input().split())
    # 단방향 도로
    graph[s].append((e,t))
    # 역방향 도로
    reverseGraph[e].append((s,t))


# 가장 오래 걸리는 학생 시간 저장
ans = 0

# x에서 출발하여 각 마을에 도착하는 최단 시간 구하기
startX = dijkstra(x, graph)
# 각 마을에서 x까지 최단 시간 구하기 (역방향을 활용하여 계산)
reverseX = dijkstra(x, reverseGraph)
# 가장 많은 시간을 소비하는 학생 찾기
for i in range(1, n+1):
    if i == x:
        continue
    total = reverseX[i] + startX[i]
    ans = max(ans, total)

print(ans)