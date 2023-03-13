import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
for i in range(n-1):
    for num in list(map(int, input().split())):
        if arr[0] < num:
            heapq.heappop(arr)
            heapq.heappush(arr, num)

print(arr[0])