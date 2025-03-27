def solution(user_id, banned_id):
    
    # 불량 사용자가 될 수 있는 지 확인
    def is_banned_user(a, b):
        # a: 불량사용자
        # b: 불량사용자 후보
        k = len(a)
        for i in range(k):
            # "*"이 아니고, 두 문자가 같지 않으면 False 반환
            if a[i] != "*" and a[i] != b[i]:
                return False
        return True
    
    # 불량 사용자 후보 가져오기
    def find_banned_candidates():
        # 불량 사용자 후보 저장
        candidates = dict()
        for i in range(n):
            x = len(banned_id[i])
            candidates[i] = set()
            for j in range(m):
                y = len(user_id[j])
                # 아이디 길이가 같고 불량 사용자 후보이면
                if x == y and is_banned_user(banned_id[i], user_id[j]):
                    # 불량 후보로 저장
                    candidates[i].add(j)
        return candidates
    
    # 제재 아이디 목록 찾기
    def dfs(banned_idx):
        if banned_idx == n:
            answer.add(tuple(sorted(visited)))
            return
        # 불량 사용자 후보 탐색
        for candidate in banned_candidates[banned_idx]:
            if candidate not in visited:
                visited.add(candidate)
                dfs(banned_idx+1)
                visited.remove(candidate)

    # 제재 아이디 개수
    n = len(banned_id)
    # 사용자 수
    m = len(user_id)
    # 제재 아이디 목록 저장
    answer = set()
    banned_candidates = find_banned_candidates()
    # 현재 탐색에서 선정된 제재 아이디 방문 체크
    visited = set()
    dfs(0)
    
    return len(answer)