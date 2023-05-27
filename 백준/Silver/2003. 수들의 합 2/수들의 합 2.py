n, m = map(int, input().split())
arr = list(map(int,input().split()))
cnt = 0
start = 0
end = 1

while start <= end and end <= n:

    ssum = sum(arr[start:end])

    if ssum == m:
        cnt += 1
        end += 1
    elif ssum > m:
        start += 1
    else:
        end += 1
print(cnt)