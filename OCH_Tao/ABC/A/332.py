N,S,K = map(int,input().split())
cnt = 0
for i in range(N):
  P,Q = map(int,input().split())
  cnt+=P*Q
print(cnt if cnt>=S else cnt+K)