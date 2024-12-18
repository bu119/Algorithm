import sys
input = sys.stdin.readline

# 탐색 문자열(pattern)의 각 위치에서 가장 긴 접두사 = 접미사의 길이를 저장
def kmp_table(pattern):
    m = len(pattern)
    # 문자열(pattern)에서 가장 긴 반복 문자열의 길이 저장
    table = [0 for _ in range(m)]
    # 접두사 포인터 (접두사의 끝 위치를 가리킴, 현재까지 일치한 길이)
    pi = 0
    # 접미사와 접두사를 하나씩 늘려가면서 비교
    # si는 접미사를 가리키는 포인터 (두 번째 문자부터 비교 시작)
    for si in range(1, m):
        # 접두사와 접미사가 일치하지 않는 경우
        while pi > 0 and pattern[si] != pattern[pi]:
            # 이전 일치 상태로 돌아감 (이전 접두사의 끝 위치로 이동)
            pi = table[pi - 1]
            # 현재까지의 접두사=접미사 정보를 활용해 다음 비교 위치를 조정

        # 접두사와 접미사가 일치하는 경우
        if pattern[si] == pattern[pi]:
            # 접두사 길이 증가 (pi는 가장 긴 접두사=접미사의 길이를 나타냄)
            pi += 1
            # 현재 위치(si)에 일치 길이 저장
            table[si] = pi
    # 최장 접두사 = 접미사의 길이 반환
    return max(table)


string = input()
n = len(string)
ans = 0
# 문자열의 모든 접미사에 최대 테이블 생성 및 최대 길이 갱신
for i in range(n):
    ans = max(ans, kmp_table(string[i:]))
print(ans)