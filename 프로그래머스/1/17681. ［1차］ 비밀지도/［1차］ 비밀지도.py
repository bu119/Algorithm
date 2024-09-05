def make_binary_code(n, num):
    binaryCode = []

    while num:
        binaryCode.append(num % 2)
        num //= 2
    # 길이 맞추기
    binaryCode += [0] * (n - len(binaryCode))
    binaryCode.reverse()
    return binaryCode

def solution(n, arr1, arr2):
    answer = [""] * n

    for i in range(n):
        code1 = make_binary_code(n, arr1[i])
        code2 = make_binary_code(n, arr2[i])
        for j in range(n):
            if code1[j] + code2[j] == 0:
                answer[i] += " "
            else:
                answer[i] += "#"

    return answer