# 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동
# 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 레버를 당겨서만 열 수 있다.
# 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동
# 출발 - 레버 - 문

from collections import deque

def solution(maps):
    
    # 시작 점을 찾는 함수
    def findS(board, row, col):
        for i in range(row):
            for j in range(col):
                if board[i][j] == "S":
                    return i, j
    
    # target 까지 최단 거리를 찾는 bfs 함수
    def bfs(board, i, j, target):
        visited = [[-1]*m for _ in range(n)]
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            
            # 도착 지점에 도착하면 거리와 위치 값 반환
            if board[x][y] == target:
                return visited[x][y], x, y
            
            for k in range(4):
                nx = x + di[k]
                ny = y + dj[k]

                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "X" and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
        return -1, -1, -1
        
    n = len(maps)
    m = len(maps[0])
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    # 시작 점 찾기
    si, sj = findS(maps, n, m)
    
    # 레버까지의 최단 거리와 위치 찾기
    minL, li, lj = bfs(maps, si, sj, "L")
    # 도착할 수 없으면 -1 반환
    if minL == -1:
        return -1
    
    # 레버를 당기고
    # 출구까지의 최단 거리와 위치 찾기
    minE, ei, ej = bfs(maps, li, lj, "E")
    # 도착할 수 없으면 -1 반환
    if minE == -1:
        return -1
    
    return minL + minE