n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    w1, h1 = info[i]
    cnt = 1
    for j in range(n):
        w2, h2 = info[j]
        if w1 < w2 and h1 < h2:
            cnt += 1

    print(cnt, end=' ')