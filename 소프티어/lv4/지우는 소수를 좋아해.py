import sys, heapq


# 소수 찾기
def is_prime_number(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


# 최소 경로 찾기
def dijkstra():
    maxV = 1000000001
    visited = [maxV] * (n + 1)
    visited[0] = 0

    # 레벨, 위치
    heap = [(0, 1)]
    visited[1] = 0

    while heap:

        level, curr = heapq.heappop(heap)

        if curr == n:
            continue

        if visited[curr] < level:
            continue

        for posi, new_level in gym[curr]:
            # 경로 중 최대 level을 업데이트
            max_level = max(new_level, level)
            if max_level < visited[posi]:
                visited[posi] = max_level
                heapq.heappush(heap, (max_level, posi))

    return visited[n]


# ★ 항상 1번 체육관에서부터 출발하고 마지막 N번 체육관을 지나가야 마지막 포켓몬 리그로 갈 수 있다.
# 1. 소수 찾는 함수
# 2. 레벨 체크 하는 함수

# 체육관의 개수를 나타내는 정수 N과 체육관 사이의 길의 개수 정수 M
n, m = map(int, input().split())
gym = [[] for _ in range(n + 1)]

# A번 체육관과 B번 체육관 사이에 필요 레벨이 C인 길이 존재한다. (a,b 사이에 값이 존재 - 다익스트라)
for _ in range(m):
    a, b, c = map(int, input().split())
    gym[a].append((b, c))
    gym[b].append((a, c))

# 관장 최소 레벨 찾기
num = dijkstra()
# 관장들이 갖고 있는 레벨(level)보다 높아야 함
num += 1

# 소수 찾기
while not is_prime_number(num):
    num += 1

print(num)