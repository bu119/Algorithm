from itertools import combinations

def solution(n, q, ans):
    # 기존 시스템 응답과 일치 여부 반환
    def is_secret_code_match(num):
        for i in range(m):
            if len(num & set(q[i])) != ans[i]:
                return False
        return True
        
    # 가능한 정수 조합의 개수 저장
    answer = 0
    # m번 시도
    m = len(ans)
    # 1 ~ n 에서 5개 정수 가져오기
    for new_q in list(combinations(range(1,n+1), 5)):
        # 기존 시스템 응답과 일치하면 조합에 개수 추가
        if is_secret_code_match(set(new_q)):
            answer += 1
                   
    return answer