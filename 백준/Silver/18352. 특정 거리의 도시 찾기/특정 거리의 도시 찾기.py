from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    deq = deque()
    deq.append(i)
    city = []

    visited = [-1] * (n+1)
    visited[i] = 0
    while deq:
        i = deq.popleft()

        for j in road[i]:
            if visited[j] == -1:
                visited[j] = visited[i]+1  # 방문 체크
                # 거리가 k 보다 작거나 같을 때만 비교
                if visited[j] == k:
                    city.append(j)
                elif visited[j] < k:
                    deq.append(j)

    return city


# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

cities = bfs(x)

if cities:
    for z in sorted(cities):
        print(z)
else:
    print(-1)