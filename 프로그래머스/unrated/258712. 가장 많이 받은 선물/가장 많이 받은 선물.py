def solution(friends, gifts):
    n = len(friends)
    # {이름: 인덱스 ...}의 딕셔너리 형태로 저장
    friendsIdx = dict()
    for i in range(n):
        friendsIdx[friends[i]] = i
        
    # 선물 주고 받은 개수 저장 
    movingInfo = [[0]*n for _ in range(n)]
    # 선물 지수 저장
    giftIndex = [0]*n
    for gift in gifts:
        # A: 준 사람, B: 받은 사람
        A, B = gift.split()
        # 행: 준 사람, 열: 받은 사람
        movingInfo[friendsIdx[A]][friendsIdx[B]] += 1
        # 준 사람 선물 지수 변동 (한번에 변경)
        giftIndex[friendsIdx[A]] += 1
        # 받은 사람 선물 지수 변동
        giftIndex[friendsIdx[B]] -= 1

    # 다음 달에 받는 선물 수 저장
    getNextMonth = [0]*n
    for a in range(n-1):
        for b in range(a+1, n):
            # a가 b에게 주다.
            giveToB = movingInfo[a][b]
            # b가 a에게 주다.
            giveToA = movingInfo[b][a]
            # 두 사람이 선물을 주고받은 기록이 
            # 하나도 없거나 같다면
            if giveToB == giveToA or (not giveToB and not giveToA):
                # 선물 지수 큰 사람 + 1
                if giftIndex[a] > giftIndex[b]:
                    getNextMonth[a] += 1
                elif giftIndex[a] < giftIndex[b]:
                    getNextMonth[b] += 1
            # 있다면
            elif giveToB or giveToA:
                # 선물 더 많이 준 사람 +1
                if giveToB > giveToA:
                    getNextMonth[a] += 1
                else:
                    getNextMonth[b] += 1         
    return max(getNextMonth)