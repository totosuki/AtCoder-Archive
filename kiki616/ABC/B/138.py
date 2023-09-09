N,M = map(int,input().split())
k = []
a = []
ans = 1
for i in range(M):
    b = list(map(int,input().split()))
    k.append(b[0])
    a.append(b[1:])
for i in range(1,N+1):
    nm = {l for l in range(1,N+1)}
    nm = set(nm)
    for l in a:
        if i in l:
            nm = nm - set(l)
    if not len(nm) == 0:
        ans = 0
if ans:
    print("Yes")
else:
    print("No")