import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(v):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[v] != v:
        parent[v] = find_parent(parent[v])
    return parent[v]


# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    # 집의 수 m과 길의 수 n
    m, n = map(int, input().split())
    # 테스트 케이스 끝!
    if m == 0 and n == 0:
        break

    # 부모 테이블 부모를 자기 자신으로 초기화
    parent = list(range(m))
    # 모든 간선을 담을 리스트
    edges = []
    # 절약할 수 있는 최대 액수를 담을 변수
    result = 0

    # x번 집과 y번 집 사이에 양방향 도로, 거리가 z
    for i in range(n):
        x, y, z = map(int, input().split())
        # 길이, 연결 도시 저장
        edges.append((z, x, y))

    # 간선을 비용순으로 정렬
    edges.sort()
    # 간선을 하나씩 확인하며
    for cost, x, y in edges:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(x) != find_parent(y):
            union_parent(x, y)
        else:
            # 절약되는 액수는 연결되지 않은 간선의 가중치를 더해야한다.
            result += cost
            
    # 절약할 수 있는 최대 액수
    print(result)