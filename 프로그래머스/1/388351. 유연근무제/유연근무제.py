def solution(schedules, timelogs, startday):
    # 직원이 지각했는지 확인하는 함수
    def isLate(employee, work_start_time):
        for day in range(7):
            # 주말이면 (6, 7)
            if (day + startday) % 7 in {6, 0}:
                continue
            # 지각하면
            if timelogs[employee][day] > work_start_time:
                return True
        return False
    
    # 직원 n명
    n = len(schedules)
    # 상품을 받을 직원 수 저장
    answer = 0
    for i in range(n):
        scheduled_time = schedules[i] + 10
        # 10분 더했을 때 60분 넘으면
        if scheduled_time % 100 >= 60:
            scheduled_time += 40
        # 지각 안했으면
        if not isLate(i, scheduled_time):
            answer += 1
            
    return answer