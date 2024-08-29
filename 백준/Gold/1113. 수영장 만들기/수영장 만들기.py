from collections import deque

def bfs(i, j, startH):
    minH = 10

    visited = set()
    deq = deque()
    deq.append((i, j))
    visited.add((i, j))

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            # 유효 좌표를 벗어나면, 시작 좌표를 포함한 모든 좌표는 바깥 공간과 연결 되어 있다 -> 탐색 중지
            if not (0 <= nx < n and 0 <= ny < m):
                # 수영장 실패
                return 0, set()

            if ground[nx][ny] <= startH and (nx, ny) not in visited:
                visited.add((nx, ny))
                deq.append((nx, ny))

            elif ground[nx][ny] > startH:
                # 더 높은 높이를 만나면, 모든 벽에 대한 최소 높이 저장
                minH = min(minH, ground[nx][ny])
    # 수영장 가능
    return minH, visited


n, m = map(int, input().split())
ground = [list(map(int, input())) for _ in range(n)]
# 동남서북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 가능한 수영장 물 누적
ans = 0

# 외곽에는 물을 채울 수 없다.
for i in range(1, n-1):
    for j in range(1, m-1):
        wallHeight, pool = bfs(i, j, ground[i][j])
        for r, c in pool:
            # 현재 탐색의 벽 최소 높이(wallHeight)보다 땅 높이가 작으므로 그 만큼 물을 채울 수 있다.
            ans += (wallHeight - ground[r][c])
            # 수영장이 가능한 땅 높이를 현재 탐섹에서 가능한 수영장 높이로 설정 (누적 시키기 위함)
            ground[r][c] = wallHeight

print(ans)