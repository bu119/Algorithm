from copy import deepcopy

# 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
# 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
def is_join(pre_i, pre_j, cur_i, cur_j, check_board):
    global new_board
    # 합쳐질 수 있는지 판단
    # 바로 앞 순서에서합쳐지지 않았으면
    if new_board[pre_i][pre_j] == check_board[cur_i][cur_j]:
        new_board[pre_i][pre_j] += check_board[cur_i][cur_j]
        return True
    return False


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