n = sorted(map(int, input()), reverse=True)
if sum(n) % 3 != 0 or n[-1] != 0:
    print(-1)
else:
    print(''.join(map(str, n)))