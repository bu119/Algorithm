import heapq
import sys
input = sys.stdin.readline

def bfs(i,j, cnt):
    global ans

    heap = [(cnt,i,j)]
    visited[i][j] = 1

    while heap:
        cnt, i, j = heapq.heappop(heap)

        if i == n-1 and j == m-1:
            return cnt

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1

                if board[ni][nj] == '0':
                    heapq.heappush(heap, (cnt, ni, nj))
                else:
                    heapq.heappush(heap, (cnt+1, ni, nj))


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

print(bfs(0,0,0))