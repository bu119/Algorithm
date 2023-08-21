from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 1. 구역이 나뉘어 지니?
# 2. 인구차이가 얼마니?

def bfs(v, group):

    visited = set()
    visited.add(v)
    deq = deque()
    deq.append(v)
    while deq:
        v = deq.popleft()

        for w in graph[v]:
            if w in group and w not in visited:
                visited.add(w)
                deq.append(w)

    return visited == group


n = int(input())
population = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]

# 인접한 구역의 정보
for i in range(1,n+1):
    m, *tmp = list(map(int,input().split()))
    for j in range(m):
        graph[i].append(tmp[j])

# 조합으로 구역 나누기
area = range(1, n+1)
setArea = set(area)
minV = 100 * 10 + 1
# 두 그룹으로 나누기 때문에 N//2+1 이상으로 넘어가면 조합이 중복되어 똑같은 작업을 한다.
for k in range(1, n//2+1):
    for g1 in combinations(area, k):
        setG1 = set(g1)
        setG2 = setArea-setG1
        g2 = list(setG2)

        if bfs(g1[0], setG1) and bfs(g2[0], setG2):
            tmp = 0
            for p1 in g1:
                tmp += population[p1-1]

            for p2 in g2:
                tmp -= population[p2-1]

            if tmp == 0:
                print(0)
                exit()
            minV = min(minV,abs(tmp))

if minV == 1001:
    print(-1)
else:
    print(minV)