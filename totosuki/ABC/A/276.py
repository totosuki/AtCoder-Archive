S = input()
rslt = []
for i,s in enumerate(S):
  if s == "a":
    rslt.append(i+1)
if rslt:
  print(max(rslt))
else:
  print(-1)