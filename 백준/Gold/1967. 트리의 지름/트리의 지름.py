import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 각 노드에서 최대 지름 찾는 함수
def dfs(node):
    # 리프 노드 (최하단 노드)
    if not tree[node]:
        # 마지막 노드라 더 해질 길이가 없음
        return 0
    
    # 자식이 있을 때는 길 탐색
    # node에서 갈라져 나올 수 있는 길의 길이 저장
    child_lengths = []
    # node를 부모로 갈라지는 자식 길 탐색
    for child, weight in tree[node]:
        # 현재 길에서의 최장 길이 가져오기
        child_lengths.append(dfs(child) + weight)

    # 자식이 하나면, 그대로 더하기 (길이 하나뿐)
    if len(child_lengths) == 1:
        dist[node] = child_lengths[0]
    # 자식이 여러 개이면, 최대 길이 2개 찾아 node를 기준으로 연결하기
    else:
        # 최대 길이 2개 찾기
        # 갈라진 길의 길이를 내림 차순 정렬
        child_lengths.sort(reverse=True)
        # 최대 길이 2개를 가져와 연결하기
        dist[node] = child_lengths[0] + child_lengths[1]
    # 반환 되어 길이가 위로 더해질 때는 길이 하나면 그대로 더 해지고, 길이 여러 개 일때는 가장 긴 길이 더하기
    return child_lengths[0]


# 트리의 지름: 트리에 존재하는 모든 경로들 중에서 가장 긴 것
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
# 각 노드에서의 최대 길이 저장
dist = [0]*(n+1)
# 루드노드부터 하위노드 탐색 (부모노드를 기준으로 탐색하여 길이 연결)
dfs(1)
print(max(dist))