import sys
input=sys.stdin.readline

n = int(input())
# 차가 터널에 들어가는 순서 저장
daegeun = [input() for _ in range(n)]
# 추월 차량 개수 저장
overtaking_cnt = 0
for _ in range(n):
    # 나오는 차량
    out_car = input()
    if daegeun[0] != out_car:
        overtaking_cnt += 1
    daegeun.remove(out_car)
print(overtaking_cnt)