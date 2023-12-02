N = int(input())
A = list(map(int,input().split()))
Q = int(input())
li = [[0]*2 for i in range(10**5)]
o = 0
x = 0
for i in range(N):
    if A[i]:
        o += 1
    else:
        x += 1
    li[i+1] = [o,x]

for i in range(Q):
    L,R = map(int,input().split())
    O = li[R][0] - li[L-1][0]
    X = li[R][1] - li[L-1][1]
    if O > X:
        print("win")
    elif O < X:
        print("lose")
    elif O == X:
        print("draw")