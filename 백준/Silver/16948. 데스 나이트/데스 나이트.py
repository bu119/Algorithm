from collections import deque
def bfs(i,j):
    deq = deque()
    deq.append((i,j,0))
    visited[i][j] = 1

    while deq:
        i, j, cnt = deq.popleft()

        if i == r2 and j == c2:
            return cnt

        for k in range(6):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = 1
                deq.append((ni,nj,cnt+1))
    return -1

n = int(input())
r1,c1,r2,c2 = map(int,input().split())
visited = [[0]*n for _ in range(n)]

di = [-2,-2,0,0,2,2]
dj = [-1,1,-2,2,-1,1]
print(bfs(r1,c1))