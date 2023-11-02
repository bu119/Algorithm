from collections import deque

# 최소 문의 위치를 저장해서 두 죄수 사이의 문 개수를 합집합 한다.
def bfs(x, y):
    # 방문 체크
    visited = [[-1] * (w+2) for _ in range(h+2)]

    deq = deque()
    deq.append((x, y))

    visited[x][y] = 0

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if 0 <= nx < h+2 and 0 <= ny < w+2 and prison[nx][ny] != "*" and visited[nx][ny] == -1:
                # 방문 체크 지나온 문 최소 개수
                visited[nx][ny] = visited[x][y]
                # 문 만났을 때
                if prison[nx][ny] == "#":
                    visited[nx][ny] += 1
                    # 문만난 길은 뒤에 탐색
                    deq.append((nx, ny))
                else:
                    # 문 안만난 길부터 탐색
                    deq.appendleft((nx, ny))

    return visited


t = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(t):
    h, w = map(int, input().split())
    # 감옥 (출구가 여러 개일 때 밖에서 들어오는 탐색을 한번에 쉽게 찾기 위해 이동 가능한 길로 겉을 감싼다.)
    # (아니면 각 출구에서 일일이 계산 해야할 듯 하다.)
    # 윗면 감싸기
    prison = ['.' * (w + 2)]
    # 죄수 위치: 탈출 최소 문 위치
    prisoners = []
    # 감옥 만들기
    for i in range(h):
        row = input()
        for j in range(w):
            # 죄수 위치
            if row[j] == "$":
                prisoners.append((i+1, j+1))
        # 좌우 감싸기 (감옥 좌우로 이동 가능한 길 추가)
        prison.append('.' + row + '.')
    # 아랫면 감싸기
    prison.append('.' * (w + 2))
    # 출구에서 부터 안으로 탐색
    sg = bfs(0, 0)
    # 죄수1
    p1 = bfs(prisoners[0][0], prisoners[0][1])
    # 죄수2
    p2 = bfs(prisoners[1][0], prisoners[1][1])

    minV = 10001
    # 죄수1, 죄수2, 상근 이가 만났을 때 가장 적은 문을 지나는 부분을 찾으면 된다.
    for r in range(1, h+1):
        for c in range(1, w+1):
            if sg[r][c] != -1 and p1[r][c] != -1 and p2[r][c] != -1:
                # 문에서 만났을 때
                if prison[r][c] == "#":
                    minV = min(minV, sg[r][c] + p1[r][c] + p2[r][c] - 2)
                else:
                    minV = min(minV, sg[r][c] + p1[r][c] + p2[r][c])
    print(minV)