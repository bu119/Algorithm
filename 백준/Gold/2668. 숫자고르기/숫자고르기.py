import sys
input = sys.stdin.readline

def dfs(v, start):
    global ans

    if visited[v]:
        if v == start:
            ans |= tmp
        return

    visited[v] = 1
    tmp.add(v)
    dfs(graph[v], start)


n = int(input())

graph = []
set_num = set()
for _ in range(n):
    num = int(input()) - 1
    graph.append(num)
    set_num.add(num)

arr = list(set_num)
ans = set()
# 사이클이 존재하면 저장
for i in arr:
    tmp = set()
    visited = [0] * n
    dfs(i, i)

ans = sorted(ans)
print(len(ans))
for j in ans:
    print(j+1)