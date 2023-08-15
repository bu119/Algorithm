import sys
input = sys.stdin.readline

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


n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)
print(binary_search(start, end))