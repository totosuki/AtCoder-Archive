N,M=map(int,input().split())
l=list(range(1,N+1))
for i in []*M:
    A,B=map(int,input().split())
    if B in l:
        l.remove(B)
print(l[0] if len(l)==1 else -1)