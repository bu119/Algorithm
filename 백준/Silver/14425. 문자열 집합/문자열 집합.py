import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = set(input() for _ in range(n))
ans = 0
for i in range(m):
    if input() in arr:
       ans += 1

print(ans)