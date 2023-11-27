N, L, R = map(int, input().split())
A = list(map(int, input().split()))
rslt = []

for a in A:
  if a > R:
    rslt.append(R)
  elif a < L:
    rslt.append(L)
  else:
    rslt.append(a)

print(*rslt)