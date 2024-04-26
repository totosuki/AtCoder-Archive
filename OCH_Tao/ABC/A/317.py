N,H,X = map(int,input().split())
P = list(map(int,input().split()))
print(P.index(min([i for i in P if i>=X-H]))+1)