def bfs(x):
    global ans

    tmp = set()
    visited = [0] * n
    # 한개씩만 쌀인다.
    stack = [x]
    visited[x] = 1
    tmp.add(x)
    while stack:
        v = stack.pop()

        w = graph[v]
        # 사이클이 존재
        if w == x:
            # 합집합
            ans = ans | tmp
            return True

        if visited[w]:
            return False
        # 방문 안했으면
        visited[w] = 1
        tmp.add(w)
        stack.append(w)

    return False


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
    bfs(i)

ans = sorted(ans)
print(len(ans))
for j in ans:
    print(j+1)