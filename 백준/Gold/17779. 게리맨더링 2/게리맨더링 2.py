def make_area(x, y, d1, d2):
    area = [[0] * (n+1) for _ in range(n+1)]
    people = [0]*6

    # 5구역 표시
    for i in range(d1+1):
        # 조건 1
        area[x+i][y-i] = 5
        # 조건 4
        area[x+d2+i][y+d2-i] = 5

    for j in range(d2+1):
        # 조건 2
        area[x + j][y + j] = 5
        # 조건 3
        area[x+d1+j][y-d1+j] = 5

    for i in range(x+1, x+d1+d2):
        area5 = False
        # 행 기준으로 경계를 만나면
        for j in range(n):
            # 경계를 만나면
            if area[i][j] == 5:
                # 다시 경계를 만난 거면 다음 행 탐색
                if area5:
                    break
                area5 = True
            # 5구역 지정
            if area5:
                area[i][j] = 5

    for r in range(1, n+1):
        for c in range(1, n+1):
            if area[r][c] == 5:
                people[5] += population[r][c]
            # 1구역
            elif 1 <= r < x + d1 and 1 <= c <= y:
                people[1] += population[r][c]
            # 2구역
            elif 1 <= r <= x + d2 and y < c <= n:
                people[2] += population[r][c]
            # 3구역
            elif x+d1 <= r <= n and 1 <= c < y-d1+d2:
                people[3] += population[r][c]
            else:
                people[4] += population[r][c]
    return max(people) - min(people[1:])


n = int(input())
population = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
ans = 40000
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x + d1 + d2 <= n and 1 <= y - d1 < y + d2 <= n:
                    ans = min(ans, make_area(x, y, d1, d2))
print(ans)