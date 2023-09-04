import sys
input = sys.stdin.readline

def dfs(v, start):
    global ans

    if v in visited:
        if v == start:
            ans |= visited
        return

    visited.add(v)
    dfs(graph[v], start)


n = int(input())

graph = [0] + [int(input()) for _ in range(n)]

# 사이클이 존재하면 저장
ans = set()
for i in range(1, n+1):
    # 방문 체크
    visited = set()
    dfs(i, i)

ans = sorted(ans)
print(len(ans))
for j in ans:
    print(j)