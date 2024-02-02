from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    # 돌린 횟수 저장
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    # 처음 상태 바르게 변경
    if graph[x][y] == '/':
        visited[x][y] += 1
        graph[x][y] = '\\'

    deq = deque()
    deq.append((x, y, graph[x][y]))

    while deq:
        cx, cy, currState = deq.popleft()

        if cx == n-1 and cy == m-1 and currState != '/':
            return visited[cx][cy]

        # 평행 방향 제외
        if currState == '/':
            direction = [0, 2, 4, 5, 6, 7]
        else:
            direction = [1, 3, 4, 5, 6, 7]

        for k in direction:
            nx = cx + di[k]
            ny = cy + dj[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:

                if canMove(k, currState, graph[nx][ny]):
                    visited[nx][ny] = visited[cx][cy]
                    deq.appendleft((nx, ny, graph[nx][ny]))
                else:
                    visited[nx][ny] = visited[cx][cy] + 1
                    deq.append((nx, ny, changeState[graph[nx][ny]]))

    return 'NO SOLUTION'

# 전자 회로 상태로 이동 가능 여부 체크
def canMove(d, state1, state2):
    # 대각선 위치는 전자 회로의 상태가 같을 때 이동 가능
    if d in {0, 1, 2, 3}:
        return state1 == state2
    # 상하좌우는 다른 상태일 때 이동 가능
    else:
        return state1 != state2


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
# 8방향 (대각선 4방향, 좌우 4방향)
di = [-1, 1, 1, -1, 0, 1, 0, -1]
dj = [1, 1, -1, -1, 1, 0, -1, 0]
# 상태 변경
changeState = {'/': '\\', '\\': '/'}
# 현재 위치, 돌린 횟수
print(bfs(0, 0))