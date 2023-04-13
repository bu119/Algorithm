import sys
input = sys.stdin.readline

n, m = map(int,input().split())
name = []
power = []
for _ in range(n):
    na, po = input().split()
    name.append(na)
    power.append(int(po))

for _ in range(m):
    p = int(input())
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if p > power[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(name[right + 1])