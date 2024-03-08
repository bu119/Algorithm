from collections import deque

def solution(board):
    # 미끄러지기 (벽이나 장애물 만나면 멈춤)
    def move_robot(ni, nj, d):
        while 0 <= ni + di[d] < n and 0 <= nj + dj[d] < m and board[ni + di[d]][nj + dj[d]] != 'D':
            ni += di[d]
            nj += dj[d]

        return ni, nj


    def bfs(x, y):
        visited = [[-1]*m for _ in range(n)]
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 0

        while queue:
            x, y = queue.popleft()
            # 목표지점에 도달하면 멈춤
            if board[x][y] == 'G':
                return visited[x][y]

            for k in range(4):
                nx, ny = move_robot(x, y, k)
                # 이동 위치가 변함없으면 탐색 안함
                if x == nx and y == ny:
                    continue
                # 안 간 곳 이면 방문체크, 탐색 진행
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        # 목표 위치에 도달할 수 없으면
        return -1
    

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    n = len(board)
    m = len(board[0])
    
    start = [-1, -1]
    # 시작점 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start[0] = i
                start[1] = j
                break
        if start[0] != -1:
            break

    return bfs(start[0], start[1])
