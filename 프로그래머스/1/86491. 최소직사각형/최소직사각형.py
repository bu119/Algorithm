def solution(sizes):
    maxW = 0
    maxH = 0
    for w, h in sizes:
        maxW = max(w, h, maxW)
        maxH = max(min(w, h), maxH)
    return maxW * maxH