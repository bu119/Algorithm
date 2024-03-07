import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
dp = [0] * (n+1)
queue = []
for i in range(1, n+1):
    wt, cnt, *num = map(int, input().split())
    time[i] = wt
    if cnt == 0:
        queue.append(i)
        dp[i] = wt
        continue
    for j in num:
        graph[j].append(i)
        indegree[i] += 1

while queue:
    curr = queue.pop(0)

    for next in graph[curr]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[curr] + time[next])
        if indegree[next] == 0:
            queue.append(next)

print(max(dp))