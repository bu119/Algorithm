def is_consistent(number):
    # 번호 저장
    prefix = set()
    # 번호 길이 저장
    number_len = set()
    for i in range(n):
        for j in number_len:
            # 접두어 가능한 지 확인
            if number[i][:j] in prefix:
                return "NO"
        # 번호 추가
        prefix.add(number[i])
        number_len.add(len(number[i]))
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    phone_number = sorted(input() for _ in range(n))
    print(is_consistent(phone_number))