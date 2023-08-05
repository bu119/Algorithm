n = int(input())
arr = sorted(list(map(int, input().split())) for _ in range(n))

for a,b in arr:
    print(a,b)