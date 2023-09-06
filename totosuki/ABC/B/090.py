A, B = map(int, input().split())
cnt = 0

for n in range(A, B+1):
  n = list(str(n))
  n_rev = reversed(n)
  n = "".join(n)
  n_rev = "".join(n_rev)
  if int(n) == int(n_rev):
    cnt += 1

print(cnt)