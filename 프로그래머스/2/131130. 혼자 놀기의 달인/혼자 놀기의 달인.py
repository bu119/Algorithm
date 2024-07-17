# 각 카드에는 1부터 100까지 숫자
# 2 이상 100 이하의 자연수를 하나 정해 그 수보다 작거나 같은 숫자 카드들을 준비
# 준비한 카드의 수만큼 작은 상자를 준비

# 게임 방법
#1. 준비된 상자에 카드를 한 장씩 넣고, 상자를 무작위로 섞어 일렬로 나열
#2. 상자가 나열된 순서에 따라 1번부터 순차적으로 증가하는 번호를 붙
#3. 임의의 상자를 하나 선택하여 선택한 상자 안의 숫자 카드를 확인
#4. 확인한 카드에 적힌 번호에 해당하는 상자를 열어 안에 담긴 카드에 적힌 숫자를 확인
#5. 숫자에 해당하는 번호를 가진 상자를 계속해서 열어가며, 열어야 하는 상자가 이미 열려있을 때까지 반복
#6. 이렇게 연 상자들은 1번 상자 그룹
#7. 만약 1번 상자 그룹을 제외하고 남는 상자가 없으면 그대로 게임이 종료되며, 이때 획득하는 점수는 0점
#8. 그렇지 않다면 남은 상자 중 다시 임의의 상자 하나를 골라 같은 방식으로 이미 열려있는 상자를 만날 때까지 상자를 엽니다. 
#9. 이렇게 연 상자들은 2번 상자 그룹
#10. 1번 상자 그룹에 속한 상자의 수와 2번 상자 그룹에 속한 상자의 수를 곱한 값이 게임의 점수
# 싸이클 생성 몇 개 되냐?

def solution(cards):
    # 사이클이 가능한 상자의 수 저장
    boxes = []
    # 첫 번째 박스 번호 1로 맟추기
    cards = [0] + cards
    n = len(cards)
    # 방문 체크
    visited = [0] * n
    
    # 사이클 만들기
    def dfs(x):
        nonlocal cnt
        if 0 < x <= n and visited[x] == 0:
            visited[x] = 1
            cnt += 1
            # 숫자에 해당하는 상자 탐색
            dfs(cards[x])
    
    # 차례대로 사이클 탐색
    for i in range(1, n):
        if visited[i] == 0:
            # 현재 그룹의 상자 수 저장
            cnt = 0
            # 사이클 탐색
            dfs(i)
            # 탐색이 끝난 그룹의 전체 상자 수 저장
            boxes.append(cnt)
    
    # 그룹이 2개 이하이면 0 리턴
    if len(boxes) < 2:
        return 0

    boxes.sort(reverse=True)
    # 선택한 두 그룹의 최고 점수 리턴
    return boxes[0] * boxes[1]