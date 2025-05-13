def solution(n, bans):
    # 숫자 위치를 문자로 표현
    def get_string(idx):
        string = []
        while idx > 0:
            # 인덱스 기반으로 변경 (0~25)
            idx -= 1
            string.append(alphabet[idx % 26])
            idx //= 26
        return ''.join(reversed(string))

    # 문자를 숫자 위치로 표현
    def get_idx_to_string(string):
        m = len(string)
        idx = 0
        for x in range(m):
            idx += (26**(m-x-1))*(alphabet_num[string[x]])
        return idx
    
    # 삭제된 문자 적용 후 위치 숫자
    def get_new_n(number, new_n):
        for num in number:
            if num <= new_n:
                new_n += 1
            else:
                break
        return new_n

    
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    alphabet_num = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
        'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
        's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }
    # 주문을 숫자 위치로 변환해서 저장
    bans_num = []
    for ban in bans:
        bans_num.append(get_idx_to_string(ban))
    
    answer = get_string(get_new_n(sorted(bans_num), n))
    return answer