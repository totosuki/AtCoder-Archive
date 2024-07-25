N,A = map(int,input().split())
T = list(map(int,input().split()))
cnt = 0
for i in range(N):
  if cnt<T[i]:
    cnt=T[i]
  cnt+=A
  print(cnt)