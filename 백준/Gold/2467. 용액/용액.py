import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

num = 2000000000
ans_s, ans_e = 0, 0
end = n-1
start = 0

while start < end:
    ssum = arr[start] + arr[end]

    if abs(ssum) < num:
        num = abs(ssum)
        ans_s = start
        ans_e = end

    if ssum < 0:
        start += 1
    elif ssum > 0:
        end -= 1
    else:
        break

print(arr[ans_s], arr[ans_e])