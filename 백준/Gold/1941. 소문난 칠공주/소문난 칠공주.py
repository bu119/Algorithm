from collections import deque
import sys
input = sys.stdin.readline

# 7명 선택
def dfs(idx, yCnt, memCnt):
    global cnt, members

    # 임도‘연’파가 4이상이면 이다‘솜’파가 4이상 안됨
    if yCnt >= 4:
        return

    if memCnt == 7:
        if bfs(members):
            cnt += 1
        return

    for k in range(idx, 25):
        # 25번 까지 중 행은 번호를 5로 나눈 몫
        ni = k // 5
        # 25번 까지 중 열은 번호를 5로 나눈 나머지
        nj = k % 5
        # 임도‘연’파 변화 저장
        new = yCnt
        if students[ni][nj] == 'Y':
            new += 1
        # 해당 위치를 멤버로 추가
        members.append((ni, nj))
        dfs(k+1, new, memCnt+1)
        # 해당 위치를 제거 (멤버X)
        members.pop()

        
# 7명이 인접해 있는지 확인        
def bfs(members):
    deq = deque()
    # 7공주 방문 체크
    visited = [[1] * 5 for _ in range(5)]

    # 첫 사람부터 탐색 시작
    total = 1
    deq.append(members[0])
    # 방문 위치 제거하고 저장
    for x, y in members[1:]:
        visited[x][y] = 0

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                # 방문 체크
                visited[nx][ny] = 1
                deq.append((nx,ny))
                total += 1
    # 7명 모두 인접
    if total == 7:
        return True
    return False


students = [input() for _ in range(5)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 7공주 경우의 수 저장
cnt = 0
# 7공주 멤버 저장
members = []
dfs(0, 0, 0)

print(cnt)