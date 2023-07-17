from collections import deque

def solution(board):
    n = len(board)

    # 우하좌상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    deq = deque()
    deq.append((0, 0, 0, 1, 0))

    # 방문체크
    visited = set()
    visited.add((0, 0, 0, 1))
    visited.add((0, 1, 0, 0))

    while deq:
        x1, y1, x2, y2, cnt = deq.popleft()

        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            return cnt

        # 상하좌우
        for k in range(4):
            nx1 = x1 + di[k]
            ny1 = y1 + dj[k]

            nx2 = x2 + di[k]
            ny2 = y2 + dj[k]

            # 벽 체크
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if not board[nx1][ny1] and not board[nx2][ny2] and (nx1, ny1, nx2, ny2) not in visited:
                    visited.add((nx1, ny1, nx2, ny2))
                    visited.add((nx2, ny2, nx1, ny1))
                    deq.append((nx1, ny1, nx2, ny2, cnt + 1))

        # 90도 회전
        for k in [-1, 1]:
            # 가로로 있을 때 (기준점에서 행만 움직이는 걸로 다른 점이 대체)
            if x1 == x2:
                nx1 = x1 + k
                nx2 = x2 + k
                if 0 <= nx1 < n and 0 <= nx2 < n and not board[nx1][y1] and not board[nx2][y2]:
                    # x1,y1 기준점 (x2,y2 위치가 x1 위아래 움직임, y1으로 대체)
                    # 왼쪽 기준점
                    if (nx1, y1, x1, y1) not in visited:
                        visited.add((nx1, y1, x1, y1))
                        visited.add((x1, y1, nx1, y1))
                        deq.append((nx1, y1, x1, y1, cnt + 1))

                    # 오른쪽 기준점 (x2,y2 기준점)
                    if (nx2, y2, x2, y2) not in visited:
                        visited.add((nx2, y2, x2, y2))
                        visited.add((x2, y2, nx2, y2))
                        deq.append((nx2, y2, x2, y2, cnt + 1))

            # 세로로 있을 때
            if y1 == y2:
                ny1 = y1 + k
                ny2 = y2 + k
                if 0 <= ny1 < n and 0 <= ny2 < n and not board[x1][ny1] and not board[x2][ny2]:
                    if (x1, ny1, x1, y1) not in visited:
                        visited.add((x1, ny1, x1, y1))
                        visited.add((x1, y1, x1, ny1))
                        deq.append((x1, ny1, x1, y1, cnt + 1))

                    if (x2, ny2, x2, y2) not in visited:
                        visited.add((x2, ny2, x2, y2))
                        visited.add((x2, y2, x2, ny2))
                        deq.append((x2, ny2, x2, y2, cnt + 1))