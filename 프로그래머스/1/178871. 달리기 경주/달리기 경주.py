def solution(players, callings):
    # {선수 이름: 현재 순위(인덱스)} 저장
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i

    for calling in callings:
        # 현재 순위
        i = rank[calling]
        # 딕셔너리 내 인덱스 정보 교체
        rank[players[i]] = i - 1
        rank[players[i-1]] = i
        # 순위 교체
        players[i-1], players[i] = players[i], players[i-1]

    return players
