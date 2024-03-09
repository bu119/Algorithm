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
        
        for key, value in dices[case[k]].items():
            dfs(k+1, case, ssum + key, cnt*value, team)

            
    n = len(dice)
    # 각 주사위 숫자 딕셔너리 형태로 저장 {번호:{1:2, 10:1, ...}}
    dices = dict()
    for i in range(n):
        dices[i+1] = dict()
        for num in dice[i]:
            if num in dices[i+1]:
                dices[i+1][num] += 1
            else:
                dices[i+1][num] = 1
    
    case = set(range(1, n+1))
    # (1, 2, ..., n) 중에 n//2개 뽑기
    cases = list(combinations(case, n//2))
    m = len(cases)
    # 승리할 확률이 가장 높은 팀
    max_win_team = []
    # 승리할 확률이 가장 높은 팀의 경우의 수
    max_win = 0
    for i in range(m//2):
        # A, B 팀 주사위 번호 모음([1,2])
        case_a = list(cases[i])
        case_b = sorted(case - set(case_a))
        # 각 팀이 나올 수 있는 합과 개수 저장
        team_a = dict()
        team_b = dict()
        # 선택한 각 주사위를 굴려서 나온 수의 합과 개수 구하기
        dfs(0, case_a, 0, 1, 'a')
        dfs(0, case_b, 0, 1, 'b')
        # 팀 a가 이긴 수
        win_a = 0
        # 팀 b가 이긴 수 저장
        win_b = 0
        for a in team_a:
            for b in team_b:
                # 해당 경우의 수
                winning_cnt = team_a[a] * team_b[b]
                if a > b:
                    win_a += winning_cnt
                elif a < b:
                    win_b += winning_cnt
        # a팀의 이긴 횟수가 더 크면            
        if max_win < win_a:
            max_win = win_a
            max_win_team = case_a
        # b팀의 이긴 횟수가 더 크면    
        if max_win < win_b:
            max_win = win_b
            max_win_team = case_b
                    
    return max_win_team