N, S, T = map(int, input().split())
W = int(input())
rslt = [W]
for _ in range(N - 1):
  W += int(input())
  rslt.append(W)
rslt_count = 0
for w in rslt:
  if S <= w <= T:
    rslt_count += 1
print(rslt_count)