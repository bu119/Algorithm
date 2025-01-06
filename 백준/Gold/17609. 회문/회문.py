def is_palindrome():
    # 왼쪽 인덱스
    start = 0
    # 오른쪽 인덱스
    end = n-1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            # 다른 경우 -> 한 문자열 제거 후 회문 확인
            # end쪽 제거
            if start <= end - 1:
                palindrome = string[:end] + string[end + 1:]
                if palindrome == palindrome[::-1]:
                    return 1
            # start쪽 제거
            if start + 1 <= end:
                palindrome = string[:start] + string[start + 1:]
                if palindrome == palindrome[::-1]:
                    return 1
            return 2
    return 0


t = int(input())
for _ in range(t):
    # 문자열
    string = input()
    n = len(string)
    print(is_palindrome())