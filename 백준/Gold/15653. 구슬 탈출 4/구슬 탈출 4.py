from collections import deque

def leanBoard(d, x, y):
    cnt = 0

    while board[x+di[d]][y+dj[d]] != "#" and board[x][y] != "O":
        x += di[d]
        y += dj[d]
        cnt += 1

    return cnt, x, y


def bfs(rx, ry, bx, by):
    deq = deque()
    deq.append((0, rx, ry, bx, by))
    # 방문체크
    visited = set()
    visited.add((rx, ry, bx, by))

    while deq:
        moveCnt, rx, ry, bx, by = deq.popleft()

        if board[rx][ry] == "O":
            return moveCnt

        for k in range(4):
            rCnt, rnx, rny = leanBoard(k, rx, ry)
            bCnt, bnx, bny = leanBoard(k, bx, by)

            if board[bnx][bny] == "O":
                continue

            if rnx == bnx and rny == bny:
                if rCnt < bCnt:
                    bnx -= di[k]
                    bny -= dj[k]
                else:
                    rnx -= di[k]
                    rny -= dj[k]

            if (rnx, rny, bnx, bny) not in visited:
                visited.add((rnx, rny, bnx, bny))
                deq.append((moveCnt+1, rnx, rny, bnx, bny))

    return -1


n, m = map(int, input().split())
board = []
for i in range(n):
    row = input()
    board.append(row)
    for j in range(m):
        if row[j] == "R":
            ri, rj = i, j
        elif row[j] == "B":
            bi, bj = i, j

di = [0,1,0,-1]
dj = [1,0,-1,0]

print(bfs(ri, rj, bi, bj))