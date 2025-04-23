n = int(input())
# 각 주사위 마주보는 면 저장
dices = {}
for i in range(1, n+1):
    dices[i] = {}
    a, b, c, d, e, f = map(int, input().split())
    dices[i][a] = f
    dices[i][b] = d
    dices[i][c] = e
    dices[i][d] = b
    dices[i][e] = c
    dices[i][f] = a

ans = 0
# 첫 번째 주사위의 바닥 면
for x in range(1, 7):
    ssum = 0
    down = x
    up = dices[1][down]
    # 옆면 중 가장 큰 수 찾기
    for y in range(1, n+1):
        if 6 not in {up, down}:
            ssum += 6
        elif 5 not in {up, down}:
            ssum += 5
        else:
            ssum += 4

        if y == n:
            continue
        down = up
        up = dices[y+1][down]
        
    ans = max(ans, ssum)

print(ans)