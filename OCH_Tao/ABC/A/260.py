S = list(input())
for i in range(3):
  if S.count(S[i])==1:
    print(S[i])
    break
else:
  print(-1)