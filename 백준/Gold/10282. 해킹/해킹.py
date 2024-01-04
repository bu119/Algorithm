import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    visited = [10000001]*(n+1)
    visited[x] = 0
    heap = [(0, x)]
    while heap:
        currTime, x = heapq.heappop(heap)

        if visited[x] < currTime:
            continue

        for nextCom, nextTime in graph[x]:
            totalTime = currTime + nextTime
            if totalTime < visited[nextCom]:
                visited[nextCom] = totalTime
                heapq.heappush(heap, (totalTime, nextCom))

    return visited


t = int(input())
for _ in range(t):
    # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    visitedTime = dijkstra(c)
    infectionCnt = 0
    infectionTime = 0
    for i in visitedTime:
        if i != 10000001:
            infectionCnt += 1
            infectionTime = max(infectionTime, i)
    print(infectionCnt, infectionTime)