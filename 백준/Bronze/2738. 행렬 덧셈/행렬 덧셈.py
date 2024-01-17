n, m = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(n)]
matrixB = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrixA[i][j] + matrixB[i][j], end=" ")
    print()