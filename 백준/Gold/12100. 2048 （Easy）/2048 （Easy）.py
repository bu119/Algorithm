from copy import deepcopy

def west_move(move_board):
    new_board = [[0]*n for _ in range(n)]

    # 서
    for wi in range(n):
        idx = 0
        pre_join = True
        for wj in range(n):
            # 0이 아니면
            if move_board[wi][wj]:
                # 바로 이전에 안 합쳐졌고, 이전 값과 같은 값을 가지면
                if not pre_join and new_board[wi][idx-1] == move_board[wi][wj]:
                    new_board[wi][idx-1] += move_board[wi][wj]
                    pre_join = True
                    continue

                # 이전에 안합쳐 쳤거나 이전값과 다르면 신경안쓰고 추가
                new_board[wi][idx] = move_board[wi][wj]
                idx += 1
                pre_join = False

    return new_board


def east_move(move_board):
    new_board = [[0] * n for _ in range(n)]

    # 동
    for ei in range(n):
        idx = n-1
        pre_join = True
        for ej in range(n-1,-1,-1):
            # 0이 아니면
            if move_board[ei][ej]:

                if not pre_join and new_board[ei][idx+1] == move_board[ei][ej]:
                        new_board[ei][idx+1] += move_board[ei][ej]
                        pre_join = True
                        continue

                new_board[ei][idx] = move_board[ei][ej]
                idx -= 1
                pre_join = False

    return new_board


def north_move(move_board):
    new_board = [[0] * n for _ in range(n)]

    # 북
    for ni in range(n):
        idx = 0
        pre_join = True
        for nj in range(n):
            # 0이 아니면
            if move_board[nj][ni]:

                if not pre_join and new_board[idx-1][ni] == move_board[nj][ni]:
                    new_board[idx-1][ni] += move_board[nj][ni]
                    pre_join = True
                    continue

                new_board[idx][ni] = move_board[nj][ni]
                idx += 1
                pre_join = False

    return new_board


def south_move(move_board):
    new_board = [[0] * n for _ in range(n)]

    # 남
    for si in range(n):
        idx = n-1
        pre_join = True
        for sj in range(n-1,-1,-1):
            # 0이 아니면
            if move_board[sj][si]:

                if not pre_join and new_board[idx+1][si] == move_board[sj][si]:
                    new_board[idx+1][si] += move_board[sj][si]
                    pre_join = True
                    continue

                new_board[idx][si] = move_board[sj][si]
                idx -= 1
                pre_join = False

    return new_board


def bruteforce(cnt, game_board):
    global ans

    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(game_board[i]))
        return

    bruteforce(cnt + 1, east_move(deepcopy(game_board)))
    bruteforce(cnt + 1, west_move(deepcopy(game_board)))
    bruteforce(cnt + 1, south_move(deepcopy(game_board)))
    bruteforce(cnt + 1, north_move(deepcopy(game_board)))


# 완전 탐색
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0
bruteforce(0, board)
print(ans)