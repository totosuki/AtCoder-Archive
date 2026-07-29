M, D = map(int, input().split())
S = input()
ok = [False] * M

for i in range(M):
    if S[i] == "G":
        for j in range(max(i-D, 0), min(i+D+1, M)):
            ok[j] = True

print(ok.count(False))
