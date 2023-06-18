def binarySearch(a):
    start = 0
    end = m-1
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if b[mid] < a:
            start = mid + 1
            result = mid
        else:
            end = mid-1
    return result + 1


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(map(int,input().split()))
    b = sorted(map(int, input().split()))
    cnt = 0
    for i in a:
        if i > b[0]:
            t = binarySearch(i)
            cnt += t
    print(cnt)