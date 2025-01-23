import heapq

# 최소 비용 다익스트라 알고리즘
def solution(board):
    
    def dijkstra():
        # 최대 비용
        max_cost = 25*25*500
        # 3차원 배열: 방향에 따른 최소비용 저장
        visited = [[[max_cost] * n for _ in range(n)] for _ in range(4)]
        # 비용, 방향, 행 열 위치
        # 동쪽, 남쪽 방향 두개 저장, 출발점 (0,0)
        heap = [(0, 0, 0, 0), (0, 1, 0, 0)]
        # 출발점 방문 체크
        for i in range(4):
            visited[i][0][0] = 0
            
        while heap:
            # 현재 비용, 방향, 행 열 위치
            cost, k, x, y = heapq.heappop(heap)

            if visited[k][x][y] < cost:
                continue
            
            for nk in range(4):
                nx = x + dx[nk]
                ny = y + dy[nk]
                if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                    # 도로 설계 비용
                    # 방향이 같으면 직선도로 생성
                    # 직선 도로면 직선도로 1개만 추가: 100원
                    new_road_cost = 100
                    # 방향이 다르면 코너 생성
                    # 코너면 코너 1개 + 직선도로 1개: 600원(500원 + 100원)
                    if k != nk:
                        new_road_cost += 500
                    # 도로를 추가한 설계 비용
                    next_cost = cost + new_road_cost
                    # 새로 설계한 도로가 기존에 저장된 비용보다 적으면 비용 갱신
                    if next_cost < visited[nk][nx][ny]:
                        visited[nk][nx][ny] = next_cost
                        heapq.heappush(heap, (next_cost, nk, nx, ny))
        # 각 방향에서의 최소비용을 가져와 비교하여 최소비용 반환
        return min(visited[0][n-1][n-1], visited[1][n-1][n-1], visited[2][n-1][n-1], visited[3][n-1][n-1])
        

    n = len(board)
    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = dijkstra()
    return answer