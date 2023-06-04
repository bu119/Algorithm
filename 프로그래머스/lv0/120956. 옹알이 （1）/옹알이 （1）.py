def solution(babbling):
    
    answer = 0
    for w in babbling:
        words = ["ye", "ma", "aya", "woo"]
        while w or words:      
            if w[:2] in words:
                words.remove(w[:2])
                w = w[2:]
            elif w[:3] in words:
                words.remove(w[:3])
                w = w[3:]
            else:
                break
        
        if not w:
            answer += 1
        
    return answer