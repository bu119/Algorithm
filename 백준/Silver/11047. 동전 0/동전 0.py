n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-1,-1,-1):
    q = k // arr[i]
    r = k % arr[i]
    if r == 0:
        cnt += q
        break

    if q:
        cnt += q
        k = r

print(cnt)