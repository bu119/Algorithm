import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set(input().rstrip() for _ in range(n))
see = set(input().rstrip() for _ in range(m))

ans = list(listen & see)
ans.sort()

print(len(ans))
for name in ans:
    print(name)