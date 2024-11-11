def solution(diffs, times, limit):
    # 퍼즐 게임 소요시간 구하기
    def puzzle_game(level):
        # 현재 숙련도에서 소요 시간
        total_time = 0
        # 퍼즐 게임 시작
        for i in range(n):
            # 시간 계산
            if diffs[i] <= level:
                total_time += times[i]
            else:
                # 틀린 횟수
                cnt = diffs[i] - level
                total_time += (times[i] + times[i-1]) * cnt + times[i]

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