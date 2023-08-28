from collections import deque

# 1. 해안가 찾기 (bfs)
def findCoast(i, j):
	# 해안가 위치 저장 (섬과 맞닿은 바다 위치 저장)
    coast = set()
    stack = [(i,j)]
    # 섬 방문 체크
    visited[i][j] = islandNum

    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] != islandNum:
                # 섬이면 방문 체크, 해안가에 맞닿은 바다도 미리 방문체크
                visited[ni][nj] = islandNum
                # 바다면 섬과 맞닿아 있는 바다면 위치, 다리 길이 개수 1로 초기화 하여 저장
                if ocean[ni][nj] == '0':
                    coast.add((ni, nj, 1))
                else:
                    stack.append((ni,nj))
    return coast


# 2. 해안가에서 다른 섬해안가 까지 최단거리 찾기
def bfs(coast):
    # 거리 저장
    deq = deque(coast)

    while deq:
        x, y, dist = deq.popleft()

        if dist >= minV:
            return 10000

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            # 구역안에 들어오고, 탐색을 시작하는 섬에서 방문 안했으면 탐색
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != islandNum:
                # 바다면 탐색
                if ocean[nx][ny] == '0':
                    visited[nx][ny] = islandNum
                    deq.append((nx, ny, dist+1))
                else:
                    # 섬 만나면 거리 반환
                    return dist


n = int(input())
ocean = [input().split() for _ in range(n)]
visited = [[0]*n for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
minV = 10000
# 섬에 번호를 붙여 구분한다.
islandNum = 0
for i in range(n):
    for j in range(n):
        # 방문 안한 섬이면
        if ocean[i][j] == '1' and visited[i][j] == 0:
            islandNum += 1
            # 해당 섬의 해안가 찾기
            coast = findCoast(i, j)
            # 최단 거리 찾기
            minV = min(minV, bfs(coast))
            if minV == 1:
                print(1)
                exit()
print(minV)
