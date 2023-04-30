n, x = map(int,input().split())
visitor = list(map(int,input().split()))
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

if ans:
    print(ans)
    print(cnt)
else:
    print("SAD")