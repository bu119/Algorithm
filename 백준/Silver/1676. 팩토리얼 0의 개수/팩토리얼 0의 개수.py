n = int(input())
num = 1
for i in range(2,n+1):
    num *= i

num = str(num)
ans = 0
for j in range(len(num)-1,-1,-1):
    if num[j] == '0':
        ans += 1
    else:
        print(ans)
        break