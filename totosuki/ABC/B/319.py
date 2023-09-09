N = int(input())
rslt = []
divs = []

for j in range(1, 10):
  if N % j == 0:
    divs.append(j)

for i in range(N+1):
  for j in divs:
    if i % (N//j) == 0:
      rslt.append(f"{j}")
      break
  else:
    rslt.append("-")

print("".join(rslt))