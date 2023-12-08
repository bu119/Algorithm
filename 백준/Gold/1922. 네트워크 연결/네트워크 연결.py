# 크루스칼 알고리즘
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
# 부모 테이블 부모를 자기 자신으로 초기화
parent = list(range(n+1))
# 모든 간선을 담을 리스트
edges = []
# 최소 비용을 담을 변수
ans = 0
# a컴퓨터와 b컴퓨터를 연결하는데 비용이 c
for i in range(m):
    a, b, c = map(int, input().split())
    # 길이, 연결 도시 저장
    edges.append((c, a, b))
# 간선을 비용순으로 정렬
edges.sort()
# 간선을 하나씩 확인하며
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)