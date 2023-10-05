from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = sorted(set(combinations_with_replacement(arr, m)))

for i in ans:
    print(' '.join(map(str, i)))
