N,P,Q = map(int, input().split())
D = min(list(map(int, input().split())))
if P < Q+D:
    print(P)
else:
    print(Q+D)