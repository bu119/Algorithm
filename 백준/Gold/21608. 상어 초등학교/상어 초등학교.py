def find_max_favorite_st():
    candidates = []
    maxFavoriteCnt = 0

    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                favoriteCnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and classroom[ni][nj] in favoriteSt:
                        favoriteCnt += 1

                if maxFavoriteCnt < favoriteCnt:
                    maxFavoriteCnt = favoriteCnt
                    candidates = [(i, j)]
                elif maxFavoriteCnt == favoriteCnt:
                    candidates.append((i, j))
    return candidates


def find_max_blank(favoriteCandidates):
    candidates = []
    maxBlankCnt = 0

    for i, j in favoriteCandidates:
        blankCnt = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and classroom[ni][nj] == 0:
                blankCnt += 1

        if maxBlankCnt < blankCnt:
            maxBlankCnt = blankCnt
            candidates = [(i, j)]
        elif maxBlankCnt == blankCnt:
            candidates.append((i, j))

    return candidates


def find_min_row(blankCandidates):
    minRow = n+1
    candidates = []

    for i, j in blankCandidates:
        if minRow > i:
            minRow = i
            candidates = [(i, j)]
        elif minRow == i:
            candidates.append((i, j))

    return candidates


def find_min_col(rowCandidates):
    minCol = n + 1
    candidates = (-1, -1)

    for i, j in rowCandidates:
        if minCol > j:
            minCol = j
            candidates = (i, j)

    return candidates


def satisfaction_survey():
    satisfaction = 0
    for i in range(n):
        for j in range(n):
            favoriteCnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and classroom[ni][nj] in student[classroom[i][j]]:
                    favoriteCnt += 1

            if favoriteCnt == 1:
                satisfaction += 1
            elif favoriteCnt == 2:
                satisfaction += 10
            elif favoriteCnt == 3:
                satisfaction += 100
            elif favoriteCnt == 4:
                satisfaction += 1000

    return satisfaction


n = int(input())
classroom = [[0]*n for _ in range(n)]
student = dict()
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(n**2):
    st, *favoriteSt = list(map(int, input().split()))
    favoriteSt = set(favoriteSt)
    student[st] = favoriteSt
    
    candidate = find_max_favorite_st()
    if len(candidate) == 1:
        x, y = candidate[0]
        classroom[x][y] = st
        continue

    candidate = find_max_blank(candidate)
    if len(candidate) == 1:
        x, y = candidate[0]
        classroom[x][y] = st
        continue

    candidate = find_min_row(candidate)
    if len(candidate) == 1:
        x, y = candidate[0]
        classroom[x][y] = st
        continue

    x, y = find_min_col(candidate)
    classroom[x][y] = st

print(satisfaction_survey())