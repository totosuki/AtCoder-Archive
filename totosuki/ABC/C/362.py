N = int(input())
L = []
R = []
for _ in range(N):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

ans = sum(L)
rslt = L.copy()

for i in range(N):
  if ans < 0 and ans + (R[i] - L[i]) < 0:
    ans += R[i] - L[i]
    rslt[i] = R[i]
  elif ans < 0:
    rslt[i] = L[i] + (0 - ans)
    ans = 0

if ans == 0:
  print("Yes")
  print(*rslt)
else:
  print("No")
