N,K = map(int,input().split())
P = sorted(list(map(int,input().split())))
print(sum(P[:K]))