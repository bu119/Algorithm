import sys, heapq
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    # 해당 숫자가 존재하는지 여부 저장 (삭제시 저장)
    visited = set()
    for i in range(k):
        operation, n = input().split()
        n = int(n)
        
        if operation == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
        else:
            if n == 1:
                # max_heap있고 max_heap[0]이 삭제된 값이면
                while max_heap and max_heap[0][1] in visited:
                    heapq.heappop(max_heap)
                # max_heap에 값이 있으면
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    visited.add(idx)
            else:
                # min_heap있고 min_heap[0]이 삭제된 값이면
                while min_heap and min_heap[0][1] in visited:
                    heapq.heappop(min_heap)
                # min_heap에 값이 있으면
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    visited.add(idx)

    while max_heap and max_heap[0][1] in visited:
        heapq.heappop(max_heap)

    while min_heap and min_heap[0][1] in visited:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')