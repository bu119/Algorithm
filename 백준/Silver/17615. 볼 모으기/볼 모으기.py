n = int(input())
arr = input()
red = arr.count("R")
blue = n - red

ans = min(red, blue)

cnt = 1
for i in range(1, n):
    if arr[0] != arr[i]:
        break
    cnt += 1

if arr[0] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

cnt = 1
for i in range(n-2,-1,-1):
    if arr[n-1] != arr[i]:
        break
    cnt += 1

if arr[n - 1] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

print(ans)