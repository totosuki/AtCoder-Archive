N,Q = map(int,input().split())
A = list(map(int,input().split()))
al = []
sm = 0
for i in A:
    sm += i
    al.append(sm)

for i in range(Q):
    L,R = map(int,input().split())
    if L == 1:
        print(al[R-1])
    else:
        print(al[R-1] - al[L-2])