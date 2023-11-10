N = int(input())
rslt = float("inf")

for _ in range(N):
  a, p, x = map(int, input().split())
  if x > a:
    rslt = min(p, rslt)

print(rslt if rslt != float("inf") else -1 )