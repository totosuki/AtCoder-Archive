A, B, C, D = map(int, input().split())
rate_takahashi = B / A
rate_aoki = D / C
if rate_takahashi > rate_aoki:
  print("TAKAHASHI")
elif rate_takahashi < rate_aoki:
  print("AOKI")
else:
  print("DRAW")