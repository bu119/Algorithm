from copy import deepcopy
from collections import deque 

def solution(m, n, board):
    # 블록 제거하는 함수
    def remove_blocks():
        new_board = deepcopy(board)
        removable_blocks = set()
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] != "" and board[x][y] == board[x][y+1] == board[x+1][y] == board[x+1][y+1]:
                    for rx, ry in [(x,y), (x,y+1), (x+1,y), (x+1,y+1)]:
                        new_board[rx][ry] = ""
                        removable_blocks.add((rx, ry))
        return new_board, len(removable_blocks)

    # 블록 내리는 함수
    def drop_blocks():
        # 열 기준 처리
        for col in range(n):
            # 현재 열의 숫자를 저장할 큐
            queue = deque()

            # 위에서 아래로 내려가며 숫자만 큐에 추가
            for row in range(m):
                if board[row][col] != "":
                    queue.append(board[row][col])

            # 아래쪽부터 숫자를 채워 넣기
            for row in range(m - len(queue)):  # 빈 공간을 0으로 유지
                board[row][col] = ""

            for row in range(m - len(queue), m):  # 큐에 있는 숫자를 아래부터 채우기
                board[row][col] = queue.popleft()

    answer = 0
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        # 현재 타임에 사라지는 블록 저장
        board, removable_cnt = remove_blocks()
        # 제거되는 블록이 없으면 탐색 종료
        if removable_cnt == 0:
            break
            
        # 사라지는 블록 개수 추가
        answer += removable_cnt
        # 블록 내리기
        drop_blocks()
    return answer