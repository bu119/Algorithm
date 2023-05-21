s = list(input())
t = list(input())
cnt = len(t)
# s-t 시간초과
# t-s
def dfs(t):
    global s

    if t == s:
        print(1)
        exit(0)

    if len(t) == len(s):
        return

    # 반대로
    if t[-1] == 'A':
        t.pop()
        dfs(t)
        t.append('A')

    if t[0] == 'B':
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()

dfs(t)

print(0)