import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, w):
    global compliment

    for k in tree[v]:
        compliment[k] += w
        dfs(k, compliment[k])


n, m = map(int, input().split())
superior = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
compliment = [0]*(n+1)

for p in range(n):
    # 부하직원 입력
    super = superior[p]
    if super > 0:
        tree[super].append(p+1)

for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

# 한번에 처리하기
dfs(1, compliment[1])
print(*compliment[1:])