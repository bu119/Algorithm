def solution(id_list, report, k):
    # 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송
    # 한 번에 한 명의 유저를 신고 가능 #
    # 동일한 유저에 대한 신고 횟수는 1회로 처리
    # k번 이상 신고된 유저는 게시판 이용이 정지
    # 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송 #
    # 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송
    
    # 이용자의 ID가 담긴 문자열 배열 id_list
    # 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report
    # 정지 기준이 되는 신고 횟수 k
    
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
                reported_cnt[j] += 1

    return list(reported_cnt.values())