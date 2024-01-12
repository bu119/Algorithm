a, b, c = map(int, input().split())
if (c - b) > 0:
    n = a / (c - b)
    if type(n) == int:
        print(int(n))
    else:
        print(int(n)+1)
else:
    print(-1)