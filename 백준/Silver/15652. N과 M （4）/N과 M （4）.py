from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(range(1,n+1))

data = combinations_with_replacement(arr, m)

for i in data:
    print(*i)