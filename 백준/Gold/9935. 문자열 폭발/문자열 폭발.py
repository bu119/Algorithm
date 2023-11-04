string = input() # mirkovC4nizCC44
explosion = list(input()) # C4
m = len(explosion)

stack = []
for s in string:
    stack.append(s)
    if stack[-m:] == explosion:
        for _ in range(m):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")