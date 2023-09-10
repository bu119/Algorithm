import sys, heapq
input = sys.stdin.readline

# 중복 제거
def de_duplication(heap):
    global min_heap, max_heap

    if heap == 'max_heap':
        # max_heap에 값이 있고 -max_heap[0]이 삭제된 값이면
        while max_heap and visited[-max_heap[0]] < 1:
            heapq.heappop(max_heap)

    else:
        # min_heap에 값이 있고 min_heap[0]이 삭제된 값이면
        while min_heap and visited[min_heap[0]] < 1:
            heapq.heappop(min_heap)


t = int(input())
for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    # 값의 추가, 삭제 기록
    visited = {}
    for i in range(k):
        operation, n = input().split()
        n = int(n)
        
        if operation == 'I':
            # 이미 값이 존재하면 개수만 올려줌
            if visited.get(n):
                visited[n] += 1
            else:
                heapq.heappush(min_heap, n)
                heapq.heappush(max_heap, -n)
                visited[n] = 1

        else:
            if not max_heap or not min_heap:
                continue

            if n == 1:
                # 중복 제거
                de_duplication('max_heap')
                # 최댓값 삭제
                if max_heap:
                    visited[-max_heap[0]] -= 1

            else:
                # 중복 제거
                de_duplication('min_heap')
                # 최솟값 삭제
                if min_heap:
                    visited[min_heap[0]] -= 1

    de_duplication('max_heap')
    de_duplication('min_heap')

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')