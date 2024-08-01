# 기본 부품과 그 기본 부품으로 조립하여 만든 중간 부품이 사용
# -> 트리에 순서가 존재
# 기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품
# -> 시작 점
# 1부터 N-1까지는 기본 부품이나 중간 부품의 번호, N은 완제품의 번호
from collections import deque

# 위상 정렬 함수
def topology_sort():
    q = deque()
    # 기본 부품 저장
    start = set()
    # 처음 시작할 때
    # 진입차수가 0인 노드를 큐에 삽입 (기본 부품)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            start.add(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        curr = q.popleft()
        # 연결 가능한 다음 단계 번호, 현재 제품이 다음 단계에 얼마나 필요한지
        for next, need in graph[curr]:
            # 현재 부품이 기본 부품이면
            if curr in start:
                needs[next][curr] += need
            # 현재 부품이 중간 부품이면
            else:
                for i in range(1, n + 1):
                    # 필요한 부품의 개수를 곱해 나가야 한다.
                    needs[next][i] += needs[curr][i] * need

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            indegree[next] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[next] == 0:
                q.append(next)

    # 기본 부품의 번호와 소요 개수 출력
    for j in sorted(start):
        print(j, needs[n][j])


# 부품 수 (노드 개수)
n = int(input())
# 필요한 부품들 간의 관계의 개수 (간선 개수)
m = int(input())

# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n + 1)]
# 각 제품을 만들때 필요한 부품 (누적 시킬 배열이 필요)
needs = [[0] * (n + 1) for _ in range(n + 1)]

# 방향 그래프의 모든 간선 정보 받기
for _ in range(m):
    # 중간 부품이나 완제품 X를 만드는데
    # 중간 부품 혹은 기본 부품 Y가 K개 필요
    x, y, k = map(int, input().split())
    # 정점 y에서 x로 이동 가능 (x를 만들 때, 5개 필요)
    graph[y].append((x, k))
    # 진입 차수를 1 증가
    indegree[x] += 1

topology_sort()