import sys
from collections import deque
input = sys.stdin.readline
def bfs(v):
    global ans
    deq = deque()
    deq.append([0, v])

    while deq:
        cnt, v = deq.popleft()

        for i in range(1, A[v]+1):

            if v+i >= n - 1:
                if ans > cnt+1:
                    ans = cnt+1
                visited[n - 1] = 1
                continue

            if visited[v+i] and visited[v+i] <= cnt+1:
                continue
            visited[v + i] = cnt + 1
            deq.append([cnt + 1, v+i])



n = int(input())
A = list(map(int,input().split()))
visited = [0]*n
if n > 1:
    ans = n
    bfs(0)
    if visited[n-1] == 0:
        ans = -1

    print(ans)
else:
    print(0)