a = int(input())
b = list(map(int, input()))
n = len(b)
ans = 0

for i in range(n):
    num = a*b[n-1-i]
    print(num)
    ans += num*(10**i)
    
print(ans)
