import sys, heapq

def dijkstra():
    heap = []
    visited = [maxV] * (n + 1)

    heapq.heappush(heap, (0, 1))
    visited[1] = 0

    while heap:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        time, now = heapq.heappop(heap)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if visited[now] < time:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next, inum in graph[now]:
            # 주기 구하기 (시작 시간 = 주기*m + i번째 신호)
            # dist: 현재 시간
            cycle = (time - inum) // m
            # 나머지 있으면 주기 + 1
            if (time - inum) % m != 0:
                cycle += 1
            # 신호 끝나는 시간: 시작시간 + 1
            totalT = inum + cycle * m

            if totalT + 1 < visited[next]:
                visited[next] = totalT + 1
                heapq.heappush(heap, (totalT + 1, next))

    return visited[n]


input = sys.stdin.readline
# 지역의 수 N, 횡단보도의 주기 M
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
maxV = 770000000000
# 모든 간선 정보를 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

print(dijkstra())