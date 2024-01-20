t = int(input())
for _ in range(t):
    sound = input().split()
    notFox = set()
    while True:
        animal = input()
        if animal == 'what does the fox say?':
            break
        notFox.add(animal.split()[2])

    for s in sound:
        if s not in notFox:
            print(s, end=' ')