from collections import deque
import sys
input = sys.stdin.readline

def bfs(rx, ry, bx, by):
    deq = deque()
    deq.append((rx, ry, bx, by))
    # 방문체크
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = True
    cnt = 0
    while deq:
        # 같은 이동 횟수끼리 탐색
        for _ in range(len(deq)):
            rx, ry, bx, by = deq.popleft()
            # 움직인 횟수가 10회 초과면 -1 출력
            if cnt > 10:
                return -1
            # 빨간 구슬의 위치가 구멍이면 탐색 종료
            if board[rx][ry] == 'O':
                return cnt
            # 4방향 탐색
            for k in range(4):
                # 빨간 구슬 이동
                nrx, nry = rx, ry
                while board[nrx][nry] != 'O':
                    nrx += dx[k]
                    nry += dy[k]
                    # 벽이면 이동 종료, 이전 위치로 되돌림
                    if board[nrx][nry] == '#':
                        nrx -= dx[k]
                        nry -= dy[k]
                        break

                # 파란 구슬 이동
                nbx, nby = bx, by
                while board[nbx][nby] != 'O':
                    nbx += dx[k]
                    nby += dy[k]
                    # 벽이면 이동 종료, 이전 위치로 되돌림
                    if board[nbx][nby] == '#':
                        nbx -= dx[k]
                        nby -= dy[k]
                        break
                # 파란 구슬이 구멍에 들어가는 경우 무시
                if board[nbx][nby] == 'O':
                    continue
                # 두 구슬의 위치가 같으면 이동거리로 순서 구분
                # 더 많이 이동한 구슬이 더 늦게 도착, 구슬 한칸 뒤로 이동
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[k]
                        nry -= dy[k]
                    else:
                        nbx -= dx[k]
                        nby -= dy[k]
                # 방문 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    deq.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1


n, m = map(int, input().split())
board = []
for i in range(n):
    arr = list(input())
    board.append(arr)
    for j in range(m):
        if arr[j] == 'R':
            ri, rj = i, j
        elif arr[j] == 'B':
            bi, bj = i, j

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

print(bfs(ri, rj, bi, bj))