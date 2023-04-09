n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans = n*m

for i in range(n-8+1):
    for j in range(m-8+1):
        cntB = 0
        cntW = 0
        for r in range(8):
            for c in range(8):
                # 왼쪽 위 검
                if (r+i) % 2 == 0 and (c+j) % 2 == 0:
                    if board[r+i][c+j] != 'B':
                        cntB += 1
                elif (r+i) % 2 == 1 and (c+j) % 2 == 1:
                    if board[r+i][c+j] != 'B':
                        cntB += 1
                else:
                    if board[r+i][c+j] != 'W':
                        cntB += 1

                # 왼쪽 위 흰
                if (r + i) % 2 == 0 and (c + j) % 2 == 0:
                    if board[r + i][c + j] != 'W':
                        cntW += 1
                elif (r + i) % 2 == 1 and (c + j) % 2 == 1:
                    if board[r + i][c + j] != 'W':
                        cntW += 1
                else:
                    if board[r + i][c + j] != 'B':
                        cntW += 1

                if cntB > ans and cntW > ans:
                    break

            if cntB > ans and cntW > ans:
                break

        if ans > min(cntB, cntW):
            ans = min(cntB,cntW)

print(ans)