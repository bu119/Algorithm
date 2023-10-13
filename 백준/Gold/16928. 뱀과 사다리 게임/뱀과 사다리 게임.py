from collections import deque

def bfs(start):
    visited = [0]*101
    deq = deque()
    # 플레이어 위치, 주사위 횟수
    deq.append((start, 0))
    visited[start] = 1
    while deq:
        curr, cnt = deq.popleft()
        
        # 100번 칸에 도착
        if curr == 100:
            return cnt
        # 주사위 굴리기
        for k in range(1, 7):
            next = curr + k
            if next <= 100 and not visited[next]:
                visited[next] = 1
                # 사다리 or 뱀을 만나서 이동할 경우
                if board[next]:
                    # 이동 위치
                    next = board[next]
                    # 방문한 위치면 탐색 안함
                    if visited[next]:
                        continue
                    # 방문하지 않은 위치면 방문 체크
                    visited[next] = 1

                deq.append((next, cnt + 1))


# 사다리의 수 N, 뱀의 수 M
n, m = map(int, input().split())
board = [0]*101

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

print(bfs(1))