N = int(input())
S = []
P = []
for i in range(N):
  x,y = input().split()
  S.append(x)
  P.append(int(y))
T = sum(P)
for i in range(N):
  if P[i]>T//2:
    print(S[i])
    break
else:
  print("atcoder")