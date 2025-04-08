N,M = map(int,input().split())
L = []
cnt = [[i for i in [False]*N] for j in range(N)]
for i in range(M):
  U,V = map(int,input().split())
  cnt[U-1][V-1]=True
  cnt[V-1][U-1]=True
ans = 0
for i in range(N-2):
  for j in range(i,N-1):
    for k in range(j,N):
      if cnt[i][j] and cnt[j][k] and cnt[k][i]:
        ans+=1
print(ans)