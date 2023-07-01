def mid_node(level, arr):    # 부모 노드와 오른쪽,왼쪽 서브트리가 전위 순회를 한다고 생각
    global num
    mid = len(arr)//2
    if k > level:
        num[level].append(arr[mid])     # 레벨을 인덱스로 구분
        mid_node(level+1, arr[:mid])
        mid_node(level+1, arr[mid+1:])

k = int(input())
arr = list(map(int, input().split()))
num = [[]*k for _ in range(k)]

mid_node(0, arr)
for i in range(k):
    print(*num[i])