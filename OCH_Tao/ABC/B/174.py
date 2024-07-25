N,D = map(int,input().split())
cnt = 0
for i in range(N):
  X,Y = map(int,input().split())
  if X**2+Y**2<=D**2:
    cnt+=1
print(cnt)