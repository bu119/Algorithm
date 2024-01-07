import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    dist = [2000000001] * (n + 1)
    # 첫번째 집하장 저장
    firstPath = ['-']*(n+1)
    dist[x] = 0
    # 시간, 현재 위치
    heap = [(0, x)]
    while heap:
        currTime, curr = heapq.heappop(heap)

        if dist[curr] < currTime:
            continue

        for next, nextTime in graph[curr]:
            totalT = currTime + nextTime
            if totalT < dist[next]:
                dist[next] = totalT
                heapq.heappush(heap, (totalT, next))
                if firstPath[curr] == '-':
                    firstPath[next] = next
                else:
                    firstPath[next] = firstPath[curr]
    return firstPath[1:]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n+1):
    print(*dijkstra(i))