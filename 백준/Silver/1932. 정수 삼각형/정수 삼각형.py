n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]

for i in range(n-1,0,-1):
    for j in range(i):
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
print(triangle[0][0])