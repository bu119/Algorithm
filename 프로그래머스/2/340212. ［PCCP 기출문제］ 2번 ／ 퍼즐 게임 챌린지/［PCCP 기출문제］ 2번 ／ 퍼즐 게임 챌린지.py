def solution(diffs, times, limit):
    # 퍼즐 게임 소요시간 구하기
    def puzzle_game(level):
        # 현재 숙련도에서 소요 시간
        total_time = 0
        # 이전 퍼즐의 소요 시간
        time_prev = 0
        # 퍼즐 게임 시작
        for i in range(n):
            # 현재 퍼즐의 난이도
            diff = diffs[i]
            # 현재 퍼즐의 소요 시간
            time_cur = times[i]
            # 시간 계산
            if diff <= level:
                total_time += time_cur
            else:
                # 틀린 횟수
                cnt = diff - level
                total_time += (time_cur + time_prev) * cnt + time_cur
            # 이전 퍼즐의 소요 시간 변경
            time_prev = time_cur

        return total_time

    
    n = len(diffs)
    # 숙련도 최댓값
    end_level = max(diffs)
    # 숙련도 최솟값
    start_level = 1
    # 숙련도 이분 탐색
    while start_level <= end_level:
        mid_level = (start_level + end_level) // 2
        game_time = puzzle_game(mid_level) 
        if game_time <= limit:
            end_level = mid_level - 1
        else:
            start_level = mid_level + 1
            
    # 숙련도의 최솟값
    return start_level