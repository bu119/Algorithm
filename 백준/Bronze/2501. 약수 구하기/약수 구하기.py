n, k = map(int, input().split())
ans = set()
for i in range(1, n//2+1):
    if n % i == 0:
        ans.add(i)
        ans.add(n//i)
ans = sorted(ans)
if len(ans) < k:
    print(0)
else:
    print(ans[k-1])