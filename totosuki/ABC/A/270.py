A, B = map(int, input().split())
rslt = []
for n in [A, B]:
  if n == 0:
    rslt.append(0)
  elif n == 1:
    rslt.append(1)
  elif n == 2:
    rslt.append(2)
  elif n == 3:
    rslt.append(1)
    rslt.append(2)
  elif n == 4:
    rslt.append(4)
  elif n == 5:
    rslt.append(1)
    rslt.append(4)
  elif n == 6:
    rslt.append(2)
    rslt.append(4)
  else:
    rslt.append(1)
    rslt.append(2)
    rslt.append(4)
print(sum(set(rslt)))