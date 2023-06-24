import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

apple = list(map(int,input().split()))
visited = [0]*n
cnt = 0

def dfs(node, level):
    global cnt

    visited[node] = 1

    if level <= k:
        cnt += apple[node]

    for i in tree[node]:
        if not visited[i]:
            dfs(i, level+1)

dfs(0,0)
print(cnt)