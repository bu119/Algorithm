def solution(storage, requests):
    def bfs(alpha, x, y):
        nonlocal visited, answer
        
        stack = [(x, y)]
        visited[x][y] = 1
        
        while stack:
            x, y = stack.pop()
            
            for k in range(4):
                nx = x + di[k]
                ny = y + dj[k]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if storage[nx][ny] == "":
                        stack.append((nx, ny))
                    elif storage[nx][ny] == alpha:
                        # 꺼낼 때마다 answer 감소
                        storage[nx][ny] = ""
                        answer -= 1  
                        
    # 지게차: 출고 요청이 들어온 순간 접근 가능한 컨테이너를 꺼냄
    # 접근이 가능한 컨테이너란 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너
    def use_forklift(alpha):
        nonlocal answer

        # 위아래 탐색
        for i in [0, n-1]:
            for j in range(m):
                if storage[i][j] == alpha:
                    # 꺼낼 때마다 answer 감소
                    visited[i][j] = 1
                    storage[i][j] = ""
                    answer -= 1
                elif storage[i][j] == "" and not visited[i][j]:
                    bfs(alpha, i, j)
        # 좌우 탐색
        for i in range(1, n-1):
            for j in [0, m-1]:
                if storage[i][j] == alpha:
                    # 꺼낼 때마다 answer 감소
                    visited[i][j] = 1
                    storage[i][j] = ""
                    answer -= 1
                elif storage[i][j] == "" and not visited[i][j]:
                    bfs(alpha, i, j)
                    
                    
    n = len(storage)
    m = len(storage[0])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 초기 컨테이너 수
    answer = n*m
    # storage 리스트화
    for row in range(n):
        storage[row] = list(storage[row])
    
    # 각 알파벳 위치 저장
    containers = dict()
    # 각 알파벳 위치 탐색
    for row in range(n):
        for col in range(m):
            containers.setdefault(storage[row][col], set()).add((row, col))
    
    for request in requests:
        # 알파벳 하나 -> 지게차
        # 같은 알파벳이 두 번 반복 -> 크레인
        if len(request) == 1:
            # 방문 체크
            visited = [[0]*m for _ in range(n)]
            use_forklift(request)            
        else:
            if request[0] not in containers:
                continue
            # 꺼낸 컨테이너 제거
            for row, col in containers.pop(request[0]):
                if storage[row][col] != "":
                    storage[row][col] = ""
                    answer -= 1  # 꺼낼 때마다 answer 감소
    return answer