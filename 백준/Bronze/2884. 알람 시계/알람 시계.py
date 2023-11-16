h, m = map(int, input().split())

if m < 45 :	# 분단위가 45분보다 작을 때 
    if h == 0 :	# 0 시이면
        h = 23
        m += 60
    else :	# 0시가 아니면 (0시보다 크면)
        h -= 1	
        m += 60
        
print(h, m-45)