import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 특정 노드에서 각 노드로 길이 찾는 함수
def dfs(node, ssum):
    for next_node, nw in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = ssum + nw
            dfs(next_node, ssum+nw)


n = int(input())
tree = [[] for _ in range(n+1)]
# 자식이 0인 노드 -> 부모가 아닌 노드 (출발점)
leaf_node = set(range(1, n+1))
for _ in range(n-1):
    p, c, w = map(int, input().split())
    # 양방향 이동
    tree[p].append((c, w))
    tree[c].append((p, w))
    # 자식있는 노드 삭제
    leaf_node.discard(p)
    
# 특정 노드에서 각 노드의 길이 저장
visited = [-1] * (n + 1)
# 루트노드에서 출발
visited[1] = 0
# 루트노드에서 각 노드로 길이 찾기
dfs(1, 0)
# 최대 길이
max_length = 0
# 최대 길이 노드
start = -1
# 최대 길이 찾기 (리프노드만 탐색하면 됌)
for i in leaf_node:
    if max_length < visited[i]:
        max_length = visited[i]
        start = i
# 루트노드에서 가장 먼 노드를 출발점으로 각 노드의 길이 저장
visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)
print(max(visited))