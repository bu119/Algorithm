from collections import deque

def solution(queue1, queue2):
    answer = 0
    # queue1과 queue2의 모든 원소를 서로 바꾸고 다시 바꿔 원래의 모습으로 만들려면 "queue1 길이" * 4면 돌아온다.
    maxCnt = (len(queue1)) * 4
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1 + sum2) % 2:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)


    while sum1 != sum2:

        if sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
        else:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            
        answer += 1
          
        if not queue1 or not queue2 or maxCnt == answer:
            return -1      
    
    return answer