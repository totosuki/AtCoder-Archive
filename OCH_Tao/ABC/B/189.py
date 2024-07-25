N,X = map(int,input().split())
cnt = 0
for i in range(N):
  V,P = map(int,input().split())
  cnt+=V*P
  if cnt>X*100:
    print(i+1)
    break
else:
  print(-1)