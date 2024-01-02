import heapq

def dijkstra(i, j):
    rooms = [(0, i, j)]
    visited = [[2501]*n for _ in range(n)]
    visited[i][j] = 0
    while rooms:
        curr_dist, i, j = heapq.heappop(rooms)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if visited[i][j] < curr_dist:
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                # 흰 방이면 그대로 통과
                next_dist = curr_dist
                # 검정 방이면
                if graph[ni][nj] == '0':
                    next_dist += 1
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if next_dist < visited[ni][nj]:
                    visited[ni][nj] = next_dist
                    heapq.heappush(rooms, (next_dist, ni, nj))

    return visited[n-1][n-1]


# 흰 방이면 0, 검은 방이면 1
# 다익스트라 알고리즘으로 지나야하는 검은 방 최소 개수 세기
n = int(input())
graph = [input() for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
print(dijkstra(0, 0))