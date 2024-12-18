# 접미사와 접두사를 하나씩 늘려가면서 비교 후 
# 일치하지 않으면, 일치했던 부분으로 돌아가서 재 검사하는 함수
def kmp_table(pattern):
    m = len(pattern)
    # 패턴 길이 저장
    table = [0 for _ in range(m)]
    # 접두사 포인터 -> 일치 패턴 길이
    pi = 0
    # 접미사와 접두사를 하나씩 늘려가면서 비교
    # 접미사 포인터
    for si in range(1, m):
        # pi와 si가 가리키는 문자가 다르면 -> 접두사 = 접미사 존재 x
        # 접두사 포인터 pi는 (접두사 = 접미사) 였던 이전 위치로 돌아감
        while pi > 0 and pattern[si] != pattern[pi]:
            pi = table[pi - 1]

        # pi와 si가 가리키는 문자가 일치하면 -> 접두사 = 접미사 존재 o
        # pi는 0부터 가장 길게 매칭된 패턴의 길이
        if pattern[si] == pattern[pi]:
            # 패턴 일치 길이 1 증가
            pi += 1
            # si 위치에 최장 일치 길이 저장
            table[si] = pi

    return max(table)


string = input()
n = len(string)
ans = 0
# 패턴이 될 수 있는 모든 문자열에 대해 최대값 갱신
for i in range(n):
    ans = max(ans, kmp_table(string[i:]))
print(ans)