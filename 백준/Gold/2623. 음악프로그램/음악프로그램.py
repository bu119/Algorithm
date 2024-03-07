import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 진입 차수 정보 저장 (1부터 시작)
indegree = [0]*(n+1)
# 각 노드 별 나가는 간선의 위치 저장
graph = [[] for _ in range(n+1)]

for _ in range(m):
    num, *singers = list(map(int, input().split()))

    for i in range(num-1):
        a = singers[i]
        b = singers[i+1]
        indegree[b] += 1
        graph[a].append(b)

queue = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

answer = []
while queue:
    curr = queue.pop(0)
    # 순서 저장
    answer.append(curr)
    for next in graph[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
# 사이클 판별
if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)