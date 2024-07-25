N,M,T = map(int,input().split())
cnt = N
X = 0
for i in range(M):
  A,B = map(int,input().split())
  cnt=max(0,cnt-(A-X))
  if cnt>0:
    cnt=min(N,cnt+(B-A))
    X=B
  else:
    print("No")
    break
else:
  cnt=max(0,cnt-(T-X))
  if cnt>0:
    print("Yes")
  else:
    print("No")