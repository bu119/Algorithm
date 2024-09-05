# 상어에는 1 이상 M 이하의 자연수 번호
# 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내
# 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.
# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다.
# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동
# 자신의 냄새를 그 칸에 뿌린다.
# 냄새는 상어가 k번 이동하고 나면 사라진다.

# 각 상어가 이동 방향을 결정할 때,
# 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
# 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
# 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

# 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성
def move_shark():
    # 보드 내 존재하는 상어 개수 체크
    cnt = 0
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
            # 보드 내 존재하는 상어 개수 증가
            cnt += 1
        else:
            # 이전에 이동한 상어가 이미 존재한다면 쫓아내기
            del sharks[z]

    return cnt


def no_smell(i, si, sj, sd):
    # 우선순위에 따른 4방향 탐색
    for nd in priorities[i][sd]:
        ni = si + di[nd]
        nj = sj + dj[nd]
        # 아무 냄새가 없는 칸
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and smellTimer[ni][nj] == 0:
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