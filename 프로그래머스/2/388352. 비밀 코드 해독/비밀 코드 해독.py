from itertools import combinations

def solution(n, q, ans):
    # 가장 많이 일치하는 시스템 응답 인덱스와 일치 개수 반환
    def get_max_ans():
        value = ans[0]
        idx = 0
        for i in range(1, m):
            # 5가 최대 시스템 응답
            if ans[i] == 5:
                idx = i
                value = 5
                break

            if value < ans[i]:
                idx = i
                value = ans[i]
                
        return idx, value
    
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
    # 경우의 수를 줄이기 위해 겹치는 수가 제일 많은 입력 수 가져오기
    max_idx, max_ans = get_max_ans()
    # 1 ~ n 까지의 번호 중 가장 많이 일치하는 입력 정수 제외하고 가져오기
    number = set(range(1, n+1)) - set(q[max_idx])
    # 1 ~ n (입력 정수 제외) 에서 일치 안하는 개수 많큼 가져오기
    for x in list(combinations(number, 5-max_ans)):
        # 입력 정수에서 일치하는 만큼 가져오기
        for y in list(combinations(q[max_idx], max_ans)):
            # 합쳐서 5개로 만들기
            new_q = set(x) | set(y)
            # 기존 시스템 응답과 일치하면 조합에 개수 추가
            if is_secret_code_match(new_q):
                answer += 1
                   
    return answer