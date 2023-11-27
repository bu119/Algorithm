n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = n
for i in range(n):
    a[i] -= b
    if a[i] > 0:
        if a[i] % c > 0:
            ans += a[i] // c + 1
        else:
            ans += a[i] // c
print(ans)