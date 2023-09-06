N, T = map(int, input().split())
rslt = 0
bf_a = -1000000
for i in range(N):
  a = int(input())

  if (a - bf_a) > T:
    rslt += T
  else:
    rslt += a - bf_a

  bf_a = a
print(rslt)