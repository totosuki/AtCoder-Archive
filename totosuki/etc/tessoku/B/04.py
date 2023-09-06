N = input()
rslt = 0

for i, n in enumerate(reversed(N)):
  rslt += int(n) * 2**i

print(rslt)