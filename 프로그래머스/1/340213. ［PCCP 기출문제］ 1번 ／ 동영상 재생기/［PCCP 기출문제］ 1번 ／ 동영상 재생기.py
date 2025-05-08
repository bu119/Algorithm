def solution(video_len, pos, op_start, op_end, commands):
    
    def time_to_seconds(time):
        minutes, seconds = map(int, time.split(":"))
        return minutes * 60 + seconds

    def seconds_to_time(seconds):
        return f"{seconds // 60:02}:{seconds % 60:02}"

    video_len_sec = time_to_seconds(video_len)
    second = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    for command in commands:
        # 오프닝 건너뛰기
        if op_start_sec <= second <= op_end_sec:
            second = op_end_sec
        # 명령어 적용
        if command == "prev":
            second -= 10
        else:
            second += 10
        # 영상의 처음 위치 또는 마지막 위치로 이동
        if second < 0:
            second = 0
        elif video_len_sec < second:
            second = video_len_sec

    # 오프닝 건너뛰기
    if op_start_sec <= second <= op_end_sec:
        second = op_end_sec

    return seconds_to_time(second)