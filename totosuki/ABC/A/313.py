N = int(input())
P = list(map(int, input().split()))
mx = max(P)

if P[0] == mx and P.count(mx) == 1:
  print(0)
else:
  print(mx - P[0] + 1)