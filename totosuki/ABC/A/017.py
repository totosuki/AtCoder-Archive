L = []
rslt = 0
for _ in range(3):
  L.append(list(map(int, input().split())))
for l in L:
  rslt += (l[0] / 10) * l[1]
print(int(rslt))