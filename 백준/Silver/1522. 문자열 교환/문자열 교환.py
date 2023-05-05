arr = input()
size = arr.count('a')
arr += arr
cnt = len(arr)
ans = cnt
for i in range(cnt-size):
    ans = min(ans, arr[i:i+size].count('b'))
print(ans)