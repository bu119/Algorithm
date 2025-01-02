import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 트리 길이 찾는 함수
def dfs(node):
    # 리프 노드 (최하단 노드)
    if not tree[node]:
        # 마지막 노드라 더 해질 길이가 없음
        return 0
    # 자식이 하나뿐인 노드 (길이 하나뿐)
    elif len(tree[node]) == 1:
        child, weight = tree[node][0]
        # 길의 길이 가져오기
        dist[node] = dfs(child) + weight
        # 반환 되어 위로 더해질 때는 길이 하나라 그대로 더해짐
        return dist[node]
    # 자식이 여러개 일 때 최대 길이 2개 찾아 연결하기
    else:
        # node 노드에서 갈라져 나올 수 있는 길이 저장
        child_lengths = []
        # node 노드 기준으로 갈라지는 길 탐색
        for child, weight in tree[node]:
            # 현재 길에서의 길이 구하기
            child_lengths.append(dfs(child) + weight)
        # 최대 길이 2개 찾기
        # 갈라진 길의 길이를 내림 차순 정렬
        child_lengths.sort(reverse=True)
        # 최대 길이 2개를 가져와 연결하기
        dist[node] = child_lengths[0] + child_lengths[1]
        # 반환되어 위로 더해질 때는 가장 긴 길이 가져가기
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