# 비밀번호 규칙 만족하는지 확인하는 함수
def use_password():
    for k in range(4):
        if password_rule[k] > cnt[k]:
            return False
    return True


s, p = map(int, input().split())
string = input()
dna = {"A": 0, "C": 1, "G": 2, "T": 3}
# 비밀번호 가능 최소 개수
password_rule = list(map(int, input().split()))
# 비밀번호 가능한 부분 문자열 개수 저장
ans = 0
# 부분 문자열 문자 개수 저장
cnt = [0]*4
# 초기 개수 저장
for i in range(p):
    cnt[dna[string[i]]] += 1
# 초기 부분 문자열
sub_string = string[:p]
# 비밀번호 가능하면 저장
if use_password():
    ans += 1
# 부분 문자열 탐색
for i in range(s-p):
    cnt[dna[string[i]]] -= 1
    cnt[dna[string[i+p]]] += 1
    # 비밀번호 가능하면 개수 증가
    if use_password():
        ans += 1
print(ans)