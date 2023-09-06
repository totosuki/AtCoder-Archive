N,H,X = map(int,input().split())
P = sorted(list(map(int,input().split())))
reversed(P)
for i in range(N):
    if H + P[i] >= X:
        print(i+1)
        break