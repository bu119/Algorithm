n, m = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(m)]

matrix = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            matrix[i][j] += matrixA[i][z] * matrixB[z][j]
            
for row in matrix:
    print(*row)