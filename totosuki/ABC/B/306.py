A = list(map(int, input().split()))
rslt = 0
for i, a in enumerate(A):
  if a == 1:
    rslt += 2**i
print(rslt)