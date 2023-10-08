import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def postorder(root, end):
    if root > end:
        return

    # 만약 root보다 큰 값 없는 경우 전부 왼쪽 서브트리로 취급
    right_start = end + 1

    for i in range(root + 1, end + 1):
        if preorder[root] < preorder[i]:
            right_start = i
            break

    # root 다음부터 왼쪽 서브트리 탐색
    postorder(root + 1, right_start - 1)

    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    postorder(right_start, end)

    # 왼쪽, 오른쪽 서브트리 탐색 끝나면 root 출력
    print(preorder[root])


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0, len(preorder) - 1)