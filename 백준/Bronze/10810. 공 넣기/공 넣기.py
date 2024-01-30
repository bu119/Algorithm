n, m = map(int, input().split())
baskets =  [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        baskets[x] = k
        
print(' '.join(map(str, baskets[1:])))