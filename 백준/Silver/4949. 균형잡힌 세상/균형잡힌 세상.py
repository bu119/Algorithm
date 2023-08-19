import sys
input=sys.stdin.readline

def check(sentence):
    stack = []

    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                return 'no'
        elif i == ']':
            if not stack or stack.pop() != '[':
                return 'no'

    if stack:
        return 'no'

    return 'yes'


while True:
    arr = input().rstrip()
    if arr == '.':
        break
    print(check(arr))