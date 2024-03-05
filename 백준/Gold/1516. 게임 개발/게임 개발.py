import sys
input = sys.stdin.readline

# 순서가 존재, 위상 정렬
n = int(input())
# 진입 차수 정보 저장 (1부터 시작)
indegree = [0]*(n+1)
# 각 노드 별 나가는 간선의 위치 저장
graph = [[] for _ in range(n+1)]
# 건물 짖는 시간
cost = [0] * (n+1)
# 건물 짖는 최소 시간
dp = [0] * (n+1)

for b in range(1, n+1):
    t, *m = map(int, input().split())
    # 시간 저장
    cost[b] = t
    # 집입 차수
    indegree[b] += len(m)-1
    for a in m:
        if a == -1:
            continue
        graph[a].append(b)
# 진입 차수가 없는 노드 저장
queue = []
# 진입 차수가 0인 노드 찾기
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = cost[i]

# 그래프에 사이클이 존재하면 무한 루프
while queue:
    curr = queue.pop(0)
    for next in graph[curr]:
        # 사용 간선 삭제
        indegree[next] -= 1
        # 한 건물이 여러 건물을 거쳐야 지을 수 있는 경우, max로 갱신
        dp[next] = max(dp[next], dp[curr]+cost[next])
        # 진입 차수가 0이 된 노드 찾기
        if indegree[next] == 0:
            queue.append(next)
# 각 건물이 완성되기까지 걸리는 최소 시간 출력
for i in range(1, n+1):
    print(dp[i])