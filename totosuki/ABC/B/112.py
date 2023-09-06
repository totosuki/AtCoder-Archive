N, T = map(int, input().split())
min_cost = 1001

for _ in range(N):
  c, t = map(int, input().split())
  if t <= T:
    min_cost = min(min_cost, c)

print(min_cost) if min_cost != 1001 else print("TLE")