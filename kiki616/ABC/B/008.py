N = int(input())
S = {}
for i in range(N):
    s = input()
    if s in S.keys():
        S[s] = S[s] + 1
    else:
        S[s] = 1
for k,v in S.items():
    if v==max(S.values()):
        print(k)
        break