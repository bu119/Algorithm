# 해당 행의 길이 지나갈 수 있는 길인지 판별
def way(i, matrix):
    j = 0
    # 평지 개수
    same = 1
    while j < n-1:
        if matrix[i][j] == matrix[i][j+1]:
            # 평지일 때
            j += 1
            same += 1
        elif matrix[i][j] - 1 == matrix[i][j+1]:
             # 내리막길일 때
            for k in range(1,l+1):
                if j+l < n and matrix[i][j] - 1 == matrix[i][j+k]:
                    pass
                else:
                    return False
            j += l
            same = 0

        elif matrix[i][j] + 1 == matrix[i][j+1]:
            # 오르막길일 때
            if same < l:
                return False
            same = 1
            j += 1
        else:
            return False

    return True


n, l = map(int,input().split())
height = [list(map(int,input().split())) for _ in range(n)]
colHeight = list(zip(*height))
cnt = 0

for i in range(n):
    if way(i, height):
        cnt += 1
    if way(i, colHeight):
        cnt += 1

print(cnt)