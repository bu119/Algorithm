import sys
input = sys.stdin.readline

def bfs(v):
    check = set()
    visited = [0] * n
    stack = [v]
    visited[v] = 1

    while stack:
        v = stack.pop()

        if v+1 in set_plan:
            check.add(v+1)

        if not set_plan-check:
            return 'YES'

        for w in graph[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)
    return 'NO'


# 도시의 수
n = int(input())
# 여행 계획에 속한 도시들의 수
m = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            graph[i].append(j)
            graph[j].append(i)

# 같은 도시를 여러 번 방문하는 것도 가능
# 출발지를 시작으로 순서에 관계없이 각 여행지를 방문 가능한지만 체크
plan = list(map(int, input().split()))
set_plan = set(plan)

print(bfs(plan[0]-1))