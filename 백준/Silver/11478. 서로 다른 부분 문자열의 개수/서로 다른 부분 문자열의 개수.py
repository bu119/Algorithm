s = input()
n = len(s)
ans = 0

for k in range(1, n+1):
    substring = set()
    for i in range(n-k+1):
        substring.add(s[i:i+k])
    ans += len(substring)

print(ans)