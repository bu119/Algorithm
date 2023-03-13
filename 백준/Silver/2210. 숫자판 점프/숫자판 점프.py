def dfs(i, j, k, num):
    global number

    if k == 6:
        number.add(num)
        return

    for z in range(4):
        ni = i + di[z]
        nj = j + dj[z]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, k+1, num+arr[ni][nj])


arr = [input().split() for _ in range(5)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
number = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, 1, arr[i][j])

print(len(number))