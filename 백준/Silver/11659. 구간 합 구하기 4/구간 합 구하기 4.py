import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ssum = [0] * (n+1)

for k in range(1,n+1):
    ssum[k] = ssum[k-1] + arr[k-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(ssum[j]-ssum[i-1])