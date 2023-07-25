import sys
input = sys.stdin.readline


def spring_summer():
    global tree, nutrient

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                live = []
                cnt = 0
                for age in tree[i][j]:
                    if age <= nutrient[i][j]:
                        # 나이만큼 양분을 먹
                        nutrient[i][j] -= age
                        live.append(age+1)
                    else:
                        # 여름
                        cnt += (age // 2)
                nutrient[i][j] += cnt
                tree[i][j] = live


def autumn():
    global tree, nutrient

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    # 번식하는 나무는 나이가 5의 배수
                    if age % 5 == 0:
                        for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                tree[ni][nj].append(1)


def winter():
    global arr, nutrient

    for i in range(n):
        for j in range(n):
            nutrient[i][j] += arr[i][j]


n, m, k = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

nutrient = [[5]*n for _ in range(n)]

year = 0
die = []
while year != k:

    spring_summer()
    autumn()
    winter()

    year += 1

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)