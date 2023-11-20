from collections import deque
import sys
input = sys.stdin.readline

# 두 보물 사이의 최단거리 찾는 함수
def bfs(i, j):
    global maxTime
    
    visited = [[0]*m for _ in range(l)]
    visited[i][j] = 1
    deq = deque()
    deq.append((i, j))
    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < l and 0 <= nj < m and graph[ni][nj] == 'L' and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni, nj))

    return visited[i][j] - 1

# 바다와 연결된 땅인지 확인 (가장 자리인 지 판별)
def is_edge(i, j):
    # 지도 모서리 부분이면 탐색
    if i == 0 or i == l-1 or j == 0 or j == m-1:
        return True
    # 지도 모서리 부분이 아닐 때 (ㅣ, ㅡ 모양으로 길이 더 있을 때)
    # 아래위 길이 있을 때
    if graph[i-1][j] == "L" and graph[i+1][j] == "L":
        return False
    # 좌우 길이 있을 때
    if graph[i][j-1] == "L" and graph[i][j+1] == "L":
        return False
    # ㄴ, ㄱ, ㄷ을 돌린 모양으로 바다에 인접해 있으면 가장자리
    return True


l, m = map(int, input().split())
graph = [input() for _ in range(l)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 최대 시간 저장
maxTime = 0
# 보물 하나의 위치 선정
for x in range(l):
    for y in range(m):
        # 바다와 연결된 육지인 경우 탐색 (가장 자리)
        if graph[x][y] == 'L' and is_edge(x, y):
            maxTime = max(maxTime, bfs(x, y))
print(maxTime)