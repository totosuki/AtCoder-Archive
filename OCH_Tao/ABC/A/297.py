N,D = map(int,input().split())
T = list(map(int,input().split()))
for i in range(1,N):
  if T[i]-T[i-1]<=D:
    print(T[i])
    break
else:
  print(-1)