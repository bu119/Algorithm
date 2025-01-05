# 모음
vowels = {"a", "e", "i", "o", "u"}

while True:
    password = input()
    # 종료 조건
    if password == "end":
        break
        
    # 문자열 길이
    n = len(password)
    # 조건 체크
    condition = True

    # 조건 1
    # 모음(a,e,i,o,u) 하나를 반드시 포함
    set_password = set(password)
    if not (set_password & vowels):
        # 조건 만족 안함
        condition = False

    if condition:
        # 모음 개수 세기
        vowel_cnt = 0
        for i in range(n):
            # 조건 2
            # 모음 또는 자음이 3개 연속으로 오면 안됨
            if password[i] in vowels:
                vowel_cnt += 1
            # 4개 째부터 앞에 문자 판단
            if i > 2 and password[i-3] in vowels:
                vowel_cnt -= 1
            # 3개 부터 판단
            if i > 1 and vowel_cnt in {0, 3}:
                condition = False
                break

            # 조건 3
            # 같은 글자가 연속 두번 오면 안됨 (ee 와 oo는 허용)
            if i > 0 and password[i-1] == password[i] and password[i] not in {"e", "o"}:
                # 조건 만족 안함
                condition = False
                break

    if condition:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")