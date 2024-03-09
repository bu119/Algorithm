from itertools import combinations

def solution(dice):
    # 주사위 합과 나오는 경우의 수 계산
    def dfs(k, case, ssum, cnt, team):
        if k == n//2:
            if team == 'a':
                if ssum in team_a:
                    team_a[ssum] += cnt
                else:
                    team_a[ssum] = cnt
            else:
                if ssum in team_b:
                    team_b[ssum] += cnt
                else:
                    team_b[ssum] = cnt
            return
        
        # case[k]: 뽑은 주사위 번호 (dice_num[case[k]] = {숫자: 횟수})
        for key, value in dice_num[case[k]].items():
            dfs(k+1, case, ssum + key, cnt*value, team)

            
    n = len(dice)
    # 각 수가 나올 경우의 수 저장 {주사위 번호: {1:1, 숫자:개수, ...}...}
    dice_num = dict()
    for i in range(n):
        # 숫자가 나오는 개수 저장 {숫자: 개수}
        dice_num[i + 1] = dict()
        for num in dice[i]:
            if num in dice_num[i+1]:
                dice_num[i+1][num] += 1
            else:
                dice_num[i+1][num] = 1
        
    # 주사위 번호
    case = set(range(1, n+1))
    # 주사위 반틈씩 선택 (1, 2, ..., n 중에 n//2개 뽑기)
    cases = list(combinations(case, n//2))
    # 승리할 확률이 가장 높은 팀의 경우의 수
    winner_cnt = 0
    # 승리할 확률이 가장 높은 팀
    winner = []

    for i in range(len(cases)//2):
        # A, B 팀 주사위 번호 모음([1,2])
        case_a = list(cases[i])
        case_b = sorted(case - set(case_a))
        # 각 팀이 나올 수 있는 합과 개수 저장
        team_a = dict()
        team_b = dict()
        # 선택한 각 주사위를 굴려서 나온 수의 합과 개수 구하기
        # 주사위 굴린 횟수, 뽑은 주사위, 숫자 합, 경우의 수, 뽑은 팀
        dfs(0, case_a, 0, 1, 'a')
        dfs(0, case_b, 0, 1, 'b')
        # 각 팀이 이긴 경우의 수 저장
        win_a = 0
        win_b = 0
        # 주사위 합 비교
        for ssum_a in team_a:
            for ssum_b in team_b:
                # 해당 결과가 나올 경우의 수
                winning_cnt = team_a[ssum_a] * team_b[ssum_b]
                if ssum_a > ssum_b:
                    win_a += winning_cnt
                elif ssum_a < ssum_b:
                    win_b += winning_cnt
        # a팀의 이긴 횟수가 더 크면            
        if winner_cnt < win_a:
            winner_cnt = win_a
            winner = case_a
        # b팀의 이긴 횟수가 더 크면    
        if winner_cnt < win_b:
            winner_cnt = win_b
            winner = case_b
                    
    return winner