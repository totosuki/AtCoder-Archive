N,X = map(int,input().split())
A = list(map(int,input().split()))
A.pop(A.index(max(A)))
m = A.pop(A.index(min(A)))
if X <= sum(A) + m:
    print(0)
else:
    if X - sum(A) <= 100:
        print(X - sum(A))
    else:
        print(-1)