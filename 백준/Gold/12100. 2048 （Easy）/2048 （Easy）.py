from copy import deepcopy

def east_move(new_board):
    # 동
    for ei in range(n):
        idx = n-1
        for ej in range(n-2,-1,-1):
            if new_board[ei][ej]:
                tmp = new_board[ei][ej]
                new_board[ei][ej] = 0

                if new_board[ei][idx] == 0:
                    new_board[ei][idx] = tmp

                elif new_board[ei][idx] == tmp:
                    new_board[ei][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    new_board[ei][idx] = tmp

    return new_board


def west_move(new_board):
    # 서
    for wi in range(n):
        idx = 0
        for wj in range(1,n):
            if new_board[wi][wj]:  # 0이 아닌 값이
                tmp = new_board[wi][wj]
                new_board[wi][wj] = 0  # 일단 비워질꺼니까 0으로 바꿈

                if new_board[wi][idx] == 0:  # 비어있으면
                    new_board[wi][idx] = tmp  # 옮긴다

                elif new_board[wi][idx] == tmp:  # 같으면
                    new_board[wi][idx] *= 2  # 합친다
                    idx += 1
                else:  # 비어있지도 않고 다른 값일때
                    idx += 1  # pass
                    new_board[wi][idx] = tmp  # 바로 옆에 붙임

    return new_board


def north_move(new_board):
    # 북
    for nj in range(n):
        idx = 0
        for ni in range(1,n):
            if new_board[ni][nj] != 0:
                tmp = new_board[ni][nj]
                new_board[ni][nj] = 0
                # idx가 가리키는 수가 0일 때
                if new_board[idx][nj] == 0:
                    new_board[idx][nj] = tmp
                # idx가 가리키는 수와 현재 위치의 수가 같을 때
                elif new_board[idx][nj] == tmp:
                    new_board[idx][nj] *= 2
                    idx += 1
                # idx가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    idx += 1
                    new_board[idx][nj] = tmp

    return new_board


def south_move(new_board):

    # 남
    for sj in range(n):
        idx = n-1
        for si in range(n-1,-1,-1):
            if new_board[si][sj]:
                tmp = new_board[si][sj]
                new_board[si][sj] = 0

                if new_board[idx][sj] == 0:
                    new_board[idx][sj] = tmp

                elif new_board[idx][sj] == tmp:
                    new_board[idx][sj] *= 2
                    idx -= 1

                else:
                    idx -= 1
                    new_board[idx][sj] = tmp

    return new_board


def bruteforce(cnt, move_board):
    global ans

    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(move_board[i]))
        return

    bruteforce(cnt + 1, east_move(deepcopy(move_board)))
    bruteforce(cnt + 1, west_move(deepcopy(move_board)))
    bruteforce(cnt + 1, south_move(deepcopy(move_board)))
    bruteforce(cnt + 1, north_move(deepcopy(move_board)))


# 완전 탐색
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0
bruteforce(0, board)
print(ans)