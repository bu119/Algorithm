import sys, heapq
input = sys.stdin.readline

def dijkstra(x, y, turnCnt):
    # 돌린 횟수 저장
    visited = [[250001] * m for _ in range(n)]
    heap = [(turnCnt, x, y, graph[x][y])]
    visited[x][y] = turnCnt

    while heap:
        turnCnt, cx, cy, currState = heapq.heappop(heap)

        if visited[cx][cy] < turnCnt:
            continue

        if cx == n-1 and cy == m-1:
            return turnCnt

        # 평행 방향 제외
        if currState == '/':
            direction = [0, 2, 4, 5, 6, 7]
        else:
            direction = [1, 3, 4, 5, 6, 7]

        for k in direction:
            nx = cx + di[k]
            ny = cy + dj[k]
            if 0 <= nx < n and 0 <= ny < m:
                totalTurnCnt = turnCnt
                nextState = graph[nx][ny]
                if not canMove(k, currState, nextState):
                    # 마지막 방향은 옳은 방향으로 이미 변경
                    if nx == n-1 and ny == m-1:
                        continue
                    totalTurnCnt += 1
                    nextState = changeState[nextState]

                if totalTurnCnt < visited[nx][ny]:
                    visited[nx][ny] = totalTurnCnt
                    heapq.heappush(heap, (totalTurnCnt, nx, ny, nextState))

    return 'NO SOLUTION'

# 전자 회로 상태로 이동 가능 여부 체크
def canMove(d, state1, state2):
    # 대각선 위치는 전자 회로의 상태가 같을 때 이동 가능
    if d in {0, 1, 2, 3}:
        return state1 == state2
    # 상하좌우는 다른 상태일 때 이동 가능
    else:
        return state1 != state2

# 시작과 끝이 방향 변경 함수
def changeEdge():
    cnt = 0

    if graph[0][0] == '/':
        cnt += 1
        graph[0][0] = '\\'

    if graph[n - 1][m - 1] == '/':
        cnt += 1
        graph[n - 1][m - 1] = '\\'

    return cnt

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
# 8방향 (대각선 4방향, 좌우 4방향)
di = [-1, 1, 1, -1, 0, 1, 0, -1]
dj = [1, 1, -1, -1, 1, 0, -1, 0]
# 상태 변경
changeState = {'/': '\\', '\\': '/'}
# 시작과 끝 방향이 / 이면 먼저 \로 변경
turnCnt = changeEdge()
# 현재 위치, 돌린 횟수
print(dijkstra(0, 0, turnCnt))