def fn(x):
  return [i for i,j in enumerate(x) if j==True]
N,K,Q = map(int,input().split())
A = set(list(map(int,input().split())))
L = list(map(int,input().split()))
X = [i in A for i in range(1,N+1)]
for i in L:
  tmp = fn(X)[i-1]
  if tmp==N-1:
    continue
  else:
    if not X[tmp+1]:
      X[tmp]=False
      X[tmp+1]=True
print(*map(lambda x:x+1,fn(X)),sep=" ")