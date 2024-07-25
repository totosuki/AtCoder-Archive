H,W,X,Y = map(int,input().split())
S = []
for i in range(H):
  I = list(input())
  if i!=X-1:
    S.append(I)
  else:
    I[Y-1]="X"
    S.append(I)
L = []
L+=("".join(S[X-1]).split("#"))
L+=("".join([i[Y-1] for i in S]).split("#"))
print(len("".join([i for i in L if "X" in i]))-1)