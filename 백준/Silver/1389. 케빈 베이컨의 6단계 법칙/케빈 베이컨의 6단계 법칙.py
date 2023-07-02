import sys
from collections import deque
input = sys.stdin.readline

def bfs(k):
    visited = [0] * (n + 1)
    deq = deque()
    deq.append(k)
    visited[k] = 1

    while deq:
        k = deq.popleft()

        for i in arr[k]:
            if not visited[i]:
                visited[i] = visited[k]+1
                deq.append(i)

    return sum(visited)


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

minV = bfs(1)
num = 1
for k in range(2, n+1):
    total = bfs(k)
    if total < minV:
        num = k
        minV = total

print(num)