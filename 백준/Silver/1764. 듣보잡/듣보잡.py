n, m = map(int, input().split())

listen = set(input() for _ in range(n))
see = set(input() for _ in range(m))

ans = list(listen & see)
ans.sort()
print(len(ans))
for name in ans:
    print(name)