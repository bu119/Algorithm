import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = sorted(arr, key = lambda x :(x[1], x[0]))

for a, b in ans:
    print(a,b)