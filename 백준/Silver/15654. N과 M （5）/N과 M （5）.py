from itertools import permutations

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
for i in permutations(arr, m):
    print(*i)