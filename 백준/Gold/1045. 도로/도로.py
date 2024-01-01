def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# M개의 도로를 가진 도로의 집합 중
# 우선 순위가 가장 높은 것을 찾는 것
# M은 N-1보다 크거나 같다.
n, m = map(int, input().split())
parent = list(range(n))
edges = []
for i in range(n):
    row = input()
    for j in range(n):
        if i < j and row[j] == 'Y':
            edges.append((i, j))
# 총 간선의 수가 m보다 적다면 구현 불가
# 안해주면 인덱스 에러난다!!!
if len(edges) < m:
    print(-1)
else:
    edges.sort()
    ans = [0]*n
    road_cnt = 0
    unselected_road = []
    for c1, c2 in edges:
        if find(c1) != find(c2):
            union(c1, c2)
            ans[c1] += 1
            ans[c2] += 1
            road_cnt += 1
        else:
            # 선택되지 않은 도로를 추가해 M개의 도로 집합을 만들어야한다.
            # 우선순위대로 저장
            unselected_road.append((c1, c2))
    # mst 가능 여부
    if road_cnt != n-1:
        print(-1)
    else:
        # 도로를 m개까지만 체크한다.
        for idx in range(m-road_cnt):
            i, j = unselected_road[idx]
            ans[i] += 1
            ans[j] += 1
        print(*ans)