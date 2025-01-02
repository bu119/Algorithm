import sys
input = sys.stdin.readline

# 심장 찾기
def find_heart():
    # 맨 윗 줄 부터 처음 등장하는 부분이 머리
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "*":
                # 심장은 머리 바로 아랫 칸
                return i+1, j

# 신체 길이 측정
def measure_body(i, j, d):
    cnt = 1
    while 0 <= i+di[d] < n and 0 <= j+dj[d] < n and graph[i+di[d]][j+dj[d]] == "*":
        cnt += 1
        i += di[d]
        j += dj[d]
    return cnt, i, j


n = int(input())
graph = [input() for _ in range(n)]
# 동서 남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
visited = [[0]*n for _ in range(n)]
# 심장이 위치한 행, 열
x, y = find_heart()
# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이 순
left_arm, _, _ = measure_body(x, y-1, 1)
right_arm, _, _ = measure_body(x, y+1, 0)
waist, wx, wy = measure_body(x+1, y, 2)
left_leg, _, _ = measure_body(wx+1, wy-1, 2)
right_leg, _, _ = measure_body(wx+1, wy+1, 2)

print(x+1, y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)