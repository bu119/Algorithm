n, k = map(int, input().split())
a = 1
b = 1
for i in range(k):
    a *= (n-i)
    b *= (i+1)

print(a//b % 10007)