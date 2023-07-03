def solution(survey, choices):
    # 첫 번째 i+1번 질문의 비동의 관련,두 번째 i+1번 질문의 동의 관련
    # choices의 길이 = survey의 길이
    # choices[i]는 검사자가 선택한 i+1번째 질문의 선택지
    # 하나의 지표에서 각 성격 유형 점수가 같으면, 사전 순으로 빠른 성격 유형 선택
    
    answer = ''
    score = [0,-3,-2,-1,0,1,2,3]
    mbti = {"RT":0, "CF":0, "JM":0, "AN":0}
    
    n = len(survey)
    for i in range(n):
        # 위치만 다르고 중복된 지표가 존재하므로
        check = "".join(sorted(survey[i]))
        
        # 지표의 순서가 같은지 체크해서
        if survey[i] == check:
            # 같으면 그대로 더하고
            mbti[check] += score[choices[i]]
        else:
            # 반대면 +- 를 바꿔준다.
            mbti[check] -= score[choices[i]]
            
    for j in mbti:
        # 음수이거나 0 이면
        if mbti[j] <= 0:
            answer += j[0]
        else:
            # 양수이면
            answer += j[1]

    return answer