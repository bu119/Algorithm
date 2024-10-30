from collections import deque

# 이동 위치 찾기
def save_shortest(start, end):
    sr, sc = start
    er, ec = end
    path = []
    # 행 이동
    if sr < er:
        for i in range(1, er-sr+1):
            path.append((sr+i, sc))
    elif sr > er:
        for i in range(1, sr-er+1):
            path.append((sr-i, sc))
    # 열 이동
    if sc < ec:
        for j in range(1, ec-sc+1):
            path.append((er, sc+j))
    elif sc > ec:
        for j in range(1, sc-ec+1):
            path.append((er, sc-j))
    
    return path
            
    
def solution(points, routes):    
    # points: 각 포인트의 위치
    # routes: 각 로봇이 지나야하는 경로의 순서 (경로: 1~n)    
    x = len(routes)
    m = len(routes[0])
    # 두 포인트 사이의 경로 저장
    shortest = dict()
    # 각 로봇의 이동위치, 시간 저장
    move = dict()
    # 각 로봇의 총 방문 경로 찾기
    for i in range(x):
        # 시작 포인트
        p1 = routes[i][0] - 1
        # 시작 위치
        r, c = points[p1]
        # 움직인 시간
        time = 0
        # 시작 포인트
        if (r, c, time) not in move:
            move[(r, c, time)] = 1
        else:
            move[(r, c, time)] += 1
            
        # 경로 탐색    
        for j in range(1, m):
            # 도착 포인트
            p2 = routes[i][j] - 1
            # 앞서 이동한 경로가 아니라면 경로 탐색 후 저장 
            if (p1, p2) not in shortest:
                shortest[(p1, p2)] = save_shortest(points[p1], points[p2])
            # 이동 위치, 시간 저장
            for r, c in shortest[(p1, p2)]:
                # 몇 번째 이동인지 체크
                time += 1
                # 각 위치를 몇 번째로 지나는 지 추가
                if (r, c, time) not in move:
                    move[(r, c, time)] = 1
                else:
                    move[(r, c, time)] += 1
            p1 = p2
    # 충돌 횟수 저장        
    answer = 0
    # 충돌 횟수 확인
    for k in move.values():
        # 위험 상황 발생
        if k > 1:
            answer += 1
    return answer