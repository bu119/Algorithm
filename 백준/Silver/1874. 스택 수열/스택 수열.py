import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

def solution():
    global arr
    
    stack = []
    ans = []
    i = 1
    
    for num in arr:
    
        # 입력한 수를 만날 때 까지 push
        while i <= num:
            stack.append(i)
            ans.append('+')
            i += 1
    
        # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        # 오름차순으로 스택이 입력되는데 TOP이 num보다 크면
        # num은 TOP보다 더 아래에 쌓여있기 때문
        if stack.pop() != num:
            return 'NO'
    
        ans.append('-')
    
    return '\n'.join(ans)

print(solution())