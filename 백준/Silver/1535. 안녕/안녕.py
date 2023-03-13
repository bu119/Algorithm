import sys
input = sys.stdin.readline

def dfs(i, pow, ple):
    global max_pleasure

    if pow <= 0:
        return

    if max_pleasure < ple:
        max_pleasure = ple

    for j in range(i+1, n):
        dfs(j, pow - minus_pow[j], ple + plus_ple[j])


n = int(input())
minus_pow = list(map(int, input().split()))
plus_ple = list(map(int, input().split()))

pleasure = 0
power = 100
ans = 0
for i in range(n):
    max_pleasure = 0
    dfs(i, power - minus_pow[i], pleasure + plus_ple[i])
    if ans < max_pleasure:
        ans = max_pleasure

print(ans)