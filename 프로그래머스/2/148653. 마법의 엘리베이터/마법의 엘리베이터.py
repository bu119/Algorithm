import heapq

def solution(storey):
    # 마법의 돌을 아끼기 위해 민수는 항상 최소한의 버튼을 눌러서 이동
    # 민수가 어떤 층에서 엘리베이터를 타고 0층으로 내려가는데 필요한 마법의 돌의 최소 개수
    # -1, +1, -10, +10, -100, +100 등, 절댓값이 10^c (c ≥ 0 인 정수) 형태인 정수들이 적힌 버튼이 있다.
    # 엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면 엘리베이터는 움직이지 않는다.
    # 0층으로 가기 위해 필요한 마법의 돌의 최소값을 return 하도록 solution 함수를 완성하세요.

    heap = []
    heapq.heappush(heap, (0, storey))

    while heap:
        cnt, floor = heapq.heappop(heap)

        if floor == 0:
            return cnt

        # 일의 자리 나머지
        num = floor % 10
        # 층수 욜리기
        up = 10 - num
        # 층수 내리기
        down = num

        if up < down:
            heapq.heappush(heap, (cnt + up, floor // 10 + 1))
        elif up > down:
            heapq.heappush(heap, (cnt + down, floor // 10))
        else:
            # 5이면 둘다하기
            heapq.heappush(heap, (cnt + 5, floor // 10))
            heapq.heappush(heap, (cnt + 5, floor // 10 + 1))

    return 100000001