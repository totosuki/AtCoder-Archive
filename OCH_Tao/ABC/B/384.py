N, R = map(int, input().split())
for i in range(N):
  D, A = map(int, input().split())
  if D == 1:
    if 1600 <= R < 2800:
      R += A
  else:
    if 1200 <= R < 2400:
      R += A
print(R)
