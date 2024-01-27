import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
ssum = 0
for _ in range(n-1):
    x, y = map(int, input().split())
    if end < x:
        ssum += end - start
        start = x
        end = y
    elif x <= end and end < y:
        end = y
ssum += end - start
print(ssum)