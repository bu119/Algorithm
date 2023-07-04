def solution(id_list, report, k):
    
    reported_cnt = {}
    reported_me = {}
    
    for user in id_list:
        reported_cnt[user] = 0
        reported_me[user] = set()
    
    for info in report:
        i, user = info.split()
        # 나를 신고한 유저 목록
        reported_me[user].add(i)

    n = len(id_list)

    for i in range(n):
        # 나를 투표한 사람이 기준치 이상이면
        if k <= len(reported_me[id_list[i]]):
            # 나를 투표한 사람에게 메일을 날림
            for j in reported_me[id_list[i]]:
                # 내가 받은 메일 수
                reported_cnt[j] += 1

    return list(reported_cnt.values())