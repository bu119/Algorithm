import heapq

def solution(board):
    # 미끄러지기 (벽이나 장애물 만나면 멈춤)
    def move_robot(ni, nj, d):
        while 0 <= ni + di[d] < n and 0 <= nj + dj[d] < m and board[ni + di[d]][nj + dj[d]] != 'D':
            ni += di[d]
            nj += dj[d]

        return ni, nj


    def dijkstra(x, y):
        visited = [[maxV]*m for _ in range(n)]
        heap = [(0, x, y)]
        visited[x][y] = 0

        while heap:
            cost, x, y = heapq.heappop(heap)
            # 목표지점에 도달하면 멈춤
            if board[x][y] == 'G':
                return cost
            # 이미 지난 곳이면 탐색 안함
            if visited[x][y] < cost:
                continue

            for k in range(4):
                nx, ny = move_robot(x, y, k)
                # 위치 그대로면 탐색 안함
                if x == nx and y == ny:
                    continue
                # 움직이면 횟수 추가
                newCost = cost + 1
                if newCost < visited[nx][ny]:
                    visited[nx][ny] = newCost
                    heapq.heappush(heap, (newCost, nx, ny))
        # 목표 위치에 도달할 수 없으면
        return -1
    
    maxV = float('inf')
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    n = len(board)
    m = len(board[0])
    
    start = [-1, -1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start[0] = i
                start[1] = j
                break
        if start[0] != -1:
            break

    return dijkstra(start[0], start[1])
