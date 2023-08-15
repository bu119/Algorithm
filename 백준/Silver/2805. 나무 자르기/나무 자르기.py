def binary_search(start, end):

    while start <= end:

        mid = (start + end) // 2
        ssum = 0

        for tree in trees:
            if mid < tree:
                ssum += tree-mid

        if ssum >= m:
            start = mid + 1
        else:
            end = mid - 1

    return end

# 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)
print(binary_search(start, end))