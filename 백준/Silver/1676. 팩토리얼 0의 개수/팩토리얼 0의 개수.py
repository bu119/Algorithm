n = int(input())
num = 1
for i in range(2,n+1):
    num *= i

ans = 0
check = 10
while True:
    if num % check:
        print(ans)
        break
    else:
        ans += 1
        check *= 10