import heapq

def solution(numbers):
        
    # 각 번호로 부터 최소 시간 저장 (인덱스, 위치)
    def find_weights_dijkstra(idx, x, y):
        heap = []
        # 왼손 위치, 현재 가중치
        heapq.heappush(heap, (0, x, y))
        dist[idx][x][y] = 1

        while heap:
            currCost, x, y = heapq.heappop(heap)
            
            # 현재 비용이 저장된 비용보다 크면 탐색안함
            if currCost > dist[idx][x][y]:
                continue

            for k in range(8):
                nx = x + di[k]
                ny = y + dj[k]
                # 가중치
                if k < 4:
                    nc = currCost + 2
                else:
                    nc = currCost + 3
                if 0 <= nx < 4 and 0 <= ny < 3 and nc < dist[idx][nx][ny]:
                        dist[idx][nx][ny] = nc
                        heapq.heappush(heap, (nc, nx, ny))
    
    # 타이핑 최소 시간 찾기 
    def find_min_cost_dijkstra():

        heap = []
        # 비용, 왼손 번호, 오른손 번호, 다음 숫자 인덱스 
        heap.append((0, "4", "6", 0))
        visited = dict()
        # (왼손 번호, 오른손 번호, 다음 인덱스): 비용
        visited[("4", "6", 0)] = 0
        while heap:
            # 현재 비용, 왼손 위치, 오른손 위치, 다음에 누를 숫자 인덱스
            cost, leftHand, rightHand, numIdx = heapq.heappop(heap)
            # 같은 숫자 위에 두 엄지 손가락 불가
            if leftHand == rightHand:
                continue
            # 현재 비용이 저장된 비용보다 크면 탐색 안함
            if visited[(leftHand, rightHand, numIdx)] < cost:
                continue
            
            # 마지막 숫자 타이핑이 끝나면 최소 시간 반환
            if numIdx == n:
                return cost
        
            # 타이핑할 숫자
            number = numbers[numIdx]
            # 티이핑할 숫자 위치
            ex, ey = board[number]
            # 왼손 위치 인덱스
            leftIdx = convertToIdx[leftHand]
                
            # 왼손 이동
            if (number, rightHand, numIdx + 1) not in visited or visited[(number, rightHand, numIdx + 1)] > cost + dist[leftIdx][ex][ey]:
                visited[(number, rightHand, numIdx + 1)] = cost + dist[leftIdx][ex][ey]
                heapq.heappush(heap, (cost + dist[leftIdx][ex][ey], number, rightHand, numIdx + 1))
            # 오른손 위치 인덱스
            rightIdx = convertToIdx[rightHand]
            # 오른손 이동
            if (leftHand, number, numIdx + 1) not in visited or visited[(leftHand, number, numIdx + 1)] > cost + dist[rightIdx][ex][ey]:
                visited[(leftHand, number, numIdx + 1)] = cost + dist[rightIdx][ex][ey]
                heapq.heappush(heap, (cost + dist[rightIdx][ex][ey], leftHand, number, numIdx + 1))

    
    # 자판의 위치 저장
    board = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2)
    }
    # 자판을 인덱스로 변환
    convertToIdx = {
        "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
        "7": 6, "8": 7, "9": 8, "*": 9, "0": 10, "#": 11
    }
    
    # 가능한 최대 비용
    maxV = 300001
    # 각 위치에서 최소 시간 저장
    dist = [[[maxV] * 3 for _ in range(4)] for _ in range(12)]
    # 상하좌우(2), 대각선(3)
    di = [-1, 1, 0, 0, -1, 1, 1, -1]
    dj = [0, 0, -1, 1, 1, 1, -1, -1]
    
    # 각 위치에서 최소 시간 저장
    for i in board:
        find_weights_dijkstra(convertToIdx[i], board[i][0], board[i][1])

    # 문자열 길이
    n = len(numbers)
    # 최소 가중치 저장
    answer = find_min_cost_dijkstra()

    return answer