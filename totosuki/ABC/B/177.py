S = input()
T = input()
rslt = []

for i in range(len(S) - len(T) + 1):
  cnt = 0
  for j in range(len(T)):
    if S[i+j] != T[j]:
      cnt += 1
  rslt.append(cnt)

print(min(rslt))