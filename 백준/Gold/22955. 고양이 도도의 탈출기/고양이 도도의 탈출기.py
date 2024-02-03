import sys, heapq
input = sys.stdin.readline

def dijkstra(x, y):
    visited = [[10000001]*m for _ in range(n)]
    visited[x][y] = 0
    # 데미지, 고양이 위치
    heap = [(0, x, y)]
    while heap:
        damage, cx, cy = heapq.heappop(heap)

        if visited[cx][cy] < damage:
            continue

        if graph[cx][cy] == 'E':
            return visited[cx][cy]
        # 떨어짐
        if graph[cx][cy] == 'X':
            nx = cx + dx[1]
            ny = cy
            total = damage + 10
            # 아래로~~
            while graph[nx][ny] == 'X' and total < visited[nx][ny]:
                visited[nx][ny] = total
                nx += dx[1]

            if total < visited[nx][ny] and graph[nx][ny] != 'D':
                visited[nx][ny] = total
                heapq.heappush(heap, (total, nx, ny))
        # 사다리 위치
        else:
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'D':
                    # 사다리타고 올라가기, 내려가기
                    if (k == 0 and graph[cx][cy] == 'L') or (k == 1 and graph[nx][ny] == 'L'):
                        total = damage + 5
                    # 좌우 이동
                    elif k == 2 or k == 3:
                        total = damage + 1
                    else:
                        continue

                    if total < visited[nx][ny]:
                        visited[nx][ny] = total
                        heapq.heappush(heap, (total, nx, ny))
    return 'dodo sad'


n, m = map(int, input().split())
graph = []
catI = -1
catJ = -1
for i in range(n):
    row = input()
    graph.append(row)
    if catI != -1 and catJ != -1:
        continue
    for j in range(m):
        if row[j] == 'C':
            catI = i
            catJ = j
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dijkstra(catI, catJ))