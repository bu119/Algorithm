def solution(sizes):
    width = 0
    high = 0
    for w, h in sizes:
        w1 = max(width, w)
        h1 = max(high, h)
        w2 = max(width, h)
        h2 = max(high, w)
        
        if w1 * h1 < w2 * h2:
            width = w1
            high = h1
        else:
            width = w2
            high = h2
            
    return width * high