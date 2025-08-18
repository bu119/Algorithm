def solution(sequence, k):
    n = len(sequence)
    answer = [-1, n]
    left = 0
    right = 0
    total = sequence[0]
    while left <= right and right < n:
        if right < n-1 and total < k:
            right += 1
            total += sequence[right]
        else:
            if total == k and right - left < answer[1] - answer[0]:
                answer[0] = left
                answer[1] = right
            total -= sequence[left]
            left += 1

    return answer