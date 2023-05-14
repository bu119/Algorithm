n = int(input())
arr = input()
red = arr.count("R")
blue = n - red

ans = min(red, blue)

for i in range(1, n):
    if arr[0] != arr[i]:
        cnt = arr[i:].count(arr[0])
        ans = min(ans, cnt)
        break

for i in range(n-2,-1,-1):
    if arr[n-1] != arr[i]:
        cnt = arr[:i+1].count(arr[n-1])
        ans = min(ans, cnt)
        break

print(ans)