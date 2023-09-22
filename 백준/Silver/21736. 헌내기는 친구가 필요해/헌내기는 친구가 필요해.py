def bfs(i, j):
    stack = [(i,j)]
    campus[i][j] = 'X'
    cnt = 0
    
    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    cnt += 1

                campus[nx][ny] = 'X'
                stack.append((nx, ny))

    if cnt == 0:
        return 'TT'
    return cnt


n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            print(bfs(i,j))
            exit()