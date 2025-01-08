n, m = map(int, input().split())
idx = {"A": 0, "C": 1, "G": 2, "T": 3}
dna = {0: "A", 1: "C", 2: "G", 3: "T"}
dna_cnt = [[0]*4 for _ in range(m)]
for _ in range(n):
    string = input()
    for i in range(m):
        dna_cnt[i][idx[string[i]]] += 1
ans_hd = 0
ans_dna = ""
for i in range(m):
    hd = max(dna_cnt[i])
    ans_dna += dna[dna_cnt[i].index(hd)]
    ans_hd += (n - hd)
print(ans_dna)
print(ans_hd)