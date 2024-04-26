N = int(input())
P = list(range(0,101,5))
X = list(map(lambda x:abs(N-x),P))
print(P[X.index(min(X))])