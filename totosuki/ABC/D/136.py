import itertools
S = input()
L = itertools.groupby(S)
rslt = [0] * len(S)
i = 0
for k, l in L:
  l = list(l)
  len_l = len(l)
  if k == "R":
    i += len(l) - 1
    if len_l % 2 == 1:
      rslt[i] += int(len(l) / 2) + 1
      rslt[i+1] += int(len(l) / 2)
    else:
      rslt[i] += int(len(l) / 2)
      rslt[i+1] += int(len(l) / 2)
    i += 1
  else:
    if len_l % 2 == 1:
      rslt[i] += int(len(l) / 2) + 1
      rslt[i-1] += int(len(l) / 2)
    else:
      rslt[i] += int(len(l) / 2)
      rslt[i-1] += int(len(l) / 2)
    i += len(l)
print(*rslt)
