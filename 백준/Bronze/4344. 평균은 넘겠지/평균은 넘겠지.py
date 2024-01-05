c = int(input())
for _ in range(c):
    n, *grads = map(int, input().split())
    avg = sum(grads) / n
    cnt = 0
    for i in grads:
        if avg < i:
            cnt += 1
    print(f'{round(cnt*100/n,3):.3f}%')