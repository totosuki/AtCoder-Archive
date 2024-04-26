S = list(input())
T = list(input().lower())
if T[2]=="x":
  X=2
else:
  X=3
L = [False]*X
cnt = 0
for i in range(len(S)):
  if S[i]==T[cnt]:
    L[cnt]=True
    cnt+=1
  if cnt==X:
    break
if all(L):
  print("Yes")
else:
  print("No")