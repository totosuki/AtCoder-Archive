N = int(input())
P = list(map(int, input().split()))
mx = max(P)
need = mx - P[0]
if need > 1 or P.count(mx) != 1:
  need += 1
else:
  need = 0
print(need)