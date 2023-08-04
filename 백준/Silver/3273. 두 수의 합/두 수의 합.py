n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

cnt = 0
start = 0
end = n-1

while start < end:
    ssum = arr[start] + arr[end]

    if ssum < x:
        start += 1
        continue
        
    if ssum == x:
        cnt += 1

    end -= 1

print(cnt)