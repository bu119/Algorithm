from itertools import combinations

n, m = map(int,input().split())
arr = range(1,n+1)
ans = combinations(arr, m)

for i in ans:
    print(*i)