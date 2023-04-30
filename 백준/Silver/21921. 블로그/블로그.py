n, x = map(int,input().split())
visitor = list(map(int,input().split()))

if max(visitor) == 0:
    print("SAD")
else:
    ssum = sum(visitor[:x])
    ans = ssum
    cnt = 1
    for i in range(x, n):
        ssum = ssum-visitor[i-x]+visitor[i]
        if ans < ssum:
            ans = ssum
            cnt = 1
        elif ans == ssum:
            cnt += 1
    print(ans)
    print(cnt)