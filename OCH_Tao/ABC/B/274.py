H,W = map(int,input().split())
X = [0]*W
for i in range(H):
  C = list(input())
  for j in range(W):
    if C[j]=="#":
      X[j]+=1
print(*X,sep=" ")