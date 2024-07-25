N = int(input())
L = []
for i in range(N):
  X,Y = map(int,input().split())
  L.append(X==Y)
cnt = 0
for i in L:
  if i:
    cnt+=1
  else:
    cnt=0
  if cnt==3:
    print("Yes")
    break
else:
  print("No")