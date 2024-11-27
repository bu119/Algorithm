def solution(book_time):
    # 분으로 변환하여 시작, 종료 시간을 각각 저장
    times = []
    # 시간 -> 분으로 변환하여 저장
    for start, end in book_time:
        # 시작 시각 저장 (1) 표시
        start_hour, start_minute = map(int, start.split(":"))
        times.append((start_hour*60 + start_minute, 1))
        # 종료 시각 + 10분 청소 저장 (-1) 표시 
        end_hour, end_minute = map(int, end.split(":"))
        times.append((end_hour*60 + end_minute + 10, -1))

    # 시간을 기준으로 정렬
    times.sort()
    # 최대 방 개수 저장
    answer = 0
    # 현재 방 개수 저장
    room_cnt = 0
    for time, room in times:
        # 시작 시각이면 +1, 종료된 시각이면 -1
        room_cnt += room
        # 최댓값 갱신
        answer = max(answer, room_cnt)

    return answer