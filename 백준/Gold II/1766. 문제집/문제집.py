import sys, heapq
input = sys.stdin.readline

def bfs():
    # 1번 문제가 가장 쉬운 문제이고 N번 문제가 가장 어려운 문제이므로 heapq 사용
    heap = []
    # 진입차수가 0인 노드를 deq에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heap.append(i)
    # 순서 저장
    order = []
    while heap:
        v = heapq.heappop(heap)
        order.append(v)

        for j in graph[v]:
            # 연결된 노드들의 진입차수 1 빼기
            indegree[j] -= 1
            # 진입차수가 0이 되면 deq에 삽입
            if indegree[j] == 0:
                heapq.heappush(heap, j)
    return order


n, m = map(int, input().split())
# 각 노드의 진입차수 저장
indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
# 순서 저장
result = bfs()
print(" ".join(map(str, result)))