def solution(sequence):
    # 연속 펄스 부분 수열의 합 중 가장 큰 것
    # 연속 펄스 부분 수열: 연속 부분 수열 * 펄스 수열
    # 펄스 수열: 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열
    n = len(sequence)
    answer = 0
    # [1,-1, ...]
    even = 0
    # [-1, 1, ...]
    odd = 0
    for i in range(n):
        pulse_num = (sequence[i] if i%2 == 0 else -sequence[i])
        even = max(pulse_num, even + pulse_num)
        odd = min(pulse_num, odd + pulse_num)
        answer = max(answer, even, -odd)
    return answer