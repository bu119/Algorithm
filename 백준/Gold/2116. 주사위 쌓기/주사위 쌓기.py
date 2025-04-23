import sys
input = sys.stdin.readline

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
# 최댓값 저장
ans = 0
# 1번 주사위의 바닥 면을 x로 했을 때
for x in range(1, 7):
    ssum = 0
    bottom = x
    # 최종 기둥의 옆면 중 최댓값 찾기
    for y in range(1, n+1):
        top = dices[y][bottom]
        if 6 not in {top, bottom}:
            ssum += 6
        elif 5 not in {top, bottom}:
            ssum += 5
        else:
            ssum += 4
        # 위로 쌓은 주사위의 바닥면
        bottom = top
    # 최댓값 갱신
    ans = max(ans, ssum)
print(ans)