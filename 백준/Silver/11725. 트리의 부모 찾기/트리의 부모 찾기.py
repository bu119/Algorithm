import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    for i in tree[node]:
        if parent_node[i] == 0:
            parent_node[i] = node
            dfs(i)


n = int(input())
tree = [[] for _ in range(n+1)]
parent_node = [0] * (n+1)
root = 1
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

dfs(1)
for k in range(2, n+1):     # 2번 노드 부터 출력
    print(parent_node[k])