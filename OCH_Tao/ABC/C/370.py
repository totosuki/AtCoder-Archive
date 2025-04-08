S = input()
T = input()
M = 0
diff = set()
for i in range(len(S)):
  if S[i]!=T[i]:
    M+=1
    diff.add(i)
print(M)
for i in range(M):
  tmp = []
  for j in diff:
    tmp.append((S[:j]+T[j]+S[j+1:],j))
  ans = min(tmp,key=lambda x:x[0])
  S = ans[0]
  diff.discard(ans[1])
  print(S)