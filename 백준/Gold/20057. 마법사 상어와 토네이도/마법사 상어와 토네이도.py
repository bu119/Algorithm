def flySand(d):
    # 알파면 비율 0으로 저장
    # 서
    if d == 0:
        return {1: [(-1, 1), (1, 1)], 2: [(-2, 0), (2, 0)], 5: [(0, -2)], 7: [(-1, 0), (1, 0)], 10: [(-1, -1), (1, -1)], 0: [(0, -1)]}
    # 남
    elif d == 1:
        return {1: [(-1, -1), (-1, 1)], 2: [(0, -2), (0, 2)], 5: [(2, 0)], 7: [(0, -1), (0, 1)], 10: [(1, -1), (1, 1)], 0: [(1, 0)]}
    # 동
    elif d == 2:
        return {10: [(-1, 1), (1, 1)], 2: [(-2, 0), (2, 0)], 5: [(0, 2)], 7: [(-1, 0), (1, 0)], 1: [(-1, -1), (1, -1)], 0: [(0, 1)]}
    # 북
    else:
        return {10: [(-1, -1), (-1, 1)], 2: [(0, -2), (0, 2)], 5: [(-2, 0)], 7: [(0, -1), (0, 1)], 1: [(1, -1), (1, 1)], 0: [(-1, 0)]}

def tornado(k, x, y):
    # 밖으로 나간 모래 저장
    outSand = 0
    # 이동 칸수 저장
    move = 1
    while move < n+1:
        # 이동 칸 수가 두번 씩 반복 된다.
        for _ in range(2):
            for _ in range(move):
                x += di[k]
                y += dj[k]
                if not (0 <= x < n and 0 <= y < n):
                    break
                currSand = graph[x][y]
                # 모래 없으면 패스
                if currSand == 0:
                    continue
                # 모래 날리기
                sandRatio = flySand(k)
                # 날리고 남은 모래 저장
                remainingSand = currSand
                # 날리는 모래 비율
                for r in sandRatio:
                    for dx, dy in sandRatio[r]:
                        nx = x + dx
                        ny = y + dy
                        # 비율이 있을 때
                        if r > 0:
                            # 날리는 모래 계산
                            sand = (currSand * r) // 100
                            remainingSand -= sand
                        else:
                            # 알파이면 남은 모래 저장
                            sand = remainingSand

                        if 0 <= nx < n and 0 <= ny < n:
                            graph[nx][ny] += sand
                        else:
                            # 밖으로 나간 모래 더하기
                            outSand += sand
            # 방향 전환
            k = (k+1) % 4
        move += 1
    return outSand


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 반시계 (서 남 동 북)
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

print(tornado(0, n//2, n//2))