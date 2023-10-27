from collections import deque

def bfs(x):
    totalCnt = 0

    deq = deque()
    deq.append(x)
    visited[x] = 0

    while deq:
        x = deq.popleft()

        if x == k:
            totalCnt += 1
            continue

        if visited[k] != -1 and visited[k] < visited[x]:
            return visited[k], totalCnt

        for nextX in [x-1, x+1, x*2]:
            if 0 <= nextX <= 100000 and (visited[nextX] == -1 or visited[x] + 1 == visited[nextX]):
                visited[nextX] = visited[x] + 1
                deq.append(nextX)

    return visited[k], totalCnt


n, k = map(int, input().split())

visited = [-1] * 100001
minV, cnt = bfs(n)
print(minV)
print(cnt)