def solution(user_id, banned_id):
    n = len(banned_id)
    banned_user = set()
    users = set(user_id)
    # 불량 사용자 목록에 해당하는 사용자 목록
    visited = set()
    
    
    # 불량 사용자 a에 사용자 b가 해당되는 지 확인 (c는 길이)
    def is_same(a, b, c):
        for x in range(c):
            # "*" 는 비교 x
            if a[x] == "*":
                continue
            # 문자가 다르면 False 반환
            if a[x] != b[x]:
                return False
        return True
    
    def dfs(banned_idx):
        nonlocal visited
        if banned_idx == n:
            visited.add(tuple(sorted(banned_user)))
            return
        # 불량 사용자 길이 *
        m = len(banned_id[banned_idx])
        for user in users:
            # 비교 사용자 길이
            k = len(user)
            # 길이 비교
            if m != k:
                continue
            # 길이가 같으면 불량 사용자인지 탐색
            if is_same(banned_id[banned_idx], user, m):
                # 같으면 불량사용자에 포함
                banned_user.add(user)
                # 응모 사용자에서 제거
                users.remove(user)
                # 다음 불량 사용자 아이디 목록 탐색
                dfs(banned_idx+1)
                # 재귀 나오면 복구
                banned_user.remove(user)
                users.add(user)
                
                
    dfs(0)
    return len(visited)