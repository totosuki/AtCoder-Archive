S = input()
rslt = 0

tmp = 0
for i in range(len(S)):
  if S[i] in "ACGT":
    tmp += 1
    rslt = max(rslt, tmp)
  else:
    rslt = max(rslt, tmp)
    tmp = 0

print(rslt)