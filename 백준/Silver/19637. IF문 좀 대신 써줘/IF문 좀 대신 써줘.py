import sys
input = sys.stdin.readline

def binary_search(p):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if p > power[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(name[right+1])

n, m = map(int,input().split())
name = []
power = []
for _ in range(n):
    na, po = input().split()
    name.append(na)
    power.append(int(po))

for _ in range(m):
    binary_search(int(input()))