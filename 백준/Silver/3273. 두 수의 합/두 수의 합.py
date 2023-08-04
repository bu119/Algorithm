n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

cnt = 0
start = 0
end = n-1

while start < end and end < n:
    ssum = arr[start] + arr[end]

    if ssum == x:
        cnt += 1

    if ssum < x:
        start += 1
        continue

    end -= 1

print(cnt)