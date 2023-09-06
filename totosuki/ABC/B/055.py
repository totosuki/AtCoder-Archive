N = int(input())
rslt = 1

for i in range(1, N+1):
  rslt = ((rslt * i) % (10**9 + 7))

print(rslt)