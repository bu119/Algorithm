import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if clothes.get(kind):
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    cnt = 1
    for key in clothes:
        # 선택 안하는 경우도 추가해서 경우의 수를 센다.
        cnt *= (clothes[key] + 1)
    # 하나도 안고르는 경우를 제외
    print(cnt - 1)