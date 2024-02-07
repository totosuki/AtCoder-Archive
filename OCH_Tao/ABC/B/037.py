N,Q = map(int,input().split())
x = [0]*N
for i in range(Q):
  l,r,t = map(int,input().split())
  x[l-1:r] = [t]*(r-l+1)
print("\n".join(str(i) for i in x))