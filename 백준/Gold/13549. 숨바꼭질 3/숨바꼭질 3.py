import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [100001] * 100001

def dijkstra(n,k):

    heap = [(0,n)]
    visited[n] = 0

    while heap:

        now_time, now = heapq.heappop(heap)

        if now == k:
            return now_time

        if visited[now] < now_time:
            continue

        new_time = now_time + 1

        for i in [now-1, now+1, now*2]:

            if 0 <= i < 100001 and new_time < visited[i]:

                if i == now * 2:
                    new_time -= 1

                visited[i] = new_time
                heapq.heappush(heap,(new_time, i))


print(dijkstra(n,k))