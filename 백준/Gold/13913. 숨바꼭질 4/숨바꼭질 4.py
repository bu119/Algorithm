from collections import deque

def bfs(v):
    deq = deque()
    deq.append((v, 0))
    # visited[v] = v
    while deq:
        v, moveCnt = deq.popleft()

        if v == k:
            return moveCnt

        for w in [v - 1, v + 1, v * 2]:
            if 0 <= w <= 100000 and visited[w] == -1:
                deq.append((w, moveCnt+1))
                visited[w] = v


n, k = map(int, input().split())
if n > k:
    print(n-k)
    print(*range(n, k-1, -1))

else:
    visited = [-1] * 100001
    cnt = bfs(n)
    print(cnt)

    # 경로 찾기
    route = []
    posi = k
    for _ in range(cnt + 1):
        route.append(posi)
        posi = visited[posi]
    print(*reversed(route))