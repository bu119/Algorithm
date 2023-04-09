import sys, heapq
input = sys.stdin.readline
def bfs(v):
    heap = []
    heapq.heappush(heap, [0, v])

    while heap:
        cnt, v = heapq.heappop(heap)

        for i in range(1, A[v]+1):
            if v+i >= n - 1:
                return cnt + 1

            if 0 < visited[v+i] <= cnt+1:
                continue
            visited[v+i] = cnt+1
            heapq.heappush(heap, [cnt + 1, v+i])

    return -1


n = int(input())
A = list(map(int,input().split()))

if n == 1:
    print(0)
else:
    visited = [0]*n
    print(bfs(0))