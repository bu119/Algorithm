import sys
input=sys.stdin.readline

while True:
    arr = input().rstrip()
    if arr == '.':
        break

    if arr.count('(') != arr.count(')') or arr.count('[') != arr.count(']'):
        print('no')
        continue

    check = ''

    for i in arr:
        if i in '()[]':
            check += i

    while "()" in check or "[]" in check:
        if "()" in check:
            check = check.replace("()", "")
        if "[]" in check:
            check = check.replace("[]", "")

    if check:
        print('no')
    else:
        print('yes')