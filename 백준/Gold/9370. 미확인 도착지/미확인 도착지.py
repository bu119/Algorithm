import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    visited = [maxV] * (n+1)
    visited[x] = 0
    visitedGH = set()
    # 총 거리 현재 위치, g와 h 교차로 통과 여부
    heap = [(0, x, False)]
    # g와 h 교차로 통과 여부 체크
    checkGH = {(g, h), (h, g)}

    while heap:
        currDist, x, gh = heapq.heappop(heap)

        if visited[x] < currDist:
            continue

        for next, dist in graph[x]:
            total = dist + currDist
            # g와 h 통과 여부 변경
            nextGH = gh
            if (x, next) in checkGH:
                nextGH = True

            if total < visited[next] or (total == visited[next] and nextGH and (next, total, nextGH) not in visitedGH):
                visited[next] = total
                heapq.heappush(heap, (total, next, nextGH))
                visitedGH.add((next, total, nextGH))

                # 목적지에 도착하면 g와 h 교차로 통과 여부 체크 후 값 저장
                if next in destination and nextGH:
                    # 도착 목적지에 최소 거리 저장
                    arrival[next] = min(arrival[next], total)

    return visited


tc = int(input())
maxV = 50000001
for _ in range(tc):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    # s는 예술가들의 출발지, 예술가는 g와 h 교차로 사이에 있는 도로를 지나갔다.
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    destination = set()
    arrival = dict()
    for _ in range(t):
        city = int(input())
        destination.add(city)
        arrival[city] = maxV+1
    visitedDist = dijkstra(s)
    for i in sorted(destination):
        if visitedDist[i] == arrival[i]:
            print(i, end=" ")