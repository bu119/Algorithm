import sys
input = sys.stdin.readline

# 파이어볼 이동 함수
def moveFireball(x, y):
    global newGraph, newFireballs

    for _ in range(len(graph[x][y])):
        m, s, d = graph[x][y].pop()
        ni = (x + s * di[d]) % n
        nj = (y + s * dj[d]) % n

        newGraph[ni][nj].append((m, s, d))
        newFireballs.add((ni, nj))

#  2개 이상의 파이어볼이 있는 칸에서 일어나는 동작 함수
def sumFireballs(x, y):
    sumM = 0
    sumS = 0
    oddCnt = 0
    evenCnt = 0
    fireballCnt = len(newGraph[x][y])

    for _ in range(fireballCnt):
        m, s, d = newGraph[x][y].pop()
        sumM += m
        sumS += s
        if d % 2:
            oddCnt += 1
        else:
            evenCnt += 1

    newM = sumM//5
    # 질량이 0인 파이어볼은 소멸되어 없어진다.
    if newM == 0:
        return
    # 나누어진 속도
    newS = sumS//fireballCnt
    # 홀수
    if oddCnt == fireballCnt or evenCnt == fireballCnt:
        newD = [0, 2, 4, 6]
    else:
        newD = [1, 3, 5, 7]

    for nd in newD:
        newGraph[x][y].append((newM, newS, nd))


n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
fireballs = set()
# 방향 0,1,2,3,4,5,6,7
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    # 위치 (r, c)는 r행 c열
    # 질량은 m이고, 방향은 d, 속력은 s
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    graph[r][c].append((m, s, d))
    fireballs.add((r, c))

ans = 0

for _ in range(k):
    newGraph = [[[] for _ in range(n)] for _ in range(n)]
    newFireballs = set()
    # 모든 파이어볼 이동
    for i, j in fireballs:
        moveFireball(i, j)
    # 2개이상 존재하면 나누기
    for i, j in newFireballs:
        if len(newGraph[i][j]) > 1:
            sumFireballs(i, j)

    fireballs = newFireballs
    graph = newGraph

for i, j in fireballs:
    while graph[i][j]:
        ans += graph[i][j].pop()[0]
print(ans)