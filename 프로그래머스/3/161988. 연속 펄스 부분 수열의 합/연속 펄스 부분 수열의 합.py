def solution(sequence):
    # 연속 펄스 부분 수열의 합 중 가장 큰 것
    # 연속 펄스 부분 수열: 연속 부분 수열 * 펄스 수열
    # 펄스 수열: 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열
    n = len(sequence)
    dp_even = [0]*n
    dp_odd = [0]*n
    for i in range(n):
        num = (1 if i%2 == 0 else -1)
        dp_even[i] = max(dp_even[i], dp_even[i-1] + sequence[i]*num)
        dp_odd[i] = max(dp_odd[i], dp_odd[i-1] - sequence[i]*num)
    return max(max(dp_even), max(dp_odd))