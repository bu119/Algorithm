from collections import deque

def bfs(posi):
    deq = deque()
    deq.append([posi,0])

    visited = set()
    visited.add(posi)

    while deq:
        x, time = deq.popleft()

        if x == k:
            return time

        for i in [x-1, x+1, x*2]:
            if i < 0 or i > 100000:
                continue

            if i not in visited:
                visited.add(i)
                deq.append([i, time+1])

                
n, k = map(int, input().split())
print(bfs(n))