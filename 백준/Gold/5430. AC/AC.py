from collections import deque

t = int(input())
for _ in range(t):
    # 수행할 함수
    p = input()
    # 배열에 들어있는 수의 개수
    n = int(input())
    arrX = input().strip('[]')
    if arrX:
        arrX = deque(map(int, arrX.split(',')))

    # 뒤집었는 지 확인
    checkRev = False
    # 에러 인지
    checkE = False
    # 연산 시행
    for i in p:
        if i == 'D':
            # 에러 체크
            if not arrX:
                checkE = True
                break

            # 처음 방향
            if not checkRev:
                arrX.popleft()
            else:
                # 뒤집은 방향일 때
                arrX.pop()
        else:
            # 뒤집기
            checkRev = not checkRev

    if checkE:
        print('error')
    else:
        if checkRev:
            arrX = reversed(arrX)
        print('['+','.join(map(str, arrX))+']')