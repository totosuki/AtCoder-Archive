N = int(input())
S = list(input())
T = list(input())
if S.count("B")!=T.count("B"):
  print(-1)
else:
  cnt = 0
  for i in range(N):
    if S[i]!=T[i]:
      cnt+=1
  print(cnt)