K,X = map(int,input().split())
L = list(range(X-K+1,X+K))
print(" ".join([str(i) for i in L]))