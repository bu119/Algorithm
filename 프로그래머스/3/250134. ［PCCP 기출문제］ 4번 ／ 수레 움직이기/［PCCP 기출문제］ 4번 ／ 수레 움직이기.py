from copy import deepcopy
    
def solution(maze):
    
    # 공이 이동 가능한 위치 반환
    def move(curr, visited):
        nonlocal maze, n, m
        
        possiblePosi = []

        for k in range(4):
            ni = curr[0] + di[k]
            nj = curr[1] + dj[k]
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 5 and visited[ni][nj] == 0:
                possiblePosi.append((ni, nj))
        
        return possiblePosi
        
    # 퍼즐을 푸는데 필요한 최소 턴 탐색
    def dfs(idx, currRed, currBlue, visitedRed, visitedBlue, isArrivedRed, isArrivedBlue):
        nonlocal minV
        # 이동한 공 방문 체크
        visitedRed[currRed[0]][currRed[1]] = 1
        visitedBlue[currBlue[0]][currBlue[1]] = 1
        
        if minV <= idx:
            return
        
        # 모두 도착
        if isArrivedRed and isArrivedBlue:
            if idx < minV:
                minV = idx
            return
        
        redPosi = []
        bluePosi = []
        
        # 빨간공 도착 안했을 때 이동 가능한 위치
        if not isArrivedRed:
            redPosi = move(currRed, visitedRed)
            # 이동 가능 한 위치 없음
            if not redPosi:
                return
            
        # 파란공 도착 안했을 때 이동 가능한 위치
        if not isArrivedBlue:
            bluePosi = move(currBlue, visitedBlue)
            # 이동 가능 한 위치 없음
            if not bluePosi:
                return        
            
        # 빨강 도착 -> 파란공 이동
        if isArrivedRed and not isArrivedBlue:
            for nextBlue in bluePosi:
                if currRed == nextBlue:
                    continue
                dfs(idx+1, currRed, nextBlue, visitedRed, deepcopy(visitedBlue), isArrivedRed, ba == nextBlue)
                
        # 파랑 도착 -> 빨간공 이동
        elif not isArrivedRed and isArrivedBlue:
            for nextRed in redPosi:
                if nextRed == currBlue:
                    continue
                dfs(idx+1, nextRed, currBlue, deepcopy(visitedRed), visitedBlue, ra == nextRed, isArrivedBlue)
       # 빨간 공, 파란 공 모두 이동 
        for nextRed in redPosi:
            for nextBlue in bluePosi:
                # 동시에 같은 칸으로 이동 불가
                if nextRed == nextBlue:
                    continue
                # 자리 바꾸기 불가
                if currRed == nextBlue and nextRed == currBlue:
                    continue

                dfs(idx+1, nextRed, nextBlue, deepcopy(visitedRed), deepcopy(visitedBlue), ra == nextRed, ba == nextBlue)
                    
                    
    n = len(maze)
    m = len(maze[0])

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rs = (i, j)
            elif maze[i][j] == 2:
                bs = (i, j)
            elif maze[i][j] == 3:
                ra = (i, j)
            elif maze[i][j] == 4:
                ba = (i, j)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
              
    visitedRed = [[0]*m for _ in range(n)]
    visitedBlue = [[0]*m for _ in range(n)]
    
    # 퍼즐을 푸는데 필요한 최소 턴
    minV = 400
    # 퍼즐 탐색
    dfs(0, rs, bs, visitedRed, visitedBlue, rs==ra, bs==ba)
    # 퍼즐을 풀 수 없는 경우
    if minV == 400:
        minV = 0
    return minV