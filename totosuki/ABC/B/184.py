_, rslt = map(int, input().split())
S = input()

for s in S:
  rslt = rslt + 1 if s == "o" else rslt - 1
  if rslt < 0:
    rslt = 0

print(rslt, flush = True)