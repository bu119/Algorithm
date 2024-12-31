def dfs(node):
    tree[node] = -2
    for i in range(n):
        # 부모 parents[i]의 자식은 i
        if tree[i] == node:
            dfs(i)


n = int(input())
# 각 노드의 부모 저장
tree = list(map(int, input().split()))
# 지울 노드 번호
target_node = int(input())
# 리프 노드 개수
ans = 0
dfs(target_node)
for i in range(n):
    if tree[i] != -2 and i not in tree:
        ans += 1
print(ans)