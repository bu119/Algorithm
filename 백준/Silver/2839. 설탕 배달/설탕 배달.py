n = int(input())
ans = 0
flag = 1

while n >= 0:
    if n % 5 == 0:
        ans += (n//5)
        flag = 0
        print(ans)
        break
    n -= 3
    ans += 1

if flag:
    print(-1)