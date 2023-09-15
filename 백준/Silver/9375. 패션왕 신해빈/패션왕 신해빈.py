t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if clothes.get(kind):
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]
    
    cnt = 1
    for key in clothes:
        cnt *= (len(clothes[key]) + 1)

    print(cnt - 1)