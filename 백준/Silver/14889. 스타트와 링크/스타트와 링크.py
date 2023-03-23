from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 100
check = set()
for num in combinations(range(n), n//2):

    if num in check:
        continue

    startT = 0
    linkT = 0
    linkTeam = list(range(n))

    for k in num:
        linkTeam.remove(k)

    check.add(num)
    check.add(tuple(linkTeam))

    # print(num, tuple(linkTeam))

    for i, j in combinations(num, 2):
        startT += (arr[i][j] + arr[j][i])
    for x, y in combinations(linkTeam, 2):
        linkT += (arr[x][y] + arr[y][x])

    if abs(startT-linkT) < ans:
        ans = abs(startT-linkT)

    if ans == 0:
        break

print(ans)