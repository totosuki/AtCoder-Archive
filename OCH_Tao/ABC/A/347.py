N,K = map(int,input().split())
A = list(map(int,input().split()))
L = []
for i in A:
  if i%K==0:
    L.append(i//K)
print(" ".join([str(i) for i in L]))