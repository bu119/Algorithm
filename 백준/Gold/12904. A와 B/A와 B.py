s = input()
t = input()
n = len(s)
m = len(t)

while n < m:
    # 문자열의 뒤에 A를 추가 -> A 제거
    if t[m-1] == "A":
        t = t[:m-1]
    # 문자열을 뒤집고 뒤에 B를 추가 -> B 삭제 -> 뒤집
    else:
        t = t[:m-1][::-1]
    m -= 1

if s == t:
    print(1)
else:
    print(0)