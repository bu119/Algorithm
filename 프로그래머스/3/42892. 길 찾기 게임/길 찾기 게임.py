import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
        
    # 트리 만들기
    def make_tree(parent, child):
        # 부모 노드의 왼쪽, 오른쪽 자식
        left, right = tree[parent] 
        # 왼쪽 자식 조건 (부모 노드 x 좌표보다 작아야 함)
        if child[0] < parent[0]:
            # 왼쪽 자식이 없으면
            if left == (-1, -1):
                # 왼쪽 자식으로 설정
                tree[parent][0] = child
                # 손자 트리 생성
                tree[child] = [(-1, -1), (-1, -1)]

            else:
                # 재귀로 계속 탐색
                make_tree(left, child)  
                
        # 오른쪽 자식 조건 (부모 노드 x 좌표보다 커야 함)
        else:
            # 오른쪽 자식이 없으면
            if right == (-1, -1): 
                # 오른쪽 자식으로 설정
                tree[parent][1] = child
                # 손자 트리 생성
                tree[child] = [(-1, -1), (-1, -1)]
            else:
                # 재귀로 계속 탐색
                make_tree(right, child)
                
    # 전위 순회
    def pre_order(node):
        if node != (-1, -1):  # 마지막 정점번호 이내
            answer[0].append(nodeIdx[node])
            pre_order(tree[node][0])  # 왼쪽 자식정점 방문
            pre_order(tree[node][1])  # 오른쪽 자식정점 방문
    
    # 후위 순회
    def post_order(node):
        if node != (-1, -1):  # 마지막 정점번호 이내
            post_order(tree[node][0])  # 왼쪽 자식정점 방문
            post_order(tree[node][1])  # 오른쪽 자식정점 방문
            answer[1].append(nodeIdx[node])

                
    n = len(nodeinfo)
    # 트리 저장: {(x좌표, y좌표): [(left x좌표, y좌표), (right x좌표, y좌표)]}
    tree = dict()
    # 인덱스 저장: {(x좌표, y좌표): 번호} 
    nodeIdx = dict()
    # 인덱스 저장하기
    for i in range(n):
        nodeIdx[tuple(nodeinfo[i])] = i+1
    
    # 좌표를 트리의 레벨별로 순서대로 저장
    nodeinfo.sort(key=lambda x:-x[1])
    # 트리의 루트
    root = tuple(nodeinfo[0])
    # 트리에 루트 저장
    tree[root] = [(-1, -1), (-1, -1)]
    # 트리 만들기
    for i in range(1, n):
        make_tree(root, tuple(nodeinfo[i]))
        
    # 전위 순회, 후위 순회 결과 저장
    answer = [[],[]]
    # 전위순회
    pre_order(root)
    # 후위순회
    post_order(root)

    return answer