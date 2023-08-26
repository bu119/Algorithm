def binary_search(start, end, num):

    while start <= end:

        mid = (start+end)//2

        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
cards.sort()

for num in check:
    print(binary_search(0,n-1,num), end=' ')