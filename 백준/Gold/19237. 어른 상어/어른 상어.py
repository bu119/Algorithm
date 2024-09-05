def move_shark():
    # 보드 내 존재하는 상어 위치 및 개수 체크
    sharkCheck = set()
    # 번호 별 이동
    for z in range(1, m + 1):
        if z not in sharks:
            continue
        # 현재 상어 위치, 방향
        si, sj, sd = sharks[z]
        x, y, d = no_smell(z, si, sj, sd)

        # 상어 위치, 방향 갱신 및 상어 쫓아내기
        if (x, y) not in sharkCheck:
            sharkCheck.add((x, y))
            # 이동한 상어 위치, 방향 갱신
            sharks[z] = [x, y, d]

        else:
            # 이전에 이동한 상어가 이미 존재한다면 쫓아내기
            del sharks[z]
    # 보드 내 존재하는 상어 개수
    return len(sharkCheck)


def no_smell(i, si, sj, sd):
    # 우선순위에 따른 4방향 탐색
    for nd in priorities[i][sd]:
        ni = si + di[nd]
        nj = sj + dj[nd]
        # 아무 냄새가 없는 칸
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            return ni, nj, nd

    # 냄새 없는 칸이 없으면 내 냄새 칸으로 이동
    return my_smell(i, si, sj, sd)


def my_smell(i, si, sj, sd):
    # 우선순위에 따른 4방향 탐색
    for nd in priorities[i][sd]:
        ni = si + di[nd]
        nj = sj + dj[nd]
        # 내 냄새가 나는 칸
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == i:
            return ni, nj, nd

    return -1, -1, -1


def spray_smell():
    for key in sharks:
        x, y, _ = sharks[key]
        # 자신의 위치에 냄새 뿌리기
        visited[x][y] = key
        smellTimer[x][y] = k


def reduce_smell():
    for x in range(n):
        for y in range(n):
            if smellTimer[x][y] > 0:
                smellTimer[x][y] -= 1
                if smellTimer[x][y] == 0:
                    visited[x][y] = 0


n, m, k = map(int, input().split())
# 격자 저장
board = []
# 상어의 초기 위치 저장: {상어 번호: 위치}
sharks = dict()
# 상어 번호별 각 방향에서의 우선순위 저장: {상어 번호: 우선순위 배열} ex) {1: [[],[4,2,3,1],[2,3,1,4], ... }
priorities = dict()
# 냄새 남아 있는 시간 저장
smellTimer = [[0]*n for _ in range(n)]
# 누구 냄새 인지 저장
visited = [[0]*n for _ in range(n)]

# 격자 및 상어 위치 저장
for i in range(n):
    row = list(map(int, input().split()))
    # 상어 번호별 위치 저장 (추후 방향 같이 저장)
    for j in range(n):
        if row[j] > 0:
            sharks[row[j]] = [i, j, 0]
    board.append(row)
# 상어의 초기 방향 저장
initSharksDirection = list(map(int, input().split()))
for i in range(m):
    sharks[i+1][2] = initSharksDirection[i]

# 각 상어의 방향 우선순위 저장 (각 상어의 위, 아래, 완쪽, 오른쪽 방향 당 우선순위가 차례로 주어짐)
for i in range(1, m+1):
    # 각 상어의 방향별 우선순위를 배열로 저장 (베열 인덱스 상어의 방향)
    priorities[i] = [[]]
    for _ in range(4):
        priority = list(map(int, input().split()))
        priorities[i].append(priority)

# 각 숫자가 의미하는 방향을 배열로 저장 (1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽 -> 배열의 인덱스)
# 상하좌우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

time = -1
for t in range(1, 1001):
    # 냄새 뿌리기
    spray_smell()
    # 상어 이동
    sharkCnt = move_shark()
    if sharkCnt == 1:
        time = t
        break
    # 냄새 줄이기
    reduce_smell()
print(time)