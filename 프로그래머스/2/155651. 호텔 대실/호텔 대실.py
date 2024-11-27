import heapq

def solution(book_time):
    # 최소한의 객실만을 사용하여 예약 손님들을 받
    # 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소
    n = len(book_time)
    # 분으로 변환하여 저장
    book_times = []
    # 시간 -> 분으로 변환
    for i in range(n):
        time = []
        for j in range(2):       
            hour, minute = map(int, book_time[i][j].split(":"))
            time.append((hour*60 + minute))
        book_times.append(time)
    # 정렬
    book_times.sort()
    # 방마다 끝나는 시간 저장 (heap)
    rooms = []
    for start, end in book_times:
        if rooms and rooms[0] + 10 <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)