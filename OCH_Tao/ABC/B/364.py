H,W = map(int,input().split())
Si,Sj = map(int,input().split())
C = []
for i in range(H):
  C.append(list(input()))
X = list(input())
Si-=1
Sj-=1
for i in X:
  if i=="U":
    if Si!=0 and C[Si-1][Sj]==".":
      Si-=1
  elif i=="D":
    if Si!=H-1 and C[Si+1][Sj]==".":
      Si+=1
  elif i=="L":
    if Sj!=0 and C[Si][Sj-1]==".":
      Sj-=1
  else:
    if Sj!=W-1 and C[Si][Sj+1]==".":
      Sj+=1
print(Si+1,Sj+1,sep=" ")