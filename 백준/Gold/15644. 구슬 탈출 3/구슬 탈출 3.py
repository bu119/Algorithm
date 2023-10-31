from collections import deque

def lean(d, x, y):
    dist = 0

    while board[x+di[d]][y+dj[d]] != "#" and board[x][y] != "O":
        x += di[d]
        y += dj[d]
        dist += 1
    return dist, x, y


def bfs(ri, rj, bi, bj):
    deq = deque()
    deq.append((0, ri, rj, bi, bj, ""))
    # 방문 체크
    visited = set()
    visited.add((ri, rj, bi, bj))
    while deq:
        cnt, ri, rj, bi, bj, move = deq.popleft()

        if cnt > 10:
            print(-1)
            return

        if board[ri][rj] == "O":
            print(cnt)
            print(move)
            return

        for k in range(4):
            rdist, nri, nrj = lean(k, ri, rj)
            bdist, nbi, nbj = lean(k, bi, bj)

            if board[nbi][nbj] == "O":
                continue

            if nri == nbi and nrj == nbj:
                if rdist < bdist:
                    nbi -= di[k]
                    nbj -= dj[k]
                else:
                    nri -= di[k]
                    nrj -= dj[k]
            if (nri, nrj, nbi, nbj) not in visited:
                visited.add((nri, nrj, nbi, nbj))
                deq.append((cnt+1, nri, nrj, nbi, nbj, move+dir[k]))
    print(-1)
    return


n, m = map(int, input().split())
board = []
for i in range(n):
    row = input()
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            ri, rj = i, j
        elif row[j] == 'B':
            bi, bj = i, j

di = [0,1,0,-1]
dj = [1,0,-1,0]
dir = {0:"R", 1:"D", 2:"L", 3:"U"}

bfs(ri, rj, bi, bj)