import heapq

def dijkstra(start, end, n):
    global road_graph, maxV
    charge = [maxV] * (n + 1)

    heap = [(0, start)]
    charge[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if charge[now] < cost:
            continue

        for e, price in road_graph[now]:
            new_cost = cost + price
            if new_cost < charge[e]:
                charge[e] = new_cost
                heapq.heappush(heap, (new_cost, e))

    return charge[end]


def solution(n, s, a, b, fares):
    global road_graph, maxV

    road_graph = [[] for _ in range(n+1)]
    maxV = 0

    for c, d, f in fares:
        road_graph[c].append((d, f))
        road_graph[d].append((c, f))
        maxV += f

    # 각자 바로 가는 경우
    answer = dijkstra(s, a, n) + dijkstra(s, b, n)

    # 합승했다가 찢어지는 경우 (모든 경우 계산)
    for i in range(1, n + 1):

        # 시작점 제외
        if i == s:
            continue

        answer = min(answer, (dijkstra(s, i, n) + dijkstra(i, a, n) + dijkstra(i, b, n)))

    return answer
