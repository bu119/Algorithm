from itertools import combinations

# 해당 경우에서 선생님 피하기가 가능한 지 체크
def avoid_teacher():
    # 선생님들 탐색 (선생님의 수는 5이하이므로 학생을 탐색하는 것 보다 효율적이다.)
    for x, y in teachers:
        # 특정 선생님이 4방향에서 감시 (학생 만나는지 체크)
        # 특정 선생님이 학생을 잡으면 True, 못 잡으면 False
        for k in range(4):
            for z in range(1, n):
                nx = x + di[k] * z
                ny = y + dj[k] * z
                # 이동 가능한 범위이면 계속 탐색 (범위 안에 있고, 장애물을 만나지 않으면)
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in obstacle:
                    # 학생을 만나면 성공
                    if graph[nx][ny] == "S":
                        return False
                else:
                    break
    return True


n = int(input())
graph = []
# 선생님 위치
teachers = []
# 장애물 후보
candidates = []
for i in range(n):
    row = list(input().split())
    for j in range(n):
        if row[j] == 'X':
            candidates.append((i, j))
        elif row[j] == 'T':
            teachers.append((i, j))
    graph.append(row)

# 상하좌우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
# 장애물 후보들 (3개의 장애물을 설치)
obstacles = combinations(candidates, 3)
# 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부 저장
ans = "NO"
# 각 장애물 후보를 탐색
for obstacle in obstacles:
    if avoid_teacher():
        ans = "YES"
        break
print(ans)