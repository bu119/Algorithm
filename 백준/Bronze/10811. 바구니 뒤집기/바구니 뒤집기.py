n, m = map(int, input().split())
baskets = list(range(n+1))
for _ in range(m):
    i, j = map(int, input().split())
    baskets = baskets[:i] + list(reversed(baskets[i: j+1])) + baskets[j+1:]
print(*baskets[1:])