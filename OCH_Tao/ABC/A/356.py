N,L,R = map(int,input().split())
X = list(range(1,N+1))
X[L-1:R] = reversed(X[L-1:R])
print(*X)