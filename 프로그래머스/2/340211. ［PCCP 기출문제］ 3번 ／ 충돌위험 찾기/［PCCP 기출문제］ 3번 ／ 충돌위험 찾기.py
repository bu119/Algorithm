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
    n = len(points)
    x = len(routes)
    m = len(routes[0])
        
    # 두 포인트 사이의 경로 저장
    route = dict()
    # 각 로봇이 몇 번째 방문인지 저장
    totalShortest = [[] for _ in range(x)]
    # 각 routes의 전체 경로 길이 저장
    routeLenth = [0]*x
    # 각 routes의 전체 경로 찾기
    for i in range(x):
        # 시작 포인트
        p1 = routes[i][0] - 1
        # 시작 위치 추가
        totalShortest[i].append(tuple(points[p1]))
        for j in range(1, m):
            # 도착 포인트
            p2 = routes[i][j] - 1
            # 앞서 이동한 경로가 아니라면 경로 탐색 후 저장 
            if (p1, p2) not in route:
                route[(p1, p2)] = save_shortest(points[p1], points[p2])
            # p1에서 p2 경로 저장
            totalShortest[i] += route[(p1, p2)]
            p1 = p2
        routeLenth[i] = len(totalShortest[i])
        
    # 충돌 횟수 저장    
    answer = 0
    # 이동 경로 탐색
    for i in range(sorted(routeLenth, reverse=True)[1]):
        # 각 로봇의 이동 위치, 방문 횟수 저장
        moved = dict()
        for j in range(x):
            # j번째 로봇의 경로가 마지막 지점에 도착했으면 통과
            if routeLenth[j] <= i:
                continue
            # 이동 중이라면 이동 위치 방문 횟수 저장
            if totalShortest[j][i] in moved:
                moved[totalShortest[j][i]] += 1
            else:
                moved[totalShortest[j][i]] = 1
        # 충돌 횟수 확인
        for posi in moved:
            if moved[posi] > 1:
                answer += 1
            
    return answer