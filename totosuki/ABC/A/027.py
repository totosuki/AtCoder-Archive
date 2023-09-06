l = list(map(int, input().split()))
lset = list(set(l))
if len(lset) == 1:
  print(lset[0])
else:
  if l.count(lset[0]) == 1:
    print(lset[0])
  else:
    print(lset[1])