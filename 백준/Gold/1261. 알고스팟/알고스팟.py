import sys, heapq
input = sys.stdin.readline

def bfs(i,j, cnt):

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
                # 벽이면 cnt에 1 더 해진다
                heapq.heappush(heap, (cnt+board[ni][nj], ni, nj))


m, n = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

print(bfs(0,0,0))