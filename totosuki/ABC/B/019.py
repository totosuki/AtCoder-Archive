import itertools

S = input()
data = [list(g) for k, g in itertools.groupby(S)]
rslt = ""
for d in data:
  rslt += d[0] + str(len(d))
print(rslt)