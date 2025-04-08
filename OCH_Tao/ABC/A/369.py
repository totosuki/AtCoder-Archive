A,B = map(int,input().split())
cnt = 0
for i in range(-1000,1000):
  L = sorted([A,B,i])
  if L[0]-L[1]==L[1]-L[2]:
    cnt+=1
print(cnt)