def solution(land):

    def bfs(x, y):
        nonlocal totalOil, visited, n, m, di, dj
        
        col = {y}
        oil = 1
        stack = [(x, y)]
        visited[x][y] = 1
        
        while stack:
            x, y = stack.pop()
            
            for k in range(4):
                nx = x + di[k]
                ny = y + dj[k]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    oil += 1
                    stack.append((nx, ny))
                    col.add(ny)
                    
        # 현재 영역의 석유량 포함 열에 저장
        for c in col:
            totalOil[c] += oil
    
    
    n = len(land)
    m = len(land[0])
    totalOil = [0]*m
    visited = [[0]*m for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    # 석유 덩어리 탐색
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i, j)

    return max(totalOil)