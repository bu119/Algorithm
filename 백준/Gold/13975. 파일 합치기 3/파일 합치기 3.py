import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    size = input().split()

    ans = 0
    arr = []
    for i in size:
        heapq.heappush(arr, int(i))

    while len(arr) > 1:

        num = heapq.heappop(arr)
        num += heapq.heappop(arr)
        
        ans += num
        heapq.heappush(arr, num)

    print(ans)