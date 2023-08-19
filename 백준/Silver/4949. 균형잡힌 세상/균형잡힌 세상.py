import sys
input=sys.stdin.readline

while True:
    arr = input().rstrip()

    if arr == '.':
        break

    check = ''
    arr = ''.join(arr.split())
    if arr.count('(') != arr.count(')') and arr.count('[') != arr.count(']'):
        print('no')
        continue

    for i in arr:
        if i == '(' or i == ')' or i == '[' or i == ']':
            check += i
        n = len(check)
        if n > 1:
            if check[n - 2:n] == '()' or check[n - 2:n] == '[]':
                check = check[:n - 2]

    if check:
        print('no')
    else:
        print('yes')