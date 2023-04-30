import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))
check = [0] * (max(arr) + 1)
ans = 0
start, end = 0, 0

while end < n:
    if check[arr[end]] < k:
        check[arr[end]] += 1
        end += 1
    else:
        check[arr[start]] -= 1
        start += 1
    ans = max(ans, end - start)

print(ans)