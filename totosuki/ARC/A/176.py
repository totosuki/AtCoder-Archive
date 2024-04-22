N, M = map(int, input().split())
now_x = set()
for _ in range(M):
  A, B = map(int, input().split())
  x = B - (A-1)
  if x <= 0:
    x += N
  now_x.add(x)

if len(now_x) != M:
  for i in range(1, N+1):
    now_x.add(i)
    if len(now_x) == M:break
now_x = sorted(now_x)

ans = []

for i in range(1, N+1):
  for j in range(M):
    x = now_x[j]
    ans.append((i, x))
    if x == N:
      x = 0
    x += 1
    now_x[j] = x

print(len(ans))
for a in ans: print(*a)

# 一番上の列から右斜め下に進んでいくと、行と列の和が一定になる
# ABのいちをすべて上の列に配置してから調整する