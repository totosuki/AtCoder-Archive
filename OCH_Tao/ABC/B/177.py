S = input()
T = input()
ans = len(T)
for i in range(len(S)-len(T)+1):
  X = S[i:i+len(T)]
  cnt = 0
  for j in range(len(T)):
    if X[j]!=T[j]:
      cnt+=1
  else:
    ans = min(cnt,ans)
print(ans)