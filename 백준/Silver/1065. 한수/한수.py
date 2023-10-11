n = int(input())
if n < 100:
    print(n)
else:
    if n != 1000:
        n += 1

    cnt = 99

    for num in range(100, n):
        a, b, c = str(num)
        if int(a) - int(b) == int(b) - int(c):
            cnt += 1

    print(cnt)