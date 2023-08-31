def zzz(x, y, size, num):

    if not x <= r < x + size or not y <= c < y + size:
        return

    if x == r and y == c:
        print(num)
        exit(0)
    else:
        size //= 2
        for i in range(2):
            for j in range(2):
                zzz(x + size * i, y + size * j, size, num + (size**2) * (i*2 + j))

n, r, c = map(int, input().split())
zzz(0, 0, 2**n, 0)