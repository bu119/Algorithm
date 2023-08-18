import sys
input = sys.stdin.readline

def dfs(v):
    global check, visited
    visited[v] = 1

    if v+1 in set_plan:
        check.add(v+1)

    for w in graph[v]:
        if visited[w] == 0:
            dfs(w)

            
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

# 경로가 가능한것은 이어져있기 때문있다.
# 따라서 이러져 있는지만 판별하면된다.
plan = list(map(int, input().split()))
set_plan = set(plan)
visited = [0]*n
check = set()
dfs(plan[0]-1)
if set_plan-check:
    print('NO')
else:
    print('YES')