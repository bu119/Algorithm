t = int(input())
for _ in range(t):
    sound = input().split()
    while True:
        animal = input()
        if animal == 'what does the fox say?':
            break
        notFox = animal.split()[2]
        animalCnt = sound.count(notFox)
        for _ in range(animalCnt):
            sound.remove(notFox)
    print(' '.join(sound))