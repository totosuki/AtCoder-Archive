N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
ans = int(1e10)
for i in range(K+1):
  ans=min(ans,A[i+(N-K)-1]-A[i])
print(ans)